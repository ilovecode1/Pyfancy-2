### Download
Go to the [releases page](https://github.com/ilovecode1/Pyfancy-2/releases) and download the latest (or previous) version.

### Overview
pyfancy is a simple Python library that provides a mechanism for easily styling text in some terminal enviroments. Text is styled by chaining together methods that add escape codes for color modifiers to the text.

### Usage
Formatting using pyfancy all follows the same basic pattern. First, there is the initializer, which just sets up the pyfancy object. Next is a chain of function calls that provide text formatting. Finally, there is a last method chained on which either returns the text string with format escape codes, or which directly outputs the text using the print statement / method. (The output method *should* be compatible with Python 2 and 3.)

This chain of code looks basically like this:
```python
pyfancy().[chained statements].output() # To print using print statement / method
pyfancy().[chained statements].get()    # To get formatted text string
```

There are two different ways to use the chained statements. The first is to provide the text that is to be chained as part of the statement call. For example, the following prints "Hello, world!" in red:
```python
pyfancy().red("Hello, world!").output()
```
However, chained statements are really just modifiers with an optional text argument. The following example works identically to the previous example:
```python
pyfancy().red().add("Hello, world!").output()
```
Using chained statements, then, allows for modifiers to be stacked:
```python
pyfancy().red().bold().add("Hello, world!").output()

# or

pyfancy().red().bold("Hello, world!").output()

# The red() and bold() calls can also be in the opposite order.
```
Of course, there can only be, for example, one color active at a time. This allows for the creation of multicolored statements:
```python
pyfancy().red("Hello").magenta(", ").blue("world!").output()
```
It is also possible to reset all styles, either to get default styling, or to ensure that styles are reset, using the `raw` modifier:
```python
pyfancy().raw("You walk into a ").red().bold("DANGEROUS").raw(" room.").output()
```

In order to use pyfancy, import the module with `from pyfancy import *`.

### Types of effects

| Text Effect | Background |               |
|:-----------:|:----------:|---------------|
|             |            |               |
| bold        | n/a        |               |
| dim         | n/a        | Light/Dark    |
| underlined  | n/a        | n/a           |
| blinking    | n/a        | n/a           |
| black       | black_bg   | n/a           |
| red         | red_bg     | light_red     |
| green       | green_bg   | light_green   |
| yellow      | yellow_bg  | light_yellow  |
| blue        | blue_bg    | light_blue    |
| magenta     | n/a        | light_magenta |
| cyan        | n/a        | light_cyan    |
| n/a         | gray_bg    | dark_gray     |
| white       | n/a        | n/a           |
| rainbow     | n/a        | n/a           |
| multi       | n/a        | n/a           |

### Contributors

Project by @CosmicWebServices

https://github.com/ilovecode1/Pyfancy-2/graphs/contributors
