import csv
import os
import random
import sys


def main():
    """
    The purpose of this program is to randomly generate characters for the TTRPG game "Mörk Borg" by Free League Publishing.  The characters are not from the optional classes; they are completely randomly generated based on the initial character rules.
    """
    charStats = statsRoller()
    hitPoints = 1
    startingEquipment = equipmentRoller()
    startingScrolls = []
    startingWeapon = ""
    startingArmor = ""

    if startingEquipment[1][0] == "Unclean Scroll":
        startingScrolls.append(scrollPicker("UNCLEAN SCROLL"))
    if startingEquipment[2][0] == "Sacred Scroll":
        startingScrolls.append(scrollPicker("SACRED SCROLL"))
    if len(startingScrolls) < 1:
        startingWeapon = weaponRoller()
        startingArmor = armorRoller()
    else:
        startingWeapon = weaponRoller(True)
        startingArmor = armorRoller(True)

    hitPointRoll = random.randint(1,8) + charStats["Toughness"]
    if hitPointRoll > 0:
        hitPoints = hitPointRoll

    terribleTraits = traitPicker("TERRIBLE TRAITS")
    brokenBody = traitPicker("BROKEN BODY")
    badHabit = traitPicker("BAD HABIT")
    troublingTales = traitPicker("TROUBLING TALES")

    os.system('cls')

    # Character Stat Display
    print(f"NAME:\t{namePicker()}")
    print(f"\nHP: {hitPoints}")
    print("\nSTATS:")
    for stat in charStats:
        print(f"\t{stat}: {charStats[stat]}")
    print("\nITEMS:")
    for i in range(3):
        printCase = ""
        match i:
            case 0:
                printCase = f"\t{startingEquipment[0][0]}"
                if startingEquipment[0][1]:
                    printCase += f": {startingEquipment[0][1]}"
            case 1:
                printCase = f"\t{startingEquipment[1][0]}"
                if startingEquipment[1][1]:
                    printCase += f": {startingEquipment[1][1]}"
                if startingEquipment[1][2]:
                    printCase += f" ({startingEquipment[1][2]})"
            case 2:
                printCase = f"\t{startingEquipment[2][0]}"
                if startingEquipment[2][1]:
                    printCase += f": {startingEquipment[2][1]}"
                if startingEquipment[2][2]:
                    printCase += f" ({startingEquipment[2][2]})"
        print(printCase)

def namePicker() -> str:
    """
    Function for populating & selecting a name for the created character.
    :return: str
    """
    characterNamesTable = csvReader("documents\\traits\\characterNames.csv", "|", False)
    characterName = random.choice(characterNamesTable)
    characterName = characterName[0]
    return characterName


def traitPicker(traitType) -> list:
    """
    Function for generating different types of traits for characters.  These traits are not mechanically important; just adding roleplay flavor for characters.
    :param traitType: The table that the requested trait should be pulled from.
    :type traitType: str
    :return: list
    """
    returnTraits = []
    terribleTraitTable = csvReader("documents\\traits\\terribleTraits.csv")
    brokenBodyTable = csvReader("documents\\traits\\brokenBody.csv")
    badHabitTable = csvReader("documents\\traits\\badHabits.csv")
    troublingTalesTable = csvReader("documents\\traits\\troublingTales.csv")

    match traitType.upper():
        case "TERRIBLE TRAITS":
            while len(returnTraits) < 2:
                traitChoice = random.choice(terribleTraitTable)
                if traitChoice not in returnTraits:
                    returnTraits.append(traitChoice[0])
        case "BROKEN BODY":
            traitChoice = random.choice(brokenBodyTable)
            returnTraits.append(traitChoice[0])
        case "BAD HABIT":
            traitChoice = random.choice(badHabitTable)
            returnTraits.append(traitChoice[0])
        case "TROUBLING TALES":
            traitChoice = random.choice(troublingTalesTable)
            returnTraits.append(traitChoice[0])
        case _:
            print(f"{traitType} is not a valid choice.")
            sys.exit()

    return returnTraits


def scrollPicker(scrollType) -> list:
    """
    Function for randomly selecting a scroll from the base Mörk Borg pool of scrolls based on the input
    :param scrollType: Defines the type of scroll that will be chosen from("UNCLEAN SCROLL" or "SACRED SCROLL")
    :type scrollType: str
    :return: list
    """
    uncleanScrolls = csvReader("documents\\equipment\\uncleanScrolls.csv")
    sacredScrolls = csvReader("documents\\equipment\\sacredScrolls.csv")

    if scrollType.upper() == "UNCLEAN SCROLL":
        return random.choice(uncleanScrolls)
    elif scrollType.upper() == "SACRED SCROLL":
        return random.choice(sacredScrolls)
    else:
        print(f"\'{scrollType}\' is not a valid scroll type. Viable options: \'UNCLEAN SCROLL\' or \'SACRED SCROLL\'")
        sys.exit()


def armorRoller(scrollPresent=False) -> list:
    """
    Function for determining the armor that will be given to the character.  If the character has a scroll then they are limited to tier 0 & tier 1 armor.  Otherwise, they will have tier 0 through tier 3 to select.
    :param scrollPresent: States whether the character has been given a scroll during item selection.
    :type scrollPresent: bool
    :return: list
    """
    startingArmor = csvReader("documents\\equipment\\armor.csv")
    defaultDie = len(startingArmor)
    if scrollPresent:
        defaultDie = 2

    return startingArmor[random.randint(0, defaultDie-1)]


def weaponRoller(scrollPresent=False) -> list:
    """
    Function for determining the weapon that will be given to the character.  If the character has a scroll then they are limited to weapons 0-5.  Otherwise, they will have access to all weapons present.
    :param scrollPresent: States whether the character has been given a scroll during item selection.
    :type scrollPresent: bool
    :return: list
    """
    startingWeapons = csvReader("documents\\equipment\\weapons.csv")
    defaultDie = len(startingWeapons)
    if scrollPresent:
        defaultDie = 6

    return startingWeapons[random.randint(0, defaultDie-1)]


def equipmentRoller() -> list:
    """
    Function for determining the starting equipment for PCs
    :return: list
    """
    startingEquipment = [] # list for holding returned equipment
    startingContainers = csvReader("documents\\equipment\\startingContainers.csv") # list for holding starting containers pulled from outside document startingContainers.csv
    startingItems01 = csvReader("documents\\equipment\\startingItems01.csv") # list for holding the starting items pulled from outside document startingItems01.csv
    startingItems02 = csvReader("documents\\equipment\\startingItems02.csv") # list for holding the starting items pulled from outside document startingItems02.csv

    startingEquipment.append(random.choice(startingContainers))
    startingEquipment.append(random.choice(startingItems01))
    startingEquipment.append(random.choice(startingItems02))

    return startingEquipment


def statsRoller() -> dict:
    """
    Function for determining the character's initial stats. Will also determine two preferred stats randomly. Returns the results as a dict of the abilities.
    :return: dict
    """
    stats = {"Agility": -4, "Presence": -4, "Strength": -4, "Toughness": -4} # Initially populates the stats with invalid values to generate the dictionary
    preferredStats = [] # List for holding the preferred stats after they are selected
    while len(preferredStats) < 2:
        preferredStatChoice = random.choice(list(stats))
        if preferredStatChoice not in preferredStats:
            preferredStats.append(preferredStatChoice) # Check if selected stat is already in preferredStats.  If not append it, if so then try again until the preferredStats list holds two entries.

    for currentStat in stats:
        if currentStat in preferredStats:
            stats[currentStat] = abilityRoller(True) # Call abilityRoller() & have it return results of roll 4d6 drop the lowest
        else:
            stats[currentStat] = abilityRoller() # Call abilityRoller & have it return results of roll 3d6
    return stats


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


def csvReader(filePath, delimiterChar='|', hasHeader=True) -> list:
    """
    Function for reading in designated CSV files, populating contents of rows to a list, then returning a list of lists for said contents
    :param filePath: Document filepath where the csv file is located, including the csv file itself(i.e. "\\documents\\containersFile.csv"
    :type filePath: str
    :param delimiterChar: Character defined as the seperator between columns within the csv file
    :type: char
    :param hasHeader: Specifies if the csv file has a header included for the information or not.
    :type hasHeader: bool
    :return: list
    """
    csvContentList = [] # Final list that will be returned to caller
    with open(filePath, 'r') as csvContentFile:
        csvReadEngine = csv.reader(csvContentFile, delimiter=delimiterChar)
        if hasHeader:
            next(csvReadEngine)
        for row in csvReadEngine:
            csvContentList.append(row)
    csvContentFile.close()

    return csvContentList


if __name__ == '__main__':
    main()
