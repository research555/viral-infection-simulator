import random
import time

# Create the students
n_tot = list(range(50))

# Create list of students that are infected and immune
list_of_infected = []
list_of_immune = []

# Define iterations before loop
iterations = 0

# Initial infector is any student
initial_infector = random.randint(0,50)
print("""\n\n\nMaximize this window. This is a code that models how a virus spreads\n
in a population of 50 people, named 1-50. Each day, two people interact with each other and if\n
one of them is infected, there is a certain likelihood that they will also get infected.\n
This goes on for 100 days . . . \n
\n
PS. If when you run the program, all you get are empty brackets, exit and start again\n\n""")

input("Click enter once to continue . . . \n")

# # # # Iterate through and update the lists created above # # # #

while iterations <= 100:
    iterations += 1
    pool = n_tot.copy() # Create pool of students using the same list as n_tot
    random.shuffle(pool) # Shuffle them around
    rooms = [] # Place them in rooms

    for i in range(20):
        rooms.append([pool.pop(), pool.pop()]) # create 20 sublists with 2 students in each room

    for couple in rooms:
        for student in couple: # iterate through every student in room
            if student == initial_infector:
                infection_rate = random.randint(0, 100)
                if infection_rate <= 99: # Set infection rate
                    if couple[0] not in list_of_immune: # Check if students are immune, if not, add them to infected
                        if couple[0] not in list_of_infected:
                            list_of_infected.append(couple[0])
                    if couple[1] not in list_of_immune:
                        if couple[1] not in list_of_infected:
                            list_of_infected.append(couple[1])
                else:
                    if student not in list_of_immune:
                        if student not in list_of_infected:
                            list_of_infected.append(student)
            else:
                pass

    for student in list_of_infected:
        immune_rate = random.randint(2, 100)
        if immune_rate <= 1: # Set immune rate
            list_of_infected.remove(student)
            list_of_immune.append(student)

    print("day " + str(iterations), list_of_infected)
    time.sleep(0.3)


print("\nWith an incredibly miniscule knowledge of Python, and just 60 lines of code, its possible to model the spread of disease.\n"
      "To look at its progression over the days, scroll up and down on the console below.\n"
      "Coding is an extremely powerful tool to have in your toolbox. Consider it.\n"
      "\n"
      "Your next task is to open Microsoft Edge (the blue-green e on the taskbar below)\n")

input("\nWhen you are done, come back here.\n\n Press enter to continue . . . ")

word = "\nCONGRATULATIONS"
for letter in word:
    print(letter)
    time.sleep(0.3)


print("\n\nYou are now the proud owner of a Scientific American magazine subscription.\n"
      "You will receive one issue in the mail every month for a year.\n")

input("Press enter to continue . . . ")

print("\nYou are falling asleep in your bed. You hear footsteps approach your bedroom door.\n"
      "You brush it off and think to yourself that its probably just your brother coming to bother you.\n"
      "You realize that you just recently moved out of your parents house, and are living alone.\n"
      "Your eyes light up, adrenaline kicks in, and you jump off the bed to find the nearest object to defend yourself with.\n"
      "That object is a bucket full of water that you use to catch the rain leaking in from your roof.\n"
      "You pick the bucket up to prepare splashing it onto the intruder in hopes of shocking them for long enough to escape.\n"
      "The door creaks open, and your heart races - bom-bom-bom-bom.\n"
      "\n. . .\n"
      ". . .\n"
      ". . .\n")

input("Press enter to learn your fate\n")

for iter in range(20):
    print("bom-bom-bom-bom")
    time.sleep(0.3)

print("\n . . .\n")
time.sleep(3)

print("\nYou jolt up from your bed, your heart still racing.\n"
      "It was a dream, you sigh to yourself.\n")
time.sleep(3)

print("\n\nLocate your weapon from your nightmare.\n"
      "Hint: 961")


input("\n Press enter to exit")