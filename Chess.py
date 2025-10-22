# Creation of chess game in python
import pygame
import time

pygame.init()
WIDTH, HEIGHT = 1000, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

font = pygame.font.Font(None, 20)
med_font = pygame.font.Font(None, 30)
big_font = pygame.font.Font(None, 50)

timer = pygame.time.Clock()
fps = 60

# Game variables and images
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_location = [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0),
                    (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1)]

black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_location = [(0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7),
                    (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6)]

captured_white = []
captured_black = []

# turns
turn_step = 0
selection = 100
valid_moves = []

# load images
# Note: load in queen, king, rook, bishop, knight, pawn images for both colors

## Load white pieces
white_king = pygame.image.load('assets/images/white king.png')
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))

white_queen = pygame.image.load('assets/images/white queen.png')
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))

white_rook = pygame.image.load('assets/images/white rook.png')
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))

white_bishop = pygame.image.load('assets/images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))

white_knight = pygame.image.load('assets/images/white knight.png')
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))

white_pawn = pygame.image.load('assets/images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (65, 65))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))

## Load black pieces
black_king = pygame.image.load('assets/images/black king.png')
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (45, 45))

black_queen = pygame.image.load('assets/images/black queen.png')
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))

black_rook = pygame.image.load('assets/images/black rook.png')
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))

black_bishop = pygame.image.load('assets/images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))

black_knight = pygame.image.load('assets/images/black knight.png')
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))

black_pawn = pygame.image.load('assets/images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))

# List of piece images

white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small, white_rook_small, white_bishop_small]

black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small, black_rook_small, black_bishop_small]

# Piece list for indexing
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

# Checking functions

counter = 0

# win factor
winner = ''

# Game over flag
game_over = False

# Clock Variables

game_start_time = time.time() # Records when the game started
white_turn_start = time.time() # Records when white's current turn started
black_turn_start = 0 # Update when black's turn starts (starts at 0 since white is first)
white_total_time = 0 # Total time white has spent across all turns
black_total_time = 0 # Total time black has spent across all turns


# Function to draw the chessboard

def draw_board():
    for i in range (32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, (255,204,204), [600 - (column * 200),row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, (255,204,204), [700 - (column * 200),row * 100, 100, 100])

        pygame.draw.rect(screen, (108,77,160), [0,800,WIDTH,100]) # bottom box fill
        pygame.draw.rect(screen, (63,162,154), [800,0,200,HEIGHT]) # right box fill
        pygame.draw.rect(screen, (20, 50, 80), [600,800,200,100]) # forfeit box fill
        pygame.draw.rect(screen, (255,179,71), [800,800,200,100]) #bottom right corner box fill

        pygame.draw.rect(screen, (47,107,104), [0,800,WIDTH,100], 5) # bottom line border
        pygame.draw.rect(screen, (75,59,115), [800,0,200,800], 5) # right line border
        pygame.draw.rect(screen, (190, 50, 50), [600,800,200,100], 5) # forfeit line border
        pygame.draw.rect(screen, (139,64,0), [800,800,200,100], 5) # bottom right corner line border



        status_text = ['White: Select a piece to play!','White: Select a square to place!',
                       'Black: Select a piece to play!','Black: Select a square to place!']
        big_font = pygame.font.Font("assets/Fonts/FredokaOne-Regular.ttf",37)
        med_font = pygame.font.Font("assets/Fonts/Arvo-Bold.ttf", 35) 
        screen.blit(big_font.render(status_text[turn_step], True, 'black'),(20, 825))
        screen.blit(big_font.render(status_text[turn_step], True, (255,250,205)), (18, 823)) #102,0,51 for red
        for i in range(9):
            pygame.draw.line(screen, (75,75,75), (0,100 * i), (800, 100 * i), 2) #Horizontal lines
            pygame.draw.line(screen, (75,75,75), (100 * i,0), (100 * i, 800), 2) #Vertical lines
        screen.blit(med_font.render('FORFEIT', True, (160,40,40)), (622, 830)) #forfeit text

# Function to draw pieces on the board

def draw_pieces():
   
    # Draw white pieces

    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_location[i][0] * 100 + 18, white_location[i][1] * 100 + 18))
        else:
            screen.blit(white_images[index], (white_location[i][0] * 100 + 10, white_location[i][1] * 100 + 10))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [white_location[i][0] * 100 + 1, white_location[i][1] * 100 + 1, 100, 100], 2)

    # Draw black pieces
    
    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_location[i][0] * 100 + 18, black_location[i][1] * 100 + 18))
        else:
            screen.blit(black_images[index], (black_location[i][0] * 100 + 10, black_location[i][1] * 100 + 10))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [black_location[i][0] * 100 + 1, black_location[i][1] * 100 + 1, 100, 100], 2)

# Function to check valid moves for each piece

def check_options(pieces, locations, turn):
    
    moves_list = []
    all_moves_list = []
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn_moves(location, turn)
        elif piece == 'rook':
            moves_list = check_rook_moves(location, turn)
        elif piece == 'knight':
            moves_list = check_knight_moves(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop_moves(location, turn)
        elif piece == 'queen':
            moves_list = check_queen_moves(location, turn)
        elif piece == 'king':
            moves_list = check_king_moves(location, turn)

        all_moves_list.append(moves_list)

    return all_moves_list

# Check valid moves for each piece type

## pawn moves
def check_pawn_moves(position, color):
    moves_list = []
    if color == 'white':
        if (position[0], position[1] + 1) not in white_location and (position[0], position[1] + 1) not in black_location and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in white_location and (position[0], position[1] + 2) not in black_location and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in black_location:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in black_location:
            moves_list.append((position[0] - 1, position[1] + 1))

    else: 
        if (position[0], position[1] - 1) not in white_location and (position[0], position[1] - 1) not in black_location and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in white_location and (position[0], position[1] - 2) not in black_location and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in white_location:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in white_location:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list

## rook moves
def check_rook_moves(position, color):
    moves_list = []
    
    if color == 'white':
        enemies_list = black_location
        friends_list = white_location
    else:
        enemies_list = white_location
        friends_list = black_location
    
    for i in range(4): #vertical and horizontal directions
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and 0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))

                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False

    return moves_list

## knight moves
def check_knight_moves(position, color):
    moves_list = []

    if color == 'white':
        enemies_list = black_location
        friends_list = white_location
    else:
        enemies_list = white_location
        friends_list = black_location

    #Knight moves in L shape [8 squares to check]

    targets = [(1,2), (1,-2), (2,1), (2,-1), (-1,2), (-1,-2), (-2,1), (-2,-1)]
    
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)

    return moves_list

## bishop moves
def check_bishop_moves(position, color):
    moves_list = []

    if color == 'white':
        enemies_list = black_location
        friends_list = white_location
    else:
        enemies_list = white_location
        friends_list = black_location
    
    for i in range(4): #diagonal directions
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and 0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))

                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False


    return moves_list

## queen moves
def check_queen_moves(position, color):
    moves_list = check_bishop_moves(position, color)

    second_list = check_rook_moves(position, color)

    for i in range(len(second_list)):
        moves_list.append(second_list[i])

    return moves_list

## king moves
def check_king_moves(position, color):
    moves_list = []

    if color == 'white':
        enemies_list = black_location
        friends_list = white_location
    else:
        enemies_list = white_location
        friends_list = black_location

    #King moves in 8 squares around it
    
    targets = [(1,0), (1,1), (1,-1), (-1,0), (-1,1), (-1,-1), (0,1), (0,-1)]
    
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)


    return moves_list

# check for valid moves for the selected piece
def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    
    return valid_options


# draw valid moves on the board
def draw_valid_moves(moves):
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5)


# Function to draw captured pieces
def draw_captured_pieces():
    for i in range(len(captured_white)):
        captured_piece = captured_white[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_black_images[index], (825, 5 + 50*i))

    for i in range(len(captured_black)):
        captured_piece = captured_black[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_white_images[index], (925, 5 + 50*i))

# Function to draw check status
def draw_check():
    if turn_step < 2:
      if 'king' in white_pieces:
        king_index = white_pieces.index('king')
        king_location = white_location[king_index]
        for i in range(len(black_options)):
            if king_location in black_options[i]:
                if counter < 15:
                    pygame.draw.rect(screen, 'dark red', [white_location[king_index][0] * 100 + 1, white_location[king_index][1] * 100 + 1, 100, 100], 5)

    else:
        king_index = black_pieces.index('king')
        king_location = black_location[king_index]
        for i in range(len(white_options)):
            if king_location in white_options[i]:
                if counter < 15:
                    pygame.draw.rect(screen, 'dark blue', [black_location[king_index][0] * 100 + 1, black_location[king_index][1] * 100 + 1, 100, 100], 5)

# Function to draw game over screen
def draw_game_over():
    pygame.draw.rect(screen, (0, 0, 0), [200, 200, 400, 70])  # Black background
    screen.blit(font.render(f'{winner} wins!', True, 'white'), (210, 210)) # White text
    screen.blit(font.render(f'press ENTER to restart!', True, 'white'), (210, 240)) # White text

# Function to draw clock over screen
def draw_clock():
    """Draw the game clock and turn timers in the bottom right box"""
    current_time = time.time()

    #Calculate total elapsed time
    total_game_time = current_time - game_start_time
    total_minutes = int(total_game_time // 60)
    total_seconds = int(total_game_time % 60)

    # Calculate current turn time and total times
    if turn_step < 2: # White's turn
        white_current_turn = current_time - white_turn_start
        white_display_time = white_total_time + white_current_turn
        black_display_time = black_total_time
    else: # Black's turn
        black_current_turn = current_time - black_turn_start
        black_display_time = black_total_time + black_current_turn
        white_display_time = white_total_time

    # Formatting the times
    white_mins = int(white_display_time // 60)
    white_secs = int(white_display_time % 60)
    black_mins = int(black_display_time // 60)
    black_secs = int(black_display_time % 60)

    # Fonts for clock
    clock_font = pygame.font.Font("assets/Fonts/Arvo-Bold.ttf", 20)
    time_font = pygame.font.Font("assets/Fonts/Arvo-Bold.ttf", 28)

    # Draw Total Game Time
    screen.blit(clock_font.render('GAME TIME', True, (50,50,50)), (835, 805))
    screen.blit(time_font.render(f'{total_minutes:02d}:{total_seconds:02d}', True, (255,255,255)), (860, 825))

    # Only display active player's clock 
    if turn_step < 2: # Draw White's Time (highlighted)
        screen.blit(clock_font.render('WHITE', True, (255,250,250)), (815, 860))
        screen.blit(time_font.render(f'{white_mins:02d}:{white_secs:02d}', True, (99,149,238)), (900, 855))
        
    else: # Draw Black's Time (highlighted)
        screen.blit(clock_font.render('BLACK', True, (53,56,57)), (815, 860))
        screen.blit(time_font.render(f'{black_mins:02d}:{black_secs:02d}', True, (250,80,83)), (900,855))

# main loop
black_options = check_options(black_pieces, black_location, 'black')
white_options = check_options(white_pieces, white_location, 'white')


run = True
while run:
    timer.tick(fps)
    if counter < 30:
        counter += 1
    else:
        counter = 0

    screen.fill((129, 134, 74))

    # Draw the checkerboard
    draw_board()
    draw_pieces()
    draw_captured_pieces()
    draw_check()
    draw_clock()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid_moves(valid_moves)
    

# Event handling
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:  # Left mouse button click
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coord = (x_coord, y_coord)
            
            #For white's turn

            if turn_step <= 1:
               
                if click_coord == (6, 8) or click_coord == (7, 8):
                    winner = 'black'
                    game_over = True
                if click_coord in white_location:
                    selection = white_location.index(click_coord)
                    if turn_step == 0:
                        turn_step = 1
                if click_coord in valid_moves and selection != 100:
                    white_location[selection] = click_coord
                    if click_coord in black_location:
                        black_piece = black_location.index(click_coord)
                        captured_white.append(black_pieces[black_piece])
                        if black_pieces[black_piece] == 'king':
                            winner = 'white'
                        black_pieces.pop(black_piece)
                        black_location.pop(black_piece)
                    black_options = check_options(black_pieces, black_location, 'black')
                    white_options = check_options(white_pieces, white_location, 'white')
                    turn_step = 2
                    white_total_time += time.time() - white_turn_start # Update white's total time
                    black_turn_start = time.time() # Start black's turn timer
                    selection = 100
                    valid_moves = []

            # For black's turn

            if turn_step > 1:
                
                if click_coord == (6, 8) or click_coord == (7,8): 
                    winner = 'white'
                    game_over = True
                if click_coord in black_location:
                    selection = black_location.index(click_coord)
                    if turn_step == 2:
                        turn_step = 3
                if click_coord in valid_moves and selection != 100:
                    black_location[selection] = click_coord
                    if click_coord in white_location:
                        white_piece = white_location.index(click_coord)
                        captured_black.append(white_pieces[white_piece])
                        if white_pieces[white_piece] == 'king':
                            winner = 'black'
                        white_pieces.pop(white_piece)
                        white_location.pop(white_piece)
                    black_options = check_options(black_pieces, black_location, 'black')
                    white_options = check_options(white_pieces, white_location, 'white')
                    turn_step = 0
                    black_total_time += time.time() - black_turn_start # Update black's total time
                    white_turn_start = time.time() # Start white's turn timer
                    selection = 100
                    valid_moves = []
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                # Reset game state
                game_over = False
                winner = ''
                
                game_start_time = time.time()
                white_turn_start = time.time()
                black_turn_start = 0
                white_total_time = 0
                black_total_time = 0

                white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                white_location = [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0),
                                    (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1)]

                black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                black_location = [(0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7),
                                    (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6)]

                captured_white = []
                captured_black = []
                turn_step = 0
                selection = 100
                valid_moves = []
                black_options = check_options(black_pieces, black_location, 'black')
                white_options = check_options(white_pieces, white_location, 'white')

    if winner != '':
        game_over = True
        draw_game_over()

    pygame.display.flip()
pygame.quit()