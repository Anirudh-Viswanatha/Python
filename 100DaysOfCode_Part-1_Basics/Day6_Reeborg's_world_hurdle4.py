#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def hurdle():
    if wall_in_front():
        turn_left()
        while (wall_on_right()) and (front_is_clear()) and (at_goal()!=True):
            move()
            if right_is_clear():
                turn_right()
                move()
                turn_right()
    else:
        move()
while (at_goal()!=True):
    hurdle()

----------------------------------------------
# Option 2 (I like option 1 better.)

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left

while (at_goal()!=True):
    if wall_in_front():
        hurdle()
    else:
        move()

