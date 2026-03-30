# number-guessing-game
A simple Python CLI game where the user guesses a randomly generated number.
Features
- Random number generation (1–100)
- User feedback (Too high / Too low)
- Attempt counter
- Input validation

## ▶️ How to Run
```bash
python src/game.py
Right now your game is too simple.

👉 Add *Replay option*

Update your code:

```python
while True:
    play_game()
    again = input("Play again? (y/n): ").lower()
    if again != 'y':
        break
