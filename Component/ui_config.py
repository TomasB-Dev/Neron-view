from Component.config import *
import customtkinter as ctk
def Config_Ui():
    ctk.set_appearance_mode("dark")
    config_cams = ctk.CTkToplevel()
    config_cams.after(201, lambda :config_cams.iconbitmap(RUTA_ICONO))
    config_cams.title("Configuracion")
    config_cams.geometry("600x480")
    config_cams.grab_set()
    config_cams.resizable(0,0)