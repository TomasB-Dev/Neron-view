from Component.config import *
import customtkinter as ctk
import cv2
import threading
from tkinter import Label, Frame
from PIL import Image, ImageTk
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="Component/.env")
cam1 = None
cam2 = None
stop_threads = False
def show_camera(cam, cam_lbl):
    global stop_threads
    while not stop_threads:
        ret, frame = cam.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_resized = cv2.resize(frame, (250, 250))
            if frame_resized is not None and frame_resized.size > 0:
                im = Image.fromarray(frame_resized)
                img = ImageTk.PhotoImage(im)
                cam_lbl.configure(image=img)
                cam_lbl.image = img
        else:
            cam_lbl.configure(text="DETENIDO")
        
        cv2.waitKey(10)

def start_capture():
    global cam1, cam2, stop_threads, cam_lbl, cam_lbl1, start_btn
    cam1 = os.getenv("CAM1")
    if cam1 is None and cam2 is None:
        
        cam1 = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        cam2 = cv2.VideoCapture(cam1)

        if not cam1.isOpened():
            cam_lbl.configure(text="Error al abrir la camara")
            return
        if not cam2.isOpened():
            cam_lbl1.configure(text="Error al abrir la camara")
            return


        stop_threads = False
        threading.Thread(target=show_camera, args=(cam1, cam_lbl), daemon=True).start()
        threading.Thread(target=show_camera, args=(cam2, cam_lbl1), daemon=True).start()

        start_btn.configure(text="Detener")
    else:
        
        stop_threads = True
        cam1.release()
        cam2.release()
        cam_lbl.configure(image=None, text="DETENIDO")
        cam_lbl1.configure(image=None, text="DETENIDO")
        start_btn.configure(text="Comenzar")
        cam1 = None
        cam2 = None

def loged_user(usuario, root):

    global cam_lbl, start_btn, cam_lbl1
    root.destroy()
    ctk.set_appearance_mode("dark")
    root = ctk.CTk()
    root.title(APP_NAME + f" ({usuario})")
    root.resizable(0, 0)
    root.geometry(APP_SCREEN)

    config_btn = ctk.CTkButton(
        root, text="Configuracion", font=LOGIN_FONT,
        height=HEIGHT_BOTONES, corner_radius=10, border_width=2
    )
    config_btn.place(x=20, y=20)

    start_btn = ctk.CTkButton(
        root, text="Comenzar", font=LOGIN_FONT,
        height=HEIGHT_BOTONES, corner_radius=10, border_width=2,
        command=start_capture
    )
    start_btn.place(x=200, y=20)

    cam_lbl = ctk.CTkLabel(root, text="")
    cam_lbl.place(x=20, y=200)
    cam_lbl1 = ctk.CTkLabel(root, text="")
    cam_lbl1.place(x=400, y=200)

    root.mainloop()