# Snake-game
# 🐍 Snake Game in Python (Pygame)

A classic Snake Game made using Python and Pygame with added features like high score tracking and level progression.

---

## 🚀 Features

- ✅ Smooth grid-based movement
- 🍎 Random food placement
- 📈 Increasing difficulty with levels
- 🏆 High score tracking (stored in a file)
- 💥 Collision detection
- 🎮 Simple keyboard controls

---

## 📸 Screenshot

> _(Optional: Add your own screenshot here)_  
> Example:
> ![Snake Game Screenshot](screenshot.png)

---

## 🛠 Requirements

- Python 3.x
- [Pygame](https://www.pygame.org/)

### Install Pygame:

```bash
pip install pygame
```
## ▶️ How to Run
Clone or download the repository.

Make sure highscore.txt exists (it will be created automatically if not).

Run the game:

python snake_game.py
## 🎮 Controls
Key	Action
⬅️ Left Arrow	Move left
➡️ Right Arrow	Move right
⬆️ Up Arrow	Move up
⬇️ Down Arrow	Move down
Q	Quit after Game Over
C	Continue after Game Over

## 🧠 Game Mechanics
Snake moves continuously and grows when it eats food.

Game over if the snake hits the wall or itself.

Every 5 points increase the level (and speed).

High score is saved between runs in highscore.txt.

## 📂 File Structure

.
├── snake_game.py       # Main game code
├── highscore.txt       # Stores the high score
└── README.md           # Game documentation
## 🔧 To Do (Optional Enhancements)
🔊 Add sound effects

🧩 Add obstacles

🌐 Convert to web-based game

🥇 Online leaderboard
