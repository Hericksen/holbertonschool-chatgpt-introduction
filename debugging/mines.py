#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        print('    ' + ' '.join(f"{i:2}" for i in range(self.width)))
        print('   ' + '-' * (3 * self.width))
        for y in range(self.height):
            print(f"{y:2} |", end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('* ', end='')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(f"{count if count > 0 else ' '} ", end='')
                else:
                    print('. ', end='')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if self.revealed[y][x]:
            return True  # Already revealed
        if (y * self.width + x) in self.mines:
            return False  # Hit a mine

        self.revealed[y][x] = True
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        self.reveal(nx, ny)
        return True

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input(f"Enter x coordinate (0-{self.width - 1}): "))
                y = int(input(f"Enter y coordinate (0-{self.height - 1}): "))
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Coordinates out of bounds. Try again.")
                    continue
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
                if all(
                    self.revealed[ny][nx] or (ny * self.width + nx) in self.mines
                    for ny in range(self.height)
                    for nx in range(self.width)
                ):
                    self.print_board(reveal=True)
                    print("Congratulations! You cleared the board!")
                    break
            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
