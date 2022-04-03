import tkinter as tk
from tkinter import Entry, filedialog
import sphere
import os


def open_file():
    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfile(initialdir='/', title='Select File',
                                      filetypes=(('text files', '*.txt'), ('all files', '*.*')))
    label = tk.Label(frame, text=filename.name, bg='#ffd100')
    label.pack()


def change_pos(event):
  print('CLICK')

root = tk.Tk()
root.configure(bg='#333533')

e = Entry(root, bg='#ffd100', width=15)
e.insert(5, 'Enter a radius...')
e.pack()


canvas = tk.Canvas(root, height=700, width=700, bg='#333533')
canvas.pack()

frame = tk.Frame(root, bg='#202020')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

btn_open_file = tk.Button(root, text="Open File", padx=10,
                          pady=5, fg='white', bg='#333533', command=open_file)
btn_open_file.place(relx=0.5, rely=0.8, anchor='center')

root.bind("<Button-1>", change_pos)

root.mainloop()
