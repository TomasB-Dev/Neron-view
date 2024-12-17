from tkinter import messagebox
def validar_user(user,key):
    print(user,"////", key)
    if user == "user" and key == "key":
        print("Valido, o no?...")
    else:
        messagebox.showerror("Error Login","Contraseña y usuarios incorrectos")