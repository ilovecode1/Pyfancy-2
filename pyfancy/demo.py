from pyfancy import pyfancy

pyfancy().red("Hello").raw(", ").blue("world!").output()
pyfancy().multi("Multicolored text").output()
pyfancy().rainbow("Rainbow text").output()
pyfancy("{red foo {bold bar} baz}").output()
pyfancy().black_bg("Black background").output()
pyfancy().green_bg("Green background").output()
pyfancy().red_bg("Red background").output()
pyfancy().black().yellow_bg("Yellow background").output()
pyfancy().blue_bg("Blue background").output()
pyfancy().purple_bg("Purple background").output()
pyfancy().cyan_bg("Cyan background").output()
pyfancy().black().gray_bg("Gray background").output()
pyfancy().read("pyfancy/demo/import.txt").output()
pyfancy().red("This should not be seen!").reset().output()
print(pyfancy().red("Hello").raw(", ").blue("world!").strip())
