import tkinter as tk
from tkinter import ttk  
import random
import pygame
from tkinter import messagebox

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Камень, ножницы, бумага")

        style = ttk.Style()
        style.configure("TButton", padding=(10, 5, 10, 5), font=('Helvetica', 12))

        self.label = tk.Label(root, text="Выберите: Камень, Ножницы или Бумага", font=('Helvetica', 14))
        self.label.pack(pady=10)

        self.choice_var = tk.StringVar()
        choices = ["Камень", "Ножницы", "Бумага"]
        for choice in choices:
            tk.Radiobutton(root, text=choice, variable=self.choice_var, value=choice, font=('Helvetica', 12)).pack()

        self.play_button = ttk.Button(root, text="Играть", command=self.play_game, style="TButton")
        self.play_button.pack(pady=10)

        pygame.mixer.init()

    def play_game(self):
        user_choice = self.choice_var.get()
        computer_choice = random.choice(["Камень", "Ножницы", "Бумага"])

        try:
            if user_choice == computer_choice:
                self.show_result("Ничья! Компьютер выбрал", computer_choice)
                self.play_sound(r"C:\Users\ainur\Downloads\tutututu-mem-demotivator.mp3")
            elif (user_choice == "Камень" and computer_choice == "Ножницы") or \
                 (user_choice == "Ножницы" and computer_choice == "Бумага") or \
                 (user_choice == "Бумага" and computer_choice == "Камень"):
                self.show_result("Ты победил! Компьютер выбрал", computer_choice)
                self.play_sound(r"C:\Users\ainur\Downloads\povezlo-povezlo.mp3")
            else:
                self.show_result("Ты проиграл( Компьютер выбрал", computer_choice)
                self.play_sound(r"C:\Users\ainur\Downloads\pojili-i-hvatit.mp3")
        except Exception as e:
            print(e)

    def show_result(self, message, computer_choice):
        result_message = f"{message} {computer_choice}"
        messagebox.showinfo("Результат", result_message)

    def play_sound(self, sound_file):
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
