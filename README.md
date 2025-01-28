# Rush Hour Game

## Description

Rush Hour is a fun and engaging logic puzzle game where players maneuver their cars to help the red car (Car X) escape the congested parking lot grid. The objective is to move other cars out of the way and navigate the red car to the exit square in as few moves as possible.

## Background

I created this project primarily to see what the experience of writing some amount of code in NeoVim. The game itself is mildly interesting, just from a how would I implement an console based game in Python.

### Features

- **Interactive Game**: Use keyboard commands to move the cars around the grid.
- **Multiple Puzzles**: The game includes different pre-defined puzzles for varied levels of difficulty.
- **Color-Coded Cars**: Each car has a specific color, enhancing visual appeal and indicating different cars.
- **Rich Console Display**: Utilizes the `rich` library for a visually appealing terminal interface.
- **Real-time updates**: The game provides real-time feedback on the state of the board as moves are made.

## Installation

1. Install `uv` (Universal Virtualenv) from the terminal using the following command:

   ```bash
   curl -LsSf <https://astral.sh/uv/install.sh> | sh
   ```

2. Install gcc:
  One of the dependencies (getch) requires that gcc be installed.

   ```bash
    apt install gcc
    ```

Use `uv` to create a project environment and run the project. Navigate to your project directory and execute:

   ```bash
   uv run app/main.py
   ```

   This command will handle the environment setup and install all necessary dependencies automatically. `uv` creates an isolated environment specific to this project.

## Usage

To start playing the game, you can execute:

```bash
uv run app/main.py
```

### Controls

- **Move Car X**:
  - `h`: Move left
  - `j`: Move down
  - `k`: Move up
  - `l`: Move right

- **Select Car**: Press the key corresponding to the car's ID (e.g., `x`, `a`, `b` for Cars X, A, B respectively) to select it before moving.
- `q`: Quit the game.

## Testing

The project comes with unit tests to validate the functionality of the game logic. To run the tests, execute:

```bash
uv run -m pytest
```

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Enjoy playing Rush Hour! May you guide Car X to victory! 🚗💨
