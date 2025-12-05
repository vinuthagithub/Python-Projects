words = [
"river", "planet", "silver", "motion", "branch", "garden", "thunder", "candle", "harbor", "feather",
"mirror", "puzzle", "anchor", "winter", "forest", "tablet", "melody", "copper", "bridge", "shadow",
"thread", "ember", "canvas", "orbit", "valley", "crystal", "harvest", "wander", "splash", "timber",
"breeze", "lantern", "marble", "filter", "ribbon", "scarlet", "beacon", "cobalt", "frost", "meadow",
"drift", "cipher", "ripple", "summit", "velvet", "quartz", "hollow", "parlor", "whisper", "legend",
"cinder", "acorn", "distant", "socket", "cosmic", "quiver", "hazel", "tunnel", "sparrow", "nested",
"petal", "amber", "tundra", "harp", "grove", "tidal", "magnet", "pebble", "glider", "woven",
"canyon", "glimmer", "plume", "sacred", "vessel", "twilight", "glyph", "maple", "anthem", "lattice",
"domain", "siren", "ember", "carve", "gust", "ponder", "artifact", "seeker", "chime", "mantle",
"fusion", "granite", "shimmer", "raven", "solace", "drizzle", "cascade", "horizon", "chorus", "haven"
]

import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0:
        print('You have used these letters: ', ''.join(used_letters))

    word_list = [letter if letter in user_letter else '-' for letter in word]
    print('Current word:', ''.join(word_list))

    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)

        else:
            lives = lives - 1
            print('Letter is not in word.')

    elif user_letter in user_letter:
        print('You have already sed that character Please try again')

    else:
        print('Invalid charcter. Please try again. ')

hangman()
