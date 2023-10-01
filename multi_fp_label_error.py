from manim import *

class DrawRooms(Scene):
    def construct(self):
        floorplan_data_list = [
            {
                'room_x': [0., 1., 0.],
                'room_y': [0., 1., 1.],
                'room_width': [2., 1., 1.],
                'room_height': [1., 1., 1.]
            },
            {
                'room_x': [0., 1., 0.],
                'room_y': [0., 1., 1.],
                'room_width': [2., 1., 1.],
                'room_height': [1., 1., 1.]
            },
        ]

        floorplans = []

        for room_data in floorplan_data_list:
            floorplan = self.create_floorplan(room_data)
            floorplans.append(floorplan)

        '''total_width = sum([floorplan[0].get_width() for floorplan in floorplans])'''

        start_x = -6

        for floorplan in floorplans:
            floorplan[0].next_to(ORIGIN, RIGHT, buff=0)
            floorplan[0].shift(RIGHT * start_x)
            start_x += floorplan[0].get_width()+1

        self.play(*[Create(floorplan) for floorplan in floorplans])

        self.wait(2)

    def create_floorplan(self, room_data):
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
           
            label = Text(f"{i+1}", color=WHITE).scale(0.5)
            label.move_to(room.get_center())
            rooms.add(room)
            labels.add(label)
           

        floorplan = VGroup(rooms, labels)  
        return floorplan