from sense_hat import SenseHat 

sense = SenseHat()
sense.clear()
r = (255, 0, 0)  #color red 
w = (0, 0 ,0) #blank color 
# c = (0, 255, 255) end
p = (128, 0, 128) #ball




maze = [[r, r, r, r, r, r, r, r],
        [r, w, w, w, w, w, w, r],
        [r, r, r, w, w, r, w, r],
        [r, w, r, w, w, r, r, r],
        [r, w, w, w, w, w, w, r],
        [r, w, w, r, r, r, w, r],
        [r, w, r, w, w, w, w, r],
        [r, r, r, r, r, r, r, r]]

game_over = False

def move_marble(pitch, roll, x, y):
    new_x = x
    new_y = y
    if 1 < pitch < 179:
        new_x -= 1


    return new_x, new_y

    
while game_over == False:
    o = sense.get_orientation()
    pitch = o["pitch"]
    roll = o["roll"]
    maze[y][x] = w
    sense.set_pixels(sum(maze,[]))




