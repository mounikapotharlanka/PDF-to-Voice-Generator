
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

from pypdf import PdfReader
from gtts import gTTS

import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
from pypdf import PdfReader
from gtts import gTTS

selected_pdf = ""


def choose_pdf():
    global selected_pdf

    path = filedialog.askopenfilename(
        title="Select a PDF document",
        filetypes=[("PDF files", "*.pdf")]
    )

    if path:
        selected_pdf = path
        file_label.config(text=Path(path).name)
        status_label.config(text="PDF selected. Ready to convert.")


def convert_pdf():
    if not selected_pdf:
        messagebox.showwarning(
            "Select PDF", "Please select a PDF file first."
        )
        return

    try:
        status_label.config(text="Reading PDF...")
        root.update_idletasks()

        reader = PdfReader(selected_pdf)
        pages = [
            page.extract_text() or ""
            for page in reader.pages
        ]
        text = "\n".join(pages).strip()

        if not text:
            messagebox.showwarning(
                "No text found",
                "This PDF has no extractable text. Try another PDF."
            )
            status_label.config(text="No readable text found.")
            return

        output = filedialog.asksaveasfilename(
            title="Save audio file",
            defaultextension=".mp3",
            initialfile=Path(selected_pdf).stem + ".mp3",
            filetypes=[("MP3 audio", "*.mp3")]
        )

        if not output:
            status_label.config(text="Conversion cancelled.")
            return

        language = language_var.get()
        status_label.config(text="Generating speech. Please wait...")
        root.update_idletasks()

        speech = gTTS(text=text, lang=language)
        speech.save(output)

        status_label.config(text="Conversion completed successfully!")

        messagebox.showinfo(
            "Success",
            f"Your audio was saved here:\n{output}"
        )

    except Exception as error:
        status_label.config(text="Conversion failed.")
        messagebox.showerror(
            "Error",
            f"Unable to convert this PDF.\n\n{error}"
        )


root = tk.Tk()
root.title("PDF to Voice Generator")
root.geometry("620x460")
root.resizable(False, False)
root.configure(bg="#EAF2F8")

header = tk.Frame(root, bg="#17365D", height=110)
header.pack(fill="x")

tk.Label(
    header,
    text="PDF TO VOICE GENERATOR",
    font=("Arial", 21, "bold"),
    bg="#17365D",
    fg="white"
).pack(pady=(22, 5))

tk.Label(
    header,
    text="Convert your documents into spoken audio",
    font=("Arial", 11),
    bg="#17365D",
    fg="white"
).pack()

content = tk.Frame(root, bg="#EAF2F8")
content.pack(fill="both", expand=True, padx=35, pady=22)

tk.Label(
    content,
    text="Step 1: Select your PDF",
    font=("Arial", 12, "bold"),
    bg="#EAF2F8",
    fg="#17365D"
).pack(anchor="w")

tk.Button(
    content,
    text="Browse PDF",
    command=choose_pdf,
    font=("Arial", 11, "bold"),
    bg="#2874A6",
    fg="white",
    padx=18,
    pady=8
).pack(anchor="w", pady=8)

file_label = tk.Label(
    content,
    text="No PDF selected",
    font=("Arial", 10),
    bg="#EAF2F8",
    fg="#34495E",
    wraplength=520
)
file_label.pack(anchor="w", pady=(0, 15))

tk.Label(
    content,
    text="Step 2: Select speech language",
    font=("Arial", 12, "bold"),
    bg="#EAF2F8",
    fg="#17365D"
).pack(anchor="w")

language_var = tk.StringVar(value="en")

language_menu = tk.OptionMenu(
    content,
    language_var,
    "en", "hi", "te", "ta"
)
language_menu.config(font=("Arial", 10), width=12)
language_menu.pack(anchor="w", pady=8)

tk.Label(
    content,
    text="English (en) | Hindi (hi) | Telugu (te) | Tamil (ta)",
    font=("Arial", 9),
    bg="#EAF2F8",
    fg="#566573"
).pack(anchor="w", pady=(0, 15))

tk.Button(
    content,
    text="Convert PDF to Audio",
    command=convert_pdf,
    font=("Arial", 12, "bold"),
    bg="#239B56",
    fg="white",
    padx=20,
    pady=10
).pack()

status_label = tk.Label(
    root,
    text="Ready to convert",
    font=("Arial", 10),
    bg="#D5E8D4",
    fg="#1E5631",
    pady=10
)
status_label.pack(fill="x", side="bottom")

root.mainloop()


def convert_pdf_to_voice():
    pdf_path = filedialog.askopenfilename(
        title="Select a PDF file",
        filetypes=[("PDF files", "*.pdf")]
    )

    if not pdf_path:
        return

    try:
        reader = PdfReader(pdf_path)
        text_parts = []

        for page in reader.pages:
            text = page.extract_text() or ""
            if text.strip():
                text_parts.append(text)

        full_text = "\n".join(text_parts).strip()

        if not full_text:
            messagebox.showwarning(
                "No Text Found",
                "This PDF has no extractable text."
            )
            return

        output_path = filedialog.asksaveasfilename(
            title="Save Audio File",
            defaultextension=".mp3",
            initialfile=Path(pdf_path).stem + ".mp3",
            filetypes=[("MP3 Audio", "*.mp3")]
        )

        if not output_path:
            return

        status_label.config(text="Generating audio...")
        root.update_idletasks()

        # Generate speech in manageable text chunks
        speech = gTTS(text=full_text, lang="en")
        speech.save(output_path)

        status_label.config(text="Conversion completed!")

        messagebox.showinfo(
            "Success",
            "Your audio file was saved at:\n" + output_path
        )

    except Exception as error:
        status_label.config(text="Conversion failed.")
        messagebox.showerror(
            "Error",
            f"Something went wrong:\n{error}"
        )


root = tk.Tk()
root.title("PDF to Voice Generator")
root.geometry("520x300")
root.resizable(False, False)

heading = tk.Label(
    root,
    text="PDF to Voice Generator",
    font=("Arial", 20, "bold")
)
heading.pack(pady=(30, 10))

description = tk.Label(
    root,
    text="Convert your PDF document into spoken audio.",
    font=("Arial", 11)
)
description.pack(pady=5)

convert_button = tk.Button(
    root,
    text="Choose PDF and Convert",
    command=convert_pdf_to_voice,
    font=("Arial", 12),
    padx=20,
    pady=12
)
convert_button.pack(pady=25)

status_label = tk.Label(
    root,
    text="Ready to convert",
    font=("Arial", 10)
)
status_label.pack()

root.mainloop()
