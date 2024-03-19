import os

os.system("pip install tk")
os.system("pip install tkinter")

import tkinter as tk
import time
import datetime

# Цветовая схема
bgColor = "#000000"
fgColor = "#FFFFFF"

# Частота кадров
fps_options = [24, 30, 25, 50, 60, 120]

class Timer:
    def __init__(self, root, fps):
        self.root = root
        self.fps = fps

        # Создать холст
        self.canvas = tk.Canvas(root, bg=bgColor, width=600, height=300)
        self.canvas.pack()

        # Создать таймер
        self.timer_label = tk.Label(root, text="00:00:00:00", bg=bgColor, fg=fgColor, font=("Courier", 24))
        self.timer_label.pack()

        # Создать кнопки
        self.start_button = tk.Button(root, text="Старт", command=self.start_timer)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Стоп", command=self.stop_timer)
        self.stop_button.pack()

        # Установить начальное время
        self.start_time = None
        self.elapsed_time = datetime.timedelta()

    def start_timer(self):
        # Запустить таймер
        self.start_time = time.time()
        self.update_timer()

    def stop_timer(self):
        # Остановить таймер
        self.start_time = None

    def update_timer(self):
        # Обновить таймер
        if self.start_time:
            self.elapsed_time = datetime.timedelta(seconds=time.time() - self.start_time)
            self.timer_label.configure(text=str(self.elapsed_time))

        # Запланировать следующее обновление
        self.root.after(int(1000 / self.fps), self.update_timer)

# Создать окно
root = tk.Tk()
root.title("Таймер с таймкодами")
root.configure(bg=bgColor)

# Создать таймеры
timers = {}
for fps in fps_options:
    timers[fps] = Timer(root, fps)

# Запустить главный цикл
root.mainloop()

# softy_plug