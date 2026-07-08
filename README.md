# Spaceship_Game
A simple 2D arcade-style space shooter built from scratch using **Python** and **Pygame**.

This project was created to strengthen my understanding of Python, Object-Oriented Programming (OOP), game loops, event handling, collision detection, and basic game architecture. Instead of following a complete tutorial, I designed the game mechanics and implemented each system step by step.

---

## Gameplay

Control a spaceship and survive for as long as possible while destroying incoming UFOs.

Be careful—colliding with a UFO or an asteroid (bomb) ends the game instantly.

Your objective is to survive, destroy as many UFOs as possible, and achieve the highest score.

---

##  Features

* Player-controlled spaceship
* Bullet shooting system
* Random UFO spawning
* Asteroid/Bomb spawning
* Collision detection
* Score system
* Survival timer
* Game Over screen
* Restart functionality
* Custom sprites for game entities

---

## Controls

| Key   | Action                  |
| ----- | ----------------------- |
| ← / → | Move spaceship          |
| Space | Shoot                   |
| R     | Restart after Game Over |

---

## Built With

* Python
* Pygame

---

## Project Structure

```text
Shooter-Game/
│
├── assets/
│   ├── spaceship.png
│   ├── ufo.png
│   ├── bullet.png
│   ├── asteroid.png
│   └── ...
│
├── entity.py
├── system.py
├── main.py
├── README.md
└── requirements.txt
```

---

## How to Run

1. Clone the repository.

```bash
git clone <repository-url>
```

2. Navigate to the project directory.

```bash
cd Shooter-Game
```

3. Install the required dependency.

```bash
pip install pygame
```

4. Run the game.

```bash
python main.py
```

---

## 📸 Gameplay

*Add a gameplay screenshot or GIF here.*

---

## What I Learned

This project helped me gain practical experience with:

* Object-Oriented Programming
* Game loops
* Event-driven programming
* Collision detection
* State management
* Managing multiple game entities
* Structuring medium-sized Python projects
* Debugging and iterative development

---

## Future Improvements

Some ideas for future versions include:

* Different UFO sizes with unique health and scores
* Power-ups (double bullets, shields, etc.)
* Improved collision detection using custom hitboxes
* Animated explosions
* Sound effects and background music
* Difficulty scaling
* Persistent high score
* Better UI and menus

---

## 📄 License

This project was created for learning and educational purposes.
