import pygame
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 600
HEIGHT = 400
SNAKE_SIZE = 20
FOOD_SIZE = 20
BLOCK_SIZE = 20

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Snake:
    def __init__(self):
        self.body = [(200, 150), (180, 150), (160, 150)]
        self.direction = "Right"
        self.growing = False

    def move(self):
        if self.direction == "Right":
            head = (self.body[0][0] + SNAKE_SIZE, self.body[0][1])
        elif self.direction == "Left":
            head = (self.body[0][0] - SNAKE_SIZE, self.body[0][1])
        elif self.direction == "Up":
            head = (self.body[0][0], self.body[0][1] - SNAKE_SIZE)
        elif self.direction == "Down":
            head = (self.body[0][0], self.body[0][1] + SNAKE_SIZE)

        if head in self.body or head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
            return False

        self.body.insert(0, head)
        if not self.growing:
            self.body.pop()
        else:
            self.growing = False
        return True

    def eat(self):
        self.growing = True

    def draw(self):
        for pos in self.body:
            pygame.draw.rect(screen, WHITE, (pos[0], pos[1], SNAKE_SIZE, SNAKE_SIZE))

class Food:
    def __init__(self):
        self.position = random.choice([(x, y) for x in range(0, WIDTH, BLOCK_SIZE)
                                       for y in range(0, HEIGHT, BLOCK_SIZE)])
        while self.position in snake.body:
            self.position = random.choice([(x, y) for x in range(0, WIDTH, BLOCK_SIZE)
                                           for y in range(0, HEIGHT, BLOCK_SIZE)])

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.position[0], self.position[1], FOOD_SIZE, FOOD_SIZE))

def main():
    clock = pygame.time.Clock()

    global snake
    snake = Snake()
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != "Down":
                    snake.direction = "Up"
                elif event.key == pygame.K_DOWN and snake.direction != "Up":
                    snake.direction = "Down"
                elif event.key == pygame.K_LEFT and snake.direction != "Right":
                    snake.direction = "Left"
                elif event.key == pygame.K_RIGHT and snake.direction != "Left":
                    snake.direction = "Right"

        if not snake.move():
            return

        if snake.body[0] == food.position:
            snake.eat()
            food = Food()

        screen.fill(BLACK)

        snake.draw()
        food.draw()

        pygame.display.update()
        clock.tick(10)

if __name__ == "__main__":
    main()
