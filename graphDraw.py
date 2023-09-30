from manim import *

class ManyCircles(Scene):
    def construct(self):
        c1 = Circle(1, color = RED, fill_opacity = 0.4)
        self.play(DrawBorderThenFill(c1), run_time = 0.2)
        title1 = Text("Kitchen", font_size = 35)
        self.play(Write(title1,run_time=0.2))
        self.wait(0.3)

        c2 = Circle(1, color = BLUE, fill_opacity = 0.4)
        c2.shift(UP*3)
        self.play(DrawBorderThenFill(c2), run_time = 0.2)
        title2 = Text("Bedroom", font_size = 35)
        title2.shift(UP*3)
        self.play(Write(title2,run_time=0.2))
        self.wait(0.3)

        c3 = Circle(1, color = GREEN, fill_opacity = 0.4)
        c3.shift(RIGHT*3)
        self.play(DrawBorderThenFill(c3), run_time = 0.2)
        title3 = Text("Hall", font_size = 35)
        title3.shift(RIGHT*3)
        self.play(Write(title3,run_time=0.2))
        self.wait(0.3)

        c4 = Circle(1, color = YELLOW, fill_opacity = 0.4)
        c4.shift(LEFT*3)
        self.play(DrawBorderThenFill(c4), run_time = 0.2)
        title4 = Text("Bathroom", font_size = 35)
        title4.shift(LEFT*3)
        self.play(Write(title4,run_time=0.2))
        self.wait(0.3)

        line1 = Line(c3.get_center(), c2.get_center(), color=WHITE)
        line2 = Line(c3.get_center(), c1.get_center(), color=WHITE)
        line3 = Line(c2.get_center(), c4.get_center(), color=WHITE)
        line1.shift(OUT)
        # line1.to_back()
        line2.shift(OUT)
        # line2.to_back()
        line3.shift(OUT)
        # line3.to_back()
        self.add(line1, line2, line3)
        self.wait(3)

