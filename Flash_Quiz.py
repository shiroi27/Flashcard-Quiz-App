import tkinter as tk
import random

# Sample flashcards (Question:Answer pairs)
flashcards = {
    "What is the capital of France?": "Paris",
    "What is 9 x 9?": "81",
    "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
    "What is the chemical symbol for Water?": "H2O",
    "What planet is known as the Red Planet?": "Mars",
    "What language is primarily spoken in Brazil?": "Portuguese",
    "Who painted the Mona Lisa?": "Leonardo da Vinci",
    "What is the tallest mountain in the world?": "Mount Everest",
    "What is the square root of 64?": "8",
    "What year did World War II end?": "1945",
    "Which gas do plants absorb from the atmosphere?": "Carbon Dioxide",
    "Who is known as the father of computers?": "Charles Babbage",
    "What is the currency of Japan?": "Yen"
}

# Function to show a new flashcard
def show_new_card():
    global current_question
    current_question = random.choice(list(flashcards.keys()))
    question_label.config(text=current_question)
    answer_label.config(text="")  # Hide answer

# Function to show the answer
def show_answer():
    answer = flashcards.get(current_question, "")
    answer_label.config(text=answer)

# Setup the window
root = tk.Tk()
root.title("Flashcard Quiz")
root.geometry("700x500+300+150")
root.config(bg="#E3F2FD")
root.resizable(False, False)

# Header
header_frame = tk.Frame(root, bg="#42A5F5", width=700, height=60)
header_frame.place(x=0, y=0)
header_label = tk.Label(header_frame, text="FLASHCARD QUIZ", font=("Times New Roman", 28, "bold"), bg="#42A5F5", fg="#000000")
header_label.place(relx=0.5, rely=0.5, anchor="center")

# Decorative Line
line = tk.Frame(root, bg="#1E88E5", height=4, width=700)
line.place(x=0, y=60)

# Question Display
question_label = tk.Label(root, text="", font=("Times New Roman", 20, "bold"), bg="#FFFFFF", fg="#000000", bd=3, relief="solid", wraplength=500, justify="center")
question_label.place(x=100, y=120, width=500, height=120)

# Answer Display
answer_label = tk.Label(root, text="", font=("Times New Roman", 18), bg="#FFFFFF", fg="#000000", bd=3, relief="solid", wraplength=400, justify="center")
answer_label.place(x=150, y=270, width=400, height=70)

# Buttons
show_btn = tk.Button(root, text="Show Answer", font=("Times New Roman", 14, "bold"), bg="#81D4FA", fg="#000000", command=show_answer)
show_btn.place(x=170, y=370, width=150, height=40)

new_btn = tk.Button(root, text="New Card", font=("Times New Roman", 14, "bold"), bg="#4FC3F7", fg="#000000", command=show_new_card)
new_btn.place(x=380, y=370, width=150, height=40)

# Footer
footer = tk.Label(root, text="🧠 Keep learning, keep growing! 🚀", font=("Times New Roman", 10), bg="#E3F2FD", fg="#333")
footer.place(x=230, y=460)

# Start with a flashcard
show_new_card()

root.mainloop()