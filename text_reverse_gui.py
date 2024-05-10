# -*- coding=utf-8 -*-
import tkinter as tk
import tkinter.scrolledtext as sct
import pyperclip as cb
from datetime import datetime

def reverse_and_copy():
    # Get the text from the clipboard
    input_text = cb.paste()
    # Remove any '\r' characters
    input_text = input_text.replace("\r", "")
    # Split the text into a list using '\n' as the delimiter
    lines = input_text.split("\n")
    # Remove empty elements ('', None)
    lines = [line for line in lines if line.strip()]
    # Reverse the order of the list
    reversed_lines = lines[::-1]
    # Join the list elements back together using '\n' as the separator
    reversed_text = "\n".join(reversed_lines)
    # Set the reversed text back into the clipboard
    cb.copy(reversed_text)
    # Display the status line
    input_lines = len(lines)
    input_chars = sum(len(line) for line in lines)
    output_lines = len(reversed_lines)
    output_chars = len(reversed_text)
    status_text = f"{datetime.now():%Y-%m-%d %H:%M:%S}\n" \
        f"你貼上了 {input_lines} 行 {input_chars} 個字,\n" \
        f"轉換成 {output_lines} 行 {output_chars} 個字," \
        "複製完成!"
    status_label.config(text=status_text)

    # Display the reversed text in the read-only text area
    output_text_area.config(state=tk.NORMAL)
    output_text_area.delete("1.0", "end")
    output_text_area.insert("1.0", reversed_text)
    output_text_area.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("文字順序顛倒")  # Set window title
root.geometry("600x800")  # Set window size

# Create a dark mode theme (optional)
root.tk_setPalette(background="#333", foreground="white")

FONT = ("新細明體", 16)

# Create the combined button
combined_button = tk.Button(root, text="顛倒文字順序 & 複製到剪貼簿", command=reverse_and_copy, font=FONT)
combined_button.pack(pady=5)

# Create the read-only text area for displaying the output
output_text_area = sct.ScrolledText(root, wrap=tk.WORD, height=10, width=1, font=FONT)
output_text_area.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)
output_text_area.config(state=tk.DISABLED)

# Create the status label
status_label = tk.Label(root, text="", anchor="w", font=FONT, justify="left")
status_label.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

try:
    # Start the tkinter event loop
    root.mainloop()
except KeyboardInterrupt:
    print('強制關閉!')
