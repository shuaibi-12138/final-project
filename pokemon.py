import random

class Pokemon:
    def __init__(self, name, hp, attack, defense, skills):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.skills = skills
        self.status = None  
        self.status_duration = 0  # number of turns the status lasts

    def is_alive(self):
        return self.hp > 0

    def apply_status(self):
        """
        Applies the current status effect, such as poison damage or paralysis chance.
        Reduces the status duration each turn.
        """
        if self.status:
            if self.status_duration > 0:
                self.status_duration -= 1
                if self.status == "poison":
                    damage = int(self.max_hp * 0.1)
                    self.hp -= damage
                    self.hp = max(0, self.hp)
                    print(f"{self.name} is hurt by poison! Lost {damage} HP.")
                elif self.status == "paralysis":
                    if random.random() < 0.3:
                        print(f"{self.name} is paralyzed and can't move!")
                        return False
            else:
                print(f"{self.name}'s {self.status} effect has worn off.")
                self.status = None
        return True

    def use_skill(self, skill, opponent):
        """
        Uses a skill against the opponent.
        Applies damage and may inflict a status effect.
        """
        if not self.apply_status():
            return  # Skips turn due to status effect

        damage = max(0, self.attack + skill.power - opponent.defense)
        opponent.hp -= damage
        opponent.hp = max(0, opponent.hp)
        print(f"{self.name} used {skill.name}! It dealt {damage} damage.")

        # Apply status effect
        if skill.status_effect and opponent.is_alive():
            if opponent.status is None and random.random() < 0.4:
                opponent.status = skill.status_effect
                opponent.status_duration = 1
                print(f"{opponent.name} is now affected by {skill.status_effect} for 1 turns!")
