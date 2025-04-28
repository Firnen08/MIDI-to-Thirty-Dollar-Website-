import tkinter as tk
from tkinter import filedialog, messagebox
import os
import main
import threading
import sys

def run_gui():
    def select_file():
        file_path = filedialog.askopenfilename(
            title="Select MIDI file",
            filetypes=[("MIDI files", "*.mid")],
            initialdir=os.path.abspath("in")
        )
        if file_path:
            entry_file.delete(0, tk.END)
            entry_file.insert(0, file_path)
            status_var.set(f"Selected: {os.path.basename(file_path)}")

    def convert():
        midi_path = entry_file.get()
        if not midi_path or not os.path.isfile(midi_path):
            messagebox.showerror("Error", "Please select a valid MIDI file.")
            status_var.set("No valid MIDI file selected.")
            return
        try:
            status_var.set("Converting...")
            root.update_idletasks()
            output_path = main.convert_file(midi_path)
            lbl_result.config(text=f"✅ Done!\nOutput: {output_path}")
            status_var.set("Conversion successful.")
        except Exception as e:
            messagebox.showerror("Conversion Error", str(e))
            status_var.set("Conversion failed.")

    def clear_selection():
        entry_file.delete(0, tk.END)
        lbl_result.config(text="")
        status_var.set("Selection cleared.")

    root = tk.Tk()
    root.title("MIDI to Thirty Dollar Website Converter")
    root.resizable(False, False)

    lbl_title = tk.Label(root, text="🗿 MIDI to Thirty Dollar Website Converter 🗿", font=("Segoe UI", 16, "bold"), pady=10)
    lbl_title.pack()

    frm = tk.Frame(root, padx=20, pady=10)
    frm.pack()

    lbl = tk.Label(frm, text="Select a MIDI file to convert", font=("Segoe UI", 11))
    lbl.grid(row=0, column=0, columnspan=2, sticky="n", pady=(0, 8), padx=0)

    entry_file = tk.Entry(frm, width=40, font=("Segoe UI", 10))
    entry_file.grid(row=1, column=0, columnspan=2, pady=(0, 8))

    btn_browse = tk.Button(frm, text="Browse...", command=select_file, width=12)
    btn_browse.grid(row=2, column=0, pady=(0, 8), padx=(0, 4), sticky="e")

    btn_clear = tk.Button(frm, text="Clear", command=clear_selection, width=10)
    btn_clear.grid(row=2, column=1, pady=(0, 8), padx=(4, 0), sticky="w")

    btn_convert = tk.Button(frm, text="Convert", command=convert, width=20, bg="#4CAF50", fg="white", font=("Segoe UI", 10, "bold"))
    btn_convert.grid(row=3, column=0, columnspan=2, pady=(5, 0), sticky="n")

    lbl_result = tk.Label(frm, text="", fg="green", wraplength=350, justify="center", font=("Segoe UI", 10))
    lbl_result.grid(row=4, column=0, columnspan=2, pady=(12, 0), sticky="n")

    status_var = tk.StringVar()
    status_var.set("Ready.")
    status_bar = tk.Label(root, textvariable=status_var, bd=1, relief=tk.SUNKEN, anchor="w", font=("Segoe UI", 9), padx=8)
    status_bar.pack(fill=tk.X, side=tk.BOTTOM, ipady=2)

    root.mainloop()
