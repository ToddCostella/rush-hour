# Rush Hour Game

## Description

Rush Hour is a fun and engaging logic puzzle game where players maneuver their cars to help the red car (Car X) escape the congested parking lot grid. The objective is to move other cars out of the way and navigate the red car to the exit square in as few moves as possible.

### Features

- **Interactive Game**: Use keyboard commands to move the cars around the grid.
- **Multiple Puzzles**: The game includes different pre-defined puzzles for varied levels of difficulty.
- **Color-Coded Cars**: Each car has a specific color, enhancing visual appeal and indicating different cars.
- **Rich Console Display**: Utilizes the `rich` library for a visually appealing terminal interface.
- **Real-time updates**: The game provides real-time feedback on the state of the board as moves are made.

## Installation

1. Ensure you have [Python 3.13 or later](https://www.python.org/downloads/) installed on your machine.

2. Install `uv` (Universal Virtualenv) from the terminal using the following command:

   ```bash
   pip install uv
   ```

3. Use `uv` to create a project environment and run the project. Navigate to your project directory and execute:

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

### Example Puzzle Definitions

The following strings represent different puzzles you can play:

- Puzzle 1: `"XR2H14,AG2H01,BO2V25,CC2H29,PP3V07,TB3V10,OY3V06,RG3H33"`
- Puzzle 2: `"XR2H13,AG2V01,BY3H04,CC2V10,DP3V12,EB2V17,FO2H29,GG2H31,MC2V27,NB2H34,OB3H19"`

You can modify the `puzzle_one` variable in the `app/main.py` file to start with any of these puzzles.

## Testing

The project comes with unit tests to validate the functionality of the game logic. To run the tests, execute:

```bash
uv run -m pytest
```

## Future Improvements

- Add more pre-defined puzzles to play.
- Enable users to select specific puzzles to start the game.
- Improve the main puzzle loop to be more generic.
- Add additional visual aids or instructions within the game.

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to submit a pull request or open an issue.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Enjoy playing Rush Hour! May you guide Car X to victory! 🚗💨
