from manim import *

class CopyExample(Scene):
    def construct(self):
        # Create a circle Mobject
        circle = Circle()
        circle.set_color(RED)  # Set the color of the original circle

        # Create a copy of the circle
        circle_copy = circle.copy()
        circle_copy.set_color(BLUE)  # Set the color of the copied circle

        # Add the original circle to the scene
        self.play(Create(circle))

        # Add the copied circle to the scene
        self.play(Create(circle_copy))

        self.wait(2)
