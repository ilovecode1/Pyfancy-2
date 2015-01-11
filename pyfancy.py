#Pyfancy 0.1 by Cosmic Open Source Projects learn more at https://github.com/ilovecode1/pyfancy

class pyfancy:

	END = '\033[0m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

def demo():
	print(pyfancy.BLUE + “H” + pyfancy.END + pyfancy.GREEN + “e” + pyfancy.END + pyfancy.YELLOW + “l” + pyfancy.END + pyfancy.RED + “l” + pyfancy.END + pyfancy.BOLD + “o” + pyfancy.END + pyfancy.UNDERLINE + pyfancy.END)
