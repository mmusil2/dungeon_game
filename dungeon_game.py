import random
import os

# draw grid
# pick random location for player
# pick random location for exit door
# pick random location for the monster
# draw player in the grid
# take input for movement
# move player, unless invalid move (past edges of grid)
# check for win/loss
# clear screen and redraw grid

CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_locations():
    return random.sample(CELLS, 3)
    
    
def move_player(player, move):
    # get the player's location
    x, y = player
    # if move == LEFT, x-1
    if move == 'LEFT':
        x -= 1
    if move == 'RIGHT':
        x += 1
    if move == 'UP':
        y -= 1
    if move == 'DOWN':
        y += 1
    return x, y
  
  
def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    x, y = player
    if y == 0:
        moves.remove('UP')
    if y == 4:
        moves.remove('DOWN')
    if x == 0:
        moves.remove('LEFT')
    if x == 4:
        moves.remove('RIGHT')
    return moves
  
  
def draw_map(player):
    print(" _"*5)
    tile = "|{}"

    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        print(output, end=line_end)
                
  
def game_loop():
    monster, door, player = get_locations()
    playing = True
    
    while playing:
        clear_screen()
        draw_map(player)
        #door = (2, 2)
        available_moves = get_moves(player)
        print("You're currently in room {}".format(player)) #fill with player position
        print("You can move {}".format(" , ".join(available_moves))) # fill with available moves
        print("Enter QUIT to quit")
          
        move = input("> ")      
        move = move.upper()
        # if move not in available_moves:
        #    print("That is not an option!")
        #    break
        
        #if player == door:
        #    input("You Win!")
        #    break
        
        if move == 'QUIT':
            print("\n ** See you next time! **\n")
            break
        if move in available_moves:
            player = move_player(player, move)
            
            if player == door:
                print("\n ** You escaped! Congratulations!! ** \n")
                playing = False
            if player == monster:
                print("\n ** You died! The monster ate you! ** \n")
                playing = False
        else:
            input("\n ** Walls are hard! Don't run into them! **\n")
    else:
        if input("Play again? [Y/n] ").lower() != "n":
            game_loop()
            
clear_screen()
print("Welcome to the dungeon!")
input("Press return to start!")
clear_screen()
game_loop()
    
        
    # Good move? Change player position
    # Bad move? Don't change anything!
    # On the door? They win!
    # On the monster? They lose!
    # Otherwise, loop back around