import tkinter as tk
#create window
window = tk.Tk()
window.title("Password Manager")

#create menubar
menubar = tk.Menu(window)
window.config(menu=menubar)

#create a menu
file_menu = tk.Menu(menubar)
file_menu.add_command(label="Import", command=window.destroy)
file_menu.add_command(label="Export", command=window.destroy)
file_menu.add_command(label="Exit", command=window.destroy)

edit_menu = tk.Menu(menubar)
edit_menu.add_command(label="New password", command=window.destroy)
edit_menu.add_command(label="Edit a password", command=window.destroy)
edit_menu.add_command(label="Delete a password", command=window.destroy)

help_menu = tk.Menu(menubar)
help_menu.add_command(label="Help", command=window.destroy)
help_menu.add_command(label="About us", command=window.destroy)

menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Edit", menu=edit_menu)
menubar.add_cascade(label="View", menu=file_menu)
menubar.add_cascade(label="Help", menu=help_menu)
#print some texts
#greeting = tk.Label(text="Hello world")
#greeting.pack()
picture = tk.PhotoImage(file = "Logo-Lilmy.png")
window.iconphoto(False, picture)
#draw window
window.mainloop()
