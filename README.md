# Quiz Game

A simple command-line quiz game written in Python. It asks multiple-choice questions, checks your answers, and keeps score.

## Features

- Multiple-choice questions (a/b/c/d)
- Questions are shuffled every round
- Input validation (re-prompts on invalid answers)
- Shows the correct answer when you get one wrong
- Running score after every question
- Final score with a rating
- Play again option

## Requirements

- Python 3.6 or higher
- No external libraries needed

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/quiz-game.git
   cd quiz-game
   ```

2. Run the game:

   ```bash
   python quiz_game.py
   ```

## Example Output

```
========================================
        WELCOME TO THE QUIZ GAME
========================================

Q1. What does CPU stand for?
   a) Central Process Unit
   b) Central Processing Unit
   c) Computer Personal Unit
   d) Core Processing Utility
Your answer (a/b/c/d): b
Correct!
Score so far: 1/1
```

## Adding Your Own Questions

Open `quiz_game.py` and add a tuple to the `QUESTIONS` list in this format:

```python
("Your question here?", ["Option A", "Option B", "Option C", "Option D"], "b")
```

The last value is the letter of the correct option.

## Project Structure

```
quiz-game/
├── quiz_game.py
└── README.md
```

## Contributing

Pull requests are welcome. Feel free to add more questions, categories, or features such as a timer or a high-score board.

## License

This project is open source and available under the [MIT License](LICENSE).
