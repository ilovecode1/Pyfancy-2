#Pyfancy 0.2 by Cosmic Open Source Projects learn more at https://github.com/ilovecode1/pyfancy

class pyfancy:

	END = '\033[0m'
	PURPLE='\033[35m'
        CYAN='\033[36m'
        LIGHTGREY='\033[37m'
        DARKGREY='\033[90m'
        LIGHTRED='\033[91m'
        LIGHTGREEN='\033[92m'
        LIGHTBLUE='\033[94m'
        PINK='\033[95m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	REVERSE='\033[07m'
        STRIKETHROUGH='\033[09m'
        INVISABLE='\033[08m'
        
        
def demo():
	print(pyfancy.RED + "HELLO RED!" + pyfancy.END)
