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
make get_voices
```

### Build module

```sh
git clone https://github.com/maryszmary/RusTranslit
cd RusTranslit
pip install .
```

## Usage

Sample code:

```python
from rus_translit import transliterate

transliterate('is this just fantasy') 
```

Sample output:
```python
'из зис джаст фентеси'
```