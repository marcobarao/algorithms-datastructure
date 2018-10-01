import random
import string

name_list = []

class Robot(object):
    def __init__(self):
        self.name = self._generate_name()
        self.reset()
    
    def reset(self):
        if self.name  not in name_list:
            name_list.append(self.name)
        else:
            self.name = self._generate_name()
            self.reset()

    def _generate_name(self):
        name = ""

        name += ''.join(random.sample(string.ascii_uppercase, 2))
        name += ''.join(random.sample(string.digits, 3))

        return name

        