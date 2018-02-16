|Build Status| |FOSSA Status Shield Badge|

Download
~~~~~~~~

Go to the `releases
page <https://github.com/ilovecode1/Pyfancy-2/releases>`__ and download
the latest (or previous) version.

Or use pip ``pip install git+https://github.com/ilovecode1/Pyfancy-2/``

Overview
~~~~~~~~

pyfancy is a simple Python library that provides a mechanism for easily
styling text in some terminal environments. Text is styled by chaining
together methods that add escape codes for color modifiers to the text.

Usage
~~~~~

Formatting using pyfancy all follows the same basic pattern. First,
there is the initializer, which just sets up the pyfancy object. Next is
a chain of function calls that provide text formatting. Finally, there
is a last method chained on which either returns the text string with
format escape codes, or which directly outputs the text using the print
statement / method. (The output method *should* be compatible with
Python 2 and 3.)

This chain of code looks basically like this:

.. code:: python

    pyfancy().[chained statements].output() # To print using print statement / method
    pyfancy().[chained statements].get()    # To get formatted text string

There are two different ways to use the chained statements. The first is
to provide the text that is to be chained as part of the statement call.
For example, the following prints “Hello, world!” in red:

.. code:: python

    pyfancy().red("Hello, world!").output()

However, chained statements are really just modifiers with an optional
text argument. The following example works identically to the previous
example:

.. code:: python

    pyfancy().red().add("Hello, world!").output()

Using chained statements, then, allows for modifiers to be stacked:

.. code:: python

    pyfancy().red().bold().add("Hello, world!").output()

    # or

    pyfancy().red().bold("Hello, world!").output()

    # The red() and bold() calls can also be in the opposite order.

Of course, there can only be, for example, one color active at a time.
This allows for the creation of multicolored statements:

.. code:: python

    pyfancy().red("Hello").magenta(", ").blue("world!").output()

It is also possible to reset all styles, either to get default styling,
or to ensure that styles are reset, using the ``raw`` modifier:

.. code:: python

    pyfancy().raw("You walk into a ").red().bold("DANGEROUS").raw(" room.").output()

Parsing is a simple, shorter and faster way to use Pyfancy 2. Instead
of:

.. code:: python

    pyfancy().red("Hello").blue(" world!").output()

You can do this:

.. code:: python

    pyfancy("{red Hello {blue world!}}").output()

For parsing you can also import from a text file:

.. code:: python

    pyfancy().open("import.txt").output()

In order to use pyfancy, import the module with
``from pyfancy import *``.

Types of effects
~~~~~~~~~~~~~~~~

+-------------+-----------------+--------------+
| Text Effect | Background      |              |
+=============+=================+==============+
|             |                 |              |
+-------------+-----------------+--------------+
| bold        | n/a             |              |
+-------------+-----------------+--------------+
| dim         | n/a             | Light/Dark   |
+-------------+-----------------+--------------+
| underlined  | n/a             | n/a          |
+-------------+-----------------+--------------+
| blinking    | n/a             | n/a          |
+-------------+-----------------+--------------+
| black       | black_bg        | n/a          |
+-------------+-----------------+--------------+
| red         | red_bg          | dark_red     |
+-------------+-----------------+--------------+
| green       | green_bg        | dark_green   |
+-------------+-----------------+--------------+
| yellow      | yellow_bg       | dark_yellow  |
+-------------+-----------------+--------------+
| blue        | blue_bg         | dark_blue    |
+-------------+-----------------+--------------+
| magenta     | n/a             | dark_magenta |
+-------------+-----------------+--------------+
| cyan        | n/a             | dark_cyan    |
+-------------+-----------------+--------------+
| n/a         | gray_bg         | light_gray   |
+-------------+-----------------+--------------+
| white       | n/a             | n/a          |
+-------------+-----------------+--------------+
| rainbow     | n/a             | n/a          |
+-------------+-----------------+--------------+
| multi       | n/a             | n/a          |
+-------------+-----------------+--------------+
| n/a         | dark_gray_bg    | dark_gray    |
+-------------+-----------------+--------------+
| n/a         | light_red_bg    | light_red    |
+-------------+-----------------+--------------+
| n/a         | light_green_bg  | light_green  |
+-------------+-----------------+--------------+
| n/a         | light_yellow_bg | light_yellow |
+-------------+-----------------+--------------+
| n/a         | light_blue_bg   | light_blue   |
+-------------+-----------------+--------------+
| n/a         | light_purple_bg | light_purple |
+-------------+-----------------+--------------+
| n/a         | light_cyan_bg   | light_cyan   |
+-------------+-----------------+--------------+
| n/a         | white_bg        | white        |
+-------------+-----------------+--------------+

License
~~~~~~~

Pyfancy-2 is under the MIT license.

|FOSSA Status Large Badge|

Contributors
~~~~~~~~~~~~

Project by `CosmicWebServices`_

`TheMonsterFromTheDeep`_

`joker314`_

`baranskistad`_

`jonathan50`_

`rogersouza`_

`vutondesign`_

`cruxicheiros`_

`hiccup01`_

`Kristinita`_

.. _CosmicWebServices: https://github.com/CosmicWebServices
.. _TheMonsterFromTheDeep: https://github.com/TheMonsterFromTheDeep
.. _joker314: https://github.com/joker314
.. _baranskistad: https://github.com/baranskistad
.. _jonathan50: https://github.com/Jonathan50
.. _rogersouza: https://github.com/rogersouza
.. _vutondesign: https://github.com/vutondesign
.. _cruxicheiros: https://github.com/cruxicheiros
.. _hiccup01: https://github.com/hiccup01
.. _Kristinita: https://github.com/Kristinita

.. |Build Status| image:: https://travis-ci.org/ilovecode1/Pyfancy-2.svg?branch=master
   :target: https://travis-ci.org/ilovecode1/Pyfancy-2
.. |FOSSA Status Shield Badge| image:: https://app.fossa.io/api/projects/git%2Bgithub.com%2Filovecode1%2FPyfancy-2.svg?type=shield
   :target: https://app.fossa.io/projects/git%2Bgithub.com%2Filovecode1%2FPyfancy-2?ref=badge_shield
.. |FOSSA Status Large Badge| image:: https://app.fossa.io/api/projects/git%2Bgithub.com%2Filovecode1%2FPyfancy-2.svg?type=large
   :target: https://app.fossa.io/projects/git%2Bgithub.com%2Filovecode1%2FPyfancy-2?ref=badge_large
