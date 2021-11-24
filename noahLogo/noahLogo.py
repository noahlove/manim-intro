from textwrap import fill
from manim import *

class noahLogo(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"
        noah = MathTex(r"\mathbb{NOAH}", fill_color=logo_black).scale(5)
        noah.shift(2.5 * UP)
        love = MathTex(r"\mathbb{LOVE}", fill_color = logo_black).scale(4)

        circle2 = Circle()
        square2 = Square(color = logo_green)
        triangle2 = Triangle()

        circle2.shift(LEFT)
        square2.shift(UP)
        triangle2.shift(RIGHT)

        shapes = VGroup(circle2, square2, triangle2)
        logo = VGroup(noah, love)  # order matters
        logo.move_to(ORIGIN).shift(LEFT * 2.5)
        shapes.move_to(ORIGIN).shift(RIGHT * 4) 
        self.add(logo, shapes)