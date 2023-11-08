from customtkinter import *
from runprogram import open_py_file
app = CTk()
app.geometry("1920x1080")
app.title("SignLink")

app.after(1,app.wm_state,'zoomed')
# app.attributes("-fullscreen", True)
# app.bind("<F11>", lambda event: app.attributes("-fullscreen",not app.attributes("-fullscreen")))
# app.bind("<Escape>", lambda event: app.attributes("-fullscreen", False))

frame1 = CTkFrame(app)
frame1.place(relx = 0.5,rely = 0.5,anchor="center")

btn1 =CTkButton(master=frame1,text="Speech to Sign",text_color="#C6DBF0",corner_radius=20,fg_color='transparent',border_color='#C6DBF0',border_width=2,hover_color='#A0C4E2',hover_text_color="#111111",command=open_py_file)


btn1.place(relx = 0.5,rely = 0.4,anchor = "center" )

btn2 =CTkButton(master=frame1,text="Sign to Sign",text_color="#C6DBF0",corner_radius=20,fg_color='transparent',border_color='#C6DBF0',border_width=2,hover_color='#A0C4E2',hover_text_color="#111111")
btn2.place(relx = 0.5,rely = 0.6,anchor = "center" )

# app.attributes('-fullscreen', True)
app.mainloop()