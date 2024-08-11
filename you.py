import tkinter as tk
import webbrowser
import math

# Function to open websites
def open_website(url):
    webbrowser.open(url, new=1)

# Function to toggle rotation
def toggle_rotation():
    if not button.rotating:
        button.rotating = True
        show_logos()
    else:
        button.rotating = False
        hide_logos()

# Function to show logos in a circular pattern
def show_logos():
    angle_offset = 45  # Starting angle for the first image
    radius = 100  # Radius from the center to the image
    for i, (image, url) in enumerate(logos):
        angle = math.radians(angle_offset + i * 45)  # Adjust angle per image
        x = center_x + radius * math.cos(angle) - image.width() / 2
        y = center_y + radius * math.sin(angle) - image.height() / 2
        canvas.coords(image_id[i], x, y)
        canvas.tag_raise(image_id[i])  # Raise the image to the top

def hide_logos():
    for image in image_id:
        canvas.coords(image, center_x, center_y)

# Create the main window
root = tk.Tk()
root.title("Rotating Button")

# Create a canvas for drawing
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Center of the canvas
center_x = 200
center_y = 200

# Create a circular button
button = tk.Button(root, text="A", font=("Arial", 20), bg="#349788", fg="white", command=toggle_rotation)
button_window = canvas.create_window(center_x, center_y, window=button)
button.rotating = False

# List of logos and their respective URLs
logos = [
    (tk.PhotoImage(file="facebook_logo.png"), "https://www.facebook.com/"),
    (tk.PhotoImage(file="google_logo.png"), "https://www.google.com/"),
    (tk.PhotoImage(file="youtube_logo.png"), "https://www.youtube.com/"),
    (tk.PhotoImage(file="playstore_logo.png"), "https://play.google.com/store"),
    (tk.PhotoImage(file="freefire_logo.png"), "https://play.google.com/store/search?q=free+fire&c=apps"),
    (tk.PhotoImage(file="massenger_logo.png"), "https://www.massenger.com/")
]

# Create image widgets for logos and hide them initially
image_id = []
for i, (image, url) in enumerate(logos):
    img_id = canvas.create_image(center_x, center_y, image=image, anchor="center")
    canvas.tag_bind(img_id, "<Button-1>", lambda e, url=url: open_website(url))
    image_id.append(img_id)

# Run the Tkinter event loop
root.mainloop()
