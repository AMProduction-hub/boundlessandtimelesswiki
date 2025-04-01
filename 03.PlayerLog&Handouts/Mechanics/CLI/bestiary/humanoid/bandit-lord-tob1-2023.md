---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/environment/farmland
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/any-race
statblock: inline
aliases: ["Bandit Lord"]
---
# [Bandit Lord](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/bandit-lord-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 406*  

Not just the leader of a simple gang, the bandit lord has gathered a small army of outlaws and brigands together through force of personality, wit, and strength of arms. To keep those followers in line, the bandit leader must rely on loyal captains whom the bandit lord rewards for their successes and brutally punishes for their failures.

## Ambitious Leaders

Unlike those captains, who crave coin and maybe fame, the bandit lord is building an empire. The bandit lord is always on the lookout for ways to expand at the expense of various rivals and plans contingencies for every occasion, realizing that nothing lasts forever. The bandit lord is ruthless when that's beneficial and magnanimous when it costs nothing.

```statblock
"name": "Bandit Lord (ToB1-2023)"
"size": "Medium"
"type": "humanoid"
"subtype": "any race"
"alignment": "Any Non-Lawful alignment"
"ac": !!int "16"
"ac_class": "[breastplate](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/breastplate.md)"
"hp": !!int "91"
"hit_dice": "14d8 + 28"
"stats":
- !!int "16"
- !!int "15"
- !!int "14"
- !!int "14"
- !!int "11"
- !!int "14"
"speed": "30 ft."
"saves":
  "Dexterity": !!int "4"
  "Wisdom": !!int "2"
  "Strength": !!int "5"
"skillsaves":
  "Intimidation": !!int "4"
  "Athletics": !!int "5"
  "Deception": !!int "4"
"senses": "passive Perception 10"
"languages": "any two languages"
"cr": "4"
"traits":
- "desc": "A melee weapon deals one extra die of its damage when the bandit lord hits\
    \ with it (included in the attack)."
  "name": "Brute"
- "desc": "The bandit lord has advantage on attack rolls against a creature if at\
    \ least one of the bandit lord's allies is within 5 feet of the creature and the\
    \ ally isn't [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)."
  "name": "Pack Tactics"
"actions":
- "desc": "The bandit lord makes two Longsword attacks and one Dagger attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 12\
    \ (2d8 + 3) slashing damage, or 14 (2d10 + 3) slashing damage if used with\
    \ two hands."
  "name": "Longsword"
- "desc": "Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 20/60\
    \ ft., one target. Hit: 5 (1d4 + 3) piercing damage, or 8 (2d4 + 3) piercing\
    \ damage if used to make a melee attack."
  "name": "Dagger"
- "desc": "For 1 minute, the bandit lord can utter a special command or warning whenever\
    \ a nonhostile creature that it can see within 30 feet of it makes an attack roll\
    \ or a saving throw. The creature can add a d4 to its roll provided it can hear\
    \ and understand the bandit lord. A creature can benefit from only one Leadership\
    \ die at a time. This effect ends if the bandit lord is [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)."
  "name": "Leadership (Recharges after a Short or Long Rest)"
"reactions":
- "desc": "The bandit lord adds 2 to its AC against one melee attack that would hit\
    \ it. To do so, the bandit lord must see the attacker and be wielding a weapon."
  "name": "Parry"
- "desc": "When a creature the bandit lord can see targets it with an attack, the\
    \ bandit lord can sidestep behind an ally within 5 feet of it, moving to an unoccupied\
    \ space within 5 feet of the ally. The chosen ally becomes the target of the attack\
    \ instead."
  "name": "Protect Me!"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/bandit-lord-tob1-2023.webp"
```
^statblock

## Environment

desert, farmland, forest, grassland, urban