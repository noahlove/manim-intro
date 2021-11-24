from textwrap import fill
from manim import *

class name(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"
        noah = MathTex(r"\mathbb{NOAH}", fill_color=logo_black).scale(5)
        noah.shift(2.5 * UP)
        love = MathTex(r"\mathbb{LOVE}", fill_color = logo_black).scale(5)

        logo = VGroup(noah, love)  # order matters
        logo.move_to(ORIGIN)
        self.add(logo)