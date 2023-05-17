legend = [
    ("Digital pin",  "gpio"),
    ("Analog pin",   "analog"),
    ("Ground", "gnd"),
    ("Power", "pwr"),
]

# Pinlabels

pmod_left_top = [
    [("PMOD2","")],
    [("TOP",""),        ("BOTTOM",""), ("ICE40", "")],
    [("3V3","pwr"),     ("3V3","pwr")],
    [("GND","gnd"),     ("GND","gnd")],
    [("4","gpio"),      ("10","gpio")],
    [("3","gpio"),      ("9","gpio")],
    [("2","gpio"),      ("8","gpio")],
    [("1","gpio"),      ("7","gpio")],
]

pmod_left_bottom = [
    [("PMOD1","")],
    [("TOP",""),        ("BOTTOM",""), ("ICE40", "")],
    [("VIO","pwr"),     ("VIO","pwr")],
    [("GND","gnd"),     ("GND","gnd")],
    [("4","gpio"),      ("10","gpio")],
    [("3","gpio"),      ("9","gpio")],
    [("2","gpio"),      ("8","gpio")],
    [("1","gpio"),      ("7","gpio")],
]

pmod_right_top = [
    [("PMOD3","")],
    [("TOP",""),        ("BOTTOM",""), ("RP/ICE", "")],
    [("1","gpio"),      ("7","gpio")],
    [("2","gpio"),      ("8","gpio")],
    [("3","gpio"),      ("9","gpio")],
    [("4","gpio"),      ("10","gpio")],
    [("GND","gnd"),     ("GND","gnd")],
    [("3V3","pwr"),     ("3V3","pwr")],
]

pmod_right_bottom = [
    [("PMOD4","")],
    [("TOP",""),        ("BOTTOM",""), ("RP2040", "")],
    [("1","gpio"),      ("7","gpio")],
    [("2","gpio"),      ("8","gpio")],
    [("3","gpio"),      ("9","gpio")],
    [("4","gpio"),      ("10","gpio")],
    [("GND","gnd"),     ("GND","gnd")],
    [("3V3","pwr"),     ("3V3","pwr")],
]

# Text

title = "<tspan class='h1'>pico-ice</tspan>"

description = """A small, low cost board featuring:
- a Raspberry Pi Pico processor (RP2040)
- a Lattice Semiconductor iCE40UP5K FPGA
<tspan class='italic strong'>pico-ice.tinyvision.ai</tspan>"""
