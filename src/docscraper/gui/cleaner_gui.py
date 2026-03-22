#!/usr/bin/env python3
"""
PostScraperCleaner GUI

A graphical interface for cleaning and optimizing scraped markdown files.
Removes navigation, boilerplate, and redundant content using rule-based patterns.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import threading
import json
import os
from pathlib import Path
from datetime import datetime, timedelta
import queue
import logging
from typing import Optional, Callable, Dict, Any

from docscraper.cleaning.cleaner import PostScraperCleaner, CleaningConfig, CleaningResult
from docscraper.cleaning.rules import PatternRegistry, DEFAULT_REGISTRY

# Load .env file for API keys
def load_env():
    """Load environment variables from .env file"""
    env_file = Path(__file__).parent / ".env"
    if env_file.exists():
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key.strip()] = value.strip()

load_env()

logger = logging.getLogger(__name__)


class GUIPostScraperCleaner(PostScraperCleaner):
    """
    PostScraperCleaner subclass with logging for GUI integration

    Reports progress updates through callbacks for real-time UI updates
    """

    def __init__(self, config: CleaningConfig, progress_callback: Optional[Callable] = None):
        """Initialize with GUI callback"""
        super().__init__(config, progress_callback)
        self.start_time = None

    def clean_batch(self, input_folder, output_folder, pattern: str = "*.md"):
        """Override to add timing"""
        self.start_time = datetime.now()
        return super().clean_batch(input_folder, output_folder, pattern)


class PostScraperCleanerGUI:
    """
    Tkinter GUI for PostScraperCleaner

    Provides interface for configuring cleaning options, monitoring progress,
    and analyzing results.
    """

    def __init__(self, root):
        """Initialize GUI"""
        self.root = root
        self.root.title("PostScraperCleaner - Document Cleaning Processor")
        self.root.geometry("1000x750")
        self.root.minsize(800, 600)

        # State variables
        self.processing = False
        self.processor_thread = None
        self.message_queue = queue.Queue()
        self.current_config = None
        self.processor = None
        self.start_time = None
        self.processed_files = []

        # Setup UI
        self.setup_styles()
        self.setup_menu()
        self.setup_ui()
        self.center_window()

        # Start message queue check
        self.check_messages()

    def setup_styles(self):
        """Configure modern styling"""
        try:
            style = ttk.Style()
            style.theme_use('clam')

            # Button styles
            style.configure("Accent.TButton",
                          background='#007ACC',
                          foreground='white',
                          font=('TkDefaultFont', 9, 'bold'))
            style.map("Accent.TButton",
                     background=[('active', '#005a9e')])

            style.configure("Danger.TButton",
                          background='#d13438',
                          foreground='white',
                          font=('TkDefaultFont', 9, 'bold'))
            style.map("Danger.TButton",
                     background=[('active', '#a4373a')])
        except Exception:
            pass

    def setup_menu(self):
        """Create menu bar"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Load Config", command=self.load_config)
        file_menu.add_command(label="Save Config", command=self.save_config)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        # Tools menu
        tools_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Tools", menu=tools_menu)
        tools_menu.add_command(label="Clear Log", command=self.clear_log)
        tools_menu.add_command(label="Export Results", command=self.export_results)
        tools_menu.add_command(label="Open Output Folder", command=self.open_output_folder)

        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

    def setup_ui(self):
        """Setup user interface"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(4, weight=1)

        # === Input/Output Frame ===
        io_frame = ttk.LabelFrame(main_frame, text="Input/Output", padding="10")
        io_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5)
        io_frame.columnconfigure(1, weight=1)

        # Input folder
        ttk.Label(io_frame, text="Input Folder:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        self.input_var = tk.StringVar(value="./scraped_docs")
        self.input_entry = ttk.Entry(io_frame, textvariable=self.input_var)
        self.input_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 10))

        ttk.Button(io_frame, text="Browse", command=lambda: self.browse_directory('input')).grid(row=0, column=2, sticky=tk.W)

        # Output folder
        ttk.Label(io_frame, text="Output Folder:").grid(row=1, column=0, sticky=tk.W, padx=(0, 10))
        self.output_var = tk.StringVar(value="./cleaned_docs")
        self.output_entry = ttk.Entry(io_frame, textvariable=self.output_var)
        self.output_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(0, 10))

        ttk.Button(io_frame, text="Browse", command=lambda: self.browse_directory('output')).grid(row=1, column=2, sticky=tk.W)

        # === Configuration Frame ===
        config_frame = ttk.LabelFrame(main_frame, text="Cleaning Options", padding="10")
        config_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)
        config_frame.columnconfigure(0, weight=1)
        config_frame.columnconfigure(1, weight=1)

        # Pattern checkboxes
        self.remove_nav_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(config_frame, text="Remove Navigation", variable=self.remove_nav_var).grid(row=0, column=0, sticky=tk.W, padx=5, pady=3)

        self.remove_header_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(config_frame, text="Remove Headers/Footers", variable=self.remove_header_var).grid(row=0, column=1, sticky=tk.W, padx=5, pady=3)

        self.remove_boilerplate_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(config_frame, text="Remove Boilerplate", variable=self.remove_boilerplate_var).grid(row=1, column=0, sticky=tk.W, padx=5, pady=3)

        self.enable_llm_var = tk.BooleanVar(value=False)
        self.llm_check = ttk.Checkbutton(
            config_frame,
            text="🧠 Intelligent Analysis (LLM-Powered)",
            variable=self.enable_llm_var
        )
        self.llm_check.grid(row=1, column=1, sticky=tk.W, padx=5, pady=3)

        # Advanced options
        self.advanced_open = False

        def toggle_advanced():
            self.advanced_open = not self.advanced_open
            if self.advanced_open:
                self.show_advanced_options()
                adv_btn.config(text="▼ Advanced Options")
            else:
                self.hide_advanced_options()
                adv_btn.config(text="▶ Advanced Options")

        adv_btn = ttk.Button(config_frame, text="▶ Advanced Options", command=toggle_advanced)
        adv_btn.grid(row=2, column=0, columnspan=2, sticky=tk.W, padx=5, pady=5)

        # Advanced options frame (hidden initially)
        self.advanced_frame = ttk.Frame(config_frame)
        self.advanced_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), padx=10, pady=5)

        # Chunk size
        ttk.Label(self.advanced_frame, text="Chunk Size:").grid(row=0, column=0, sticky=tk.W, padx=5)
        self.chunk_size_var = tk.IntVar(value=1000)
        ttk.Spinbox(self.advanced_frame, from_=100, to=5000, textvariable=self.chunk_size_var, width=10).grid(row=0, column=1, sticky=tk.W, padx=5)
        ttk.Label(self.advanced_frame, text="tokens").grid(row=0, column=2, sticky=tk.W, padx=5)

        # Overlap size
        ttk.Label(self.advanced_frame, text="Overlap Size:").grid(row=0, column=3, sticky=tk.W, padx=5)
        self.overlap_var = tk.IntVar(value=200)
        ttk.Spinbox(self.advanced_frame, from_=0, to=500, textvariable=self.overlap_var, width=10).grid(row=0, column=4, sticky=tk.W, padx=5)
        ttk.Label(self.advanced_frame, text="tokens").grid(row=0, column=5, sticky=tk.W, padx=5)

        # Max cost and rate limit
        ttk.Label(self.advanced_frame, text="Max Cost/Doc:").grid(row=1, column=0, sticky=tk.W, padx=5)
        self.max_cost_var = tk.StringVar(value="0.05")
        ttk.Entry(self.advanced_frame, textvariable=self.max_cost_var, width=10).grid(row=1, column=1, sticky=tk.W, padx=5)

        ttk.Label(self.advanced_frame, text="Rate Limit:").grid(row=1, column=3, sticky=tk.W, padx=5)
        self.rate_limit_var = tk.IntVar(value=500)
        ttk.Spinbox(self.advanced_frame, from_=10, to=10000, textvariable=self.rate_limit_var, width=10).grid(row=1, column=4, sticky=tk.W, padx=5)
        ttk.Label(self.advanced_frame, text="RPM").grid(row=1, column=5, sticky=tk.W, padx=5)

        # Hide advanced frame initially
        self.advanced_frame.grid_remove()

        # === Processing Control Frame ===
        control_frame = ttk.LabelFrame(main_frame, text="Processing", padding="10")
        control_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=5)
        control_frame.columnconfigure(1, weight=1)

        # Buttons
        self.start_btn = ttk.Button(control_frame, text="Start Cleaning", command=self.start_cleaning, style="Accent.TButton")
        self.start_btn.grid(row=0, column=0, sticky=tk.W, padx=5)

        self.stop_btn = ttk.Button(control_frame, text="Stop", command=self.stop_cleaning, state=tk.DISABLED, style="Danger.TButton")
        self.stop_btn.grid(row=0, column=1, sticky=tk.W, padx=5)

        # Progress bar
        self.progress_var = tk.DoubleVar(value=0)
        self.progress_bar = ttk.Progressbar(control_frame, variable=self.progress_var, maximum=100)
        self.progress_bar.grid(row=0, column=2, sticky=(tk.W, tk.E), padx=10)
        control_frame.columnconfigure(2, weight=1)

        # Status
        self.status_var = tk.StringVar(value="Ready")
        ttk.Label(control_frame, textvariable=self.status_var, foreground="blue").grid(row=1, column=0, columnspan=3, sticky=tk.W, pady=5)

        # === Results Notebook ===
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.grid(row=4, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        main_frame.rowconfigure(4, weight=1)

        # Tab 1: Summary
        summary_frame = ttk.Frame(self.notebook)
        self.notebook.add(summary_frame, text="Summary")

        self.summary_text = scrolledtext.ScrolledText(summary_frame, height=15, width=100, state=tk.DISABLED)
        self.summary_text.pack(fill=(tk.BOTH), expand=True, padx=5, pady=5)

        # Tab 2: Details
        details_frame = ttk.Frame(self.notebook)
        self.notebook.add(details_frame, text="Details")

        self.details_text = scrolledtext.ScrolledText(details_frame, height=15, width=100, state=tk.DISABLED)
        self.details_text.pack(fill=(tk.BOTH), expand=True, padx=5, pady=5)

        # Tab 3: Log
        log_frame = ttk.Frame(self.notebook)
        self.notebook.add(log_frame, text="Log")

        self.log_text = scrolledtext.ScrolledText(log_frame, height=15, width=100, state=tk.DISABLED)
        self.log_text.pack(fill=(tk.BOTH), expand=True, padx=5, pady=5)

        # Configure text tags for colors
        self.log_text.tag_config("INFO", foreground="black")
        self.log_text.tag_config("SUCCESS", foreground="green")
        self.log_text.tag_config("ERROR", foreground="red")
        self.log_text.tag_config("WARNING", foreground="orange")

        # === Status Bar ===
        status_frame = ttk.Frame(main_frame)
        status_frame.grid(row=5, column=0, sticky=(tk.W, tk.E), pady=5)

        self.progress_label = ttk.Label(status_frame, text="Progress: 0/0 files")
        self.progress_label.pack(side=tk.LEFT, padx=10)

        self.current_file_label = ttk.Label(status_frame, text="Current: idle")
        self.current_file_label.pack(side=tk.LEFT, padx=10)

        self.cost_label = ttk.Label(status_frame, text="Cost: $0.00")
        self.cost_label.pack(side=tk.LEFT, padx=10)

        self.time_label = ttk.Label(status_frame, text="Time: 00:00:00")
        self.time_label.pack(side=tk.LEFT, padx=10)

    def show_advanced_options(self):
        """Show advanced options frame"""
        self.advanced_frame.grid()

    def hide_advanced_options(self):
        """Hide advanced options frame"""
        self.advanced_frame.grid_remove()

    def center_window(self):
        """Center window on screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def browse_directory(self, folder_type: str):
        """Browse for directory"""
        folder = filedialog.askdirectory(title=f"Select {folder_type} folder")
        if folder:
            if folder_type == 'input':
                self.input_var.set(folder)
            elif folder_type == 'output':
                self.output_var.set(folder)

    def start_cleaning(self):
        """Start cleaning process"""
        # Validate inputs
        input_path = Path(self.input_var.get())
        output_path = Path(self.output_var.get())

        if not input_path.exists():
            messagebox.showerror("Error", f"Input folder not found: {input_path}")
            return

        # Create config
        self.current_config = CleaningConfig(
            remove_navigation=self.remove_nav_var.get(),
            remove_headers_footers=self.remove_header_var.get(),
            remove_boilerplate=self.remove_boilerplate_var.get(),
            enable_llm_validation=self.enable_llm_var.get(),
            target_chunk_size=self.chunk_size_var.get(),
            overlap_size=self.overlap_var.get(),
            max_cost_per_document=float(self.max_cost_var.get()),
            rate_limit_rpm=self.rate_limit_var.get()
        )

        # Setup processor
        self.processor = GUIPostScraperCleaner(
            self.current_config,
            progress_callback=self.progress_callback
        )

        # Reset UI
        self.processing = True
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.status_var.set("Processing...")
        self.start_time = datetime.now()
        self.processed_files = []
        self.update_summary_display()
        self.update_details_display()
        self.clear_log()

        # Start processing in thread
        self.processor_thread = threading.Thread(
            target=self._process_files,
            args=(input_path, output_path),
            daemon=True
        )
        self.processor_thread.start()

        # Restart message checking loop
        self.check_messages()

        # Start timer
        self.update_timer()

    def _process_files(self, input_path: Path, output_path: Path):
        """Process files in background thread"""
        try:
            results = self.processor.clean_batch(input_path, output_path)
            self.processed_files = results
            self.message_queue.put({"type": "complete", "results": results})
        except Exception as e:
            self.message_queue.put({"type": "error", "error": str(e)})

    def stop_cleaning(self):
        """Stop cleaning process"""
        self.processing = False
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.status_var.set("Stopped")

    def progress_callback(self, message: Dict[str, Any]):
        """Handle progress updates from processor"""
        if message["type"] == "progress":
            self.message_queue.put(message)

    def check_messages(self):
        """Check message queue for updates"""
        while True:
            try:
                msg = self.message_queue.get_nowait()

                if msg["type"] == "progress":
                    total = msg.get("total", 1)
                    processed = msg.get("processed", 0)
                    self.progress_var.set((processed / total) * 100)
                    self.progress_label.config(text=f"Progress: {processed}/{total} files")
                    current = msg.get("current_file", "")
                    self.current_file_label.config(text=f"Current: {current}")
                    self.log(f"Processing: {current}", "INFO")

                elif msg["type"] == "complete":
                    self.on_processing_complete(msg.get("results", []))

                elif msg["type"] == "error":
                    messagebox.showerror("Error", msg.get("error", "Unknown error"))
                    self.stop_cleaning()

            except queue.Empty:
                break

        if self.processing or self.processor_thread and self.processor_thread.is_alive():
            self.root.after(200, self.check_messages)

    def on_processing_complete(self, results):
        """Handle processing complete"""
        self.processing = False
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.status_var.set("Complete")
        self.progress_var.set(100.0)

        self.update_summary_display()
        self.update_details_display()

        messagebox.showinfo("Success", "Cleaning completed successfully!")

    def update_summary_display(self):
        """Update summary tab"""
        self.summary_text.config(state=tk.NORMAL)
        self.summary_text.delete(1.0, tk.END)

        if not self.processed_files:
            self.summary_text.insert(tk.END, "No files processed yet.\n")
        else:
            results = self.processed_files
            successful = sum(1 for r in results if r.success)
            failed = len(results) - successful
            successful_results = [r for r in results if r.success]

            total_before = sum(r.original_size for r in results) / 1024 / 1024
            total_after = sum(r.cleaned_size for r in results) / 1024 / 1024
            avg_reduction = (sum(r.reduction_percentage for r in successful_results) / len(successful_results)) if successful_results else 0
            total_time = sum(r.processing_time for r in results)
            avg_time = total_time / len(results) if results else 0

            summary = f"""FILES PROCESSED: {len(results)}
Successful: {successful} ({successful/len(results)*100:.1f}%)
Failed: {failed}

SIZE REDUCTION:
Total Before: {total_before:.2f} MB
Total After: {total_after:.2f} MB
Average Reduction: {avg_reduction:.1f}%

PROCESSING TIME:
Total Time: {total_time:.2f}s
Average per File: {avg_time:.3f}s

PATTERNS APPLIED:
{len(results)} files cleaned with rule-based patterns
"""
            self.summary_text.insert(tk.END, summary)

        self.summary_text.config(state=tk.DISABLED)

    def update_details_display(self):
        """Update details tab"""
        self.details_text.config(state=tk.NORMAL)
        self.details_text.delete(1.0, tk.END)

        if not self.processed_files:
            self.details_text.insert(tk.END, "No files processed yet.\n")
        else:
            header = f"{'File':<30} {'Status':<10} {'Original':<12} {'Cleaned':<12} {'Reduction':<10} {'Time':<8}\n"
            separator = "-" * 90 + "\n"

            self.details_text.insert(tk.END, header)
            self.details_text.insert(tk.END, separator)

            for result in self.processed_files:
                status = "✓ OK" if result.success else "✗ FAIL"
                original = f"{result.original_size / 1024:.1f}KB"
                cleaned = f"{result.cleaned_size / 1024:.1f}KB"
                reduction = f"{result.reduction_percentage:.1f}%"
                time_str = f"{result.processing_time:.2f}s"

                line = f"{result.input_file.name:<30} {status:<10} {original:<12} {cleaned:<12} {reduction:<10} {time_str:<8}\n"
                self.details_text.insert(tk.END, line)

        self.details_text.config(state=tk.DISABLED)

    def log(self, message: str, level: str = "INFO"):
        """Add message to log"""
        self.log_text.config(state=tk.NORMAL)
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_line = f"[{timestamp}] {message}\n"
        self.log_text.insert(tk.END, log_line, level)
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)

    def clear_log(self):
        """Clear log text"""
        self.log_text.config(state=tk.NORMAL)
        self.log_text.delete(1.0, tk.END)
        self.log_text.config(state=tk.DISABLED)

    def update_timer(self):
        """Update elapsed time display"""
        if self.start_time and self.processing:
            elapsed = datetime.now() - self.start_time
            hours, remainder = divmod(int(elapsed.total_seconds()), 3600)
            minutes, seconds = divmod(remainder, 60)
            time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.time_label.config(text=f"Time: {time_str}")
            self.root.after(1000, self.update_timer)

    def save_config(self):
        """Save current configuration to JSON"""
        if not self.current_config:
            self.current_config = self._build_config()

        file = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )

        if file:
            config_dict = {
                "input_folder": self.input_var.get(),
                "output_folder": self.output_var.get(),
                "remove_navigation": self.remove_nav_var.get(),
                "remove_headers_footers": self.remove_header_var.get(),
                "remove_boilerplate": self.remove_boilerplate_var.get(),
                "enable_llm_validation": self.enable_llm_var.get(),
                "chunk_size": self.chunk_size_var.get(),
                "overlap_size": self.overlap_var.get(),
                "max_cost": self.max_cost_var.get(),
                "rate_limit": self.rate_limit_var.get()
            }

            with open(file, 'w') as f:
                json.dump(config_dict, f, indent=2)

            messagebox.showinfo("Success", "Configuration saved!")

    def load_config(self):
        """Load configuration from JSON"""
        file = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )

        if file:
            try:
                with open(file, 'r') as f:
                    config_dict = json.load(f)

                self.input_var.set(config_dict.get("input_folder", ""))
                self.output_var.set(config_dict.get("output_folder", ""))
                self.remove_nav_var.set(config_dict.get("remove_navigation", True))
                self.remove_header_var.set(config_dict.get("remove_headers_footers", True))
                self.remove_boilerplate_var.set(config_dict.get("remove_boilerplate", True))
                self.enable_llm_var.set(config_dict.get("enable_llm_validation", False))
                self.chunk_size_var.set(config_dict.get("chunk_size", 1000))
                self.overlap_var.set(config_dict.get("overlap_size", 200))
                self.max_cost_var.set(config_dict.get("max_cost", "0.05"))
                self.rate_limit_var.set(config_dict.get("rate_limit", 500))

                messagebox.showinfo("Success", "Configuration loaded!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load config: {e}")

    def export_results(self):
        """Export results to file"""
        if not self.processed_files:
            messagebox.showwarning("Warning", "No results to export")
            return

        file = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("CSV files", "*.csv"), ("Text files", "*.txt")]
        )

        if file:
            try:
                if file.endswith('.json'):
                    results_data = [r.to_dict() for r in self.processed_files]
                    with open(file, 'w') as f:
                        json.dump(results_data, f, indent=2)

                elif file.endswith('.csv'):
                    with open(file, 'w') as f:
                        f.write("File,Status,Original,Cleaned,Reduction%,Time\n")
                        for r in self.processed_files:
                            status = "OK" if r.success else "FAIL"
                            f.write(f"{r.input_file.name},{status},{r.original_size},{r.cleaned_size},{r.reduction_percentage:.1f},{r.processing_time:.3f}\n")

                elif file.endswith('.txt'):
                    with open(file, 'w') as f:
                        f.write("PostScraperCleaner Results\n")
                        f.write("=" * 80 + "\n\n")
                        for r in self.processed_files:
                            f.write(f"File: {r.input_file.name}\n")
                            f.write(f"Status: {'✓ OK' if r.success else '✗ FAIL'}\n")
                            f.write(f"Original: {r.original_size} bytes\n")
                            f.write(f"Cleaned: {r.cleaned_size} bytes\n")
                            f.write(f"Reduction: {r.reduction_percentage:.1f}%\n")
                            f.write(f"Time: {r.processing_time:.3f}s\n")
                            f.write("-" * 80 + "\n\n")

                messagebox.showinfo("Success", f"Results exported to {file}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export: {e}")

    def open_output_folder(self):
        """Open output folder in file explorer"""
        output_path = Path(self.output_var.get())
        if output_path.exists():
            import subprocess
            import sys

            if sys.platform == 'darwin':  # macOS
                subprocess.run(['open', str(output_path)])
            elif sys.platform == 'win32':  # Windows
                subprocess.run(['explorer', str(output_path)])
            else:  # Linux
                subprocess.run(['xdg-open', str(output_path)])

    def show_about(self):
        """Show about dialog"""
        messagebox.showinfo("About", """PostScraperCleaner v1.0

Document cleaning and optimization for vector database ingestion.

Removes navigation, boilerplate, and redundant content from scraped documentation.

© 2025 - Claude Code""")

    def _build_config(self) -> CleaningConfig:
        """Build config from UI values"""
        return CleaningConfig(
            remove_navigation=self.remove_nav_var.get(),
            remove_headers_footers=self.remove_header_var.get(),
            remove_boilerplate=self.remove_boilerplate_var.get(),
            enable_llm_validation=self.enable_llm_var.get(),
            target_chunk_size=self.chunk_size_var.get(),
            overlap_size=self.overlap_var.get(),
            max_cost_per_document=float(self.max_cost_var.get()),
            rate_limit_rpm=self.rate_limit_var.get(),
            openai_api_key=os.getenv("OPENAI_API_KEY")  # Load from .env
        )


def main():
    """Main entry point"""
    root = tk.Tk()
    app = PostScraperCleanerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
