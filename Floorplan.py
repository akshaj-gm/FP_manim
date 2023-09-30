from manim import *

class FloorplanWithCenteredLabels(Scene):
    def construct(self):
        # Define room coordinates, width, and height
        room1_left = -4
        room1_width = 6
        room1_height = 4
        
        # Create room1 with a thicker boundary
        room1 = Rectangle(
            width=room1_width, 
            height=room1_height, 
            color=WHITE, 
            stroke_width=10.0,  # Adjust the stroke width for a thicker boundary
            stroke_color=WHITE  # Set the stroke color to differentiate from the fill color
        ).shift(
            LEFT * (room1_left + room1_width / 2)
        )
        
        # Calculate the center of room1
        room1_center = room1.get_center()
        
        # Define room2 coordinates, width, and height
        room2_left = room1_left + room1_width
        room2_width = 5
        room2_height = 3
        
        # Create room2
        room2 = Rectangle(width=room2_width, height=room2_height, color=WHITE).shift(
            LEFT * (room2_left + room2_width / 2)
        )
        
        # Calculate the center of room2
        room2_center = room2.get_center()
        
        # Create a common wall using Cartesian coordinates
        '''common_wall = Rectangle(
            width=room2_left - room1_left,  # Width is the distance between the rooms
            height=room1_height,  # Height is the same as room1
            color=GRAY,
            fill_opacity=1,
        ).next_to(room2, LEFT, buff=0)'''
        
        '''# Create a door
        door = Rectangle(width=0.2, height=1, color=RED)
        door.next_to(common_wall, RIGHT, buff=0.1)'''
        
        # Create labels for rooms and place them at the center of each room
        label_room1 = Text("Room 1", color=WHITE).move_to(room1_center)
        label_room2 = Text("Room 2", color=WHITE).move_to(room2_center)
        
        # Add everything to the scene
        self.play(Create(room1), Create(room2))
        self.play(Write(label_room1), Write(label_room2))
        self.wait(2)
