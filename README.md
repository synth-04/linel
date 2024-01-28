# LINEL
The Linel is a simple word generator for a conlang (Constructed Language, an artificial language).

You need to modify the sounds.txt and the syllables.txt in order to provide the possible patterns of your conlang.
Put your patterns in the phonology folder.

In the sounds.txt file, you write your phonological system (category of sounds of the language), in the format: C=sounds, separated by commas. 

In the syllabic structures (syllables.txt) you add every possible combinations of the categories in the sounds.txt.
As an argument in the CLI, you insert the number of words you want to generate (default 10).

# Usage

Run the python3 script:
```sh
$ python3 linel.py
```
The above only returns only 10 words by default.
```sh
$ python3 linel.py 40
```
The above returns 40 words.


