'''
Författare: Matei Cananau
Datum: 2022-04-09
Revisionsdatum: 2022-04-13
'''

import tkinter as tk
from tkinter import messagebox
import sphere


def create_sphere():
    try:
        r = int(tbx_radius.get())
        origin_x = int(tbx_origin_x.get())
        origin_y = int(tbx_origin_y.get())
    except ValueError:
        tk.messagebox.showinfo(
            'Invalid values', 'Please submit proper values...')
    klot = sphere.Sphere(r, origin_x, origin_y)
    lbl_sphere.config(text=klot.calc())
    return klot


def save_sphere(klot, file_name):
    if '.txt' in file_name[len(file_name)-4:]:
        klot.save(file_name)
    else:
        klot.save(file_name+'.txt')


def change_pos(event):
    center_x = lbl_sphere.winfo_width()/2
    center_y = lbl_sphere.winfo_height()/2
    min_x = int(center_x-int(tbx_radius.get())*8)
    max_x = int(center_x+int(tbx_radius.get())*8)
    min_y = int(center_y-int(tbx_radius.get())*8)
    max_y = int(center_y+int(tbx_radius.get())*8)

    if len(tbx_radius.get()) > 0:
        # Om musen befinner sig nom sfärens intervall
        if event.x > min_x and event.x < max_x:
            if event.y > min_y and event.y < max_y:
                # Mappar origo från vänster-upp till mitten
                mapped_x = int((event.x - center_x)/int(tbx_radius.get())*2)
                mapped_y = int((event.y - center_y)/int(tbx_radius.get())*2)
                print(f'{mapped_x}, {mapped_y}')
                tbx_origin_x.delete(0, tk.END)
                tbx_origin_y.delete(0, tk.END)
                tbx_origin_x.insert(0, str(mapped_x))
                tbx_origin_y.insert(0, str(mapped_y))
                create_sphere()


root = tk.Tk()
root.title('ASCII Sphere')
root.configure(bg='#333533')
root.geometry("720x800")

frame_width = 700
frame_height = 690

frame = tk.Frame(root, width=frame_width, height=frame_height,
                 borderwidth=10, bg='#202020')
frame.grid(row=0, column=0, columnspan=30, padx=10, pady=10)
frame.pack_propagate(0)

lbl_radius = tk.Label(root, width=20, bg='#333533', anchor='w',
                      fg='#d6d6d6', text='Enter the sphere\'s radius: ')
lbl_origin_x = tk.Label(root, width=20, bg='#333533', anchor='w',
                        fg='#d6d6d6', text='Enter the sphere\'s x-origin: ')
lbl_origin_y = tk.Label(root, width=20, bg='#333533', anchor='w',
                        fg='#d6d6d6', text='Enter the sphere\'s y-origin: ')

tbx_radius = tk.Entry(root, bg='#202020', fg='#d6d6d6', width=15)
tbx_origin_x = tk.Entry(root, bg='#202020', fg='#d6d6d6', width=15)
tbx_origin_y = tk.Entry(root, bg='#202020', fg='#d6d6d6', width=15)

lbl_radius.grid(row=1, column=14)
lbl_origin_x.grid(row=2, column=14)
lbl_origin_y.grid(row=3, column=14)

tbx_radius.grid(row=1, column=15)
tbx_origin_x.grid(row=2, column=15)
tbx_origin_y.grid(row=3, column=15)

text_var = tk.StringVar()       # Variabel för uppdatering av texten

btn_create_sphere = tk.Button(
    root, width=15, bg='#ffd100', text='Create Sphere', command=create_sphere)
btn_create_sphere.grid(row=2, column=16)

tbx_file = tk.Entry(root, bg='#202020', fg='#d6d6d6', width=18)
btn_save_sphere = tk.Button(root, width=15, bg='#ffd100',
                            text='Save Sphere', command=lambda: save_sphere(create_sphere(),
                                                                            tbx_file.get()))
tbx_file.grid(row=2, column=25)
btn_save_sphere.grid(row=3, column=25)

show_sphere = tk.StringVar()
lbl_sphere = tk.Label(frame, width=100, height=100, bg='black',
                      fg='white', font=('Kemco Pixel', 8), text='')
lbl_sphere.pack()

lbl_sphere.bind('<Button-1>', change_pos)

root.mainloop()
