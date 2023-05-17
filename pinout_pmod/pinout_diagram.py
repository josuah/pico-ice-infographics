from pinout.core import Group, Image
from pinout.components.layout import Diagram_2Rows
from pinout.components.pinlabel import PinLabelGroup, PinLabel
from pinout.components.text import TextBlock
from pinout.components import leaderline as lline
from pinout.components.legend import Legend


# Import data for the diagram
import data

# Create a new diagram
# The Diagram_2Rows class provides 2 panels,
# 'panel_01' and 'panel_02', to insert components into.
diagram = Diagram_2Rows(1230, 1150, 1000, "diagram")

# Add a stylesheet
diagram.add_stylesheet("styles.css", embed=True)

# Create a group to hold the pinout-diagram components.
graphic = diagram.panel_01.add(Group(400, 42))

# Add and embed an image
hardware = graphic.add(Image("pico_ice_front.png", embed=True))

# Measure and record key locations with the hardware Image instance
pin_pitch_v = 34.9
hardware.add_coord("left_top",      100, 130)
hardware.add_coord("right_top",     307, 130)
hardware.add_coord("left_bottom",   100, 445)
hardware.add_coord("right_bottom",  307, 445)
# Other (x,y) pairs can also be stored here
hardware.add_coord("pin_pitch_v", 0, pin_pitch_v)

graphic.add(
    PinLabelGroup(
        x=hardware.coord("left_top").x,
        y=hardware.coord("left_top").y,
        pin_pitch=hardware.coord("pin_pitch_v", raw=True),
        label_start=(60, 0),
        label_pitch=(0, pin_pitch_v),
        scale=(-1, 1),
        labels=data.pmod_left_top,
    )
)

graphic.add(
    PinLabelGroup(
        x=hardware.coord("right_top").x,
        y=hardware.coord("right_top").y,
        pin_pitch=hardware.coord("pin_pitch_v", raw=True),
        label_start=(60, 0),
        label_pitch=(0, pin_pitch_v),
        scale=(1, 1),
        labels=data.pmod_right_top,
    )
)

graphic.add(
    PinLabelGroup(
        x=hardware.coord("left_bottom").x,
        y=hardware.coord("left_bottom").y,
        pin_pitch=hardware.coord("pin_pitch_v", raw=True),
        label_start=(60, 0),
        label_pitch=(0, pin_pitch_v),
        scale=(-1, 1),
        labels=data.pmod_left_bottom,
    )
)

graphic.add(
    PinLabelGroup(
        x=hardware.coord("right_bottom").x,
        y=hardware.coord("right_bottom").y,
        pin_pitch=hardware.coord("pin_pitch_v", raw=True),
        label_start=(60, 0),
        label_pitch=(0, pin_pitch_v),
        scale=(1, 1),
        labels=data.pmod_right_bottom,
    )
)

# Create a title and description text-blocks
title_block = diagram.panel_02.add(
    TextBlock(
        data.title,
        x=20,
        y=30,
        line_height=18,
        tag="panel title_block",
    )
)
diagram.panel_02.add(
    TextBlock(
        data.description,
        x=20,
        y=60,
        width=title_block.width,
        height=diagram.panel_02.height - title_block.height,
        line_height=18,
        tag="panel text_block",
    )
)

# Create a legend
legend = diagram.panel_02.add(
    Legend(
        data.legend,
        x=340,
        y=8,
        max_height=132,
    )
)

# Export the diagram via commandline:
# >>> py -m pinout.manager --export pinout_diagram.py diagram.svg
