from turtle import Turtle, Screen
SNAKE_BODY = [0, -20, -40]
MOVE_DISTANCE = 20
screen = Screen()
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for _ in range(3):
            tur = Turtle(shape="square")
            tur.penup()
            tur.goto(SNAKE_BODY[_], 0)
            self.snake_segments.append(tur)

    def create_seg(self):
        tur = Turtle(shape="square")
        tur.penup()
        seg_x = self.snake_segments[-1].xcor()
        seg_y = self.snake_segments[-1].ycor()
        tur.goto(seg_x, seg_y)
        self.snake_segments.append(tur)

    def move(self):
        for segment in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[segment - 1].xcor()
            new_y = self.snake_segments[segment - 1].ycor()
            self.snake_segments[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        screen.onkey(self.move_up, "Up")
        screen.onkey(self.move_down, "Down")
        screen.onkey(self.move_left, "Left")
        screen.onkey(self.move_right, "Right")

    def check_touch(self):
        touch = False
        for seg in self.snake_segments[1:]:
            if self.head.distance(seg) < 10:
                touch = True
        return touch

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
