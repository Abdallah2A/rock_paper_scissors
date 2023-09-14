# Importing necessary libraries
import random
import tkinter as tk

# Function to play the game
def play_game(choice):
    try:
        # Generate a random choice for the computer (0 for Rock, 1 for Paper, 2 for Scissors)
        computer_choice = random.randint(0, 2)

        # Determine the result of the game based on user's choice and computer's choice
        if choice == computer_choice:
            result = "It's a draw!"
        elif (choice == 0 and computer_choice == 2) or \
             (choice == 1 and computer_choice == 0) or \
             (choice == 2 and computer_choice == 1):
            result = "You are the winner!"
        else:
            result = "You are the loser!"

        # Update labels to display user's choice, computer's choice, and game result
        user_choice_label.config(image=images[choice])
        computer_choice_label.config(image=images[computer_choice])
        result_label.config(text=result, fg="blue")

    except Exception as e:
        # Handle exceptions and display an error message
        result_label.config(text=f"An error occurred: {e}", fg="red")

# Initialize the GUI window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.configure(bg="lightgray")

# Label to display the game result
result_label = tk.Label(root, text="", font=("Helvetica", 16), bg="lightgray")
result_label.pack(pady=10)

try:
    # Load images for Rock, Paper, and Scissors
    rock_img = tk.PhotoImage(file="images/rock.png")
    paper_img = tk.PhotoImage(file="images/paper.png")
    scissors_img = tk.PhotoImage(file="images/scissors.png")
    images = [rock_img, paper_img, scissors_img]
except tk.TclError as e:
    # Handle image loading errors
    result_label.config(text=f"Error loading images: {e}", fg="red")
    images = [tk.PhotoImage(), tk.PhotoImage(), tk.PhotoImage()]

# Label to display user's choice
user_choice_label = tk.Label(root, image=images[0], bg="lightgray")
user_choice_label.pack(side=tk.LEFT, padx=10)

# Label to display "vs" between user's choice and computer's choice
vs_label = tk.Label(root, text="vs", font=("Helvetica", 20), bg="lightgray")
vs_label.pack(side=tk.LEFT)

# Label to display computer's choice
computer_choice_label = tk.Label(root, image=images[0], bg="lightgray")
computer_choice_label.pack(side=tk.LEFT, padx=10)

# Frame to hold the buttons
button_frame = tk.Frame(root, bg="lightgray")
button_frame.pack()

# Buttons for user to choose Rock, Paper, or Scissors
rock_button = tk.Button(button_frame, text="Rock", font=("Helvetica", 12), command=lambda: play_game(0))
rock_button.pack(side=tk.LEFT, padx=5)

paper_button = tk.Button(button_frame, text="Paper", font=("Helvetica", 12), command=lambda: play_game(1))
paper_button.pack(side=tk.LEFT, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", font=("Helvetica", 12), command=lambda: play_game(2))
scissors_button.pack(side=tk.LEFT, padx=5)

# Start the GUI event loop
root.mainloop()