import random


def get_dice_roll() -> list[int]:
    return [random.randint(1, 6) for _ in range(2)]  # noqa: S311
