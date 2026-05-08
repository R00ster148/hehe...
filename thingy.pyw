import tkinter as tk
import random

root = tk.Tk()
root.title("Rainbow Bounce")

WIDTH = 900
HEIGHT = 600

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack(fill="both", expand=True)

colors = [
    "red", "orange", "yellow",
    "green", "cyan", "blue", "purple"
]

ball_size = 80

x = 200
y = 200
dx = 7
dy = 6

score = 0
fullscreen = False

ball = canvas.create_oval(
    x, y,
    x + ball_size,
    y + ball_size,
    fill=random.choice(colors),
    outline=""
)

score_text = canvas.create_text(
    100, 40,
    text="Score: 0",
    fill="white",
    font=("Arial", 24, "bold")
)

def random_color():
    return random.choice(colors)

def move_ball():
    global dx, dy

    canvas.move(ball, dx, dy)

    x1, y1, x2, y2 = canvas.coords(ball)

    w = canvas.winfo_width()
    h = canvas.winfo_height()

    bounced = False

    if x1 <= 0 or x2 >= w:
        dx *= -1
        bounced = True

    if y1 <= 0 or y2 >= h:
        dy *= -1
        bounced = True

    if bounced:
        canvas.itemconfig(ball, fill=random_color())

    root.after(16, move_ball)

def click(event):
    global score

    score += 1

    canvas.itemconfig(score_text, text=f"Score: {score}")

    size = random.randint(20, 120)

    burst = canvas.create_oval(
        event.x - size,
        event.y - size,
        event.x + size,
        event.y + size,
        outline=random_color(),
        width=5
    )

    text = canvas.create_text(
        event.x,
        event.y,
        text="+1",
        fill=random_color(),
        font=("Arial", 20, "bold")
    )

    animate_burst(burst, text, 0)

def animate_burst(burst, text, step):
    if step > 20:
        canvas.delete(burst)
        canvas.delete(text)
        return

    canvas.scale(burst, 0, 0, 1.05, 1.05)
    canvas.move(text, 0, -2)

    root.after(30, lambda: animate_burst(burst, text, step + 1))

def key_press(event):
    global fullscreen

    if event.keysym == "Escape":
        root.destroy()

    if event.keysym.lower() == "f":
        fullscreen = not fullscreen
        root.attributes("-fullscreen", fullscreen)

canvas.bind("<Button-1>", click)
root.bind("<Key>", key_press)

move_ball()

root.mainloop()