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

class pyfancy:
    def __str__(self): return self.get()
    def __init__(self, obj=""):
        # Stores output text, for reset use get()
        self.out = str(obj)

    codes = { # The different escape codes
        'raw':            0,
        'bold':           1,
        'dim':            2,
        'underlined':     4,
        'blinking':       5,
        'inverted':       7,
        'hidden':         8,
        'black':         30,
        'red':           31,
        'green':         32,
        'yellow':        33,
        'blue':          34,
        'magenta':       35,
        'cyan':          36,
        'light_gray':    37,
        'dark_gray':     90,
        'light_red':     91,
        'light_green':   92,
        'light_yellow':  93,
        'light_blue':    94,
        'light_magenta': 95,
        'light_cyan':    96,
        'white':         97
    }

    # Stores output text, for reset use get()
    out = ""

    # Returns output text and resets properties
    def get(self):
        return self.out + "\033[0m"

    # Outputs text using print (should work in Python 2 and 3)
    def output(self):
        print(self.get())

    # Adds new text without changing the styling
    def add(self,addition):
        self.out += addition;
        return self;
      
    #Alternate between all the colours of the rainbow
    #No orange, replaced with lightRed
    #No purple/violet so I ignored it
    def rainbow(self,addition=""):
        x = 0
        for i in range(len(addition)): 
            if (addition[i] in [" ", "\t", "\n", "\r"]): x+=1
            [self.red, self.light_red, self.yellow, self.green, self.light_blue, self.blue][(i-x) % 6](addition[i])
        return self

    # Multicolored text
    def multi(self,string):
        i = 31 # ID of escape code; starts at 31 (red) and goes to 36 (cyan)
        for c in string: # Iterate through string
            self.out += "\033[" + str(i) + "m" + c
            i += 1 # Why u no have ++i? >:(
            if(i > 36): i = 31
        return self

# Adds a formatting function to pyfancy with the specified name and formatting code
# This shouldn't be exported
def _add(name,number):
    def inner(self, addition = ""):
        self.out += "\033[%dm%s" % (number, addition)
        return self
    setattr(pyfancy,name,inner)

# Generate all default color / format codes
for item in pyfancy.codes.items():
    if len(item) > 1: # Just in case
        _add(item[0],item[1])
