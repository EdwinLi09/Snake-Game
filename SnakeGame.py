import pygame 
import random

class SnakeGame: 
  def __init__(self): 
    pygame.init()
    # Creating the visuals
    self.white = (255, 255, 255)
    self.yellow = (255, 255, 100)
    self.black = (0, 0, 0)
    self.red = (213, 50, 80)
    self.green = (0, 204, 60)
    self.blue = (72, 118, 233)
    # Display size
    self.dis_width = 600
    self.dis_height = 400

    # Set_mode display module initializes a window for us to play the snake game 
    # Set_caption gives the display a name
    self.dis = pygame.display.set_mode((self.dis_width, self.dis_height))
    pygame.display.set_caption('Snake Game')
    
    # Times the speed of the snake 
    self.clock = pygame.time.Clock()
    # Creating the snake
    self.snake_block = 10 
    # The snake's constant speed
    self.snake_speed = 17
    
    # Specific fonts to read the text and score that will be displaying throughout the game 
    self.font_style = pygame.font.SysFont("bahnschrift", 25)
    self.score_font = pygame.font.SysFont("comicsansms", 35)

  # Scoring system
  def your_score(self, score):
    # 'Render' font module creates a surface to write text. 
    value = self.score_font.render("Score: " + str(score), True, self.black)
    # Display the text at a certain place, by specifying the starting pixel values. 
    self.dis.blit(value, [0,0]) 

  # Messaging function for our "End Game" message
  def message(self, msg, color): 
    mesg = self.font_style.render(msg, True, color)

    self.dis.blit(mesg, [self.dis_width / 4, self.dis_height / 2]) 

  
  # Displays our snake on the screen. 
  def our_snake(self, snake_list): 
    # iterate throught the snake_list which is a list and draw a rectangle, but with the parameters at the end, it will display as a square. 
    for x in snake_list: 
      pygame.draw.rect(self.dis, self.blue, [x[0], x[1], self.snake_block, self.snake_block])

  # Main function of the game
  def game_loop(self):
    # Start/Stop the game
    game_over = False
    game_close = False

    # The turning of the snake 
    x1 = self.dis_width / 2
    y1 = self.dis_height / 2 

    # Change the size of the snake
    x1_change = 0 
    y1_change = 0 
    # Start the game with the snake's starting size 
    snake_List = [] 
    length_of_snake = 1 

    # Randomly generates the food in different places on the screen 
    # Randrange is used to randomly generate a number from a certain range, which in this case the range will be the size of the display. 
    # Round function is used to align the food perfectly with the grid
    foodx = round(random.randrange(0, self.dis_width - self.snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, self.dis_height - self.snake_block) / 10.0) * 10.0
    while not game_over: 
      # If the game is over, the game will stop and display the message if they want to play again. 
      while game_close == True:
        self.dis.fill(self.green) 
        self.message("RIP! Press C to Play again or Q to Quit", self.black)
        self.your_score(length_of_snake - 1) 
        pygame.display.update() 

        # get the user input from the keyboard 
        # event.get module gets input of a certain type and the only we are interested in is the KEYDOWN event type. 
        for event in pygame.event.get():
          # KEYDOWN event type takes a keyboard input when a button is pressed. 
          if event.type == pygame.KEYDOWN:
            # When Q is pressed, the game quits 
            if event.key == pygame.K_q: 
              game_over = True 
              game_close = False
            # When C is pressed, the game restarts 
            if event.key == pygame.K_c: 
              self.game_loop()
      
      # Keyboard inputs to control and move the snake
      for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
          game_over = True
        if event.type == pygame.KEYDOWN:
          # left button 
          if event.key == pygame.K_LEFT: 
            x1_change = -self.snake_block 
            y1_change = 0 
          # right button
          elif event.key == pygame.K_RIGHT: 
            x1_change = self.snake_block 
            y1_change = 0

          # up button
          elif event.key == pygame.K_UP:
            y1_change = -self.snake_block
            x1_change = 0 
          
          # down button 
          elif event.key == pygame.K_DOWN: 
            y1_change = self.snake_block 
            x1_change = 0 
      
      # This will allow the player to move within the screen, preventing it from going off the screen
      if x1 >= self.dis_width or x1 < 0 or y1 >= self.dis_height or y1 < 0: 
        game_close = True
      x1 += x1_change 
      y1 += y1_change 
      
      # Properly display the screen, snake, and food 
      self.dis.fill(self.green) 
      pygame.draw.rect(self.dis, self.red, [foodx, foody, self.snake_block, self.snake_block])
      
      # Each iteration of the game loop, the current head position is added to the list, and if the length of the snake exceeds the desired length, the oldest segment is removed to maintain the correct length of the snake. 
      snake_head = [] 
      snake_head.append(x1) 
      snake_head.append(y1) 
      snake_List.append(snake_head) 

      # If the snake collied with itself, the game will end. 
      if len(snake_List) > length_of_snake: 
        del snake_List[0] 
      # Iterates over checking if the head has the same coordinates as the current section of its body and then ends the game 
      for x in snake_List[:-1]: 
        if x == snake_head: 
          game_close = True 

      # Update the snake's size and the score along with the game display 
      self.our_snake(snake_List) 
      self.your_score(length_of_snake - 1) 

      pygame.display.update() 

      # Implement the food for the snake, randomly placing it on the screen. 
      if x1 == foodx and y1 == foody: 
        foodx = round(random.randrange(0, self.dis_width - self.snake_block) / 10.0) * 10.0 
        foody = round(random.randrange(0, self.dis_height - self.snake_block) / 10.0) * 10.0
        length_of_snake += 1 

      # Used to control the speed and frame rate of the game 
      # Tick module helps regulate the frame rate by pausing the executing until the next frame is drawn to meet the desired speed 
      self.clock.tick(self.snake_speed)

# to close off the game_loop function and the SnakeGame class, we be quitting the pygame modules properly and terminating the application screen. 
# Constantly loop to allow the user to decide if they want to continue or quit. 
    pygame.quit() 
    quit() 

snake_game = SnakeGame() 
snake_game.game_loop() 
       