import random


QUESTIONS = [
    ("Which language is known for its use in data science and AI?",
     ["Python", "C", "HTML", "SQL"], "a"),
    ("What does CPU stand for?",
     ["Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Core Processing Utility"], "b"),
    ("Which data structure works on the FIFO principle?",
     ["Stack", "Tree", "Queue", "Graph"], "c"),
    ("What is the time complexity of binary search?",
     ["O(n)", "O(n^2)", "O(1)", "O(log n)"], "d"),
    ("Which symbol is used for comments in Python?",
     ["#", "//", "/*", "--"], "a"),
    ("Which keyword is used to define a function in Python?",
     ["func", "define", "def", "function"], "c"),
    ("What does HTML stand for?",
     ["Hyper Text Markup Language", "High Tech Modern Language",
      "Hyperlinks and Text Markup Language", "Home Tool Markup Language"], "a"),
    ("Which of these is NOT a Python data type?",
     ["list", "tuple", "array_map", "dict"], "c"),
]


def ask_question(number, question, options, answer):
    print(f"\nQ{number}. {question}")
    for letter, option in zip("abcd", options):
        print(f"   {letter}) {option}")

    while True:
        choice = input("Your answer (a/b/c/d): ").strip().lower()
        if choice in ("a", "b", "c", "d"):
            break
        print("Please enter a, b, c, or d.")

    if choice == answer:
        print("Correct!")
        return True

    correct_text = options["abcd".index(answer)]
    print(f"Wrong! The correct answer was {answer}) {correct_text}")
    return False


def get_rating(score, total):
    percent = score / total * 100
    if percent == 100:
        return "Perfect score! Outstanding!"
    if percent >= 70:
        return "Great job!"
    if percent >= 40:
        return "Not bad, keep practicing!"
    return "Better luck next time!"


def play_quiz():
    print("=" * 40)
    print("        WELCOME TO THE QUIZ GAME")
    print("=" * 40)

    questions = QUESTIONS[:]
    random.shuffle(questions)

    score = 0
    for i, (q, opts, ans) in enumerate(questions, start=1):
        if ask_question(i, q, opts, ans):
            score += 1
        print(f"Score so far: {score}/{i}")

    print("\n" + "=" * 40)
    print(f"Final score: {score}/{len(questions)}")
    print(get_rating(score, len(questions)))
    print("=" * 40)


def main():
    while True:
        play_quiz()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()