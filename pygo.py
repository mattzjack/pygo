from tkinter import *

class Pygo(object):
    def __init__(self):
        self.width = self.height = 700
        self.cell_size = self.width / 20.0
        self.r = self.cell_size / 3.0
        self.delay = 5
        self.pieces = [[None] * 19 for _ in range(19)]
        self.curr_num = 0
        self.scheme = 1
        self.colInd = -1
        self.rowInd = -1

        self.root = Tk()
        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()
        self.root.bind('<Button-1>', self.left_pressed)
        self.root.bind('<Button-2>', self.right_pressed)
        self.root.bind('<Key>', self.key)
        self.root.bind('<Motion>', self.motion)

    def flip_curr_num(self):
        if self.curr_num == 0:
            self.curr_num = 1
        elif self.curr_num == 1:
            self.curr_num = 0

    def left_pressed(self, event):
        c = int(event.x / self.cell_size - .5)
        r = int(event.y / self.cell_size - .5)
        if r not in range(19) or c not in range(19): return
        if self.pieces[r][c] == None:
            self.pieces[r][c] = self.curr_num
            self.flip_curr_num()

    def right_pressed(self, event):
        c = int(event.x / self.cell_size - .5)
        r = int(event.y / self.cell_size - .5)
        if r not in range(19) or c not in range(19): return
        self.pieces[r][c] = None

    def key(self, event):
        if event.keysym in ['Up', 'Down']:
            self.flip_curr_num()
        elif event.keysym == 'b':
            self.scheme = 0
        elif event.keysym == 'w':
            self.scheme = 1
        elif event.keysym == 'c':
            self.pieces = [[None] * 19 for _ in range(19)]

    def motion(self, event):
        self.colInd = int(event.x / self.cell_size - .5)
        self.rowInd = int(event.y / self.cell_size - .5)

    def draw_board(self):
        if self.scheme == 0:
            fill = 'white'
        elif self.scheme == 1:
            fill = 'black'
        for i in range(19):
            self.canvas.create_line(self.cell_size, self.cell_size * (i + 1), self.width - self.cell_size, self.cell_size * (i + 1), fill=fill)
            self.canvas.create_line(self.cell_size * (i + 1), self.cell_size, self.cell_size * (i + 1), self.height - self.cell_size, fill=fill)
        for x in [0, 2, 4]:
            for y in [0, 2, 4]:
                self.canvas.create_oval(self.cell_size + (x + 1) * 3 * self.cell_size - self.r / 2.0, self.cell_size + (y + 1) * 3 * self.cell_size - self.r / 2.0, self.cell_size + (x + 1) * 3 * self.cell_size + self.r / 2.0, self.cell_size + (y + 1) * 3 * self.cell_size + self.r / 2.0, fill=fill)

    def draw_pieces(self):
        if self.scheme == 0:
            outline = 'white'
        elif self.scheme == 1:
            outline = 'black'
        for r in range(len(self.pieces)):
            row = self.pieces[r]
            for c in range(len(row)):
                if row[c] == None:
                    continue
                elif row[c] == 1:
                    fill = 'white'
                elif row[c] == 0:
                    fill = 'black'
                self.canvas.create_oval(self.cell_size * (c + 1) - self.r, self.cell_size * (r + 1) - self.r, self.cell_size * (c + 1) + self.r, self.cell_size * (r + 1) + self.r, fill=fill, outline=outline)

    def draw_curr_piece(self):
        if self.curr_num == 0:
            fill = 'black'
        elif self.curr_num == 1:
            fill = 'white'
        if self.scheme == 0:
            outline = 'white'
        elif self.scheme == 1:
            outline = 'black'
        self.canvas.create_oval(10, 10, self.r * 2 + 10, self.r * 2 + 10, fill=fill, outline=outline)

    def draw_hover(self):
        if self.colInd not in range(19) or self.rowInd not in range(19): return
        if self.scheme == 0:
            outline = 'white'
        elif self.scheme == 1:
            outline = 'black'
        if self.pieces[self.rowInd][self.colInd] != None:
            outline = 'red'
        if self.curr_num == 0:
            fill = 'black'
        elif self.curr_num == 1:
            fill = 'white'
        self.canvas.create_oval(self.cell_size * (self.colInd + 1) - self.r, self.cell_size * (self.rowInd + 1) - self.r, self.cell_size * (self.colInd + 1) + self.r, self.cell_size * (self.rowInd + 1) + self.r, outline=outline, fill=fill)

    def redraw(self):
        self.canvas.delete(ALL)
        if self.scheme == 0:
            fill = 'black'
        elif self.scheme == 1:
            fill = 'white'
        self.canvas.create_rectangle(0, 0, self.width, self.height, fill=fill, width=0)

        self.draw_board()
        self.draw_pieces()
        self.draw_curr_piece()
        self.draw_hover()

        self.canvas.update()

    def timer(self):
        self.redraw()
        self.canvas.after(self.delay, self.timer)

    def run(self):
        self.timer()
        self.root.mainloop()

pygo = Pygo()
pygo.run()
