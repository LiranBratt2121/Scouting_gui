import tkinter
from PIL import ImageTk, Image
import customtkinter
import LogInfo

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
LABEL_PADDING = [10, 20]
TEXT_PADDING = [5, 5]
FRAME_PADDING = [35, 30]
BUTTON_PADDING = [10, 10]

app = customtkinter.CTk()
app.geometry("300x480")
app.title('LogIn_Scouting')

login_frame = customtkinter.CTkFrame(master=app)
login_frame.pack(padx=FRAME_PADDING[0], pady=FRAME_PADDING[1], fill="both", expand=True)

header = customtkinter.CTkLabel(master=login_frame, justify=tkinter.LEFT, text='Login To Scout')
header.pack(padx=LABEL_PADDING[0], pady=LABEL_PADDING[1])

name_input = customtkinter.CTkEntry(master=login_frame, placeholder_text='Write Your Name', width=118)
name_input.pack(padx=TEXT_PADDING[0], pady=TEXT_PADDING[1])

team_input = customtkinter.CTkEntry(master=login_frame, placeholder_text='Write Your Team Number', width=170)
team_input.pack(padx=TEXT_PADDING[0], pady=TEXT_PADDING[1] + 5, )

scout_team_input = customtkinter.CTkEntry(master=login_frame, placeholder_text='Write The Scouted Team Number',
                                          width=217)
scout_team_input.pack(padx=TEXT_PADDING[0], pady=TEXT_PADDING[1], )

qual = customtkinter.CTkEntry(master=login_frame, placeholder_text='Write The Current Qual', width=150)
qual.pack(padx=TEXT_PADDING[0], pady=TEXT_PADDING[1])

submit_button = customtkinter.CTkButton(master=login_frame, command=LogInfo.send_info, text='Submit',
                                        hover_color='orange')
submit_button.pack(padx=BUTTON_PADDING[0], pady=BUTTON_PADDING[1])

# down_image = Image.open('./photo/neatPhoto.png')
# resize_down_image = down_image.resize((55, 50))
# down_image = ImageTk.PhotoImage(resize_down_image)
#
#
# panel = tkinter.Label(app, image=down_image)
# panel.pack()

app.mainloop()
