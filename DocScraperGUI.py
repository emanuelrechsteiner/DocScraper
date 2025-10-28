#!/usr/bin/env python3
"""
Documentation Scraper GUI
A simple GUI interface for the documentation scraper.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import threading
import asyncio
import sys
import queue
from pathlib import Path
from datetime import datetime

from DocScraper import DocumentationScraper
from firecrawl_scraper import FirecrawlDocumentationScraper
from scraper_config import ScraperConfig
from scraper_factory import ScraperFactory
from settings_dialog import show_settings


class DocScraperGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Documentation Scraper")
        self.root.geometry("900x700")
        self.root.minsize(600, 500)
        
        # Variables
        self.scraping = False
        self.scraper_thread = None
        self.current_scraper = None

        # Configuration
        self.config = ScraperConfig()

        # Thread-safe message queue
        self.message_queue = queue.Queue()
        
        # Configure style
        self.setup_styles()
        self.setup_ui()

        # Update engine info display
        self.update_engine_info()

        # Center window and start checking for messages
        self.center_window()
        self.check_messages()
    
    def setup_styles(self):
        """Configure modern styling for the GUI."""
        try:
            style = ttk.Style()
            style.theme_use('clam')
            
            # Configure button styles
            style.configure("Accent.TButton", 
                          background='#007ACC',
                          foreground='white',
                          font=('TkDefaultFont', 9, 'bold'))
            style.map("Accent.TButton",
                     background=[('active', '#005a9e')])
        except Exception:
            pass
    
    def center_window(self):
        """Center the window on the screen."""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def check_messages(self):
        """Check for messages from scraper thread."""
        try:
            while True:
                msg_type, data = self.message_queue.get_nowait()
                
                if msg_type == "log":
                    self._log_to_widget(data["message"], data["level"])
                elif msg_type == "status":
                    self.status_var.set(data)
                elif msg_type == "complete":
                    self._scraping_complete(data)
                elif msg_type == "error":
                    self._scraping_error(data)
                    
        except queue.Empty:
            pass
        finally:
            # Schedule next check
            self.root.after(100, self.check_messages)
    
    def _log_to_widget(self, message, level="INFO"):
        """Add message to log widget (called on main thread)."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        formatted_message = f"[{timestamp}] {level}: {message}\n"
        
        self.log_text.insert(tk.END, formatted_message)
        self.log_text.see(tk.END)
    
    def _scraping_complete(self, output_dir):
        """Handle scraping completion (called on main thread)."""
        self.scraping = False
        self.progress.stop()
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        
        messagebox.showinfo("Success", f"Scraping completed!\nFiles saved to: {output_dir}")
    
    def _scraping_error(self, error_msg):
        """Handle scraping error (called on main thread)."""
        self.scraping = False
        self.progress.stop()
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        
        messagebox.showerror("Error", f"Scraping failed:\n{error_msg}")
        
    def setup_ui(self):
        """Setup the user interface."""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(6, weight=1)
        
        # URL Input
        url_frame = ttk.Frame(main_frame)
        url_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        url_frame.columnconfigure(1, weight=1)
        
        ttk.Label(url_frame, text="Starting URL:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        self.url_var = tk.StringVar(value="https://docs.anthropic.com")
        self.url_entry = ttk.Entry(url_frame, textvariable=self.url_var, width=50)
        self.url_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))
        
        # Output Directory
        output_frame = ttk.Frame(main_frame)
        output_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        output_frame.columnconfigure(1, weight=1)
        
        ttk.Label(output_frame, text="Output Directory:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        self.output_var = tk.StringVar(value="scraped_docs")
        self.output_entry = ttk.Entry(output_frame, textvariable=self.output_var, width=40)
        self.output_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 10))
        
        self.browse_btn = ttk.Button(output_frame, text="Browse", command=self.browse_directory)
        self.browse_btn.grid(row=0, column=2, sticky=tk.W)
        
        # Max Pages
        pages_frame = ttk.Frame(main_frame)
        pages_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(pages_frame, text="Max Pages:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        self.max_pages_var = tk.IntVar(value=1000)
        self.max_pages_spinbox = ttk.Spinbox(
            pages_frame, 
            from_=1, 
            to=10000, 
            textvariable=self.max_pages_var,
            width=10
        )
        self.max_pages_spinbox.grid(row=0, column=1, sticky=tk.W)
        ttk.Label(pages_frame, text="(Set to high value for complete documentation scraping)", 
                 font=('TkDefaultFont', 8)).grid(row=0, column=2, sticky=tk.W, padx=(10, 0))
        
        # Scraper Engine Info
        engine_frame = ttk.Frame(main_frame)
        engine_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)

        ttk.Label(engine_frame, text="Scraper Engine:").pack(side=tk.LEFT)
        self.engine_info_var = tk.StringVar()
        self.engine_info_label = ttk.Label(
            engine_frame,
            textvariable=self.engine_info_var,
            font=('TkDefaultFont', 9, 'bold')
        )
        self.engine_info_label.pack(side=tk.LEFT, padx=(5, 0))

        # Control Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=4, column=0, columnspan=2, pady=10)

        self.settings_btn = ttk.Button(
            button_frame,
            text="Settings",
            command=self.show_settings
        )
        self.settings_btn.pack(side=tk.LEFT, padx=5)

        self.start_btn = ttk.Button(
            button_frame,
            text="Start Scraping",
            command=self.start_scraping,
            style="Accent.TButton"
        )
        self.start_btn.pack(side=tk.LEFT, padx=5)

        self.stop_btn = ttk.Button(
            button_frame,
            text="Stop",
            command=self.stop_scraping,
            state=tk.DISABLED
        )
        self.stop_btn.pack(side=tk.LEFT, padx=5)

        self.clear_btn = ttk.Button(
            button_frame,
            text="Clear Log",
            command=self.clear_log
        )
        self.clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Progress
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)

        # Log Output
        log_frame = ttk.LabelFrame(main_frame, text="Scraping Log", padding="5")
        log_frame.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        
        self.log_text = scrolledtext.ScrolledText(
            log_frame, 
            wrap=tk.WORD, 
            width=70, 
            height=20,
            bg='#f0f0f0'
        )
        self.log_text.pack(fill=tk.BOTH, expand=True)
        
        # Status Bar
        self.status_var = tk.StringVar(value="Ready to scrape")
        self.status_bar = ttk.Label(
            self.root, 
            textvariable=self.status_var, 
            relief=tk.SUNKEN
        )
        self.status_bar.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
    def browse_directory(self):
        """Open directory browser."""
        directory = filedialog.askdirectory()
        if directory:
            self.output_var.set(directory)

    def show_settings(self):
        """Show settings dialog."""
        if self.scraping:
            messagebox.showwarning("Warning", "Cannot change settings while scraping is in progress!")
            return

        # Show settings dialog
        if show_settings(self.root):
            # Settings were saved, reload config
            self.config = ScraperConfig()
            self.update_engine_info()
            self.log("Settings updated successfully", "INFO")

    def update_engine_info(self):
        """Update the engine info display."""
        info = ScraperFactory.get_scraper_info(self.config)
        self.engine_info_var.set(info['message'])

        # Update label color based on configuration status
        if info['is_configured']:
            self.engine_info_label.config(foreground='green')
        else:
            self.engine_info_label.config(foreground='red')

    def log(self, message, level="INFO"):
        """Thread-safe logging."""
        self.message_queue.put(("log", {"message": message, "level": level}))
        
    def clear_log(self):
        """Clear the log text."""
        self.log_text.delete(1.0, tk.END)
        
    def update_status(self, message):
        """Thread-safe status update."""
        self.message_queue.put(("status", message))
        
    def start_scraping(self):
        """Start the scraping process."""
        if self.scraping:
            messagebox.showwarning("Warning", "Scraping is already in progress!")
            return
            
        # Validate inputs
        url = self.url_var.get().strip()
        if not url:
            messagebox.showerror("Error", "Please enter a starting URL")
            self.url_entry.focus_set()
            return
            
        if not url.startswith(('http://', 'https://')):
            messagebox.showerror("Error", "URL must start with http:// or https://")
            self.url_entry.focus_set()
            self.url_entry.select_range(0, tk.END)
            return
            
        # Validate max pages
        max_pages = self.max_pages_var.get()
        if max_pages < 1:
            messagebox.showerror("Error", "Max pages must be at least 1")
            self.max_pages_spinbox.focus_set()
            return
            
        # Start scraping in separate thread
        self.scraping = True
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.progress.start(10)
        
        self.scraper_thread = threading.Thread(
            target=self.run_scraper,
            args=(url, self.output_var.get(), self.max_pages_var.get())
        )
        self.scraper_thread.daemon = True
        self.scraper_thread.start()
        
    def stop_scraping(self):
        """Stop the scraping process."""
        if self.scraping:
            self.scraping = False
            self.log("Stopping scraper...", "WARNING")
            self.update_status("Stopping...")
            
            # Signal the scraper to stop
            if self.current_scraper:
                self.current_scraper.stop()
            
            # Reset GUI state immediately 
            self.progress.stop()
            self.start_btn.config(state=tk.NORMAL)
            self.stop_btn.config(state=tk.DISABLED)
            
    def run_scraper(self, url, output_dir, max_pages):
        """Run the scraper in a separate thread."""
        try:
            # Get scraper info
            info = ScraperFactory.get_scraper_info(self.config)
            engine = self.config.get_scraper_engine()

            self.log(f"Starting scrape of {url}", "INFO")
            self.log(f"Scraper engine: {info['message']}", "INFO")
            self.log(f"Output directory: {output_dir}", "INFO")
            self.log(f"Max pages: {max_pages}", "INFO")
            self.update_status("Scraping in progress...")

            # Create new event loop for thread
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

            # Create scraper using factory
            try:
                base_scraper = ScraperFactory.create_scraper(output_dir, self.config)
            except ValueError as e:
                self.log(f"Configuration error: {str(e)}", "ERROR")
                self.update_status("Configuration error")
                self.message_queue.put(("error", str(e)))
                return

            # Wrap scraper with GUI logging
            if engine == ScraperConfig.ENGINE_CRAWL4AI:
                # For crawl4ai, use GUIScraper wrapper
                self.current_scraper = GUIScraper(output_dir, self)
            else:
                # For Firecrawl, use FirecrawlGUIScraper wrapper
                self.current_scraper = FirecrawlGUIScraper(
                    self.config.get_firecrawl_api_key(),
                    output_dir,
                    self
                )

            # Run scraper
            loop.run_until_complete(
                self.current_scraper.scrape_documentation(url, max_pages)
            )

            self.log("Scraping completed successfully!", "SUCCESS")
            self.update_status("Scraping completed")

            # Send completion message
            self.message_queue.put(("complete", output_dir))

        except Exception as e:
            self.log(f"Error during scraping: {str(e)}", "ERROR")
            self.update_status("Error occurred")
            self.message_queue.put(("error", str(e)))

        finally:
            self.current_scraper = None
            loop.close()


class GUIScraper(DocumentationScraper):
    """Custom scraper that logs to GUI."""
    
    def __init__(self, output_dir, gui):
        super().__init__(output_dir)
        self.gui = gui
    
    def stop(self):
        """Stop the scraper."""
        self.should_stop = True
        
    async def scrape_page(self, crawler, url):
        """Override to add GUI logging."""
        # Check stop conditions
        if not self.gui.scraping or self.should_stop:
            return None
            
        try:
            self.gui.log(f"Scraping: {url}")
            result = await super().scrape_page(crawler, url)
            
            # Check stop condition again after scraping
            if not self.gui.scraping or self.should_stop:
                return None
            
            if result:
                self.gui.log(f"Saved: {result['filepath']} ({result.get('links', []).__len__()} links found)")
                self.gui.update_status(f"Scraped {len(self.visited_urls)} pages")
            else:
                self.gui.log(f"Failed: {url}", "WARNING")
                
            return result
        except Exception as e:
            self.gui.log(f"Error scraping {url}: {str(e)}", "ERROR")
            return None


class FirecrawlGUIScraper(FirecrawlDocumentationScraper):
    """Custom Firecrawl scraper that logs to GUI."""

    def __init__(self, api_key, output_dir, gui):
        super().__init__(api_key, output_dir)
        self.gui = gui
        self.should_stop = False

    def stop(self):
        """Stop the scraper."""
        self.should_stop = True

    async def scrape_page(self, url):
        """Override to add GUI logging."""
        # Check stop conditions
        if not self.gui.scraping or self.should_stop:
            return None

        try:
            self.gui.log(f"Scraping with Firecrawl: {url}")
            result = await super().scrape_page(url)

            # Check stop condition again after scraping
            if not self.gui.scraping or self.should_stop:
                return None

            if result:
                self.gui.log(f"Saved: {result['filepath']} ({result.get('links', []).__len__()} links found)")
                self.gui.update_status(f"Scraped {len(self.visited_urls)} pages")
            else:
                self.gui.log(f"Failed: {url}", "WARNING")

            return result
        except Exception as e:
            self.gui.log(f"Error scraping {url}: {str(e)}", "ERROR")
            return None


def main():
    """Main entry point."""
    try:
        root = tk.Tk()
        
        # Set window icon if available
        try:
            root.iconname("Documentation Scraper")
        except:
            pass
        
        # Handle window closing
        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                root.destroy()
        
        root.protocol("WM_DELETE_WINDOW", on_closing)
        
        app = DocScraperGUI(root)
        root.mainloop()
        
    except Exception as e:
        print(f"Error starting GUI: {e}")
        messagebox.showerror("Error", f"Failed to start application:\n{e}")
        sys.exit(1)


if __name__ == "__main__":
    main()