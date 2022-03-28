import tkinter as tk
from tkinter import Entry, filedialog
import sphere
import os

root = tk.Tk()

e = Entry(root, bg='#ffd100', width=15)
e.insert(5, 'Enter a radius...')
e.pack()

root.configure(bg='#333533')

def open_file():
  for widget in frame.winfo_children():
    widget.destroy()
  filename = filedialog.askopenfile(initialdir='/', title='Select File',
  filetypes=(('text files', '*.txt'), ('all files', '*.*')))
  label = tk.Label(frame, text=filename.name, bg='#ffd100')
  label.pack()


canvas = tk.Canvas(root, height=700, width=700, bg='#333533')
canvas.pack()

frame = tk.Frame(root, bg='#202020')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
btn_open_file = tk.Button(root, text="Open File", padx=10, pady=5, fg='white', bg='#333533', command=open_file)
btn_open_file.place(relx=0.5, rely=0.8, anchor='center')

root.mainloop()