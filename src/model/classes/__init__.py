from src.model.classes.donation import *
from src.model.classes.user import *
from src.model.classes.team import *

class Backend:

    def __init__(self):
        self.donation=Donation()
        self.user=User()
        self.team=Team()
