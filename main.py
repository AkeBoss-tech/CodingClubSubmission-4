from utilities import player
from tools import tool
from pyfiglet import Figlet







# If you want to play this game,
# Please play it first and then read the code.
# The code will show spoilers of the game.












bigLetter = Figlet(font='slant')
word = 'Escape the Desert'
curr_word = ''
print(bigLetter.renderText(word))

p = player()

a = "In this game you will try to survive as long as possible. If you reach humanity you will win, but if you die you lose. You will die when your health reaches 0 points. Your hunger, water, and temperature points will also negatively impact your health. The only way to regenerate health is to have full hunger and water bars."
b = "You just woke up in a desert. When you get up, you can’t see anything for miles. "
c = "Just sand, cactuses, and … SNAKES!!!!"
d = "You see a large rattlesnake slithering around in front of you. Behind you, there is a stick. What do you do?"
e = "Do you try to pick the stick up and fight the snake?"
f = "Do you run away?"
g = "Do you stand as still as you can?"
h = "Or do you fight the snake with your bare hands?"
textList = [b,c,d]
p.storyTelling(textList, 3)
choice = p.getNumberInput([e,f,g,h], checkDamage = True)
a = "Before we learn your fate, let’s talk more about this game."
b = "In this game, you are trying to escape the desert."
c = "You have many different attributes like health, water, and hunger."
d = "You must make sure your health never reaches zero, otherwise, you will die. "
e = "If you run out of water or hunger you will begin losing health. "
f = "Right now you can set the game mode to Easy, Medium, or Hard. This will change the amount of health, water, and hunger you start with."
textList = [a,b,c,d,e,f]
p.storyTelling(textList)
difficulties = ["easy", "medium", "hard"]
difficulty = p.getTextInput(difficulties, 1, checkDamage = True)
p.setDifficulty(difficulty)
print(bigLetter.renderText(difficulties[difficulty]))
p.printStats()
a = "\n\nOk, now let’s see what happened to you."
if choice == 0:
    b = "You slowly reach over and pick up the stick."
    c = "The rattlesnake has started rattling its tail, it is warning you to back off. "
    d = "You jab the 1-foot long stick towards the snake’s face."
    e = "The snake stays right where it is, its rattling sound grows louder. The snake is surely going to jump at you!"
    f = "But no, you swing the stick into the snake’s mouth and smack its head on the ground."
    g = "Now you can safely leave the area."
    h = "You better hold on to the stick, sticks are rare in the desert."
    p.move("away from the snake")
    stick = tool("stick", "Killing", 10)
    p.changeInventory(stick, True)
    p.storyTelling([a,b,c,d,e,f,g,h],3)

elif choice == 1:
    b = "The snake is right in front of you."
    c = "You look behind you to see if there are any obstructions ..."
    d = "and you slowly back away and then quickly turn around and run to safety."
    p.move("away from the snake")
    p.storyTelling([a,b,c,d],3)

elif choice == 2:
    d = "The snake is slowly inching towards you. "
    e = "You try not to move but the snake can still see you."
    f = "Out of nowhere, a chipmunk lunges into the air and the snake pounces on it."
    g = "You quickly run away to safety."
    h = "That was a close call!"
    p.move("away from the snake")
    p.storyTelling([a,d,e,f,g,h],3)

elif choice == 3:
    d = "The snake is still rattling its tail. "
    e = "You are scared but you still want to assert your dominance over the snake."
    f = "You stomp around and clap your hands. "
    g = "The snake rattles louder,"
    h = " but then you kick the snake and it backs away."
    p.move("away from the snake")
    p.storyTelling([a,d,e,f,g,h],3)

print("\n\n\n")
a = "Phew!"
b = "You are glad that is over."
c = "You take some time to look around your surroundings."
d = "To the north, you see a large mountain with a green forest about 10-15 miles away."
e = "To the east, there is a large canyon about 5-10 miles away. "
f = "To the south, you see some sort of building with no walls 5-10 miles away. "
g = "To the west, the desert continues."
h = "Remember, your goal is to try and reach civilization, but you have to get there alive. "
i = "So you have to make sure you still have food, water, and a constant temperature."
p.storyTelling([a,b,c,d,e,f,g,h,i],3)
directions = ["north", "east", "south", "west"]
choice = p.getTextInput(["north", "east", "south", "west"], 1, checkDamage = True)
print(bigLetter.renderText(directions[choice]))

a = "You can look for food or water at any time by typing forage"
b = "You can use any item by typing use"
c = "You can look at your health and attributes by typing stats"
p.storyTelling([a,b,c])

if choice == 0:
    p.decidedLocation = "north"
    a = "Looks like we are heading to the north to the mountains."
    b = "You just have to make sure you don't lose too many hydration points."
    p.storyTelling([a,b])
elif choice == 1:
    p.decidedLocation = "east"
    a = "Looks like we are heading to the east to the canyon."
    b = "You just have to make sure you don't lose too many hydration points."
    p.storyTelling([a,b])
elif choice == 2:
    p.decidedLocation = "south"
    a = "Looks like we are heading to the south to the building."
    b = "You just have to make sure you don't lose too many hydration points."
    p.storyTelling([a,b])
elif choice == 3:
    p.decidedLocation = "west"
    a = "Looks like we are heading to the west."
    b = "I just have to make sure I don't lose too many hydration points."
    p.storyTelling([a,b])
p.run(2)
a = f"You’ve been walking to the {p.decidedLocation} for a long time now."
b = "It’s been an hour and you remember your backpack."
c = "You frantically take it off and search it for anything useful."
d = "There are a few pens and a notebook in the bag along with a water bottle. "
pens = tool("pen", "Killing", 4)
e = "WATER!! "
f = "You realize that your throat is parched and you don’t have a drop of water."
g = "What should you do?"
p.storyTelling([a,b,c,d,e,f,g])
notebook = tool("notebook", "Storage")
bottle = tool("bottle", "Storage")
p.changeInventory(bottle, True)
p.changeInventory(pens, True)
a = "Go off your trail in search of water"
b = "Continue on the Trail"
c = "Look for some watery plants near the trail to eat."
choice = p.getNumberInput([a,b,c], checkDamage = True)

a = p.decidedLocation
if a == "north":
    b = "east"
elif a == "east":
    b = "south"
elif a == "south":
    b = "west"
elif a == "west":
    b = "north"

if choice == 0:
    p.findWaterFeature()
    l = "You've wandered further away from the trail."
    m = f"You are close to the {b} trail."
    p.storyTelling([l,m])
    li = [a,b]
    t = p.getTextInput(li, checkDamage = True)
    p.decidedLocation = li[t]
    p.move("Midpoint", 0)
elif choice == 1:
    p.water -= 3
elif choice == 2:
    p.findWaterPlant()

a = "The sun is beginning to set."
b = "Night is quickly approaching and it is clear that you won't be able to walk at night."
c = "You need to sleep tonight."
d = "Sleep under the stars."
e = "Find shelter under a rock or ridge"
f = "Continue walking during the night"
p.storyTelling([a,b,c])
choice = p.getNumberInput([d,e,f], checkDamage = True)
if choice == 0:
    a = "You swiftly fall into a deep sleep."
    b = "You do not realize that snakes and critters scurry across your body."
    c = "While you are sleeping you roll over onto a snake."
    d = "The scared snake bites you..."
    p.storyTelling([a,b,c,d])
    p.alive = False
    p.dead()
elif choice == 1:
    a = "You see a large boulder in a clearing."
    b = "You use the stones near the rock to create a wall so that animals can't disturb you."
    c = "Then you make yourself commfortable and use your backpack as a pillow to prop it up."
    d = "\nYou sleep peacefully in the night."
    p.storyTelling([a,b,c,d])
    p.move("Campsite")
elif choice == 2:
    a = "You continue walking in the night."
    b = "You can't see a thing..."
    c = "As you are walking your foot slips."
    d = "And you fall..."
    p.storyTelling([a,b,c,d])
    p.alive = False
    p.dead()

print(bigLetter.renderText(p.decidedLocation))

if p.decidedLocation == "north":
    a = "You have to walk 10 miles to reach the mountain."
    b = "You will be really hungry after your journey."
    c = "Use this time to find food by typing forage."
    p.storyTelling([a,b,c])
    p.getTextInput(["ready"], checkDamage = True)
    p.move("Mountain", 10)
    a = "You have reached the mountain."
    b = "There lies a river near the mountain."
    e = "This decision could mean life or death."
    p.storyTelling([a,b,e])
    c = "Do we climb to the top of the mountain?"
    d = "Or do we follow the river?"
    choice = p.getNumberInput([c,d], checkDamage = True)
    if choice == 0:
        a = "Time to begin the climb up the mountain."
        p.move("Top of the Mountain")
        b = "You slowly climb your way up the mountain."
        c = "You can see a town by the banks of the river!"
        d = "In your excitement, you begin running down the hill."
        e = "and ..."
        f = "You fall to your death"
        p.storyTelling([a,b,c,d,e,f], 3)
        p.alive = False
        p.dead()
    else:
        a = "While walking by the river you see a boat."
        b = "You take the boat and start paddling down the river."
        c = "About a mile downstream, you enter the canyon."
        d = "There you see a group of happy hikers."
        e = "You get off the boat."
        f = "And they take you home!"
        p.storyTelling([a,b,c,d,e,f], 3)
        
elif p.decidedLocation == "east":
    a = "You have to walk 6 miles to reach the canyon."
    b = "You will be really hungry after your journey."
    c = "Use this time to find food by typing forage."
    p.storyTelling([a,b,c])
    p.getTextInput(["ready"], checkDamage = True)
    p.move("Canyon", 6)
    a = "Now that you have reached the canyon."
    b = "You have a decision to make"
    p.storyTelling([a,b])
    a = "Do you travel above the canyon?"
    b = "Or do you travel near the river below?"
    choice = p.getNumberInput([a,b], checkDamage = True)
    if choice == 0:
        a = "As you are walking above to canyon"
        b = "You watch the wonderful river roaring down stream."
        c = "The terrain around the canyon becomes tougher."
        d = "Eventually, you are forced to descend the canyon."
        e = "The loose rocks on the canyon walls are hard to traverse."
        f = "Then, you slip ..."
        p.storyTelling([a,b,c,d,e,f], 3)
        p.alive = False
        p.dead()
    else:
        l = "You slowly make your way down the canyon."
        p.move("river")
        a = "While walking by the river you see a boat."
        b = "You take the boat and start paddling down the river."
        c = "About a mile downstream, you exit the canyon."
        d = "There you see a group of happy hikers."
        e = "You get off the boat."
        f = "And they take you home!"
        p.storyTelling([l, a,b,c,d,e,f], 3)

elif p.decidedLocation == "south":
    a = "You have to walk 7 miles to the abandoned town."
    b = "You will be really hungry after your journey."
    c = "Use this time to find food by typing forage."
    p.storyTelling([a,b,c])
    p.getTextInput(["ready"], checkDamage = True)
    p.move("Abandoned town", 7)
    a = "You have finally entered the abandoned town."
    b = "The town has various buildings and signs leading to a highway"
    p.storyTelling([a,b])
    a = "Will you search the buildings?"
    b = "Or will you follow the signs to the highway."
    choice = p.getNumberInput([a,b], checkDamage = True)
    if choice == 0:
        a = "You look around the town."
        b = "You enter the tallest building you see, the church."
        c = "There are spiders everywhere."
        d = "The floor is creaking loudly."
        e = "The wood in the building is clearly rotting."
        f = "As you begin to walk in the rows of benches,"
        g = "The roof suddenly collapses on you..."
        p.storyTelling([a,b,c,d,e,f,g], 3)
        p.alive = False
        p.dead()
    else:
        a = "You decide to start following the signs."
        b = "You see that you are on Main street."
        c = "The signs lead you through the maze of the town."
        d = "Eventually the signs end,"
        e = "And you can hear the roaring of the cars racing down the freeway!"
        f = "You follow the sound and find the freeway."
        g = "Finally!"
        h = "You sit down to rest and then a truck stops in front of you."
        i = "The trucker asks you if you need a lift."
        j = "And you wholeheartedly say YES!!! gg pogchamp"
        p.storyTelling([a,b,c,d,e,f,g,h,i,j], 3)
elif p.decidedLocation == "west":
    a = "You have to walk 18 miles."
    b = "You will be really hungry after your journey."
    c = "Use this time to find food by typing forage."
    p.storyTelling([a,b,c])
    p.getTextInput(["ready"], checkDamage = True)
    p.move("Desert End", 18)
    a = "You reach the end of the trail."
    b = "There is still desert all around you."
    c = "You are still lost."
    d = "You begin losing hope..."
    p.storyTelling([a,b,c,d], 3)
    p.alive = False
    p.dead()

# GG YOU HAVE WON!!!!!
p.win()

print(bigLetter.renderText("Good job"))
print(bigLetter.renderText("-AkeBoss"))

# You don't know how long it took to make this
# Thank you for appreceating this!

# and yes, I am too lazy to comment my code