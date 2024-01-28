#! /usr/bin/env python3
"""A simple word generator for a conlang (Constructed Language, an artificial language). In the Phonology.txt file, you write your phonological system (category of sounds of the language), in the format: C=sounds, separated by commas. 
In the syllabic structures (Syllable.txt) you add every possible combinations of the categories in the Phonology.txt.
Running the program, you insert the number of words you want to generate."""

import random
import argparse


# gen function generates the word

def gen(phon, syl):
    structure = random.choice(syl)
    sounds = []

    for category in structure:
        sounds.append(random.choice(phon[category]))

    word = "".join(sounds)
    return word

#In the main, the program loads the txt files containing the phonological categories and syllable structures.

def main(num):
    phon = {}
    ph = []
    syl = []

    with open("phonology/sounds.txt") as f:
        [ph.append(line.rstrip()) for line in f.readlines()]

    with open("phonology/syllables.txt") as f:
        [syl.append(line.rstrip()) for line in f.readlines()]

  # the strings in Phonology.txt needs a split, dividing the type of category and the sounds. Then a dictionary is created.

    for cat in ph:
        phrase = cat.split("=")
        phon[phrase[0]] = phrase[1].split(",")
        
    # Uncomment if you want to check the phonology in the directory

    # print(f"Sounds System: {phon}")
    # print(f"Syllabic Structure: {syl}")

#We pass the phon dictionary and the syl list to the gen function

    for i in range(int(num)):
        print(gen(phon, syl))


if __name__ == "__main__":
    # Accept command line argument for number of words required where default is 10
    parser = argparse.ArgumentParser(description='Generate Words')
    parser.add_argument('num', nargs='?', type=int, default=10)
    args = parser.parse_args()
    main(args.num)
