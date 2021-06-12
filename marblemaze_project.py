from sense_emu import SenseHat 
import anvil.server
from anvil.tables import app_tables
from sense_hat import SenseHat
from time import sleep
from datetime import datetime 

# data = ""
sense = SenseHat()

anvil.server.connect("RAEJLWI3IW4QSTBYXRD5I63F-QXHXSHXFGW3EAOHT")

sense.clear()

r = (255, 0, 0)  #color red 
b = (0, 0 ,0) #blank color 
p = (128, 0, 128) #ball 
g = (0,255,0) #target green
x = 1
y = 1

# def data():
#     global data
#     if maze[y][x] == r:
#         sense.show_message("try again!")
#         data = "lose"
#         game_over = True
#     elif maze[y][x] == g:
#         sense.show_message("win!")
#         data = "win"
#         game_over = True
        



@anvil.server.callable
def save_data():

    # global data
    data = "win"
    dt=datetime.now()


    new_row = app_tables.env_data1.add_row(datetime=dt,
                                            message= data
                                            )
    
    print(new_row)


    

maze = [[r, r, r, r, r, r, r, r],
        [r, b, b, b, b, b, b, r],
        [r, r, r, b, b, r, b, r],
        [r, b, r, b, b, r, r, r],
        [r, b, b, b, b, b, b, r],
        [r, b, b, r, r, r, b, r],
        [r, b, r, g, b, b, b, r],
        [r, r, r, r, r, r, r, r]]
    
game_over = False



def move_marble(x, y):
    global game_over
    new_x = x 
    new_y = y
    if maze[y][x] == r:
        sense.show_message("try again!")
        game_over = True
    return new_x, new_y
   


        
while game_over == False:
    maze[y][x] = p
    sense.set_pixels(sum(maze,[]))
    o = sense.get_orientation()
    for event in sense.stick.get_events():
        maze[y][x] = b
        if event.action == "pressed" and event.direction == "up": 
            x,y = move_marble(x,y-1)
        elif event.action == "pressed" and event.direction == "down":
            x,y = move_marble (x,y+1)
        if event.action == "pressed" and event.direction == "right":
            x,y = move_marble (x+1, y)
        elif event.action == "pressed" and event.direction == "left":
            x,y = move_marble (x-1, y)
    if maze[y][x] == g:
        sense.show_message("win!")
        game_over = True
    

# while True:
#     save_data()
#     sleep(10)



save_data()

anvil.server.call('send_message','+16314340399', message= data )
print("game over")
    
    
    
    












