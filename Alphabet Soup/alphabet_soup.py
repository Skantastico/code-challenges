"""
Challenge: Create a function that takes a string and returns a string with its letters in alphabetical order.
Difficulty: Easy

Examples:
alphabet_soup("hello") ➞ "ehllo"
alphabet_soup("edabit") ➞ "abdeit"
alphabet_soup("hacker") ➞ "acehkr"
alphabet_soup("geek") ➞ "eegk"

Author: @joshrutkowski
"""


def alphabet_soup(text):
        for i in text:
            return ''.join(sorted(text))


# Testing
print(alphabet_soup('aardvark'))
print(alphabet_soup('TheEndIsNear'))
print(alphabet_soup('thequickbrownfoxjumpedoverthelazydog'))
