# Provides methods for manipulating text styling in specific terminals.
# Uses a basic chaining method where text properties are added by calling
# methods with related names.
# 
# For example, to print "Hello, world!" in red:
#   print pyfancy().red("Hello, world!").get()
#
# Styles can be changed for different text components. Example:
#   print pyfancy().red("Hello").raw(", ").blue("world!").get()
#
# No output text is necessary when calling a styling method. This allows
# styles to be stacked:
#   print pyfancy().red().bold("Hello, world!").get()
#
# There are two provided ways to access the modified text. The first is
# direct access to the string object called "out". However, accessing this
# object will not reset the style, so any text outputted after will have
# the same style as whatever the text was at the end of the chain.
# 
# The get() method is better for accessing text because it resets the text
# style so no new text will have unwanted styling.

def sgr(code):
    def inner(self, addition = ""):
        self.out += "\033[%sm%s" % (code, addition)
        return self
    return inner

class pyfancy:

    # Stores output text, for reset use get()
    out = ""

    # Returns output text and resets properties
    def get(self):
        return self.out + "\033[0m"

    __str__ = get

    # Outputs text using print (should work in Python 2 and 3)
    def output(self):
        print(self.get())

    # Adds new text without changing the styling
    def add(self,addition):
        self.out += addition;
        return self;

    # Raw text - i.e. default styling
    raw = sgr("0")

    # Bold text
    bold = sgr("1")

    # Dim text
    dim = sgr("2")

    # Underlined text
    underlined = sgr("4")

    # Blinking text
    blink = sgr("5")

    # Foreground / background inverted
    invert = sgr("7")

    # Hidden text
    hidden = sgr("8")

    # Black text
    black = sgr("30")
    # Red text
    red = sgr("31")
    # Green text
    green = sgr("32")
    # Yellow text
    yellow = sgr("33")
    # Blue text
    blue = sgr("34")
    # Magenta text
    magenta = sgr("35")
    # Cyan text
    cyan = sgr("36")
    # Light gray text
    lightGray = sgr("37")
    # Dark gray text
    darkGray = sgr("38")
    # Light red text
    lightRed = sgr("39")
    # Light green text
    lightGreen = sgr("92")
    # Light yellow text
    lightYellow = sgr("93")
    # Light blue text
    lightBlue = sgr("94")
    # Light magenta text
    lightMagenta = sgr("95")
    # Light cyan text
    lightCyan = sgr("96")
    # White text
    white = sgr("97")
