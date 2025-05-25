class Skill:
    def __init__(self, name, power, status_effect=None):
        self.name = name
        self.power = power
        self.status_effect = status_effect  # e.g. "poison", "paralysis"