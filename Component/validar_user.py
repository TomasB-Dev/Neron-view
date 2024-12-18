from tkinter import messagebox
from Component.loged_user_ui import *
#momentaneo hasta tener base de datos, web etc.
def validar_user(user,key,root):
    if user == "user" and key == "key":
        loged_user(user,root)
    else:
        messagebox.showerror("Error Login","Contraseña y usuarios incorrectos")