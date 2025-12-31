# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///

from typing import Final
import argparse

"""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░███░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░█▓█░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒▓█░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░█▓█░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░█▓█░░░░░░░░░░░░░░███░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░█▓█████████████░░███░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░█████▓███████████████▓████░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░█████▓█▓▓█▓██▓█▓████████████████░░░░░░░░░░░░░░░░░
░░░░░░░░███████▓█▓▓█▓▓███████▓██████████████░░░░░░░░░░░░░░░
░░░░░░░▓███▓▓▓▓▒▓█▓▒█▓▓▒█▒▓████▓███████████████░░░░░░░░░░░░
░░▒███████▓▓▓▓▓▓██▓██▒▒▓██▓█▓███▓█▓██████████████░░░░░░░░░░
░░██▓▒▒▒▒▓█▓▓▓▓▒▒▓▓██▓▓▒██▓████▓██████████████████░░░░░░░░░
░░██▓▓██▒▓▓▓▓▓████████▒░▒████████████▓▒███████████░░░░░░░░░
░░██▒▒▓▓████▓█████████████▓▓▓████████████████████░░░░░░░░░░
░░░█▓▒▓▓▓▓▓▒▒░░░░░░░░░░░██▓██▓████████░░░░▒█████░░░░░░░░░░░
░░░░█▒▓█▓▓▓▓███████░░░░░░░█▓█▒▓██████░░░░░▓██████░░░░░░░░░░
░░░░███▓▒▓▓▓▒█▓█████████▒▓▒▒██▓████▒▓███████▓▓████░░░░░░░░░
░░░░█▓▓▓▒▒▒▓▒▒▒▓▓▓████████▒▓▒░▒▓▓█████████▒▓██████░░░░░░░░░
░░░░█▓▒▒▒▒▓▓▓▓▓▓▒▒▒▓▒▒▓▓▒▓▓▒░░▓▒█▓█████████▓▒▓████░░░░░░░░░
░░░░█▓▒▓▒▓▓██▓▓▓▓▓▓▓▒▒▒▒▓▒▓▓░░░░░░░░▓███▒▒▓▓▓█████░░░░░░░░░
░░░░██▒▒▓▓▒░▒▒▒▒▓▓▓▓▓▒▓▓▒▒▒░▓▓▒░░▓████████████████░░░░░░░░░
░░░░░█▓▒▒▒▒▒▒▒▒▒▓█▓▒▓▓░░▒▓▒▒▒▒▓▓░░▒▒░▒▒▒██▒█▓▓███▒░░░░░░░░░
░░░░░▒▓▓▒▓▒▒▒▓▒▒▒▒▒▓▓▓█▓▒▒▒▒░░░░░░░░░░░█████▓█████░░░░░░░░░
░░░░░░██▓▓▒▓▓▓▓▒▒▒▓▒▒▒▒▒▒░░░░░▒░▒░░░░▓▓███████████░░░░░░░░░
░░░░░░▓▓▒▒▒▒▓▒▒▓▒▒▒▒▓▓▓▓▓▓█▓▓▓▒▒▓▓██████▓▓▓████████░░░░░░░░
░░░░░▓█▒▒▒▒░▒▒▒▒▒▒▒▒▒░▓▓▓▓█▓█████▓█▓▒░▒▒▓▓██████████░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓███████░░░░░░
"""


"""
some notes
grid is as follows:

xxxxx   GGGxx
xxxxx   GxxYY
xxxxx   GGGxY
xxxxx   GxGxY
xxxxx   GGGxY
xxxxx   xxxxY

G is green, Y is yellow

given todays answer, find a combination of submissions to get the 67 pattern (if possible)

e.g.
today's word is SPEED

SPE**
S**__
SPE*_
S*E*_
SPE*_
****_

where * is not in "speed", _ is a letter from speed that is not the current position

"""


def process_word_list(fname="combined_wordlist.txt") -> dict[str, list[str]]:
    """
    reads the word list (combined_wordlist.txt) and processes it into a dictionary for easier parsing
    format uses letters (lowercase) and _ for patterns
    e.g. "sp___": ["speed", ...]
    """
    with open(fname, "r") as f:
        words = f.readlines()
    res = {"_____": []}
    for word in words:
        word = word.strip()
        # split up the word into 3 pieces
        # for this purpose there are only 3 different patterns we are interested in:
        #
        # ***__  - first 3 letters
        # *____  - first letter
        # *_*__  - first letter + 3rd letter
        #
        search = f"{word[0:3]}__"
        if res.get(search) is None:
            res[search] = []
        res[search].append(word)

        search = f"{word[0]}____"
        if res.get(search) is None:
            res[search] = []
        res[search].append(word)

        search = f"{word[0]}_{word[2]}__"
        if res.get(search) is None:
            res[search] = []
        res[search].append(word)

        res["_____"].append(word)

    return res


def get_first_row(sol: str):
    """
    match the pattern of XXX**
    where X is the actual letter (green)
            * is the non letter (gray)
            ans _ is yellow
    """
    pattern = f"{sol[0:3]}__"
    grey = sol[3:5]
    candidates = PROCESSED_WORDS[pattern]

    # now match words without two letters
    for c in candidates:
        if is_grey(sol, grey, c[3:5]) is False:
            continue
        # anything past this point should work as a word
        return c
    if LOG_LEVEL <= LOG["debug"]:
        print("no candidates")
    return "_____"


def get_second_row(sol: str):
    """
    match the pattern of X**__
    where X is the actual letter (green)
            * is the non letter (gray)
            ans _ is yellow
    """
    pattern = f"{sol[0]}____"
    grey = sol[1:3]  # 2nd and 3rd leters gray
    yellow = sol[3:5]
    candidates = PROCESSED_WORDS[pattern]
    for candidate in candidates:
        # check grey first
        grey_ = candidate[1:3]
        if not is_grey(sol, grey, grey_):
            continue

        # next check yellow
        # letter must be in ans, but must not be the current letter
        yellow_ = candidate[3:5]

        if (
            yellow_[0] not in sol[1:]
            or yellow_[0] == yellow[0]
            or yellow_[1] not in sol[1:]
            or yellow_[1] == yellow[1]
        ):
            continue
        return candidate
    if LOG_LEVEL <= LOG["debug"]:
        print("no candidates")

    # if this doesnt work then fall back to a more lenient one (G__YY) ?
    return "_____"


def get_third_row(sol: str):
    """
    match the pattern of XXX*_
    where X is the actual letter (green)
            * is the non letter (gray)
            ans _ is yellow
    """
    pattern = f"{sol[0:3]}__"
    grey = sol[3]  # 4th letter grey
    yellow = sol[4]  # 5th letter yellow

    candidates = PROCESSED_WORDS[pattern]
    for candidate in candidates:
        # check grey first
        # if candidate != "batta":
        #     continue
        grey_ = candidate[3]
        # print(grey, grey_)
        if not is_grey(sol, grey, grey_):
            continue
        # next check yellow
        # letter must be in ans, but must not be the current letter
        yellow_ = candidate[4]
        if yellow_ not in sol[3:] or yellow_ == yellow:
            continue
        return candidate
    if LOG_LEVEL <= LOG["debug"]:
        print("no candidates")
    return "_____"


def get_fourth_row(sol: str):
    """
    match the pattern of X*X*_

    where X is the actual letter (green)
            * is the non letter (gray)
            ans _ is yellow
    """
    pattern = f"{sol[0]}_{sol[2]}__"
    grey = sol[1] + sol[3]  # 4th letter grey
    yellow = sol[4]  # 5th letter yellow

    candidates = PROCESSED_WORDS[pattern]
    for candidate in candidates:
        # check grey first
        grey_ = candidate[1] + candidate[3]
        if grey_ == grey or grey_[0] == grey[0] or grey_[1] == grey[1]:
            continue

        # next check yellow
        # letter must be in ans, but must not be the current letter
        yellow_ = candidate[4]
        if yellow_ not in sol[:] or yellow_ == yellow:
            continue
        return candidate
    if LOG_LEVEL <= LOG["debug"]:
        print("no candidates")
    return "_____"


def get_fifth_row(sol: str):
    """
    match the pattern of XXX*_

    where X is the actual letter (green)
            * is the non letter (gray)
            ans _ is yellow
    """

    pattern = f"{sol[0:3]}__"
    grey = sol[3]  # 4th letter grey
    yellow = sol[4]  # 5th letter yellow

    candidates = PROCESSED_WORDS[pattern]
    for candidate in candidates:
        # check grey first
        grey_ = candidate[3]
        if grey_ == grey:
            continue

        # next check yellow
        # letter must be in ans, but must not be the current letter
        yellow_ = candidate[4]
        if yellow_ not in sol or yellow_ == yellow:
            continue
        return candidate
    if LOG_LEVEL <= LOG["debug"]:
        print("no candidates")
    return "_____"


def get_sixth_row(sol: str):
    """
    match the pattern of ****_

    where X is the actual letter (green)
            * is the non letter (gray)
            ans _ is yellow
    """
    pattern = "_____"
    grey = sol[0:4]  # first four letters gray
    yellow = sol[4]  # 5th letter yellow

    candidates = PROCESSED_WORDS[pattern]
    for candidate in candidates:
        # check grey first
        grey_ = candidate[0:4]
        if not is_grey(sol, grey, grey_):
            continue
        # next check yellow
        # letter must be in ans, but must not be the current letter
        yellow_ = candidate[4]
        if yellow_ not in sol or yellow_ == yellow:
            continue
        return candidate
    if LOG_LEVEL <= LOG["debug"]:
        print("no candidates")
    return "_____"


def wordle_row(answer, guess):
    """
    format is _ for grey
              G for green
              Y for yellow
    """
    out = ""
    for index, letter in enumerate(guess):
        if letter == answer[index]:
            out += "G"
        elif letter in answer:
            out += "Y"
        else:
            out += "_"
    print(out)


def is_grey(sol, check, guess) -> bool:
    """
    sol: entire word (check for yellow)
    check: letters to check against
    guess: guess to check
    """
    # iterate over each of of the guess
    if LOG_LEVEL <= LOG["debug"]:
        print(f"is_grey: sol={sol}, check={check}, guess={guess}")
    if check == guess:
        return False
    for c, g in zip(check, guess):
        if c == g:
            return False
        if g in sol:
            return False
    return True


def is_yellow(sol, check, guess) -> bool:
    """
    sol: entire word (check for yellow)
    check: letters to check against
    guess: guess to check
    """
    for c, g in zip(check, guess):
        if g not in sol or c == g:
            return False
    return True


PROCESSED_WORDS: Final[dict[str, list[str]]] = process_word_list()
LOG = {"error": 4, "info": 2, "debug": 1}



def main(ans: str):

    words = [
        get_first_row(ans),
        get_second_row(ans),
        get_third_row(ans),
        get_fourth_row(ans),
        get_fifth_row(ans),
        get_sixth_row(ans),
    ]

    if LOG_LEVEL <= LOG["debug"]:
        for word in words:
            wordle_row(ans, word)

    print("found a combination:")
    [print(word) for word in words]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="wordle 67 solver")
    parser.add_argument("answer", type=str, help="wordle answer")
    parser.add_argument(
        "-d",
        "--debug",
        choices=["error", "debug", "info"],
        help="set log level",
        default="error",
        required=False,
    )
    args = parser.parse_args()
    global LOG_LEVEL
    LOG_LEVEL = LOG[args.debug]

    if LOG_LEVEL <= LOG["debug"]:
        print(args)
    main(args.answer)