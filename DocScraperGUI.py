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
from pathlib import Path
from datetime import datetime

from DocScraper import DocumentationScraper


class DocScraperGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Documentation Scraper")
        self.root.geometry("800x600")
        
        # Variables
        self.scraping = False
        self.scraper_thread = None
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the user interface."""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(4, weight=1)
        
        # URL Input
        ttk.Label(main_frame, text="Starting URL:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.url_var = tk.StringVar(value="https://docs.anthropic.com")
        self.url_entry = ttk.Entry(main_frame, textvariable=self.url_var, width=50)
        self.url_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Output Directory
        ttk.Label(main_frame, text="Output Directory:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.output_var = tk.StringVar(value="scraped_docs")
        self.output_entry = ttk.Entry(main_frame, textvariable=self.output_var, width=40)
        self.output_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 50))
        
        self.browse_btn = ttk.Button(main_frame, text="Browse", command=self.browse_directory)
        self.browse_btn.grid(row=1, column=1, sticky=tk.E, pady=5)
        
        # Max Pages
        ttk.Label(main_frame, text="Max Pages:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.max_pages_var = tk.IntVar(value=1000)
        self.max_pages_spinbox = ttk.Spinbox(
            main_frame, 
            from_=1, 
            to=10000, 
            textvariable=self.max_pages_var,
            width=10
        )
        self.max_pages_spinbox.grid(row=2, column=1, sticky=tk.W, pady=5, padx=(10, 0))
        
        # Control Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)
        
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
        self.progress.grid(row=3, column=1, sticky=(tk.W, tk.E), padx=(100, 0), pady=10)
        
        # Log Output
        log_frame = ttk.LabelFrame(main_frame, text="Scraping Log", padding="5")
        log_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        
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
            
    def log(self, message, level="INFO"):
        """Add message to log."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        formatted_message = f"[{timestamp}] {level}: {message}\n"
        
        self.log_text.insert(tk.END, formatted_message)
        self.log_text.see(tk.END)
        self.root.update_idletasks()
        
    def clear_log(self):
        """Clear the log text."""
        self.log_text.delete(1.0, tk.END)
        
    def update_status(self, message):
        """Update status bar."""
        self.status_var.set(message)
        self.root.update_idletasks()
        
    def start_scraping(self):
        """Start the scraping process."""
        if self.scraping:
            messagebox.showwarning("Warning", "Scraping is already in progress!")
            return
            
        # Validate inputs
        url = self.url_var.get().strip()
        if not url:
            messagebox.showerror("Error", "Please enter a starting URL")
            return
            
        if not url.startswith(('http://', 'https://')):
            messagebox.showerror("Error", "URL must start with http:// or https://")
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
            
    def run_scraper(self, url, output_dir, max_pages):
        """Run the scraper in a separate thread."""
        try:
            self.log(f"Starting scrape of {url}", "INFO")
            self.log(f"Output directory: {output_dir}", "INFO")
            self.log(f"Max pages: {max_pages}", "INFO")
            self.update_status("Scraping in progress...")
            
            # Create new event loop for thread
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            
            # Create custom scraper that logs to GUI
            scraper = GUIScraper(output_dir, self)
            
            # Run scraper
            loop.run_until_complete(
                scraper.scrape_documentation(url, max_pages)
            )
            
            self.log("Scraping completed successfully!", "SUCCESS")
            self.update_status("Scraping completed")
            messagebox.showinfo("Success", f"Scraping completed!\nFiles saved to: {output_dir}")
            
        except Exception as e:
            self.log(f"Error during scraping: {str(e)}", "ERROR")
            self.update_status("Error occurred")
            messagebox.showerror("Error", f"Scraping failed:\n{str(e)}")
            
        finally:
            self.scraping = False
            self.progress.stop()
            self.start_btn.config(state=tk.NORMAL)
            self.stop_btn.config(state=tk.DISABLED)
            loop.close()


class GUIScraper(DocumentationScraper):
    """Custom scraper that logs to GUI."""
    
    def __init__(self, output_dir, gui):
        super().__init__(output_dir)
        self.gui = gui
        
    async def scrape_page(self, crawler, url):
        """Override to add GUI logging."""
        if not self.gui.scraping:
            return None
            
        self.gui.log(f"Scraping: {url}")
        result = await super().scrape_page(crawler, url)
        
        if result:
            self.gui.log(f"Saved: {result['filepath']} ({result.get('links', []).__len__()} links found)")
            self.gui.update_status(f"Scraped {len(self.visited_urls)} pages")
        else:
            self.gui.log(f"Failed: {url}", "WARNING")
            
        return result


def main():
    """Main entry point."""
    root = tk.Tk()
    
    # Try to use a modern theme
    try:
        root.tk.call("source", "azure.tcl")
        root.tk.call("set_theme", "light")
    except:
        try:
            style = ttk.Style()
            style.theme_use('clam')
        except:
            pass
    
    app = DocScraperGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()