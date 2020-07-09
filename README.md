# RusTranslit

## Installation

### Dependencies

`RusTranslit` depends on `Epitran`, which requires [`CMU Flite`](https://github.com/festvox/flite).

You can build it from source:

```sh
git clone http://github.com/festvox/flite
cd flite
./configure
make
cd testsuite
make
```

For epitran to access this module, you might want to add the following line to `~/.bashrc`:

```sh
export PATH=<path-to-flite>/testsuite:$PATH
```

Or simply run the command above in terminal to get acces to it in the current terminal session.

### Build module

```sh
git clone https://github.com/maryszmary/RusTranslit
cd RusTranslit
pip install -e .
```

## Usage

Example code:

```python
from rus_translit import transliterate

transliterate('is this a real life? is this just fantasy?')
```

Example output:
```python
'из зис а рил лайф? из зис джаст фентеси?'
```

## Authors

* Maria Sheyanova @maryszmary
* Anna Nikolaeva @annnyway
