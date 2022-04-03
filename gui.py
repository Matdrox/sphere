import tkinter as tk
import sphere


def create_sphere(r, origin_x, origin_y):
    klot = sphere.Sphere(r, origin_x, origin_y)
    lbl_sphere.config(text=klot.calc())
    return klot


def save_sphere(klot, file_name):
    if '.txt' in file_name[len(file_name)-4:]:
        klot.save(file_name)
    else:
        klot.save(file_name+'.txt')


def change_pos(event):
    if len(tbx_radius.get()) > 0:
        if event.x > int(lbl_sphere.winfo_width()/2-int(tbx_radius.get())*8) and event.x < int(lbl_sphere.winfo_width()/2+int(tbx_radius.get())*8):
            if event.y > int(lbl_sphere.winfo_height()/2-int(tbx_radius.get())*8) and event.y < int(lbl_sphere.winfo_width()/2+int(tbx_radius.get())*8):
                print(
                    f'({str(int(event.x/int(tbx_radius.get())) - int(tbx_radius.get())*2)}, {str(event.y)})')
                # create_sphere(int(tbx_radius.get()), event.x, event.y)
    # print(int(tbx_radius.get()))


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

text_var = tk.StringVar()

btn_create_sphere = tk.Button(root, width=15, bg='#ffd100', text='Create Sphere', command=lambda: create_sphere(
    int(tbx_radius.get()), int(tbx_origin_x.get()), int(tbx_origin_y.get())))
btn_create_sphere.grid(row=2, column=16)

tbx_file = tk.Entry(root, bg='#202020', fg='#d6d6d6', width=18)
btn_save_sphere = tk.Button(root, width=15, bg='#ffd100',
                            text='Save Sphere', command=lambda: save_sphere(create_sphere(
                                int(tbx_radius.get()), int(tbx_origin_x.get()), int(tbx_origin_y.get())),
                                tbx_file.get()))
tbx_file.grid(row=2, column=25)
btn_save_sphere.grid(row=3, column=25)

show_sphere = tk.StringVar()
lbl_sphere = tk.Label(frame, width=100, height=100, bg='black',
                      fg='white', font=('Kemco Pixel', 8), text=text_var.get())
lbl_sphere.pack()

print(text_var.get())

lbl_sphere.bind('<Button-1>', change_pos)

root.mainloop()
