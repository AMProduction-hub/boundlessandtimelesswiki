---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/14
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/gargantuan
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Isonade"]
---
# [Isonade](03 - Player Log & Handouts\Mechanics\CLI\bestiary\monstrosity/isonade-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 240*  

*The creature's mighty tail thrashes ships, docks, and sailors in its path of destruction.*

## Coastal Destroyer

The isonade is a beast of destruction, sweeping away entire islands and villages. Though not very intelligent, it singles out a community and tries to lure residents into the waves by forcing plentiful fish to the surface, easy pickings for even the most amateur fishers.

## Ocean Sacrifices

When coastal villagers suffer from a hurricane or tsunami, they fall back on folklore and blame the stirrings of the isonade. Some say that a degenerate group seeks to draw the beast forth by dumping a long chain of bound and screaming sacrifices into the lightless depths of the sea.

## Ancient Being

The beast's age is unknown, and many coastal bards tell various legends of the creature. Some say it is the last of its kind, while others say that a small group of isonades lurks in the depths.

```statblock
"name": "Isonade (ToB1-2023)"
"size": "Gargantuan"
"type": "monstrosity"
"alignment": "Chaotic Neutral"
"ac": !!int "18"
"ac_class": "natural armor"
"hp": !!int "222"
"hit_dice": "12d20 + 96"
"stats":
- !!int "30"
- !!int "14"
- !!int "26"
- !!int "6"
- !!int "18"
- !!int "8"
"speed": "10 ft., swim 100 ft."
"saves":
  "Wisdom": !!int "9"
  "Strength": !!int "15"
  "Constitution": !!int "13"
"skillsaves":
  "Athletics": !!int "15"
  "Perception": !!int "9"
"damage_immunities": "cold"
"senses": "darkvision 90 ft., passive Perception 19"
"languages": "understands Aquan and Elvish, but can't speak"
"cr": "14"
"traits":
- "desc": "Nearby weather responds to the isonade's desires. At the start of each\
    \ minute, the isonade can choose to change the precipitation and wind within 1\
    \ mile of it by one stage, up or down (no action required). This effect works\
    \ like the changing weather conditions aspect of the [control weather](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/control-weather.md)\
    \ spell, except the isonade can't change the temperature and the conditions change\
    \ immediately."
  "name": "Influence Weather"
- "desc": "The isonade has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "The isonade deals double damage to objects and structures."
  "name": "Siege Monster"
- "desc": "The isonade can breathe only underwater."
  "name": "Water Breathing"
"actions":
- "desc": "The isonade makes one Bite attack and two Tail Slap attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +15 to hit, reach 15 ft., one target. Hit: 36\
    \ (4d12 + 10) piercing damage. If the target is a Large or smaller creature,\
    \ it must succeed on a DC 18 Dexterity saving throw or be swallowed by the isonade.\
    \ A swallowed creature is [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ and [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ it has total cover against attacks and other effects outside the isonade, and\
    \ it takes 21 (6d6) acid damage at the start of each of the isonade's turns.\
    \ An isonade can have no more than four creatures swallowed at a time. If the\
    \ isonade takes 30 damage or more on a single turn from a creature inside it,\
    \ it must succeed on a DC 23 Constitution saving throw at the end of that turn\
    \ or regurgitate all swallowed creatures, which fall [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)\
    \ in a space within 10 feet of the isonade. If the isonade dies, a swallowed creature\
    \ is no longer [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ by it and can escape from the corpse by using 20 feet of movement, exiting [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +15 to hit, reach 15 ft., one target. Hit: 24\
    \ (4d6 + 10) bludgeoning damage."
  "name": "Tail Slap"
- "desc": "If the isonade swims at least 20 feet as part of its movement, it can use\
    \ this action to emerge in a space on the surface of the water that contains one\
    \ or more other creatures. Each of those creatures and each creature within 10\
    \ of the isonade's space must make a DC 18 Dexterity saving throw. On a failure,\
    \ a creature takes 49 (14d6) bludgeoning damage and is knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone).\
    \ On a success, a creature takes half the damage and is pushed up to 10 feet out\
    \ of the isonade's space into an unoccupied space of the creature's choice. If\
    \ no unoccupied space is within range, the creature instead falls [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)\
    \ in the isonade's space."
  "name": "Breach"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/monstrosity/token/isonade-tob1-2023.webp"
```
^statblock

## Environment

underwater