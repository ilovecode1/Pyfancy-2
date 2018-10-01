import os
import tempfile
import unittest

from ddt import data, ddt, unpack
from pyfancy.pyfancy import pyfancy


def ESCAPE(code):
    return '\033[{}m'.format(code)


RESET_FMT = ESCAPE(0)
TEST_DATA = [{'name': k, 'code': v} for k, v in pyfancy.codes.items()]


def color(name, text, reset=True):
    colored = ESCAPE(pyfancy.codes[name]) + text
    if reset:
        colored += RESET_FMT
    return colored


@ddt
class PyfancyTest(unittest.TestCase):
    @data(*TEST_DATA)
    @unpack
    def test_code(self, name, code):
        expected = ESCAPE(code) + 'test' + RESET_FMT
        actual = getattr(pyfancy(), name)('test').get()
        self.assertEqual(actual, expected)

    def test_mixed(self):
        expected = color('red', 'foo', False)
        expected += color('blue', 'bar')
        actual = pyfancy().red('foo').blue('bar').get()
        self.assertEqual(actual, expected)

    def test_rainbow(self):
        text = 'rpygcb'
        expected = ''.join(
            color(c, ch, c == 'blue')
            for c, ch in zip(
                ['red', 'light_red', 'yellow', 'green', 'light_blue', 'blue'],
                text
            )
        )
        actual = pyfancy().rainbow(text).get()
        self.assertEqual(actual, expected)

    def test_reset(self):
        expected = color('red', 'test')
        pf = pyfancy().red('test')
        self.assertEqual(pf.get(), expected)
        expected = '\x1b[0m'
        actual = pf.reset().get()
        self.assertEqual(actual, expected)

    def test_read_from_file(self):
        fd, filename = tempfile.mkstemp()
        os.write(fd, '{red hi}\n'.encode())
        os.close(fd)
        expected = color('red', 'hi')
        expected += '\n' + RESET_FMT
        actual = pyfancy().read(filename).get()
        os.remove(filename)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
