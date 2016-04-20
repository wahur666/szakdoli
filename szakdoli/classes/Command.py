from classes.Rect import Rect
from abc import abstractmethod,ABCMeta


class Command(Rect, metaclass=ABCMeta):


    def __init__(self, X, Y, H, L, indetLevel):
        super().__init__(X,Y,H,L,indetLevel)

    @abstractmethod
    def runCommand(self):
        pass