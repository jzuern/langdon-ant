from Tkinter import *
import numpy as np


class Ant:
    def __init__(self, canvas, size, size_factor, pos_x, pos_y, direction):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size = size
        self.size_factor = size_factor
        self.direction = direction
        self.canvas = canvas
        self.grid = np.zeros((self.size, self.size), dtype=bool)

    def draw_canvas(self):

        # clear canvas
        canvas.delete("all")

        for i in range(self.size):
            for j in range(self.size):
                if i == self.pos_x and j == self.pos_y:
                    color = 'red' # ant
                elif self.grid[i,j] == 1:
                    color = 'black'
                else:
                    color = 'white'
                self.canvas.create_rectangle(i*self.size_factor, j*self.size_factor,
                                             (i+1)*self.size_factor, (j+1)*self.size_factor,
                                             fill=color)


    def step(self):

        # update grid
        if self.grid[self.pos_x, self.pos_y] == 0:  # white square
            self.direction += 1
            self.grid[self.pos_x, self.pos_y] = 1
            if self.direction == 4:
                self.direction = 0

        elif self.grid[self.pos_x, self.pos_y] == 1:  # black square
            self.direction -= 1
            self.grid[self.pos_x, self.pos_y] = 0
            if self.direction == -1:
                self.direction = 3

        # move forward:

        # direction = 0: right
        # direction = 1: down
        # direction = 2: left
        # direction = 3: up

        if self.direction == 0:  # pos x
            self.pos_x += 1
            if self.pos_x >= self.size:
                self.pos_x -= self.size

        if self.direction == 1:  # pos y
            self.pos_y += 1
            if self.pos_y >= self.size:
                self.pos_y -= self.size

        if self.direction == 2:  # neg x
            self.pos_x -= 1
            if self.pos_x < 0:
                self.pos_x += self.size

        if self.direction == 3:  # neg y
            self.pos_y -= 1
            if self.pos_y < 0:
                self.pos_y += self.size

        self.draw_canvas()
        self.canvas.after(1, self.step)


# initialize root Window and canvas
root = Tk()
root.title("Ant")
root.resizable(False, False)

size = 40
size_factor = 20

canvas_width = size * size_factor
canvas_height = size * size_factor

canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()


pos_x = size//2
pos_y = size//2
initial_direction = 0

# Create ant object and animate it
ant = Ant(canvas, size, size_factor, pos_x, pos_y, initial_direction)

# step
ant.step()

root.mainloop()
