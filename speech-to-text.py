import speech_recognition as sl
import os
import cv2
from customtkinter import *
from runprogram import open_main_ui
from PIL import Image,ImageTk
import time

main_bg_color ="#CEC6A1"
frame_bg_color = "#ddd8bf"
button_bg_color = "#D7263D"
white_color = "#ffffff"
black_color = "#111111"
brown_color = "#3c2410"
logo_path = "images/logo.png"
mic_path = "images/mic.png"
exit_path = "images/exit1.png"

def exit ():
    root.destroy()
    open_main_ui()

def play_video(word):
    # Check if the video file exists for the given word
    video_file_path = f"video/{word}.mp4"
    
    if not os.path.exists(video_file_path):
        cap = cv2.VideoCapture("video/idle.mp4")
    else:
        cap = cv2.VideoCapture(video_file_path)
    # Play the video
    

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame,(308,548))
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        photo = ImageTk.PhotoImage(Image.fromarray(frame))
        canvas.create_image(0,0,image=photo,anchor = NW)
        canvas.image = photo
        canvas.update()

        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break


    cap.release()

def speech():  
        
        label2.configure(text="")
        label2.update()
        sr = sl.Recognizer()
        with sl.Microphone() as source2:
            btn1.configure(text="Silent Please")
            btn1.update()
            sr.adjust_for_ambient_noise(source2,duration=2)

            btn1.configure(text="Speak Now Please")
            btn1.update()
            audio2 = sr.listen(source2)
            try:
                text = sr.recognize_google(audio2)
                text = text.lower()
                label1.configure(text= f"You said: {text.upper()} ",fg_color=button_bg_color,padx=4,pady=4)
                label1.update()
                keywords = list()
                keywords = text.split()
                for keyword in keywords:
                    play_video(keyword)
                canvas.image = None 
                canvas.update()
                label1.configure(text="",fg_color="transparent")
                label1.update()  
            except sl.UnknownValueError:
                print("Speech Recognition could not understand audio")
                label2.configure(text="Sorry, Couldn't Understand You")
                label2.update()
                # time.sleep(2)
            except sl.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                label2.configure(text="Speech Recognition error")
                label2.update()
            finally:
                btn1.configure(text="Speech to Sign")
                btn1.update()
             

root = CTk()
root.title("Speech to Sign")
root.configure(fg_color =main_bg_color)
root.geometry("1920x1080")
root.after(0,root.wm_state,"zoomed")
frame = CTkFrame(master=root,width=600,height=960,fg_color = frame_bg_color)
frame.place(relx = 0.5,rely = 0.5,anchor="center")

canvas = CTkCanvas(frame,width=310,height=550,bg=frame_bg_color,borderwidth=0,highlightthickness=0)
canvas.place(relx=0.3,rely=0.3)
logo_image = CTkImage(light_image=Image.open(logo_path),
                                  dark_image=Image.open(logo_path),
                                  size=(200, 75))
image_label = CTkLabel(frame,image=logo_image,text="")
image_label.place(relx = 0.5,rely = 0.15,anchor = "center")
label3 =CTkLabel(master= frame,text="SPEECH TO SIGN TRANSLATION",text_color=brown_color,font=("Arial",-24))
label3.place(relx = 0.5 , rely=0.2,anchor = "center")
label1 = CTkLabel(master=frame,text="",text_color=white_color,font=("Arial",-18))
label1.place(relx = 0.5 , rely=0.8,anchor = "center")
label2 = CTkLabel(master=frame,text="",text_color=button_bg_color,font=("Arial",-14))
label2.place(relx = 0.5 , rely=0.285,anchor = "center")

mic_image = CTkImage(light_image=Image.open(mic_path),
                                  dark_image=Image.open(mic_path),
                                  size=(30, 30))
btn1 =CTkButton(master=frame,text="Sign to Speech",hover_text_color=white_color,corner_radius=20,
                fg_color=button_bg_color,border_color=button_bg_color,border_width=2,
                hover_color=button_bg_color,text_color=white_color,width=150,height=40,
                font=("Arial",-14),image=mic_image,command=speech)
btn1.place(relx = 0.5 , rely=0.25,anchor = "center")
exit_image = CTkImage(light_image=Image.open(exit_path),
                                  dark_image=Image.open(exit_path),
                                  size=(30, 30))
exit_btn = CTkButton(master=root,hover_text_color=button_bg_color,text_color=button_bg_color,width=40,height=40,text="",
                     fg_color="transparent",image=exit_image,hover=False,command=exit)
exit_btn.place(relx=0.075,rely=0.05,anchor="ne")
root.mainloop()
