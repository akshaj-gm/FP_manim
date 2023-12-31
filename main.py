import numpy as np
import math
from manim import *
class DrawRooms:
    def __init__(self):
        self.rooms = VGroup()
        self.labels = VGroup() 
    def find_points(self,x1, y1, x2, y2,
                x3, y3, x4, y4):
        x7 = max(x1, x3)
        y8 = max(y1, y3)
        x8 = min(x2, x4)
        y7 = min(y2, y4)
        first_rect = ""
        second_rect = ""
        if(x7 == x8):
            if(x7 == x2):
                first_rect = "right"
                second_rect = "left"
            elif(x7 == x1):
                first_rect = "left"
                second_rect = "right"
        if(y7 == y8):
            if(y7 == y2):
                first_rect = "top"
                second_rect = "bottom"
            elif(y7 == y1):
                first_rect = "bottom"
                second_rect = "top"
        
        
        return [(x7,y7), (x8,y8)],first_rect,second_rect

    def draw_rdg(self,graph_data,count,mode,color_list,room_names):
        origin = {'x':0,'y':0}
        coordinates = {}
        for i in range(len(graph_data['room_x'])):
            data = []
            data.append([(graph_data['room_x'][i],graph_data['room_y'][i]),
                            (graph_data['room_x'][i] + graph_data['room_width'][i],graph_data['room_y'][i])])
            data.append([(graph_data['room_x'][i] + graph_data['room_width'][i],graph_data['room_y'][i]),
                            (graph_data['room_x'][i] + graph_data['room_width'][i],graph_data['room_y'][i] + graph_data['room_height'][i])])
            data.append([(graph_data['room_x'][i] + graph_data['room_width'][i],graph_data['room_y'][i] + graph_data['room_height'][i]),
                            (graph_data['room_x'][i],graph_data['room_y'][i] + graph_data['room_height'][i])])
            data.append([(graph_data['room_x'][i],graph_data['room_y'][i] + graph_data['room_height'][i]),
                            (graph_data['room_x'][i],graph_data['room_y'][i])])
            coordinates[i] = data
        
        for i in range(len(graph_data['mergednodes'])):
            node_1 = graph_data['mergednodes'][i]
            node_2 = graph_data['irreg_nodes'][i]
            common_points,first_room_dir,second_room_dir = find_points(graph_data['room_x'][node_1],
                                                                graph_data['room_y'][node_1],
                                                                graph_data['room_x'][node_1] + graph_data['room_width'][node_1],
                                                                graph_data['room_y'][node_1] + graph_data['room_height'][node_1],
                                                                graph_data['room_x'][node_2],
                                                                graph_data['room_y'][node_2],
                                                                graph_data['room_x'][node_2] + graph_data['room_width'][node_2],
                                                                graph_data['room_y'][node_2] + graph_data['room_height'][node_2])
            if(first_room_dir == 'bottom'):
                coordinates[node_1][0].append(common_points[0])
                coordinates[node_1][0].append(common_points[1])
            elif(first_room_dir == 'right'):
                coordinates[node_1][1].append(common_points[0])
                coordinates[node_1][1].append(common_points[1])
            elif(first_room_dir == 'top'):
                coordinates[node_1][2].append(common_points[0])
                coordinates[node_1][2].append(common_points[1])
            elif(first_room_dir == 'left'):
                coordinates[node_1][3].append(common_points[0])
                coordinates[node_1][3].append(common_points[1])

            if(second_room_dir == 'bottom'):
                coordinates[node_2][0].append(common_points[0])
                coordinates[node_2][0].append(common_points[1])
            elif(second_room_dir == 'right'):
                coordinates[node_2][1].append(common_points[0])
                coordinates[node_2][1].append(common_points[1])
            elif(second_room_dir == 'top'):
                coordinates[node_2][2].append(common_points[0])
                coordinates[node_2][2].append(common_points[1])
            elif(second_room_dir == 'left'):
                coordinates[node_2][3].append(common_points[0])
                coordinates[node_2][3].append(common_points[1])

        for i in coordinates:
            coordinates[i][0] = sorted(coordinates[i][0], key = lambda x: x[0])
            coordinates[i][1] = sorted(coordinates[i][1], key = lambda x: x[1])
            coordinates[i][2] = sorted(coordinates[i][2], key = lambda x: x[0], reverse=True)
            coordinates[i][3] = sorted(coordinates[i][3], key = lambda x: x[1], reverse=True)

        # pen.width(1.5)
        # pen.color('black')
        # pen.hideturtle()
        # pen.penup()
        width= np.amax(graph_data['room_width'])
        height = np.amax(graph_data['room_height'])
        if(width == 0):
            width = 1
        if(height == 0):
            height = 1
        if(width < height):
            width = height
        scale = 1
        # scale = 100*(math.exp(-0.30*width+math.log(0.8)) + 0.1)
        # origin = {'x': graph_data[origin, 'y': -550}
        dim =[0,0]
        # origin = {'x': origin['x'] - 400, 'y': -100}
        for i in range(len(graph_data['room_x'])):
            room = VGroup()
            if graph_data['room_width'][i] == 0 or i in graph_data['extranodes']:
                continue
            # if i in graph_data['mergednodes']:
            #     pen.fillcolor(color_list[graph_data['irreg_nodes'][graph_data['mergednodes'].index(i)]])
            # else:
            #     pen.fillcolor(color_list[i])
            # pen.begin_fill()
            pen_pos = 0
            prev_pos = None
            for dir in range(4):
                for idx in range(len(coordinates[i][dir])):
                    if(idx%2 == 0):
                        if pen_pos == 0:
                            prev_pos = LEFT * (coordinates[i][dir][idx][0] * scale + origin['x']) + UP * (coordinates[i][dir][idx][1] * scale + origin['y'])
                        pen_pos=1
                    else:
                        if pen_pos == 1:
                            room.add(Line(prev_pos, LEFT * (coordinates[i][dir][idx][0] * scale + origin['x']) + UP * (coordinates[i][dir][idx][1] * scale + origin['y'])))
                        pen_pos = 0
            # pen.end_fill()
            # if(graph_data['room_x'][i] + graph_data['room_width'][i]> dim[0]):
            #     dim[0] = graph_data['room_x'][i] + graph_data['room_width'][i]
            # if(graph_data['room_y'][i] + graph_data['room_height'][i]> dim[1] ):
            #     dim[1] = graph_data['room_y'][i] + graph_data['room_height'][i]
            
            self.rooms.add(room)

        x_index = int(np.where(graph_data['room_x'] == np.min(graph_data['room_x']))[0][0])
        y_index = int(np.where(graph_data['room_y'] == np.max(graph_data['room_y']))[0][0])
        new_pos = ((graph_data['room_x'][x_index]) * scale + origin['x'],(graph_data['room_y'][y_index] + graph_data['room_height'][y_index]) * scale + origin['y'] + 200)
        # pen.setposition  
        # pen.write(count,font=("Arial", 20, "normal"))
        # pen.penup()


        for i in range(len(graph_data['room_x'])):
            if i in graph_data['extranodes']:
                continue
            # pen.color('black')
            if(i not in graph_data['mergednodes']):
                # pen.setposition(((2 * graph_data['room_x'][i] ) * scale / 2) + origin['x'] + 5,
                #                 ((2 * graph_data['room_y'][i] + graph_data['room_height'][i]) * scale / 2) + origin['y'])
                x = ((2 * graph_data['room_x'][i] ) * scale / 2) + origin['x'] + 5 * 0.1
                y = ((2 * graph_data['room_y'][i] + graph_data['room_height'][i]) * scale / 2) + origin['y']
                room1_center = LEFT * x + UP * y
                label = Text(f"{i}", color=WHITE).scale(0.5)
                label.next_to(room1_center, UP, buff=SMALL_BUFF)
                # pen.write(i)
                # pen.penup()
            if(i in graph_data['mergednodes'] and mode == 2):
                x = ((2 * graph_data['room_x'][i] ) * scale / 2) + origin['x'] + 5 + 0.1
                y = ((2 * graph_data['room_y'][i] + graph_data['room_height'][i]) * scale / 2) + origin['y']
                room1_center = LEFT * x + UP * y
                label = Text(f"{i}", color=WHITE).scale(0.5)
                label.next_to(room1_center, UP, buff=SMALL_BUFF)
                # pen.write(i)
                # pen.penup()       
            self.labels.add(label)



        # value = 1
        # if(len(graph_data['area']) != 0):
        #     pen.setposition(dim[0]* scale + origin['x']+50, dim[1]* scale + origin['y']-30)
        #     pen.write('Area of Each Room' ,font=("Arial", 20, "normal"))
        #     for i in range(0,len(graph_data['area'])):
        #         if i in graph_data['extranodes']:
        #             continue
        #         pen.setposition(dim[0]* scale + origin['x']+50, dim[1]* scale + origin['y']-30-value*30)
        #         pen.write('Room ' + str(i)+ ': '+ str(graph_data['area'][i]),font=("Arial", 15, "normal"))
        #         pen.penup()
        #         value+=1



class Draw(Scene):
    def construct(self):
        
        graph = {'room_x': [0., 1., 0.], 'room_y': [0., 1., 1.], 'room_width': [2., 1., 1.], 'room_height': [1., 1., 1.], 'area': [2], 'extranodes': [], 'mergednodes': [], 'irreg_nodes': []}
        graph_data = {
        'room_x': graph['room_x'],
        'room_y': graph['room_y'],
        'room_width': graph['room_width'],
        'room_height': graph['room_height'],
        'area': graph['area'],
        'extranodes': graph['extranodes'],
        'mergednodes': graph['mergednodes'],
        'irreg_nodes': graph['irreg_nodes']
        }
        dr = DrawRooms()
        dr.draw_rdg(graph_data,1,1,['red','blue','green'],['Kitchen','Bedroom','Hall'])
        for room in dr.rooms:
            for line in room:
                self.play(Create(line),run_time = 0.2)
        self.wait(0.1)
        
        self.play(*[Write(label) for label in dr.labels])
        self.wait(0.2)

