# 🎯 Number Guessing Game (Python)

A simple **console-based number guessing game** written in Python.
The computer randomly selects a number between **1 and 100**, and the player has a limited number of attempts to guess it based on the chosen difficulty level.


## 🚀 Features

* Random number generation using Python’s `random` module
* Two difficulty levels:

  * **Easy** → 10 attempts
  * **Hard** → 5 attempts
* Clear hints for every guess:

  * Too high 📈
  * Too low 📉
* Game over message when attempts are exhausted
* ASCII logo support using a separate module

## 🧠 How the Game Works

1. The program thinks of a number between **1 and 100**
2. The player selects a difficulty level (`easy` or `hard`)
3. The player keeps guessing until:

   * The correct number is guessed 🎉
   * OR all attempts are used ❌
4. After each guess, feedback is given to guide the player


## 📂 Project Structure

```
number-guessing-game/
│
├── main.py          # Main game logic
├── logoart.py       # ASCII logo file
└── README.md        # Project documentation
```


## 🛠️ Requirements

* Python **3.8 or more**
* No external libraries required (uses standard Python modules only)

## ▶️ How to Run the Game

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/number-guessing-game.git
   ```

2. Navigate to the project folder:

   ```bash
   cd number-guessing-game
   ```

3. Run the game:

   ```bash
   python main.py
   ```

---

## 🎮 Gameplay Example

```
Let me think a number b/w 1 to 100
Choose level of difficulty.....'easy' or 'hard': easy
You have 10 remaining to guess the number:
Enter the number: 45
Your guess is too low
Guess Again
```

---

## 📌 Difficulty Levels

| Level | Attempts |
| ----- | -------- |
| Easy  | 10       |
| Hard  | 5        |


