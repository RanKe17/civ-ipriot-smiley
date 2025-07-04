import time
from blinkable import Blinkable
from smiley import Smiley


class Angry(Smiley, Blinkable):
    """
   Provides a Smiley with a happy expression
    """
    def __init__(self):
        super().__init__(complexion=self.RED)

        # adding complexion statement
        self.complexion_colour = self.complexion()

        # updating methods to use complexion_colour instead
        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self, color=None):
        """
       Renders a mouth by blanking the pixels that form that object.
        """

        # reassigning complexion colour because it doesn't like transferring across __init__
        if color is None:
            color = self.complexion_colour
        mouth = [42, 43, 44, 45, 50, 53]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, color=None, wide_open=True):
        """
       Draws the eyes (open or closed) on the standard smiley.
        :param wide_open (bool): eyes open or closed.
        """

        # resetting complexion colour again
        if color is None:
            color = self.complexion_colour


        eyes = [17, 18, 21, 22, 26, 29]
        for pixel in eyes:
            self.pixels[pixel] = self.BLANK if wide_open else self.complexion_colour

    def blink(self, delay=0.25):
        """
       Blinks the smiley's eyes once
        
        :param delay: Delay between blinks (in seconds)
        """
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()
