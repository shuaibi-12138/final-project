from pokemon import Pokemon
from pokedex import create_pokemon, get_all_names

import random

def main():
    print("🌟 Welcome to the Pokémon battle system!")
    all_names = get_all_names()

    print("\nOptional Pokémon:")
    for idx, name in enumerate(all_names):
        print(f"{idx+1}. {name}")

    while True:
        try:
            choice = int(input("Please select your Pokémon number (1-6):")) - 1
            if 0 <= choice < len(all_names):
                player_name = all_names[choice]
                break
            else:
                print("Please enter a valid number!")
        except ValueError:
            print("Please enter a number!")

    # 玩家选择
    p_name, p_hp, p_atk, p_def, p_skills = create_pokemon(player_name)
    player = Pokemon(p_name, p_hp, p_atk, p_def, p_skills)

    # 系统为敌方随机选择非玩家选择的宝可梦
    enemy_name = random.choice([name for name in all_names if name != player_name])
    e_name, e_hp, e_atk, e_def, e_skills = create_pokemon(enemy_name)
    enemy = Pokemon(e_name, e_hp, e_atk, e_def, e_skills)

    print(f"\nYou have chosen {player.name}！")
    print(f"The opponent sent out {enemy.name}！")
    print("⚔️ The Pokémon battle has begun!")

    # 战斗循环（略）保留之前主循环代码
    while player.is_alive() and enemy.is_alive():
        print(f"\nYou：{player.name} HP={player.hp} Status={player.status or 'Normal'}")
        print(f"Enemy：{enemy.name} HP={enemy.hp} Status={enemy.status or 'Normal'}")

        print("\nYour skills:")
        for i, skill in enumerate(player.skills):
            effect = f" - Status：{skill.status_effect}" if skill.status_effect else ""
            print(f"{i+1}. {skill.name}（Power {skill.power}{effect}）")

        try:
            idx = int(input("Please select the skill number:")) - 1
            player.use_skill(player.skills[idx], enemy)
        except:
            print("Selection is invalid. The first skill will be used by default.")
            player.use_skill(player.skills[0], enemy)

        if not enemy.is_alive():
            print(f"\n🎉 You win! {enemy.name} has been defeated!")
            print(f"You have become a Pokémon master!")
            break

        enemy_skill = random.choice(enemy.skills)
        enemy.use_skill(enemy_skill, player)

        if not player.is_alive():
            print(f"\n💀 You lost! {player.name} has been defeated!")
            break

if __name__ == "__main__":
    main()