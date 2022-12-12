import customtkinter as tk
from tkintermapview import TkinterMapView

tk.set_appearance_mode("dark")
tk.set_default_color_theme("blue")

def search():
    global place
    map_display.set_address(search_bar.get())

def zoom(n):
    map_display.set_zoom(n)



window = tk.CTk()
window.geometry("1080x600")
window.resizable(0,0)
window.title("Charls Gwapo Maps | CGW")


#frame
map_frame = tk.CTkFrame(window, width=1080, height=650)
map_frame.pack(fill="both", expand=True)

nav_frame = tk.CTkFrame(window)
nav_frame.pack(side="left", expand=True)

map_display = TkinterMapView(master=window, width=830, height=550, corner_radius=3, max_zoom=40)
map_display.place(x=230, y=25)


#functions
search_bar = tk.CTkEntry(master=map_frame, font=("Arial",15), placeholder_text="Search maps")
search_bar.place(x=45, y=28)

nav_button = tk.CTkButton(master=map_frame, text="Search", font=("Arial",13,"bold"), command=search)
nav_button.place(x=45, y=68)

map_display.set_address("philippines") #default position
map_display.set_zoom(6)

zoom_slider = tk.CTkSlider(master=map_frame, from_=2, to=12, orientation='HORIZONTAL',button_length=2, command=zoom)
zoom_slider.place(x=550, y=5)

window.mainloop()