import customtkinter as tk
from tkintermapview import TkinterMapView
import tkinter.messagebox 


tk.set_appearance_mode("system")
tk.set_default_color_theme("green")

def search():
    global place
    map_display.set_address(search_bar.get(), marker=True,)

def zoom(n):
    map_display.set_zoom(n)

def get_map(new_map: str):
    if new_map == "Street View":
        map_display.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
    elif new_map == "Normal View":
        map_display.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga")
    elif new_map == "Satelite View":
        map_display.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga")

def marker_place():
    global marker_array
    current_position = map_display.get_position()
    marker_array.append(map_display.set_marker(current_position[0],current_position[1]))

    content_box.insert(tkinter.END, f" {len(marker_array)}. {current_position[0],current_position[1]}")
    content_box.see(tkinter.END)
    print(marker_array)

def marker_remove():
    global marker_array
    content_box.delete(0, tkinter.END)
    content_box.clear()
    for marker in marker_array:
            marker.delete()

def change_appearance_mode(mode: str):
    tk.set_appearance_mode(mode)



window = tk.CTk()
window.geometry("1080x600")
window.resizable(0,0)
window.title("CGM")

marker_array = []


#frame
map_frame = tk.CTkFrame(window, width=1080, height=650)
map_frame.pack(fill="both", expand=True)

nav_frame = tk.CTkFrame(window)
nav_frame.pack(side="left", expand=True)

map_display = TkinterMapView(master=window, width=830, height=550, corner_radius=3, max_zoom=40)
map_display.place(x=220, y=25)

map_opt_text = tk.CTkLabel(master=map_frame, text="Switch Views", font=("Arial",13))
map_opt_text.place(x=45, y=108)

mode_text = tk.CTkLabel(master=map_frame, text="Change Look", font=("Arial",13))
mode_text.place(x=45, y=518)

#message box
content_box = tkinter.Listbox(master=map_frame, width=23, height=15)
content_box.place(x=45, y=270)


#functions
search_bar = tk.CTkEntry(master=map_frame, font=("Arial",15), placeholder_text="Search maps")
search_bar.place(x=45, y=28)

nav_button = tk.CTkButton(master=map_frame, text="Search", font=("Arial",13,"bold"), command=search)
nav_button.place(x=45, y=68)

map_display.set_address("philippines") #default position
map_display.set_zoom(6)

zoom_slider = tk.CTkSlider(master=map_frame, from_=2, to=18, orientation='HORIZONTAL',button_length=2, command=zoom)
zoom_slider.place(x=550, y=5)

map_option_menu = tk.CTkOptionMenu(master=map_frame, values=["Street View", "Normal View", "Satelite View"], command=get_map)
map_option_menu.place(x=45, y=138)

set_mode = tk.CTkOptionMenu(master=map_frame, values=["Light", "Dark"], command=change_appearance_mode)
set_mode.place(x=45, y=548)

place_marker = tk.CTkButton(master=map_frame, text="Place Marker", font=("Arial",15), command=marker_place)
place_marker.place(x=45, y=185)

remove_marker = tk.CTkButton(master=map_frame, text="Remove Marker", font=("Arial",15), command=marker_remove)
remove_marker.place(x=45, y=230)


window.mainloop()
