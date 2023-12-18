import pygame
import random
import sys
from pygame.locals import*
# Constants for colors
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()
font = pygame.font.Font(None, 36)
def wallpaper():
    # Initialize Pygame
    pygame.init()

    # Constants
    WIDTH, HEIGHT = 1350, 650
    WHITE = (255, 255, 255)
    
    # Create the screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Flappy Bird Home Screen")

    # Load background image (replace with your own image path)
    background = pygame.image.load("bp2.png").convert_alpha()
    play_button = pygame.image.load("play.png").convert_alpha()

    # Create a clock object to control the frame rate
    clock = pygame.time.Clock()

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                # Check if the mouse click is within the play button area
                mouse_x, mouse_y = pygame.mouse.get_pos()
                play_button_rect = play_button.get_rect()
                play_button_rect.center = (650, 450)
                
                if play_button_rect.collidepoint(mouse_x, mouse_y):
                    return "Game start"
        
        # Blit the background at (0, 0) to cover the entire screen
        screen.blit(background, (50, 0))
        
        # Display the play button in the center of the screen
        play_button_rect = play_button.get_rect()
        play_button_rect.center = (650, 450)
        screen.blit(play_button, play_button_rect)
        
        pygame.display.update()
        
        # Cap the frame rate to 60 FPS
        clock.tick(70)
def check_collision(bird_rect, upper_pipe_rect, lower_pipe_rect):
    return bird_rect.colliderect(upper_pipe_rect) or bird_rect.colliderect(lower_pipe_rect)
def gameplay():
    # Screen dimensions
    screen_width = 1350
    screen_height = 650
    # Create a window
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Flappy Bird")
    # Load images
    bird_img = pygame.image.load("bird.png").convert_alpha()
    pipe_img1 = pygame.image.load("pipe.png").convert_alpha()
    background_img = pygame.image.load("bg.jpg").convert_alpha()
    # Bird initial position
    bird_x = 10
    bird_y = 300
    #random pipe pos
    pos=random.randint(500, 1000)
   #my list of upper pipe    
    Pipes_up= [
        {'x': pos, 'y':random.randint(-250, 0)},
        {'x': pos + 689 ,'y':random.randint(-250, 0)},
    ]
    # my List of lower pipes
    Pipes_lower = [
        {'x': Pipes_up[0]['x'] + 355, 'y':random.randint(650 - pipe_img1.get_height(), 500)},
        {'x': Pipes_up[1]['x'] + 355, 'y':random.randint(650 - pipe_img1.get_height(), 500)},
    ]
    pipe=[Pipes_up,Pipes_lower]
     # Bird velocity
    bird_velocity_x = 0.2
    bird_velocity_y=-0.7
    score=0 # score =10
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    # Game variables
    exit_game = False
    game_over = False
    point = 0
    # Create a clock to control the frame rate
    clock = pygame.time.Clock()
    FPS = 70
    clock.tick(FPS)

    # Main game loop
    while not exit_game:
        # Move the pipes to the left
        Pipes_up[0]['x'] -= 1
        Pipes_lower[0]['x']-= 1  # Move the second pipe
        Pipes_up[1]['x']-= 1
        Pipes_lower[1]['x']-= 1 
        # Reset pipe positions and generate new random Y positions if they go off-screen
        if Pipes_up[0]['x'] < -pipe_img1.get_width() :
            Pipes_up[0]['x']= screen_width
            Pipes_up[0]['y']= random.randint(-250, 0)
        if Pipes_up[1]['x'] < -pipe_img1.get_width() :
            Pipes_up[1]['x'] = screen_width
            Pipes_up[1]['y'] = random.randint(-250, 0)
        if Pipes_lower[0]['x'] < -pipe_img1.get_width() :
            Pipes_lower[0]['x'] = screen_width
            Pipes_lower[0]['y']= random.randint(650 - pipe_img1.get_height(), 550)
        if Pipes_lower[1]['x'] < -pipe_img1.get_width() :
            Pipes_lower[1]['x'] = screen_width
            Pipes_lower[1]['y'] = random.randint(650 - pipe_img1.get_height(), 550)
        if (screen_width<= bird_x <= screen_width):        
            bird_x = 10  # Reset bird's X position
            bird_y = 300  # Reset bird's Y position
            #if it crosses screen height it will restart the game
        if bird_y < 0 or bird_y > 650:
                 main()
                 score=0
        # Rotate the pipe images
        rotated_pipe_img = pygame.transform.rotate(pipe_img1, 180)
        # event that is going to be done by us
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                exit_game = True
           
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                   bird_velocity_x=.5
                   bird_x+=10
                if event.key==pygame.K_LEFT:
                    bird_velocity_x=-.5
                    bird_x-=10
                if event.key==pygame.K_UP:
                    bird_velocity_y=-.7
                if event.key==pygame.K_DOWN:
                    bird_velocity_y=.7
        bird_x=bird_x+bird_velocity_x
        bird_y=bird_y+bird_velocity_y   
        pipeupmidpos=[0,0]
        pipelowmidpos=[0,0]
        # Bird center position of x
        bird_center = bird_x + bird_img.get_width() / 2
        # pipe center position of x
        for i in range (2):
            pipeupmidpos[i]=Pipes_up[i]['x'] +pipe_img1.get_width()/2   
            pipelowmidpos[i]=Pipes_lower[i]['x'] +pipe_img1.get_width()/2   
            print(pipelowmidpos)
            print(pipeupmidpos)
        # calculation of score        
        for i in range (2):
            if (bird_center==pipelowmidpos[i])or (bird_center==pipeupmidpos[i]):
                 if ( (bird_y >  Pipes_up[i]['y']) or (bird_y < Pipes_lower[i]['y'])):
                    if ((bird_y >  Pipes_up[i]['y']) and (bird_y < Pipes_lower[i]['y'])):
                        score+=2
                        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
                    else:
                        score+=1
                        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
                  
  
    
           # Get the rectangles for collision detection
        bird_rect = pygame.Rect(bird_x, bird_y, bird_img.get_width(), bird_img.get_height())
        upper_pipe_rect1 = pygame.Rect(Pipes_up[0]['x'], Pipes_up[0]['y'], pipe_img1.get_width(), pipe_img1.get_height())
        lower_pipe_rect1 = pygame.Rect(Pipes_lower[0]['x'], Pipes_lower[0]['y'], pipe_img1.get_width(), pipe_img1.get_height())
        upper_pipe_rect2 = pygame.Rect(Pipes_up[1]['x'], Pipes_up[1]['y'], pipe_img1.get_width(), pipe_img1.get_height())
        lower_pipe_rect2 = pygame.Rect(Pipes_lower[1]['x'], Pipes_lower[1]['y'], pipe_img1.get_width(), pipe_img1.get_height())

        # Check for collisions
        if check_collision(bird_rect, upper_pipe_rect1, lower_pipe_rect1) or check_collision(bird_rect, upper_pipe_rect2, lower_pipe_rect2):
            # Perform actions when collision occurs (e.g., end the game)
            # if score < high_score:
            #     high_score = score
            gameplay()
            print("Game Over")       
        # Update the screen
        screen.fill(WHITE)
        screen.blit(background_img, (0, 0))
        screen.blit(score_text, (10, 10)) 
        screen.blit(bird_img, (bird_x, bird_y))
        screen.blit(rotated_pipe_img, (Pipes_up[0]['x'], Pipes_up[0]['y']))
        screen.blit(pipe_img1, (Pipes_lower[0]['x'] , Pipes_lower[0]['y'] ))
        screen.blit(rotated_pipe_img, (Pipes_up[1]['x'], Pipes_up[1]['y']))
        screen.blit(pipe_img1, (Pipes_lower[1]['x'] , Pipes_lower[1]['y'] ))
       
        pygame.display.update()

    pygame.quit()

def main():
    # high_score=0
    x= wallpaper()
    if x=="Game start":
        gameplay()  # Call the gameplay function to start the game

if __name__ == "__main__":
   
    main()
 