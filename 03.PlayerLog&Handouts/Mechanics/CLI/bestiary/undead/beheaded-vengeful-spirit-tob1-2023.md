---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/farmland
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Beheaded Vengeful Spirit"]
---
# [Beheaded Vengeful Spirit](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/beheaded-vengeful-spirit-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 384*  

*The ghostly humanoid floats through the air, its head hovering several inches above its severed neck.*

A vengeful spirit is created when a strong-willed humanoid with magical talent is killed by relatively mundane means wielded by angry or fearful people. The victim's angry spirit returns, looking for retribution against those involved in its death—whether that death was wrongful murder or justified execution. These spirits inflict punishment on the living with the rage that animates them, and they mete out their revenge in poetic fashion.

## Varied Vengeance

A vengeful spirit is defined by its means of death. Regardless of the cause of death, each vengeful spirit seeks to have its killer or killers die in like fashion.

```statblock
"name": "Beheaded Vengeful Spirit (ToB1-2023)"
"size": "Medium"
"type": "undead"
"alignment": "Any alignment"
"ac": !!int "15"
"ac_class": "angry defiance"
"hp": !!int "54"
"hit_dice": "12d8"
"stats":
- !!int "7"
- !!int "13"
- !!int "11"
- !!int "10"
- !!int "10"
- !!int "19"
"speed": "0 ft., fly 60 ft. (hover)"
"saves":
  "Charisma": !!int "6"
  "Wisdom": !!int "2"
"damage_resistances": "acid; fire; lightning; thunder; bludgeoning, piercing, slashing\
  \ from nonmagical attacks"
"damage_immunities": "cold, necrotic, poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
  \ [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)"
"senses": "darkvision 60 ft., passive Perception 10"
"languages": "the languages it knew in life"
"cr": "4"
"traits":
- "desc": "The vengeful spirit adds its Charisma modifier to its AC (included above)."
  "name": "Angry Defiance"
- "desc": "The vengeful spirit can move through other creatures and objects as if\
    \ they were difficult terrain. It takes 5 (1d10) force damage if it ends its\
    \ turn inside an object."
  "name": "Incorporeal Movement"
- "desc": "The vengeful spirit doesn't require air, food, drink, or sleep."
  "name": "Undead Nature"
"actions":
- "desc": "Melee or Ranged Spell Attack: +6 to hit, reach 5 ft. or range 30 ft.,\
    \ one creature. Hit: 22 (4d8 + 4) psychic damage, and the target must succeed\
    \ on a DC 14 Charisma saving throw or be enraged until the end of its next turn.\
    \ While enraged, the target has advantage on melee attack rolls and must move\
    \ to and attack the nearest creature other than the spirit. In addition, attack\
    \ rolls against the enraged target have advantage."
  "name": "Essence of Rage"
- "desc": "The vengeful spirit makes a quick, cutting gesture at one creature it can\
    \ see within 30 feet of it that has a head and that is below half its hp maximum.\
    \ The target must make a DC 14 Constitution saving throw, taking 28 (8d6) slashing\
    \ damage on a failed save, or half as much damage on a successful one. A target\
    \ that fails the saving throw also has one of its heads cut off. The creature\
    \ dies if it can't survive without the lost head."
  "name": "Decapitation (1/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/beheaded-vengeful-spirit-tob1-2023.webp"
```
^statblock

## Environment

farmland, urban