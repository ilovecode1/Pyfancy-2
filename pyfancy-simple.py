class pyfancy:  # Our Class
    
    version = "1.0.0"
    END = '\033[0m'
    BLINK = '\033[05m'
    BLACKTEXTGREYBACKGROUND = '\033[100m'
    INVISABLE2 = '\033[02m'
    PURPLEBLUE = '\033[34m'
    WHITETEXTBLACKBACKROUND = '\033[07m'
    MISTGREY = '\033[20m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    LIGHTGREY = '\033[37m'
    DARKGREY = '\033[90m'
    LIGHTRED = '\033[91m'
    LIGHTGREEN = '\033[92m'
    LIGHTBLUE = '\033[94m'
    PINK = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    REVERSE = '\033[07m'
    STRIKETHROUGH = '\033[09m'
    INVISABLE = '\033[08m'
    
    def blink(text): return BLINK + text + END
