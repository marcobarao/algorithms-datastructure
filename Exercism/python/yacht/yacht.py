# Score categories
# Change the values as you see fit
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11
YACHT = 12


def score(dice, category):
    if category == YACHT and dice.count(dice[0]) == len(dice):
        return 50
    elif category == CHOICE and dice == sorted(dice):
        return sum(dice)
    elif category == BIG_STRAIGHT and sorted(dice) == list(range(2, 7)):
        return 30
    elif category == LITTLE_STRAIGHT and sorted(dice) == list(range(1, 6)):
        return 30
    elif category == FOUR_OF_A_KIND:
        for i in range(len(dice)):
            if dice.count(dice[i]) >= 4:
                return dice[i] * 4
    elif category == FULL_HOUSE:
        dice_set = list(set(dice))
        times = dice.count(dice_set[0])
        if (times == 2 or times == 3) and len(dice_set) == 2:
            return sum(dice)
    else:
        return category * dice.count(category)
    return 0
