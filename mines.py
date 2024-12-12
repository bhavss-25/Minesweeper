import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

class Minesweeper:
    def __init__(self, root):
        self.root = root
        self.root.title("Minesweeper")
        self.root.geometry("400x500")
        self.root.configure(bg="#282c34")

        self.board_size = 8  # 8x8 grid
        self.num_mines = 10
        self.mines = set()
        self.buttons = {}
        self.score = 0
        self.game_over = False

        self.create_widgets()
        self.reset_game()

    def create_widgets(self):
        # Title
        title = tk.Label(self.root, text="Minesweeper", font=("Arial", 24, "bold"), fg="#61afef", bg="#282c34")
        title.pack(pady=10)
        
        # Score display
        self.score_label = tk.Label(self.root, text=f"Score: {self.score}", font=("Arial", 14), fg="#98c379", bg="#282c34")
        self.score_label.pack()

        # Game board frame
        self.frame = tk.Frame(self.root, bg="#282c34")
        self.frame.pack()

        # Generate buttons for the grid
        for row in range(self.board_size):
            for col in range(self.board_size):
                btn = tk.Button(
                    self.frame, width=4, height=2, bg="#3b4048",
                    font=("Arial", 12, "bold"), command=lambda r=row, c=col: self.reveal_cell(r, c)
                )
                btn.grid(row=row, column=col, padx=2, pady=2)
                self.buttons[(row, col)] = btn

        # Restart and Exit buttons
        button_frame = tk.Frame(self.root, bg="#282c34")
        button_frame.pack(pady=10)

        restart_btn = tk.Button(button_frame, text="Restart", font=("Arial", 12), bg="#98c379", fg="#282c34", command=self.reset_game)
        restart_btn.pack(side="left", padx=10)

        exit_btn = tk.Button(button_frame, text="Exit", font=("Arial", 12), bg="#e06c75", fg="#282c34", command=self.root.quit)
        exit_btn.pack(side="right", padx=10)

    def reset_game(self):
        # Reset board, score, and mines
        self.score = 0
        self.update_score()
        self.game_over = False
        self.mines = set()
        self.place_mines()

        # Reset all buttons
        for (row, col), btn in self.buttons.items():
            btn.config(text="", bg="#3b4048", state="normal")

    def place_mines(self):
        # Randomly place mines
        while len(self.mines) < self.num_mines:
            row = random.randint(0, self.board_size - 1)
            col = random.randint(0, self.board_size - 1)
            self.mines.add((row, col))

    def reveal_cell(self, row, col):
        # Check if cell has already been revealed
        if self.game_over or (row, col) not in self.buttons:
            return

        btn = self.buttons[(row, col)]
        if (row, col) in self.mines:
            btn.config(text="💣", bg="#e06c75", fg="black", disabledforeground="black")
            self.end_game(False)
        else:
            self.score += 10
            self.update_score()
            mines_count = self.count_adjacent_mines(row, col)
            btn.config(text=mines_count if mines_count > 0 else "", bg="#98c379", fg="#282c34", state="disabled")
            
            # Reveal surrounding cells if no adjacent mines
            if mines_count == 0:
                for r, c in self.get_adjacent_cells(row, col):
                    if self.buttons[(r, c)]['state'] == 'normal':
                        self.reveal_cell(r, c)
        
        # Check if the game is won
        if self.check_win():
            self.end_game(True)

    def count_adjacent_mines(self, row, col):
        return sum((r, c) in self.mines for r, c in self.get_adjacent_cells(row, col))

    def get_adjacent_cells(self, row, col):
        # Returns a list of adjacent cells' coordinates
        adjacent_cells = []
        for r in range(max(0, row - 1), min(self.board_size, row + 2)):
            for c in range(max(0, col - 1), min(self.board_size, col + 2)):
                if (r, c) != (row, col):
                    adjacent_cells.append((r, c))
        return adjacent_cells

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")

    def check_win(self):
        # Check if all non-mine cells are revealed
        for (row, col), btn in self.buttons.items():
            if (row, col) not in self.mines and btn['state'] == 'normal':
                return False
        return True

    def end_game(self, won):
        self.game_over = True
        if won:
            messagebox.showinfo("Minesweeper", "Congratulations! You won the game!")
        else:
            messagebox.showerror("Minesweeper", "Oops! You hit a mine.")
        
        # Reveal all mines
        for (row, col) in self.mines:
            btn = self.buttons[(row, col)]
            btn.config(text="💣", bg="#e06c75", fg="black", state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    game = Minesweeper(root)
    root.mainloop()


