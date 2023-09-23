from turtle import Turtle

INITIAL_POSITIONS = [(0, 0), (0, -20), (0, -40)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        self.head.shapesize(stretch_wid=1.1, stretch_len=1.1)

    def create_snake(self):
        for pos in INITIAL_POSITIONS:
            self.add_body(pos)

    def add_body(self, pos):
        sb = Turtle("square")
        sb.color("white")
        sb.pu()
        sb.setpos(pos)
        self.snake_body.append(sb)

    def extend(self):
        self.add_body(self.snake_body[-1].position())

    def move(self):
        for bod_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[bod_num - 1].xcor()
            new_y = self.snake_body[bod_num - 1].ycor()
            self.snake_body[bod_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
