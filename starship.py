#pytrek/starship.py

from math import sqrt

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
