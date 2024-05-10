import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import tkinter.messagebox as messagebox
import tkinter.simpledialog as simpledialog
import pyperclip

def reverse_text():
    # Get the text from the text area
    input_text = text_area.get("1.0", "end-1c")

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

    # Set the reversed text back into the text area
    text_area.delete("1.0", "end")
    text_area.insert("1.0", reversed_text)

def copy_to_clipboard():
    # Get the text from the text area
    text_to_copy = text_area.get("1.0", "end-1c")

    # Copy the text to the clipboard
    pyperclip.copy(text_to_copy)
    messagebox.showinfo("複製成功", "已複製到剪貼簿！")

# Create the main window
root = tk.Tk()
root.title("文字順序顛倒")  # Set window title

# Create a dark mode theme (optional)
root.tk_setPalette(background="#333", foreground="white")

# Create the text area
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10, width=40)
text_area.pack(padx=10, pady=10)

# Create the buttons
reverse_button = tk.Button(root, text="顛倒", command=reverse_text)
reverse_button.pack(side=tk.LEFT, padx=5)

copy_button = tk.Button(root, text="複製", command=copy_to_clipboard)
copy_button.pack(side=tk.RIGHT, padx=5)

# Start the tkinter event loop
root.mainloop()

