import tkinter as tk
import random
import time
import threading
import winsound

maailmanennatykset = {
    1920: {'aika': 10.6, 'nimi': 'Charlie Paddock'},
    1930: {'aika': 10.3, 'nimi': 'Percy Williams'},
    1988: {'aika': 9.79, 'nimi': 'Ben Johnson'},
    2009: {'aika': 9.58, 'nimi': 'Usain Bolt'},
}

leijonat = {
    "Simba": 8.2,
    "Nala": 8.5,
    "Mufasa": 7.9,
    "Scar": 8.7,
    "Kiara": 8.4,
}

ernesti_speed = random.uniform(10.0, 15.0)
kernesti_speed = random.uniform(10.0, 15.0)

root = tk.Tk()
root.title("Ernestin ja Kernestin Juoksu")

canvas = tk.Canvas(root, width=600, height=200, bg="white")
canvas.pack(pady=20)

canvas.create_line(50, 50, 50, 150, fill="black", width=5)
canvas.create_line(550, 50, 550, 150, fill="black", width=5)

ernesti_shape = canvas.create_oval(30, 90, 70, 130, fill="blue")
kernesti_shape = canvas.create_oval(30, 140, 70, 180, fill="red")

def juokse_ernesti():
    return run_simulation("Ernesti", ernesti_speed, ernesti_shape, 100, 100)

def juokse_kernesti():
    return run_simulation("Kernesti", kernesti_speed, kernesti_shape, 1100, 50)

def run_simulation(name, speed, shape, frequency, duration):
    progress = 0
    step = 500 / speed

    start_time = time.time()

    while progress < 500:
        progress += step
        canvas.move(shape, step, 0)
        root.update()

        winsound.Beep(frequency, duration)

        time.sleep(1)

    end_time = time.time()
    total_time = end_time - start_time
    show_result(name, total_time)
    return total_time

def show_result(name, time_taken):
    result_label.config(text=f"{name} juoksi 100m aikaan {time_taken:.2f} sekuntia!")
    result_label.config(text=winner_text)

def yhteis_laukaisu():
    ernesti_thread = threading.Thread(target=lambda: juokse_ernesti())
    kernesti_thread = threading.Thread(target=lambda: juokse_kernesti())
    ernesti_thread.start()
    kernesti_thread.start()

    ernesti_thread.join()
    ernesti_time = juokse_ernesti()

    kernesti_thread.join()
    kernesti_time = juokse_kernesti()

    if ernesti_time < kernesti_time:
        winner_text = "Ernesti voitti!"
    elif kernesti_time < ernesti_time:
        winner_text = "Kernesti voitti!"
    else:
        winner_text = "Tasapeli!"

    result_label.config(text=winner_text)

ernesti_button = tk.Button(root, text="Juokse Ernesti!", command=lambda: threading.Thread(target=juokse_ernesti).start())
ernesti_button.pack(pady=10)

kernesti_button = tk.Button(root, text="Juokse Kernesti!", command=lambda: threading.Thread(target=juokse_kernesti).start())
kernesti_button.pack(pady=10)

yhteis_laukaisu_button = tk.Button(root, text="Yhteis Laukaisu!", command=lambda: threading.Thread(target=yhteis_laukaisu).start())
yhteis_laukaisu_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
