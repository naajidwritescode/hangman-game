# 🎮 Hangman Game (Python)

A simple terminal-based **Hangman game** written in Python.  
The player must guess a randomly selected word (fruit-themed) one letter at a time before running out of attempts.

---

## 📌 Features

- Random word selection
- ASCII-art hangman display
- Input validation (only single letters allowed)
- Tracks previously guessed letters
- Displays remaining turns
- Win and lose conditions handled cleanly

---

## 🧠 How the Game Works

1. The program randomly selects a word from a predefined list of fruits.
2. The player guesses one letter at a time.
3. If the letter exists in the word, it is revealed in the correct positions.
4. If the letter is incorrect, the hangman drawing progresses.
5. The game ends when:
   - ✅ The player guesses the word correctly (WIN)
   - ❌ The player reaches 6 wrong guesses (LOSE)

---
## Example GamePlay
*******************
  o  
 /|\ 
     
*******************
_ a _ a _ a

Enter a letter: n

5 Turns Left!


---


## ▶️ How to Run

Make sure you have **Python 3** installed.

```bash
python hangman.py

