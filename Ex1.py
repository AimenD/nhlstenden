import csv
import numpy as np
from typing import Set,Tuple, List
import torch
import torch.utils
import torch.utils.data
import torch.nn as nn
NoneType = type(None)

import time

def id_to_fruit(fruit_id: int, fruits: List[str]) -> str:
    """
    This method returns the fruit name by getting the string at a specific index of the list.

    :param fruit_id: The id of the fruit to get
    :param fruits: The list of fruits to choose the id from
    :return: The string corresponding to the index ``fruit_id``

    **This method is part of a series of debugging exercises.**
    **Each Python method of this series contains bug that needs to be found.**

    | ``1   It does not print the fruit at the correct index, why is the returned result wrong?``
    | ``2   How could this be fixed?``

    This example demonstrates the issue:
    name1, name3 and name4 are expected to correspond to the strings at the indices 1, 3, and 4:
    'orange', 'kiwi' and 'strawberry'..

    >>> name1 = id_to_fruit(1, ["apple", "orange", "melon", "kiwi", "strawberry"])
    >>> name3 = id_to_fruit(3, ["apple", "orange", "melon", "kiwi", "strawberry"])
    >>> name4 = id_to_fruit(4, ["apple", "orange", "melon", "kiwi", "strawberry"])
    """
    if fruit_id < 0 or fruit_id >= len(fruits):
        raise RuntimeError(f"Fruit with id {fruit_id} does not exist")
    return fruits[fruit_id]

name1 = id_to_fruit(1, ["apple", "orange", "melon", "kiwi", "strawberry"])
name3 = id_to_fruit(3, ["apple", "orange", "melon", "kiwi", "strawberry"])
name4 = id_to_fruit(4, ["apple", "orange", "melon", "kiwi", "strawberry"])

# it is wrong because Sets do not maintain order. 
# to fix it, we can use a list instead of a set