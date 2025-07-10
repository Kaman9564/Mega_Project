import tkinter as tk
import random

# Constants
ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
emojis = { ROCK: '🪨', SCISSORS: '✂', PAPER: '📃' }
choices = (ROCK, PAPER, SCISSORS)

# Game logic
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a Tie!"
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or 
        (user_choice == SCISSORS and computer_choice == PAPER) or 
        (user_choice == PAPER and computer_choice == ROCK)):
        return "🎉 You Win!"
    else:
        return "😢 You Lose!"

# Callback when user clicks a button
def play(user_choice):
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    
    user_label.config(text=f"You chose {emojis[user_choice]}")
    comp_label.config(text=f"Computer chose {emojis[computer_choice]}")
    result_label.config(text=result)

# GUI Setup
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x300")
root.config(bg="#f2f2f2")

# Labels
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"), bg="#f2f2f2")
title_label.pack(pady=10)

user_label = tk.Label(root, text="You chose ❓", font=("Arial", 14), bg="#f2f2f2")
user_label.pack()

comp_label = tk.Label(root, text="Computer chose ❓", font=("Arial", 14), bg="#f2f2f2")
comp_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), fg="green", bg="#f2f2f2")
result_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="#f2f2f2")
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="🪨 Rock", font=("Arial", 14), width=10, command=lambda: play(ROCK))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="📃 Paper", font=("Arial", 14), width=10, command=lambda: play(PAPER))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="✂ Scissors", font=("Arial", 14), width=10, command=lambda: play(SCISSORS))
scissors_btn.grid(row=0, column=2, padx=10)

# Exit Button
exit_btn = tk.Button(root, text="Exit", font=("Arial", 12), command=root.quit, bg="red", fg="white")
exit_btn.pack(pady=10)

# Run the GUI
root.mainloop()
