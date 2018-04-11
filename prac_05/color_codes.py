"""
CP1401 Hexadecimal Colour Codes
"""

COLOR_CODES = {"DeepSkyBlue1": "#00bfff",
               "LawnGreen": "#7cfc00",
               "DarkOrange": "#ff8c00",
               "DarkOrchid": "#9932cc",
               "DeepPink1": "#ff1493",
               "FloralWhite": "#fffaf0",
               "magenta": "#ff00ff",
               "DarkSlateGray4": "#528b8b",
               "DarkGoldenrod1": "#ffb90f",
               "chartreuse1": "#7fff00"}


def main():
    color = input("Please enter a color from the list:\n>> ")
    while color != "":
        if color in COLOR_CODES:
            print("{} - {}".format(color, COLOR_CODES[color]))
        else:
            print("Invalid color!")
        color = input("Please enter a color from the list:\n>> ")


main()
