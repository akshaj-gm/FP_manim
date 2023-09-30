from manim import *

class DrawRooms(Scene):
    def construct(self):
        # getting room data from the algorithm 
        room_data = {
            'room_x': [0., 1., 0.],
            'room_y': [0., 1., 1.],
            'room_width': [2., 1., 1.],
            'room_height': [1., 1., 1.]
        }

        # making 4 lines to define a room 
        rooms = VGroup()
        labels = VGroup()

        for i in range(len(room_data['room_x'])):
            x = room_data['room_x'][i]
            y = room_data['room_y'][i]
            width = room_data['room_width'][i]
            height = room_data['room_height'][i]

            top_left = LEFT * x + UP * y  
            top_right = LEFT * (x + width) + UP * y  
            bottom_left = LEFT * x + UP * (y + height)  
            bottom_right = LEFT * (x + width) + UP * (y + height)  

            room = VGroup(
                Line(top_left, top_right),
                Line(top_right, bottom_right),
                Line(bottom_right, bottom_left),
                Line(bottom_left, top_left),
            )

            label = Text(f"Room {i+1}", color=WHITE).scale(0.5)  # Scaling of label can be a problem 
            label.next_to(room.get_center(), UP, buff=SMALL_BUFF)  

            rooms.add(room)
            labels.add(label)

        
        self.play(*[Create(room) for room in rooms])
        self.play(*[Write(label) for label in labels])
        self.wait(2)
