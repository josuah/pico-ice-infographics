legend = [
    ("Digital pin",  "gpio"),
    ("Analog pin",   "analog"),
    ("Ground", "gnd"),
    ("Power", "pwr"),
]

# Pinlabels

left_header = [
    [("iCE40",""),              ("RP2040",""),              ("iCE40",""),           ("RP2040","")],
    [("","gpio"),               ("IOB22a/IO2","gpio"),      ("#27/ADC1","analog"),  ("CRESET","gpio")],
    [("","gpio"),               ("IOB24a/IO3","gpio"),      ("GND","gnd"),          ("GND","gnd")],
    [("3V3","pwr"),             ("3V3","pwr"),              ("3V3","pwr"),          ("3V3","pwr")],
    [("GND","gnd"),             ("GND","gnd"),              ("GND","gnd"),          ("GND","gnd")],
    [("","gpio"),               ("IOT41a","gpio"),          ("","gpio"),            ("IOT42b","gpio")],
    [("","gpio"),               ("IOT43a","gpio"),          ("","gpio"),            ("IOT44b","gpio")],
    [("","gpio"),               ("IOT48b","gpio"),          ("","gpio"),            ("IOT50b","gpio")],
    [("","gpio"),               ("IOT51a","gpio"),          ("","gpio"),            ("IOT49a","gpio")],
    [("#14/RAM_SS","gpio"),     ("IOT45a/G1","gpio"),       ("#24/CLK2","gpio"),     ("IOT46b/G0","gpio")],
    [("","gpio"),               ("IOB20a","gpio"),          ("","gpio"),            ("IOB13b","gpio")],
    [("","gpio"),               ("IOB18a/PB","gpio"),       ("","gpio"),            ("IOB16a","gpio")],
    [("VCCIO2","pwr"),          ("VCCIO2","pwr"),           ("VCCIO2","pwr"),       ("VCCIO2","pwr")],
    [("GND","gnd"),             ("GND","gnd"),              ("GND","gnd"),          ("GND","gnd")],
    [("","gpio"),               ("IOB3b/G6","gpio"),        ("","gpio"),            ("IOB5b","gpio")],
    [("","gpio"),               ("IOB0a","gpio"),           ("","gpio"),            ("IOB2a","gpio")],
    [("","gpio"),               ("IOB4a","gpio"),           ("","gpio"),            ("IOB6a","gpio")],
    [("","gpio"),               ("IOB9b","gpio"),           ("","gpio"),            ("IOB8a","gpio")],
    [("SWDIO","gpio"),          ("","gpio"),                ("RESET","gpio"),       ("","gpio")],
    [("SWCLK","gpio"),          ("","gpio"),                ("GND","gnd"),          ("GND","gnd")],
    [("#25/CLK3","gpio"),       ("","gpio"),                ("BOOT","gpio"),        ("","gpio")],
]

right_header = [
    [("iCE40",""),              ("RP2040",""),              ("iCE40",""),           ("RP2040","")],
    [("#9","gpio"),             ("IOB35B/SS","gpio"),       ("#8/SO","gpio"),       ("IOB32A","gpio")],
    [("#11","gpio"),            ("IOB33b/SI","gpio"),       ("#10","gpio"),         ("IOB34a/SCK","gpio")],
    [("#0","gpio"),             ("IOT38b","gpio"),          ("#4","gpio"),          ("IOT39a","gpio")],
    [("#1","gpio"),             ("IOT36b","gpio"),          ("#5","gpio"),          ("IOT37a","gpio")],
    [("#2","gpio"),             ("IOB23b","gpio"),          ("#6","gpio"),          ("IOB25b","gpio")],
    [("#3","gpio"),             ("IOB29b","gpio"),          ("#7","gpio"),          ("IOB31b","gpio")],
    [("GND","gnd"),             ("GND","gnd"),              ("GND","gnd"),          ("GND","gnd")],
    [("3V3","pwr"),             ("3V3","pwr"),              ("3V3","pwr"),          ("3V3","pwr")],
    [("#26/ADC0","analog"),     ("CDONE","gpio"),           ("#15/LED_B","gpio"),   ("RGB1","gpio")],
    [("#28/ADC2","analog"),     ("","gpio"),                ("#13/LED_R","gpio"),   ("RGB2","gpio")],
    [("#29/ADC3","analog"),     ("","gpio"),                ("#12/LED_G","gpio"),   ("RGB0","gpio")],
    [("#17","gpio"),            ("","gpio"),                ("#21","gpio"),         ("","gpio")],
    [("#19","gpio"),            ("","gpio"),                ("#23/CLK0","gpio"),    ("","gpio")],
    [("#16","gpio"),            ("","gpio"),                ("#20","gpio"),         ("","gpio")],
    [("#18","gpio"),            ("","gpio"),                ("#22","gpio"),         ("","gpio")],
    [("GND","gnd"),             ("GND","gnd"),              ("GND","gnd"),          ("GND","gnd")],
    [("3V3","pwr"),             ("3V3","pwr"),              ("3V3","pwr"),          ("3V3","pwr")],
    [("3V3","pwr"),             ("3V3","pwr"),              ("VCC","pwr"),          ("VCC","pwr")],
    [("3V3_SBY","pwr"),         ("3V3_SBY","pwr"),          ("PWR_EN","gpio"),      ("","gpio")],
    [("VBUS","pwr"),            ("VBUS","pwr"),             ("GND","gnd"),          ("","gpio")],
]


# Text

title = "<tspan class='h1'>pico-ice</tspan>"

description = """A small, low cost board featuring:
- a Raspberry Pi Pico processor (RP2040)
- a Lattice Semiconductor iCE40UP5K FPGA
<tspan class='italic strong'>pico-ice.tinyvision.ai</tspan>"""
