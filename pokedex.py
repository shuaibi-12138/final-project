from skill import Skill

# Pokédex: stores Pokémon data
pokedex = {
    "Pikachu": {
        "hp": 100, "attack": 25, "defense": 10,
        "skills": [
            Skill("Thunder Shock", 15, "paralysis"),
            Skill("Iron Tail", 20),
            Skill("Thunderbolt", 25, "paralysis"),
            Skill("Quick Attack", 10)
        ]
    },
    "Bulbasaur": {
        "hp": 110, "attack": 20, "defense": 12,
        "skills": [
            Skill("Vine Whip", 12),
            Skill("Poison Powder", 8, "poison"),
            Skill("Leech Seed", 10, "poison"),
            Skill("Solar Beam", 30)
        ]
    },
    "Charmander": {
        "hp": 95, "attack": 26, "defense": 9,
        "skills": [
            Skill("Flamethrower", 25),
            Skill("Scratch", 15),
            Skill("Smokescreen", 18, "paralysis"),
            Skill("Dragon Rage", 20)
        ]
    },
    "Squirtle": {
        "hp": 105, "attack": 22, "defense": 14,
        "skills": [
            Skill("Water Gun", 15),
            Skill("Bubble", 20),
            Skill("Tackle", 10),
            Skill("Water Pulse", 25)
        ]
    },
    "Togepi": {
        "hp": 90, "attack": 18, "defense": 10,
        "skills": [
            Skill("Charm", 5),
            Skill("Sing", 0, "paralysis"),
            Skill("Pound", 12),
            Skill("Magical Shine", 18)
        ]
    },
    "Meowth": {
        "hp": 92, "attack": 24, "defense": 11,
        "skills": [
            Skill("Fury Swipes", 15),
            Skill("Shadow Claw", 20),
            Skill("Bite", 18),
            Skill("Fake Out", 12)
        ]
    }
}

def create_pokemon(name):
    data = pokedex[name]
    return name, data["hp"], data["attack"], data["defense"], data["skills"]

def get_all_names():
    return list(pokedex.keys())