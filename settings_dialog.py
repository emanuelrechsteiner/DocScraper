#!/usr/bin/env python3
"""
Settings Dialog for DocScraper
Allows users to configure scraper engine and API keys.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from scraper_config import ScraperConfig


class SettingsDialog:
    """Settings dialog for configuring scraper options."""

    def __init__(self, parent):
        """
        Initialize settings dialog.

        Args:
            parent: Parent window
        """
        self.parent = parent
        self.config = ScraperConfig()
        self.dialog = None
        self.result = False

        # Variables
        self.engine_var = None
        self.firecrawl_key_var = None
        self.openai_key_var = None

    def show(self) -> bool:
        """
        Show the settings dialog.

        Returns:
            True if settings were saved, False if cancelled
        """
        # Create modal dialog
        self.dialog = tk.Toplevel(self.parent)
        self.dialog.title("Scraper Settings")
        self.dialog.geometry("600x400")
        self.dialog.resizable(False, False)
        self.dialog.transient(self.parent)
        self.dialog.grab_set()

        # Center dialog
        self._center_dialog()

        # Create UI
        self._create_ui()

        # Load current settings
        self._load_settings()

        # Wait for dialog to close
        self.parent.wait_window(self.dialog)

        return self.result

    def _center_dialog(self):
        """Center the dialog on the parent window."""
        self.dialog.update_idletasks()

        # Get parent window position and size
        parent_x = self.parent.winfo_x()
        parent_y = self.parent.winfo_y()
        parent_width = self.parent.winfo_width()
        parent_height = self.parent.winfo_height()

        # Get dialog size
        dialog_width = self.dialog.winfo_width()
        dialog_height = self.dialog.winfo_height()

        # Calculate position
        x = parent_x + (parent_width - dialog_width) // 2
        y = parent_y + (parent_height - dialog_height) // 2

        self.dialog.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")

    def _create_ui(self):
        """Create the settings dialog UI."""
        # Main frame
        main_frame = ttk.Frame(self.dialog, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        title_label = ttk.Label(
            main_frame,
            text="Scraper Configuration",
            font=('TkDefaultFont', 12, 'bold')
        )
        title_label.pack(pady=(0, 20))

        # Scraper Engine Section
        engine_frame = ttk.LabelFrame(main_frame, text="Scraper Engine", padding="10")
        engine_frame.pack(fill=tk.X, pady=(0, 15))

        self.engine_var = tk.StringVar()

        # Crawl4AI option
        crawl4ai_radio = ttk.Radiobutton(
            engine_frame,
            text="Crawl4AI (Free, Open Source)",
            variable=self.engine_var,
            value=ScraperConfig.ENGINE_CRAWL4AI,
            command=self._on_engine_change
        )
        crawl4ai_radio.pack(anchor=tk.W, pady=2)

        crawl4ai_desc = ttk.Label(
            engine_frame,
            text="Uses the free crawl4ai library. No API key required.",
            font=('TkDefaultFont', 8),
            foreground='gray'
        )
        crawl4ai_desc.pack(anchor=tk.W, padx=(25, 0), pady=(0, 10))

        # Firecrawl option
        firecrawl_radio = ttk.Radiobutton(
            engine_frame,
            text="Firecrawl (API Service)",
            variable=self.engine_var,
            value=ScraperConfig.ENGINE_FIRECRAWL,
            command=self._on_engine_change
        )
        firecrawl_radio.pack(anchor=tk.W, pady=2)

        firecrawl_desc = ttk.Label(
            engine_frame,
            text="Uses Firecrawl API service. Requires API key (https://firecrawl.dev)",
            font=('TkDefaultFont', 8),
            foreground='gray'
        )
        firecrawl_desc.pack(anchor=tk.W, padx=(25, 0))

        # API Keys Section
        api_frame = ttk.LabelFrame(main_frame, text="API Keys", padding="10")
        api_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))

        # Firecrawl API Key
        firecrawl_label = ttk.Label(api_frame, text="Firecrawl API Key:")
        firecrawl_label.grid(row=0, column=0, sticky=tk.W, pady=5)

        self.firecrawl_key_var = tk.StringVar()
        self.firecrawl_entry = ttk.Entry(
            api_frame,
            textvariable=self.firecrawl_key_var,
            width=50,
            show="*"
        )
        self.firecrawl_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))

        firecrawl_help = ttk.Label(
            api_frame,
            text="Required for Firecrawl engine. Get your key at https://firecrawl.dev",
            font=('TkDefaultFont', 8),
            foreground='gray'
        )
        firecrawl_help.grid(row=1, column=0, columnspan=2, sticky=tk.W, pady=(0, 10))

        # OpenAI API Key
        openai_label = ttk.Label(api_frame, text="OpenAI API Key:")
        openai_label.grid(row=2, column=0, sticky=tk.W, pady=5)

        self.openai_key_var = tk.StringVar()
        openai_entry = ttk.Entry(
            api_frame,
            textvariable=self.openai_key_var,
            width=50,
            show="*"
        )
        openai_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))

        openai_help = ttk.Label(
            api_frame,
            text="Optional. Used for AI-powered document post-processing.",
            font=('TkDefaultFont', 8),
            foreground='gray'
        )
        openai_help.grid(row=3, column=0, columnspan=2, sticky=tk.W)

        # Configure grid
        api_frame.columnconfigure(1, weight=1)

        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X)

        save_btn = ttk.Button(
            button_frame,
            text="Save",
            command=self._save_settings,
            style="Accent.TButton" if hasattr(ttk.Style(), 'Accent.TButton') else "TButton"
        )
        save_btn.pack(side=tk.RIGHT, padx=(5, 0))

        cancel_btn = ttk.Button(
            button_frame,
            text="Cancel",
            command=self._cancel
        )
        cancel_btn.pack(side=tk.RIGHT)

    def _on_engine_change(self):
        """Handle scraper engine change."""
        engine = self.engine_var.get()

        # Enable/disable Firecrawl API key field based on selection
        if engine == ScraperConfig.ENGINE_FIRECRAWL:
            self.firecrawl_entry.config(state=tk.NORMAL)
        else:
            self.firecrawl_entry.config(state=tk.NORMAL)  # Keep it editable

    def _load_settings(self):
        """Load current settings from config."""
        # Load scraper engine
        engine = self.config.get_scraper_engine()
        self.engine_var.set(engine)

        # Load API keys
        firecrawl_key = self.config.get_firecrawl_api_key()
        if firecrawl_key:
            self.firecrawl_key_var.set(firecrawl_key)

        openai_key = self.config.get_openai_api_key()
        if openai_key:
            self.openai_key_var.set(openai_key)

        # Update UI state
        self._on_engine_change()

    def _save_settings(self):
        """Save settings to config."""
        engine = self.engine_var.get()
        firecrawl_key = self.firecrawl_key_var.get().strip()
        openai_key = self.openai_key_var.get().strip()

        # Validate Firecrawl settings
        if engine == ScraperConfig.ENGINE_FIRECRAWL and not firecrawl_key:
            messagebox.showerror(
                "Validation Error",
                "Firecrawl API key is required when using Firecrawl engine.",
                parent=self.dialog
            )
            self.firecrawl_entry.focus_set()
            return

        # Save engine
        if not self.config.set_scraper_engine(engine):
            messagebox.showerror(
                "Error",
                "Failed to save scraper engine setting.",
                parent=self.dialog
            )
            return

        # Save Firecrawl API key
        if firecrawl_key:
            if not self.config.set_firecrawl_api_key(firecrawl_key):
                messagebox.showerror(
                    "Error",
                    "Failed to save Firecrawl API key.",
                    parent=self.dialog
                )
                return

        # Save OpenAI API key
        if openai_key:
            if not self.config.set_openai_api_key(openai_key):
                messagebox.showerror(
                    "Error",
                    "Failed to save OpenAI API key.",
                    parent=self.dialog
                )
                return

        # Success
        messagebox.showinfo(
            "Settings Saved",
            "Settings have been saved successfully to .env file.",
            parent=self.dialog
        )

        self.result = True
        self.dialog.destroy()

    def _cancel(self):
        """Cancel settings dialog."""
        self.result = False
        self.dialog.destroy()


def show_settings(parent) -> bool:
    """
    Show settings dialog.

    Args:
        parent: Parent window

    Returns:
        True if settings were saved, False if cancelled
    """
    dialog = SettingsDialog(parent)
    return dialog.show()
