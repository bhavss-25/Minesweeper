# Minesweeper Game

## Description
This project is a Python implementation of the classic Minesweeper game with a graphical user interface (GUI) created using Tkinter. The game is designed with a clean, modern dark-themed interface and includes all the classic features of Minesweeper, such as uncovering cells, avoiding mines, and scoring points. It also features restart and exit options for user convenience.

## Features
- **Dark Themed Interface**: The game provides an aesthetically pleasing dark theme.
- **Customizable Grid**: The game uses an 8x8 grid with 10 hidden mines.
- **Score System**: Players earn points by successfully uncovering cells without mines.
- **Win Detection**: Automatically detects when all non-mine cells are uncovered.
- **Mine Placement**: Mines are randomly distributed across the grid.
- **Restart and Exit Options**: Buttons are available to restart the game or exit the application.
- **Game Over Alerts**: Informative messages for winning or losing the game.

## How to Play
1. Launch the game by running the script.
2. Click on any cell to reveal it:
   - If the cell contains a mine, the game ends.
   - If it does not contain a mine, the score increases, and the number of adjacent mines is displayed.
   - If no adjacent mines are detected, neighboring cells are automatically revealed.
3. The game is won when all cells without mines are uncovered.
4. If a mine is uncovered, the game is lost, and all mines are revealed.
5. Use the Restart button to reset the game or the Exit button to close the application.

## Requirements
- Python 3.x
- `tkinter` (usually included with Python installations)
- `Pillow` library for image handling

## Installation
1. Clone this repository or download the source code.
2. Install the required libraries using:
   ```bash
   pip install pillow
   ```

## Running the Game
Run the following command in your terminal or Python IDE:
```bash
python mines.py
```

## Code Structure
### Main Components
- **`create_widgets`**: Sets up the game's GUI elements, including the board and buttons.
- **`reset_game`**: Resets the board, score, and mines for a new game.
- **`place_mines`**: Randomly distributes mines across the grid.
- **`reveal_cell`**: Handles the logic for uncovering a cell and interacting with adjacent cells.
- **`count_adjacent_mines`**: Calculates the number of mines adjacent to a given cell.
- **`check_win`**: Checks if the player has successfully uncovered all non-mine cells.
- **`end_game`**: Displays the game result and reveals all mines.

### Aesthetic Features
- **Dark Theme**: Ensures a consistent and modern look throughout the game.
- **Dynamic Score Updates**: Keeps the score visible and updated in real-time.
- **Message Alerts**: Uses Tkinter message boxes to display win/loss messages.

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute the code.

## Future Enhancements
- Adding difficulty levels with varying grid sizes and mine counts.
- Implementing timer functionality to track the duration of the game.
- Adding sound effects for interactions and alerts.
- Introducing animations for cell reveals and mine explosions.

---
Enjoy playing Minesweeper!

