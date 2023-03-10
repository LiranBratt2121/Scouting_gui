import tkinter
from PIL import ImageTk, Image
import customtkinter
import LogInfo

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Set padding values for layout
PADDING = {
    "label": [10, 20],
    "text": [5, 5],
    "frame": [35, 30],
    "button": [10, 10]
}

app = customtkinter.CTk()
app.geometry("300x480")
app.title('LogIn_Scouting')

login_frame = customtkinter.CTkFrame(master=app)
login_frame.pack(padx=PADDING["frame"][0], pady=PADDING["frame"][1], fill="both", expand=True)

header = customtkinter.CTkLabel(master=login_frame, justify=tkinter.LEFT, text='Login To Scout')
header.pack(padx=PADDING["label"][0], pady=PADDING["label"][1])

name_input = customtkinter.CTkEntry(master=login_frame, placeholder_text='Write Your Name', width=118)
name_input.pack(padx=PADDING["text"][0], pady=PADDING["text"][1])

team_input = customtkinter.CTkEntry(master=login_frame, placeholder_text='Write Your Team Number', width=170)
team_input.pack(padx=PADDING["text"][0], pady=PADDING["text"][1] + 5, )

scout_team_input = customtkinter.CTkEntry(master=login_frame, placeholder_text='Write The Scouted Team Number',
                                          width=217)
scout_team_input.pack(padx=PADDING["text"][0], pady=PADDING["text"][1], )

qual = customtkinter.CTkEntry(master=login_frame, placeholder_text='Write The Current Qual', width=150)
qual.pack(padx=PADDING["text"][0], pady=PADDING["text"][1])

submit_button = customtkinter.CTkButton(master=login_frame, command=LogInfo.send_info, text='Submit',
                                        hover_color='orange')
submit_button.pack(padx=PADDING["button"][0], pady=PADDING["button"][1])

# down_image = Image.open('./photo/neatPhoto.png')
# resize_down_image = down_image.resize((55, 50))
# down_image = ImageTk.PhotoImage(resize_down_image)
#
#
# panel = tkinter.Label(app, image=down_image)
# panel.pack()

app.mainloop()
