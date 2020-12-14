typesOfTools = ["Healing", "Cooling", "Killing", "Eating", "Storage"]

class tool():
    def __init__(self, name, typeOfTool, Uses=100):
        self.name = name
        self.typeOfTool = typeOfTool
        self.maxUses = Uses
        self.numUses = 0
    
    def display(self):
        print(f"{self.name} with {self.maxUses - self.numUses} uses left.")

    def useTool(self):
        self.numUses += 1
        x = self.updateTools()
        return x

    def waterBottle(self, fill):
        if self.name == "bottle" or self.name == "water bottle":
            if self.name == "bottle" and fill:
                self.name = "water bottle"
                return False
            elif self.name == "water bottle" and not fill:
                self.name = "bottle"
                return True
        return False
    
    def updateTools(self):
        if self.numUses >= self.maxUses:
            print(f"{self.name} is broken")
            return True
        return False