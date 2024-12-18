from Component.config import *
import customtkinter as ctk
import cv2
import threading
from tkinter import Label, Frame
from PIL import Image, ImageTk


def loged_user(usuario,root):
    root.destroy()
    ctk.set_appearance_mode("dark")
    root = ctk.CTk()
    root.title(APP_NAME+f"({usuario})")
    root.resizable(0,0)
    root.geometry(APP_SCREEN)


    config_btn = ctk.CTkButton(
        root, text="Configuración", font=LOGIN_FONT,
        height=HEIGHT_BOTONES, corner_radius=10, border_width=2
    )
    config_btn.place(x=20, y=20)

    start_btn = ctk.CTkButton(
        root,text="Comenzar",font=LOGIN_FONT,
        height=HEIGHT_BOTONES,corner_radius=10,border_width=2
            )
    start_btn.place(x=200,y=20)

    stop_btn = ctk.CTkButton(
        root,text="Detener",font=LOGIN_FONT,
        height=HEIGHT_BOTONES,corner_radius=10,border_width=2
        )
    stop_btn.place(x=380,y=20)





    root.mainloop()
    