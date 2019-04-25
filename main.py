#pytrek/main.py
#A conversion of the old mainframe grid-based space game
#sdf, (c) 2018; emfol (c) 2019

#imports as needed
from math import sqrt
from sys import exit
import random

#right now the map is a global, might change later
map = []

class starship():
    """
    This class is used for all movable starship objects, both player and NPC.
    """

    def __init__(self, name, shields, hull, phaser, photons, coordX, coordY):
        """
        Starships have many attributes; this is an incomplete list that is useful 
        for our purposes, and that will likely expand later on as our models of 
        starships become slightly more complex.
        """
        self.name = name
        self.shields = shields
        self.hull = hull
        self.phaser = phaser
        self.photons = photons
        self.coordX = coordX
        self.coordY = coordY
        self.location = (coordX, coordY)

    def move(self, newX, newY):
        """
        Method that allows a ship to move along the map
        """
        map[player.coordX-1][player.coordY-1] = "." #prevents the Picard Maneuver
        map[klingon.coordX-1][klingon.coordY-1] = "."
        self.coordX = newX
        self.coordY = newY
        self.location = (newX,newY)

    def phaser_attack(self, target, strength):
        """
        Attack an opposing starship using, depleting its shields or hull.
        In the current implementation, the phaser strike weakens as a direct
        function of the distance of the shot.
        """
        phaser_intensity = strength - sqrt((self.coordX - target.coordX)**2 + (self.coordY - target.coordY)**2)
        self.phaser = self.phaser - phaser_intensity
        target.shields = target.shields - phaser_intensity
        print(self.name + " attacks "  + target.name + " for " +  str(phaser_intensity) + " damage.")

    def photon_attack(self, target, torp_count):
        """
        Photon torpedo attack; damage varies based on number of torpedos used.
        """
        photon_intensity = 8 + 2 * torp_count
        self.photons = self.photons - torp_count
        target.hull = target.hull - photon_intensity
        print(self.name + " attacks "  + target.name + " for " +  str(photon_intensity) + " damage.")

#let's make an example starship
player = starship("enterprise", 100, 100, 100, 100, 3, 3)
klingon = starship("d'var", 100, 100, 100, 100, 6, 2)


def initMap(xsize, ysize):
    """
    This creates an 8x8 single grid map, the acual game uses an 8x8 array of 8x8 local maps
    """
    for i in range(xsize):
        map.append([])
        for j in range(ysize):
            map[i].append(".")

def printHUD():
    """
    This displays the HUD at the start of each return
    """
    HUDDisplay = f"USS {player.name} - SHIELDS {player.shields} -" \
                 f"HULL {player.hull} - PHASER ENERGY {player.phaser} -"\
                 f"TORPEDOS {player.photons} - LOCATION {player.location}"
    print(HUDDisplay)

def printMap():
    """
    This puts our local map on the screen and plots the location of the ships
    """
    map[player.coordX-1][player.coordY-1] = "E"
    map[klingon.coordX-1][klingon.coordY-1] = "K"
    print("The player is at: " + str(player.location))
    for i in range(len(map)):
        print(map[i])

def drawDisplay():
    """
    On each turn, draws the HUD and the Map on the terminal.
    """
    printHUD()
    printMap()

def enemyAI():
    """
    As it stands, enemy decision making is based on an RNG that is
    weighted toward attacking rather than moving, because, well, Klingons
    would be more likely to attack than to flee.
    """
    #TODO: Make photon torpedo attacks a possible enemy action
    moveChoice = random.randint(0,100)
    if moveChoice >= 0 and moveChoice < 33:
        klingon.move(random.randint(1,8), random.randint(1,8))
    elif moveChoice >= 34 and moveChoice < 66:
        klingon.phaser_attack(player, random.randint(0,100))
    elif moveChoice > 66 and moveChoice < 99:
        klingon.photon_attack(player, random.randint(1, 5))
    else:
        pass


def gameLoop():
    """
    INCOMPLETE: the main interactive loop
    """
    #TODO: Move prompt into own function
    drawDisplay()
    prompt = input("Enter your command, Captain: ").upper()
    if prompt == "MOVE":
        inputX = input("Enter X coordinate 1-8: ")
        inputY = input("Enter Y coordinate 1-8: ")
        player.move(int(inputX), int(inputY))
        enemyAI()
    elif prompt == "PHASER":
        inputStrength = input("Enter strength of phaster attack 1-100: ")
        player.phaser_attack(klingon, int(inputStrength))
        enemyAI()
    elif prompt == "PHOTON":
        inputPhotonCount = input("How many torpedoes, Captain? ")
        player.photon_attack(klingon, int(inputPhotonCount))
        enemyAI()
    elif prompt == "HELP":
        print("Commands are MOVE and ATTACK")
        gameLoop()
    elif prompt == "EXIT":
        exit()
    else:
        print("Try again.")
        gameLoop()
    enemyAI()
    gameLoop()

initMap(8,8)
gameLoop()
