from pyfancy import *

pyfancy().red("Hello").raw(", ").blue("world!").output()
pyfancy().multi("Multicolored text").output()
pyfancy().rainbow("Rainbow text").output()
pyfancy().parse("{red foo {bold bar} baz}").output()
