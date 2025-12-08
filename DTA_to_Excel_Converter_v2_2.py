# ====================================================
# DTA to Excel Converter (v2.2)
# Author: Zidane Syukri <zimasu.pro@gmail.com>
# Version: 2.2
# Description: Converts large Stata files (.dta) to multiple Excel sheets (.xlsx) safely using pandas
# Requirements: Python 3.13.5, pyreadstat, pandas, openpyxl, tkinter
# License: MIT
# ====================================================

import os
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import pyreadstat

MAX_ROWS_PER_SHEET = 1000000  # Excel limit

# ---------------- Core Functions ----------------

def select_dta_file():
    return filedialog.askopenfilename(
        title="Select a Stata (.dta) file",
        filetypes=[("Stata files", "*.dta")]
    )

def load_dta(file_path):
    try:
        df, _ = pyreadstat.read_dta(file_path)
        return df
    except Exception as e:
        raise RuntimeError(f"Failed to load .dta file:\n{e}")

def save_to_excel(df, file_path):
    output_path = os.path.splitext(file_path)[0] + ".xlsx"
    try:
        # Use pandas ExcelWriter to allow multiple sheets
        with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
            total_rows = len(df)
            num_sheets = (total_rows // MAX_ROWS_PER_SHEET) + (1 if total_rows % MAX_ROWS_PER_SHEET else 0)

            for i, start in enumerate(range(0, total_rows, MAX_ROWS_PER_SHEET)):
                end = start + MAX_ROWS_PER_SHEET
                sheet_df = df.iloc[start:end]
                writer.sheets  # ensure writer initialized
                sheet_name = f"Sheet{i+1}"
                sheet_df.to_excel(writer, sheet_name=sheet_name, index=False)

        return output_path
    except Exception as e:
        raise RuntimeError(f"Failed to save Excel file:\n{e}")

def notify_completion(output_path):
    messagebox.showinfo(
        "Conversion Complete ✅",
        f"Excel file successfully created:\n{output_path}"
    )

# ---------------- Loading Popup (Centered) ----------------

class LoadingPopup:
    def __init__(self, parent, title="Please Wait", message="Converting file..."):
        self.top = tk.Toplevel(parent)
        self.top.title(title)
        self.top.resizable(False, False)
        self.top.grab_set()  # Modal
        self.top.configure(bg="#f0f0f0")

        width, height = 300, 100

        # Center over parent window
        parent.update_idletasks()
        parent_x = parent.winfo_x()
        parent_y = parent.winfo_y()
        parent_w = parent.winfo_width()
        parent_h = parent.winfo_height()
        x = parent_x + (parent_w - width) // 2
        y = parent_y + (parent_h - height) // 2
        self.top.geometry(f"{width}x{height}+{x}+{y}")

        tk.Label(self.top, text=message, font=("Segoe UI", 10), bg="#f0f0f0").pack(pady=(20, 10))
        self.progress = ttk.Progressbar(self.top, mode="indeterminate")
        self.progress.pack(padx=20, fill="x")
        self.progress.start(10)

    def close(self):
        self.progress.stop()
        self.top.destroy()

# ---------------- Conversion Runner ----------------

def run_conversion(file_path, parent_window):
    if not file_path:
        return
    popup = LoadingPopup(parent_window)

    def task():
        try:
            df = load_dta(file_path)
            output_path = save_to_excel(df, file_path)
            popup.close()
            notify_completion(output_path)
        except RuntimeError as e:
            popup.close()
            messagebox.showerror("Error", str(e))

    threading.Thread(target=task, daemon=True).start()

# ---------------- GUI Setup ----------------

def create_main_window():
    root = tk.Tk()
    root.title("DTA to Excel Converter")
    width, height = 400, 150
    root.geometry(f"{width}x{height}")
    root.resizable(False, False)
    root.configure(bg="#f0f0f0")

    # Center window
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

    # Footer
    tk.Label(
        root,
        text="Version 2.2 | Zidane Syukri",
        font=("Segoe UI", 8),
        bg="#f0f0f0",
        fg="#666666"
    ).pack(side="bottom", pady=5)

    return root

def add_widgets(window):
    tk.Label(
        window,
        text="DTA to Excel Converter",
        font=("Segoe UI", 14, "bold"),
        bg="#f0f0f0",
        fg="#222222"
    ).pack(pady=(20, 10))

    btn = tk.Button(
        window,
        text="Select .dta File",
        width=24,
        height=2,
        bg="#e0e0e0",
        relief="raised",
        font=("Segoe UI", 11),
        command=lambda: run_conversion(select_dta_file(), window)
    )
    btn.pack(pady=(0, 10))
    btn.bind("<Enter>", lambda e: btn.config(bg="#d0d0d0", relief="groove"))
    btn.bind("<Leave>", lambda e: btn.config(bg="#e0e0e0", relief="raised"))

# ---------------- Main Runner ----------------

def main():
    window = create_main_window()
    add_widgets(window)
    window.mainloop()

if __name__ == "__main__":
    main()
