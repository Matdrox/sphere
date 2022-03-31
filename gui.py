import tkinter as tk
import sphere

root = tk.Tk()
root.title('ASCII Sphere')
root.configure(bg='#333533')
root.geometry("720x800")

frame_width = 700
frame_height = 700

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


def create_sphere(r, origin_x, origin_y):
    for widget in frame.winfo_children():
        widget.destroy()
    klot = sphere.Sphere(r, origin_x, origin_y)
    lbl_sphere = tk.Label(frame, width=100, height=100, bg='black',
                          fg='white', font=('Kemco Pixel', 8), text=klot.calc())
    lbl_sphere.pack()


btn_create_sphere = tk.Button(root, width=15, bg='#ffd100', text='Create Sphere', command=lambda: create_sphere(
    int(tbx_radius.get()), int(tbx_origin_x.get()), int(tbx_origin_y.get())))
btn_create_sphere.grid(row=2, column=16)

root.mainloop()
