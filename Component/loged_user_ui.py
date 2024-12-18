from Component.config import *
import customtkinter as ctk
import cv2
import threading
from tkinter import Label, Frame
from PIL import Image, ImageTk
def show_camara():
    global on
    global cam_lbl
    global cam_lbl1
    global start_btn
    global cam2
    if on is not None:
        ret , frame = on.read()
        if ret == True:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_resized = cv2.resize(frame,(250,250))
            if frame_resized is not None and frame_resized.size > 0:
                im = Image.fromarray(frame_resized)
                img = ImageTk.PhotoImage(im)
                cam_lbl.configure(image = img)
                cam_lbl.image = img
                cam_lbl.after(10,show_camara)
                start_btn.configure(text="Detener")
                cam_lbl.configure(text="")
            else:
                print("tamaño incorrecto")
        else:
            cam_lbl.configure(text="DETENIDO")
            start_btn.configure(text="Comenzar")
            cam_lbl1.configure(text="DETENIDO")
            #cerrar las camaras en grl
            on.release()
            cam2.release()
    if cam2 is not None:
        ret, frame2 = cam2.read()
        if ret == True:
            frame2 = cv2.cvtColor(frame2,cv2.COLOR_BGR2RGB)
            frame_resized2 = cv2.resize(frame2,(250,250))
            if frame_resized2 is not None and frame_resized2.size > 0:
                im2 = Image.fromarray(frame_resized2)
                img2 = ImageTk.PhotoImage(im2)
                cam_lbl1.configure(image= img2)
                cam_lbl1.image = img2
                cam_lbl1.after(10,show_camara)
                cam_lbl1.configure(text="")

def start_capture():
    global on
    global cam2
    #global cam_lbl
    on = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    cam2 = cv2.VideoCapture(1,cv2.CAP_DSHOW)
    show_camara()

def loged_user(usuario,root):
    global cam_lbl
    global start_btn
    global cam_lbl1
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
        height=HEIGHT_BOTONES,corner_radius=10,border_width=2,
        command=start_capture
            )
    start_btn.place(x=200,y=20)

    cam_lbl = ctk.CTkLabel(root,text="")
    cam_lbl.place(x=20,y=200)
    cam_lbl1 = ctk.CTkLabel(root,text="")
    cam_lbl1.place(x=400,y=200)



    root.mainloop()
on = None
cam2 = None