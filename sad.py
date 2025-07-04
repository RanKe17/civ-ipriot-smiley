from smiley import Smiley

# new additions due to blinking
from blinkable import Blinkable
import time

class Sad(Smiley, Blinkable):
    def __init__(self):
        super().__init__(complexion=self.BLUE)

        # adding complexion statement
        self.complexion_colour = self.complexion()
        self.my_complexion = self.complexion_colour

        # updating methods to use complexion_colour instead
        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self, color=None):
        """
        Draws the mouth feature on a smiley
        """

        # reassigning colour because it doesn't seem to handle __init__
        if color is None:
            color = self.complexion_colour

        mouth = [49, 54, 42, 43, 44, 45]

        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, color=None, wide_open=True):
        """
        Draws open or closed eyes on a smiley
        :param wide_open: Render eyes wide open or shut
        """

        # reassigning colour again
        if color is None:
            color = self.complexion_colour


        eyes = [10, 13, 18, 21]
        for pixel in eyes:
            if wide_open:
                eyes = self.BLANK
            else:
                eyes = color
            self.pixels[pixel] = eyes

    def blink(self, delay=1.75):
        """
        eyes blink once after 1.75 seconds
        """
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()