import time, random, sys
from tools import tool
from pyfiglet import Figlet

bigLetter = Figlet(font='slant')

class player:
    def __init__(self):
        self.health = 10
        self.water = 10
        self.hunger = 10
        self.difficulty = "N/A"
        self.temperature = 98.6
        self.homeostasis = 98.6
        self.alive = True
        self.decisionsMade = 0
        self.score = 0
        self.placesVisited = []
        self.currentPosition = "Start"
        self.decidedLocation = 0
        backpack = tool("backpack", "Storage")
        self.inventory = [backpack]


    def getNumberInput(self, choices, speed = 2, checkDamage = False):
        print("\n\n Now you have to make a choice. Enter the number you choose.")
        if self.alive and checkDamage:
            self.healthUpdater()

        questions = []
        for x,i in enumerate(choices):
            questions.append(f"""\t({x+1}) {i}""")
            
        self.storyTelling(questions, speed)
        
        y = True
        while y:
            b = input(">> ").strip()
            if b == "stats" or b == "stat":
                self.printStats()
                continue
            elif b == "forage":
                self.forage()
                continue
            elif b == "use":
                self.use()
                continue

            try:
                a = int(b)
            except:
                print("Not a number please try again.")
                continue
                
            if a-1 >= 0 and a-1 <= len(choices):
                print("Your choice was accepted.")
                y = False
            else:
                print("Your number is not in the right range. Try again.")
        self.score += 50
        self.decisionsMade += 1
        return a - 1

    def healthUpdater(self):
        if self.water <= 0:
            self.water = 0
            self.health -= 1
            print("You are taking damage due to dyhydration")

        elif self.water >= 20:
            if self.health < 20:
                self.health += 1
                print("You are healing")
        
        if self.hunger <= 0:
            self.hunger = 0
            self.health -= 1
            print("You are taking damage due to starvation")
        
        elif self.water >= 20:
            if self.health < 20:
                self.health += 1
                print("You are healing")

        for i in self.inventory:
            i.updateTools()
        
        if self.temperature > 104:
            self.health -= 1
            print("You are overheating drink water")


        if self.health == 0:
            self.alive = False
            self.dead()

    def getTextInput(self, choices, speed = 2, checkDamage = False):
        print("\n\n Now you have to make a choice. Enter your choice.")
        self.storyTelling(choices, speed)
        if self.alive and checkDamage:
            self.healthUpdater()
            
        y = True
        while y:
            a = input(">> ").strip().lower()
            if a == "stats" or a == "stat":
                self.printStats()
                continue
            elif a == "forage":
                self.forage()
                continue
            elif a == "use":
                self.use()
                continue


            if a.lower() in choices:
                print("Your choice was accepted.")
                y = False
            else:
                print("Not in the list. Try Again.")
                continue
        self.score += 50
        self.decisionsMade += 1
        return choices.index(a)

    def printStatsOld(self):
        message = ""
        a = bigLetter.renderText("Escape the Desert")
        message += a
        message += f"Your death location was {self.currentPosition}"

        message += "\nThese things are in your inventory."
        for i in self.inventory:
            message += f"\n\t{i.name}"

        message += "\nThese are the places you visited."
        for t in self.placesVisited:
            message += f"\n\t{t}"
        message += f"\n\nYour Score is {self.score}"
        message += f"\nYou were playing in {self.difficulty} mode."
        return message
    
    def setDifficulty(self, difficulty):
        if difficulty == 0:
            self.difficulty = "Easy"
            self.health = 20
            self.water = 20
            self.hunger = 20
            knife = tool("knife", "Killing")
            self.changeInventory(knife, True)
        elif difficulty == 1:
            self.difficulty = "Medium"
            self.health = 10
            self.water = 10
            self.hunger = 10
        elif difficulty == 2:
            self.difficulty = "Hard"
            self.health = 5
            self.water = 5
            self.hunger = 5
        
    def printStats(self):
        print("\n\nThis is your stats page.")
        coolSideFillingBar(self.health, "Health")
        coolSideFillingBar(self.water, "Water")
        coolSideFillingBar(self.hunger, "Hunger")
        print(f"Your Temperature is {self.temperature} degrees")
        print("\nThese things are in your inventory.")
        for i in self.inventory:
            i.display()
        print(f"Your current position is {self.currentPosition}")
        print(f"\n\nYour Score is {self.score}")
        print(f"You are playing in {self.difficulty} mode.")

    def storyTelling(self, y, delay = 2):
        for x in y:
            print(x)
            # UNCOMMENT THIS AFTER PROJECT IS DONE
            time.sleep(delay)
    
    def findWaterPlant(self):
        a = "Looks like we are looking for plants"
        b = "Plants that carry water are called succulent plants."
        c = "We are going to be looking for these succulent plants."
        d = "But, it isn't very easy to get water in the desert."
        e = "Plants have evolved to have natural defenses against animals who try to take their water. "
        f = "Cacti for example have spikes."
        self.storyTelling([a,b,c,d,e,f])
        a = "\nYou can see a few different plants around you."
        b = "There are cactuses, grasses, and some flowers."
        c = "There are also some snakes and predators so you must be careful of what you choose."
        self.storyTelling([a,b,c])
        print("Choose where you try and get food.")
        a = "cacti"
        b = "flowers"
        c = "grass"
        choice = self.getTextInput([a,b,c])
        if choice == 0:
            a = "Looks like we are looking for cacti. "
            b = "You should know that we will not be able to store the water we recieve."
            c = "We will have to drink it right after we find some."
            d = "You look for the largest exposed cactus you see."
            e = "You need a tool to cut it off."
            self.storyTelling([a,b,c,d,e])
            canUse = self.useTool("Killing")
            
            if not canUse:
                print("You don't have any tools for this. Try again.")
                return
            
            chance = random.randint(1, 10)
            if chance == 1:
                print("You pricked youself on the cactus and lost one health point.")
                self.health -= 1
                self.score -= 50
                waterGain = random.randint(1, 3)
                print("You are opening the cactus. There is water in it.")
                print(f"You have gained {waterGain} water points.")
                hungerGain = random.randint(0,1)
                self.score += 10
                if hungerGain == 1:
                    print("You also gained 1 hunger point by eating the soft tissue of the cactus")
                    self.hunger += 1
                    self.score += 10

            elif 1 < choice <= 3:
                print("You opened the cacutus but there was no water.")
            else:
                waterGain = random.randint(1, 3)
                print("You are opening the cactus. There is water in it.")
                print(f"You have gained {waterGain} water points.")
                hungerGain = random.randint(0,1)
                self.score += 10
                if hungerGain == 1:
                    print("You also gained 3 hunger point by eating the soft tissue of the cactus")
                    self.hunger += 3
                    self.score += 10

        elif choice == 1:
            a = "Looks like we are looking for flowers"
            b = "Most flowers in the desert are on top of cactuses."
            c = "We will look for exposed flowers on the ground"
            self.storyTelling([a,b,c])
            print("You can see some pink flowers near the base of a cactus.")
            print("You need a tool to cut it off")
            canUse = self.useTool("Killing")
            
            if not canUse:
                print("You don't have any tools for this. Try again.")
                return
            a = "You were able to cut the flower off."
            b = "You put the flower in your mouth and prepare to eat it"
            chance = random.randint(0,2)
            if choice == 0:
                c = "The flower was poisonious."
                d = "You lose 2 health points"
                self.health -= 2
                self.score -= 10
                self.storyTelling([a,b,c,d])
            elif choice == 1:
                c = "The flower tastes bitter and you spit it out."
                self.storyTelling([a,b,c])
            elif choice == 2:
                c = "The flower tastes good"
                d = "You gain 2 water points and 1 hunger point."
                self.storyTelling([a,b,c,d])
                self.hunger += 2
                self.water += 2
                self.temperature -= 1
                self.score += 50

        elif choice == 2:
            a = "Looks like we are looking for grasses"
            b = "Grass can be found all over the desert"
            c = "But we don't want to eat weeds"
            self.storyTelling([a,b,c])
            print("You see some grass near a large rock")
            print("You need a tool to cut it off")
            canUse = self.useTool("Killing")
            
            if not canUse:
                print("You don't have any tools for this. Try again.")
                return
            a = "You were able to cut the grass off."
            b = "You take a handful of grass and put it in your mouth and prepare to eat it"
            chance = random.randint(0,2)
            if choice == 0:
                c = "The grass was poisonious."
                d = "You lose 2 health points"
                self.health -= 2
                self.score -= 10
                self.storyTelling([a,b,c,d])
            elif choice == 1:
                c = "The grass you picked were weeds"
                d = "They did not have nutritional value."
                self.storyTelling([a,b,c,d])
            elif choice == 2:
                c = "The grass tastes good"
                d = "You gain 2 water points and 1 hunger point."
                self.storyTelling([a,b,c,d])
                self.hunger += 2
                self.water += 2
                self.temperature -= 1
                self.score += 50

    def dead(self):
        print(bigLetter.renderText("YOU ARE DEAD"))
        self.printStats()
        time.sleep(5)
        print("Would you like to save your score?")
        choice = self.getTextInput(["yes", "no"])
        if choice == 0:
            name = input("Please enter the name you want for the file. Do not include the  ")
            realName = ""
            for i in name:
                
                if i == ' ' or i == '*' or i == '?' or i == '|':
                    i = ""
                realName += i

            realName += ".txt"
            try:
                f = open(realName, "w")
                message = self.printStatsOld()
                print(message)
                f.write(message)
                f.close()
                print("File has been created")
            except:
                print("File couldn't be created")
        input("Click Enter to Exit")
        print(bigLetter.renderText("Good try"))
        print(bigLetter.renderText("-AkeBoss"))
        sys.exit()

    def win(self):
        print(bigLetter.renderText("YOU WON!!!"))
        self.printStats()
        time.sleep(5)
        print(bigLetter.renderText("GG"))
        print("Would you like to save your score?")
        choice = self.getTextInput(["yes", "no"])
        if choice == 0:
            name = input("Please enter the name you want for the file. Do not include the  ")
            realName = ""
            for i in name:
                
                if i == ' ' or i == '*' or i == '?' or i == '|':
                    i = ""
                realName += i

            realName += ".txt"
            try:
                f = open(realName, "w")
                message = self.printStatsOld()
                f.write(message)
                f.close()
                print("File has been created")
            except:
                print("File couldn't be created")
        input("Click Enter to Exit")

    def findWaterFeature(self):
        if self.position == "river":
            self.water = 20
            
            self.temperature = self.homeostasis
            for i in self.inventory:
                i.waterBottle(True)
            
            print("You filled up your water bottle and drank all the water you need")
        
        else:
            a = "It looks like you want to look for water above ground"
            b = "That is the rarest place to find water in the desert"
            c = "There aren't many places you can find water."
            self.storyTelling([a,b,c])
            print("Where would you like to go?")
            a = "Try to go higher up"
            b = "Try to go lower down"
            c = "Look around where you are"
            choice = self.getNumberInput([a,b,c])
            if choice == 0:
                self.move(self.position)
                a = "You go up a hill to survey your surroundings"
                chance = random.randint(1,3)
                if chance == 1:
                    b = "You see a small pool of water"
                    self.water = 20
                    self.temperature = self.homeostasis
                    for i in self.inventory:
                        i.waterBottle(True)
                    c = "You filled up your water bottle and drank all the water you need"
                    self.score += 50
                    self.storyTelling([a,b,c])
                elif chance == 2:
                    b = "You don't see any water"
                    c = "You come back down and lose 2 hunger points."
                    self.hunger -= 2
                    self.score -= 10
                    self.storyTelling([a,b,c])
                elif chance == 3:
                    b = "You are unable to get up the hill"
                    c = "You injure yourself and lose 2 health points."
                    self.health -= 2
                    self.score -= 10
                    self.storyTelling([a,b,c])
            elif choice == 1:
                self.move(self.position)
                a = "You go into a ravine in search of a stream"
                chance = random.randint(1,3)
                if chance == 1:
                    b = "You see a small stream of water"
                    self.water = 20
                    self.temperature = self.homeostasis
                    for i in self.inventory:
                        i.waterBottle(True)
                    c = "You filled up your water bottle and drank all the water you need"
                    self.score += 50
                    self.storyTelling([a,b,c])
                elif chance == 2:
                    b = "You don't see any water"
                    c = "You come back up and lose 2 hunger points."
                    self.hunger -= 2
                    self.score -= 10
                    self.storyTelling([a,b,c])
                elif chance == 3:
                    b = "You slip during your decent"
                    c = "You fall to your death"
                    self.health = 0
                    
                    self.storyTelling([a,b,c])
                    self.healthUpdater()           
            
            elif choice == 2:
                self.move(self.position)
                a = "You look around your surroundings"
                chance = random.randint(1,3)
                if chance == 1:
                    b = "You see a small pool of water"
                    self.water = 20
                    self.temperature = self.homeostasis
                    for i in self.inventory:
                        i.waterBottle(True)
                    c = "You fill up your water bottle and drink all the water you need"
                    self.score += 50
                    self.storyTelling([a,b,c])
                elif chance == 2:
                    b = "You don't see any water"
                    c = "You lose 2 hunger points."
                    self.hunger -= 2
                    self.score -= 10
                    self.storyTelling([a,b,c])
                elif chance == 3:
                    c = "You injure yourself and lose 2 health points."
                    self.health -= 2
                    self.score -= 10
                    self.storyTelling([a,c])

    def useTool(self, toolType):
        possibleTools = []
        possibleToolNames = []
        for i in self.inventory:
            if i.typeOfTool is toolType:
                possibleTools.append(i)
                possibleToolNames.append(i.name)
        
        if not len(possibleTools) == 0:
            choice = self.getNumberInput(possibleToolNames)
            index = self.inventory.index(possibleTools[choice])
            self.inventory[index].numUses += 1
            return True
        else:
            return False
    
    def use(self):
        a = "What whould you like to use?"
        b = "Food"
        c = "Water"
        self.storyTelling([a])
        choice = self.getNumberInput([b,c])

        if choice == 0:
            possibleTools = []
            possibleToolNames = []
            for i in self.inventory:
                if i.typeOfTool == "Eating":
                    possibleTools.append(i)
                    possibleToolNames.append(i.name)
            
            choice = self.getNumberInput(possibleToolNames)
            self.useToolinInventory(possibleTools[choice].name)
            hungerChance = random.randint(2,6)
            self.hunger += hungerChance
            if self.hunger > 20:
                self.hunger = 20

        elif choice == 1:
            for i in self.inventory:
                x = i.waterBottle(False)
                if x:
                    y = self.inventory.index(i)
                    self.inventory[y].waterBottle(False)
                    self.water = 20

    def findFood(self):
        a = "In the desert, there are two different sources of food."
        b = "Plants and animals"
        c = "We have to choice a group to focus on"
        l = "plants"
        m = "animals"
        self.storyTelling([a,b,c])
        choice = self.getTextInput([l,m])
        if choice == 0:
            self.findWaterPlant()
        elif choice == 1:
            a = "\nYou can see a few different animals around you."
            b = "There are lizards, snakes, insects, and gerbils."
            c = "There are also some predators so you must be careful of what you choose."
            self.storyTelling([a,b,c])
            print("Choose where you try and get food.")
            a = "lizards"
            b = "insects"
            c = "gerbils"
            choice = self.getTextInput([a,b,c])
            if choice == 0:
                a = "Looks like we are looking for lizards. "
                b = "First, we will have to catch a lizard."
                c = "Then we have to kill it."
                d = "Then we need to cut it and eat it"
                e = "You need a tool to kill it."
                self.storyTelling([a,b,c,d,e])
                canUse = self.useTool("Killing")
                
                if not canUse:
                    print("You don't have any tools for this. Try again.")
                    return
                
                chance = random.randint(1, 10)
                if chance == 1:
                    a = "You damaged yourself while trying to get the lizards."
                    b = f"It took you {random.randint(1,20)} attempts to kill a lizard"
                    c = "The lizard has been added to your inventory. To eat it type use."
                    self.health -= 2
                    self.score -= 10
                    self.storyTelling([a,b,c])
                    lizard = tool("lizard", "Eating", 1)
                    self.changeInventory(lizard, True)

                elif 1 < choice <= 3:
                    a = "You were unable to catch a lizard."
                    b = "You lost 2 hunger points."
                    self.hunger -= 2
                    self.score -= 10
                    self.storyTelling([a,b])

                else:
                    b = f"It took you {random.randint(1,20)} attempts to kill a lizard"
                    c = "The lizard has been added to your inventory. To eat it type use."
                    self.storyTelling([b,c])
                    lizard = tool("lizard", "Eating", 1)
                    self.changeInventory(lizard, True)
                    self.score += 50


            elif choice == 1:
                a = "Looks like we are looking for insects"
                b = "Insects are easy to find, but they aren't very nutritous."
                c = "We will look near exposed flowers to find them"
                self.storyTelling([a,b,c])
                print("You can catch insects easily.")
                print("But you need a tool to kill it.")
                canUse = self.useTool("Killing")
                
                if not canUse:
                    print("You don't have any tools for this. Try again.")
                    return
                a = f"You were able to kill {random.randint(10,30)} insects."
                chance = random.randint(0,2)
                if choice == 0:
                    c = "A scorpion injected venom into you."
                    d = "You lose 2 health points"
                    self.health -= 2
                    self.score -= 10
                    e = "But you still eat all of your insects"
                    self.hunger += 2
                    self.water += 2
                    self.temperature -= 1
                    self.score += 50
                    self.storyTelling([a,b,c,d, e])
                elif choice == 1:
                    c = "A snake steals all your insects from your backpack"
                    self.storyTelling([a,b,c])
                elif choice == 2:
                    c = "You can't store the insects."
                    e = "You eat them now."
                    d = "You gain 2 water points and 1 hunger point."
                    self.storyTelling([a,b,c, e, d])
                    self.hunger += 2
                    self.water += 2
                    self.temperature -= 1
                    self.score += 50

            elif choice == 2:
                a = "Looks like we are looking for gerbils"
                b = "Gerbils can be found all over the desert."
                c = "But they are really quick and hard to catch"
                self.storyTelling([a,b,c])
                print("You need to run to try and catch them.")
                print("You need a tool to kill them.")
                canUse = self.useTool("Killing")
                
                if not canUse:
                    print("You don't have any tools for this. Try again.")
                    return
                a = "You were able to grab a gerbil."
                b = "You store it in your backpack"
                chance = random.randint(0,2)
                if choice == 0:
                    c = "You injured yourself while running after the gerbil."
                    d = "You lose 2 health points"
                    self.health -= 2
                    self.score -= 10
                    self.storyTelling([a,b,c,d])
                elif choice == 1:
                    c = "While you were away,"
                    d = "a snake slithered into your backpack and took your gerbil"
                    self.storyTelling([a,b,c,d])
                elif choice == 2:
                    c = "You know have a gerbil to use"
                    
                    self.storyTelling([a,b,c])
                    self.score += 50
                    gerbil = tool("gerbil","Eating", 1)
                    self.inventory.append(gerbil)


    def run(self, distance):
        injuryChance = random.randint(1,100)
        if injuryChance == 1:
            print("You cut yourself while walking and lost one health point.")
            self.health -= 1

        if distance > 5:
            # Higher chances
            hungerLoss = random.randint(3, 9)
            self.hunger -= hungerLoss
            print(f"You lost {hungerLoss} hunger points")
            if self.temperature > self.homeostasis:
                waterLoss = random.randint(3, 9)
                self.water -= waterLoss
                print(f"You lost {waterLoss} water points")
            
            tempGain = random.randint(1, 3)
            self.temperature += tempGain
            print(f"You gained {tempGain} degrees")
            
        elif distance < 5 or distance > 2:
            #medium chances
            hungerLoss = random.randint(2,6)
            self.hunger -= hungerLoss
            print(f"You lost {hungerLoss} hunger points")
            if self.temperature > self.homeostasis:
                waterLoss = random.randint(2, 6)
                self.water -= waterLoss
                print(f"You lost {waterLoss} water points")
            tempGain = random.randint(0, 2)
            self.temperature += tempGain
            print(f"You gained {tempGain} degrees")
        else:
            hungerLoss = random.randint(0,2)
            self.hunger -= hungerLoss
            print(f"You lost {hungerLoss} hunger points")
            if self.temperature > self.homeostasis:
                waterLoss = random.randint(0, 1)
                self.water -= waterLoss
                print(f"You lost {waterLoss} water points")

    def move(self, newArea, distance = 1):
        self.placesVisited.append(self.currentPosition)
        self.run(distance)
        self.position = newArea
        self.score += 100

    def forage(self):
        a = "What whould you like to forage for?"
        b = "Food"
        c = "Water"
        self.storyTelling([a])
        choice = self.getNumberInput([b,c])

        if choice == 0:
            self.findFood()
        elif choice == 1:
            a = "You can find food two different ways"
            b = "Search for Water Pools"
            c = "Eat watery plants"
            self.storyTelling([a])
            choice = self.getNumberInput([b,c])
            if choice == 0:
                self.findWaterFeature()
            elif choice == 1:
                self.findWaterPlant()

    def changeInventory(self, item, Add = True):
        if Add:
            self.inventory.append(item)
        else:
            for x in self.inventory:
                if x.name is item:
                    self.inventory.remove(x)
    
    def useToolinInventory(self, item):

        for x in self.inventory:
            if x.name is item:
                y = self.inventory.index(x)
                r = self.inventory[y].useTool()
                if r:
                    self.inventory.remove(x)
                break

def coolSideFillingBar(num, title):
    sidebar = ""
    sidebar += f"{title} ["
    for x in range(num):
        sidebar += '0'
    sidebar += '|'
    emptySpace = 20 - num - 1
    for x in range(emptySpace):
        sidebar += ' '

    sidebar += "} "
    sidebar += str(num)
    sidebar += " points"

    print(sidebar)

