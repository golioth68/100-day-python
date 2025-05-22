# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


for step in range(6):
    hurdle()

number_of_hurdles = 0
while number_of_hurdles > 0:
    hurdle()
    number_of_hurdles -= 1

# or if number of hurdles is unknown use while with not
while not at_goal():
    hurdle()

while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        hurdle()
    else:
        move()

def climb():                 # works for any wall height
    turn_left()              # face north, start climbing
    while wall_on_right():   # keep going up until you can step over
        move()
    turn_right()             # now the top corner is on your right
    move()                   # cross the wall
    turn_right()             # face south, climb down the far side
    while front_is_clear():  # descend until you’re back on ground level
        move()
    turn_left()              # face east again (original heading)

# -------------- MAIN LOOP --------------
while not at_goal():             # 1  sentinel guard
    if wall_in_front():          # 2  hurdle directly ahead?
        climb()                  #    → scale it
    elif right_is_clear():       # 3a open space on the right?
        turn_right()
        move()
    else:                        # 3b path ahead is clear, right is blocked
        move()

while not at_goal():
    if wall_in_front():
        climb()
    elif front_is_clear():
        move()
    elif wall_on_right() and wall_in_front():
        turn_left()
    else:
        move()