from pyfancy import *

pyfancy().red("Hello").raw(", ").blue("world!").output()
pyfancy().multi("Multicolored text").output()
pyfancy().rainbow("Rainbow text").output()
pyfancy("{red foo {bold bar} baz}").output()
print pyfancy().red("Hello").raw(", ").blue("world!").strip()
