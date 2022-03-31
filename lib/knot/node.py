from enum import Enum

class Node:
    def __init__(self, index, parity):
        self.index = index
        self.parity = parity
    
    def is_odd(self):
        return self.parity == Parity.Odd

    def is_even(self):
        return self.parity == Parity.Even

    def is_empty(self):
        return self.parity == Pariti.Empty

class Parity(Enum):
    Odd = 1
    Even = 2
    Empty = 3

class Port(Enum):
    A = 1
    B = 2
    Empty = 3
