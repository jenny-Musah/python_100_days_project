print("Welcome to Treasure Island \nYour mission is to find the treasure.")
direction: str = input("You are at a cross road, Where do you want to go type 'left' to go left or type  'right' to "
                       "go right ?\n")
if direction == "left" or direction == "Left":
    decision: str = input("You took a left turn and arrived at an island, now you are at the river bank would you"
                          " like to wait for a boat or swim type 'wait' to wait or 'swim' to swim across?\n")
    if decision == "wait" or decision == "Wait":
        rescue: str = input("Your boat got hit by some solid object in the water and you are about to"
                            "sink would you jump off the boat or realize the boat of it load"
                            "type 'jump' to jump and 'realize' to realize.").lower()
        if rescue == "realize":
            doors: str = input("You arrived at the other side of the river unharmed with three doors in front of you,"
                               "which door would you like open red ,blue or yellow, type 'red' to open the red door"
                               "'yellow' to open the yellow and 'blue' to open the blue door?\n")
            if doors == "yellow" or doors == "Yellow":
                print("Congratulations you found the treasure!!")
            else:
                print("You got locked up behind the door!,Game over!")
        else:
            print("You got carried away by the water down the rock...Game over!")
    else:
        print(" You got eaten by a crocodile!, Game Over!")
else:
    print("You got to a dead end, Game Over!")
