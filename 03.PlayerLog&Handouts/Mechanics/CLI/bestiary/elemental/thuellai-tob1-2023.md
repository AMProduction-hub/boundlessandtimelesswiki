---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/12
- ttrpg-cli/monster/environment/arctic
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/elemental
statblock: inline
aliases: ["Thuellai"]
---
# [Thuellai](03 - Player Log & Handouts\Mechanics\CLI\bestiary\elemental/thuellai-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 360*  

*This raging cloud of animate mist and ice has icicle shards for eyes and claws.*

## Servants of the North Wind

These fast-flying creatures of air and ice were created by the lord of the north wind, Boreas, to be his heralds, assassins, and hunting hounds. They appear as a swirling blizzard, often blending in with snowstorms to surprise their victims.

## Terrifying Blizzards

Thuellai love to engulf creatures in their blizzards, to lash buildings with ice and cold, and to trigger avalanches with their whirlwinds. They thrive on destruction and fear, and they share their master's unpredictable nature.

## Immune to Steel

Northerners especially fear the thuellai because of their resistance to mundane steel, their terrifying howls, and their ability to cause madness.

```statblock
"name": "Thuellai (ToB1-2023)"
"size": "Huge"
"type": "elemental"
"alignment": "Chaotic Neutral"
"ac": !!int "17"
"hp": !!int "161"
"hit_dice": "14d12 + 70"
"stats":
- !!int "22"
- !!int "24"
- !!int "20"
- !!int "10"
- !!int "11"
- !!int "14"
"speed": "0 ft., fly 100 ft. (hover)"
"saves":
  "Charisma": !!int "6"
  "Wisdom": !!int "4"
  "Intelligence": !!int "4"
"skillsaves":
  "Perception": !!int "4"
"damage_vulnerabilities": "fire"
"damage_resistances": "lightning; thunder; bludgeoning, piercing, slashing from nonmagical\
  \ attacks"
"damage_immunities": "poison"
"condition_immunities": "[exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
  \ [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
  \ [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)"
"senses": "darkvision 60 ft., passive Perception 14"
"languages": "Common, Dwarvish, Primordial"
"cr": "12"
"traits":
- "desc": "At the start of each of the thuellai's turns, each creature within 15 feet\
    \ of it must succeed on a DC 17 Constitution saving throw or take 7 (2d6) cold\
    \ damage. For each minute a creature spends within 15 feet of the thuellai, it\
    \ must succeed on a DC 17 Constitution saving throw or suffer one level of [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion)\
    \ from cold exposure. Unprotected, nonmagical flames within 15 feet of the thuellai\
    \ are extinguished. Any spells of 3rd level or lower that provide resistance to\
    \ cold damage and that are within 15 feet of the thuellai immediately end. Water\
    \ freezes if it remains within 15 feet of the thuellai for at least 1 minute."
  "name": "Chilling Presence"
- "desc": "The thuellai doesn't require air, food, drink, or sleep."
  "name": "Elemental Nature"
- "desc": "The thuellai can see through areas obscured by snowfall, sleet, rain, and\
    \ other wintry precipitation without penalty."
  "name": "Snowsight"
"actions":
- "desc": "The thuellai makes three Icy Claw attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 15\
    \ (2d8 + 6) slashing damage plus 10 (3d6) cold damage."
  "name": "Icy Claw"
- "desc": "The thuellai exhales an icy blast in a 60-foot cone. Each creature in the\
    \ area must make a DC 17 Dexterity saving throw, taking 49 (14d6) cold damage\
    \ on a failed save, or half as much damage on a successful one."
  "name": "Freezing Breath (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/elemental/token/thuellai-tob1-2023.webp"
```
^statblock

## Environment

arctic