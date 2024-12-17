from Component.config import *
import customtkinter as ctk
def loged_user(usuario,root):
    #confirma que el usuario es correcto, destruye la ventana del login y abre la nueva ventana
    root.destroy()
    ctk.set_appearance_mode("dark")
    root = ctk.CTk()
    root.mainloop()