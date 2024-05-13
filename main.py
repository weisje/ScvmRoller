import os
import random
import sys


def main():
    """
    The purpose of this program is to randomly generate characters for the TTRPG game "Mörk Borg" by Free League Publishing.  The characters are not from the optional classes; they are completely randomly generated based on the initial character rules.
    """
    print("Success")


def traitPicker(traitType) -> list:
    # TODO
    """
    Function for generating different types of traits for characters.  These traits are not mechanically important; just adding roleplay flavor for characters.
    :param traitType:
    :type traitType: str
    :return: list of str
    """
    pass


def scrollPicker(scrollType) -> str: # TODO
    """
    Function for randomly selecting a scroll from the base Mörk Borg pool of scrolls based on the input
    :param scrollType: Defines the type of scroll that will be chosen from("UNCLEAN SCROLL" or "SACRED SCROLL")
    :type scrollType: str
    :return: str
    """
    pass


def armorRoller(scrollPresent=False) -> dict:
    # TODO
    """
    Function for determining the armor that will be given to the character.  If the character has a scroll then they are limited to tier 0 & tier 1 armor.  Otherwise, they will have tier 0 through tier 3 to select.
    :param scrollPresent: States whether the character has been given a scroll during item selection.
    :type scrollPresent: bool
    :return: dict
    """
    pass


def weaponRoller(scrollPresent=False) -> dict:
    # TODO
    """
    Function for determining the weapon that will be given to the character.  If the character has a scroll then they are limited to weapons 0-5.  Otherwise, they will have access to all weapons present.
    :param scrollPresent: States whether the character has been given a scroll during item selection.
    :type scrollPresent: bool
    :return: dict
    """
    pass


def equipmentRoller() -> list:
    # TODO
    """
    Function for determining the starting equipment for PCs
    :return: list
    """
    pass


def statsRoller() -> dict:
    # TODO
    """
    Function for determining the character's initial stats. Will also determine two preferred stats randomly.
    :return: dict
    """
    pass


def abilityRoller(preferredStat=False) -> int:
    """
    Function for rolling initial abilities.
    :param preferredStat: Determines if the stat should be rolled with 4d6 drop the lowest(True) or 3d6(False).
    :type preferredStat: bool
    :return: int
    """
    rolls = [] # collection of ints representing the random rolls
    rollCount = 3 # How many d6s will be rolled for the ability

    while len(rolls) < rollCount:
        rolls.append(random.randint(1, 6))

    if preferredStat: # If the roll is listed as a preferred stat, then add one more d6 roll
        rolls.append(random.randint(1,6))
        for lowest in range(0,1): # drop the lowest roll(lowest value in rolls list)
            rolls.remove(min(rolls))

    match sum(rolls): # Add the values in the rolls list, then compare result to cases for return int value
        case 1 | 2 | 3 | 4:
            return -3
        case 5 | 6:
            return -2
        case 7 | 8:
            return -1
        case 9 | 10 | 11 | 12:
            return 0
        case 13 | 14:
            return 1
        case 15 | 16:
            return 2
        case 17 | 18 | 19 | 20:
            return 3
        case _:
            print(f"Number {sum(rolls)} outside range")
            sys.exit()


if __name__ == 'main':
    main()
