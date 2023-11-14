from customtkinter import *
from PIL import Image
from runprogram import open_sign_to_speech,open_speech_to_sign
from imagepath import *
from colors import *
def exitmain():
    app.destroy()

def speech_to_sign():
    exitmain()
    open_speech_to_sign()
 
def sign_to_speech():
    exitmain()
    open_sign_to_speech() 

main_bg_color ="#CEC6A1"
frame_bg_color = "#ddd8bf"
button_bg_color = "#D7263D"
white_color = "#ffffff"
black_color = "#111111"
brown_color = "#3c2410"

app = CTk()
app.geometry("1920x1080")
app.title("SignLink")
app.configure(fg_color =main_bg_color)
app.after(0,app.wm_state,'zoomed')
exit_image = CTkImage(light_image=Image.open(exit_path),size=(30, 30))
exit_btn = CTkButton(master=app,hover_text_color=button_bg_color,text_color=button_bg_color,width=40,height=40,text="",
                     fg_color="transparent",image=exit_image,hover=False,command=exitmain)
exit_btn.place(relx=0.975,rely=0.05,anchor="ne")
label5 = CTkLabel(app,text="Exit",text_color=button_bg_color)
label5.place(relx=0.965,rely=0.09,anchor="ne")
frame0 = CTkFrame(app)    
frame0.configure(fg_color = frame_bg_color,width = 500,height = 500) 
frame0.place(relx = 0.5,rely = 0.5,anchor="center")
logo_image = CTkImage(light_image=Image.open(logo_path),size=(320, 120))
image_label = CTkLabel(frame0,image=logo_image,text="")
image_label.place(relx = 0.5,rely = 0.2,anchor = "center")
btn1 =CTkButton(master=frame0,text="Sign to Speech",hover_text_color=white_color,corner_radius=20,
                fg_color='transparent',border_color=button_bg_color,border_width=2,
                hover_color=button_bg_color,text_color=black_color,width=150,height=40,
                font=("Arial",-14),command=sign_to_speech)
btn1.place(relx = 0.525,rely = 0.4,anchor = "center" )

btn2 =CTkButton(master=frame0,text="Speech to Sign",hover_text_color=white_color,
                corner_radius=20,fg_color='transparent',border_color=button_bg_color,
                border_width=2 ,hover_color=button_bg_color,text_color=black_color,
                width=150,height=40,font=("Arial",-14),command=speech_to_sign)
btn2.place(relx = 0.525,rely = 0.5,anchor = "center")
love_image = CTkImage(light_image=Image.open(love_path),size=(344, 195.6))
image_label = CTkButton(frame0,image=love_image,text="",fg_color="transparent",hover_text_color="white",hover=False,border_color=button_bg_color,border_width=2)
image_label.place(relx = 0.525,rely = 0.775,anchor = "center")
hand1_image = CTkImage(light_image=Image.open(hand1_path),size=(160, 106.6))
image_label = CTkButton(app,image=hand1_image,text="",fg_color="transparent",hover_text_color="white",hover=False)
image_label.place(relx = 0.95,rely = 0.935,anchor = "center")
hand2_image = CTkImage(light_image=Image.open(hand2_path),size=(160, 106.6))
image_label = CTkButton(app,image=hand2_image,text="",fg_color="transparent",hover_text_color="white",hover=False)
image_label.place(relx = 0.02,rely = 0.935,anchor = "center")


app.mainloop()