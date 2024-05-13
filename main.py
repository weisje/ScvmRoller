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
    Function for determining the character's initial stats
    :return: dict
    """
    pass


if __name__ == 'main':
    main()
