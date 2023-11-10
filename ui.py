from customtkinter import *
from PIL import Image
from runprogram import open_sign_to_speech,open_speech_to_sign
import time
def exit ():
    app.destroy()

def speech_to_sign():
    app.destroy()
    open_speech_to_sign()


main_bg_color ="#CEC6A1"
frame_bg_color = "#ddd8bf"
button_bg_color = "#D7263D"
white_color = "#ffffff"
black_color = "#111111"
logo_path = "images/logo.png"
exit_path = "images/exit.png"

app = CTk()
app.geometry("1920x1080")
app.title("SignLink")
app.configure(fg_color =main_bg_color)
app.after(0,app.wm_state,'zoomed')
exit_image = CTkImage(light_image=Image.open(exit_path),
                                  dark_image=Image.open(exit_path),
                                  size=(30, 30))
exit_btn = CTkButton(master=app,hover_text_color=button_bg_color,text_color=button_bg_color,width=40,height=40,text="",
                     fg_color="transparent",image=exit_image,hover=False,command=exit)
exit_btn.place(relx=0.975,rely=0.05,anchor="ne")
frame1 = CTkFrame(app)    
frame1.configure(fg_color = frame_bg_color,width = 500,height = 300) 
frame1.place(relx = 0.5,rely = 0.5,anchor="center")
logo_image = CTkImage(light_image=Image.open(logo_path),
                                  dark_image=Image.open(logo_path),
                                  size=(400, 150))
image_label = CTkLabel(frame1,image=logo_image,text="")
image_label.place(relx = 0.5,rely = 0.3,anchor = "center")
btn1 =CTkButton(master=frame1,text="Sign to Speech",hover_text_color=white_color,corner_radius=20,
                fg_color='transparent',border_color=button_bg_color,border_width=2,
                hover_color=button_bg_color,text_color=black_color,width=150,height=40,
                font=("Arial",-14),command=open_sign_to_speech)
btn1.place(relx = 0.525,rely = 0.6,anchor = "center" )

btn2 =CTkButton(master=frame1,text="Speech to Sign",hover_text_color=white_color,
                corner_radius=20,fg_color='transparent',border_color=button_bg_color,
                border_width=2 ,hover_color=button_bg_color,text_color=black_color,
                width=150,height=40,font=("Arial",-14),command=speech_to_sign)
btn2.place(relx = 0.525,rely = 0.75,anchor = "center")

app.mainloop()