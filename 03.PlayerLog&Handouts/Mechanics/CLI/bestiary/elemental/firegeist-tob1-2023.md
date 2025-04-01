---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/elemental
statblock: inline
aliases: ["Firegeist"]
---
# [Firegeist](03 - Player Log & Handouts\Mechanics\CLI\bestiary\elemental/firegeist-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 188*  

*Wisps of black smoke and spots of bright flame coalesce into a vaguely humanoid shape.*

## Elemental Echoes

When a fire elemental meets its destruction in a particularly humiliating fashion, particularly by humanoids, while summoned away from its home plane, its remains transform into a firegeist. Malevolent and resentful, they exist for revenge.

## Indiscriminate Arsonists

Firegeists are not adept at telling one humanoid from another, and they are satisfied with burning any similar creature, providing the creature is flammable.

## Brighter Light, Darker Smoke

A firegeist can shine brightly or be primarily smoky and dark, as it wishes. It always sheds a little light.

```statblock
"name": "Firegeist (ToB1-2023)"
"size": "Small"
"type": "elemental"
"alignment": "Neutral Evil"
"ac": !!int "14"
"hp": !!int "82"
"hit_dice": "15d6 + 30"
"stats":
- !!int "7"
- !!int "18"
- !!int "14"
- !!int "4"
- !!int "16"
- !!int "6"
"speed": "40 ft."
"skillsaves":
  "Perception": !!int "5"
"damage_immunities": "fire, poison"
"condition_immunities": "[exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
  \ [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
  \ [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)"
"senses": "darkvision 60 ft., passive Perception 15"
"languages": "Ignan"
"cr": "2"
"traits":
- "desc": "The firegeist doesn't require air, food, drink, or sleep."
  "name": "Elemental Nature"
- "desc": "The firegeist has advantage on Dexterity ([Stealth](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Stealth))\
    \ checks made to hide in fire or in areas lit by nonmagical fire."
  "name": "Hide By Firelight"
- "desc": "While in an area of light created by a spell or other magical effect, the\
    \ firegeist has disadvantage on attack rolls and ability checks."
  "name": "Magical Light Sensitivity"
- "desc": "The firegeist sheds dim light in a 5- to 20-foot radius. It can alter the\
    \ radius as a bonus action."
  "name": "Variable Illumination"
- "desc": "For every 5 feet the firegeist moves in water, or for every gallon of water\
    \ splashed on it, it takes 1 cold damage."
  "name": "Water Susceptibility"
"actions":
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7 (1d6\
    \ + 4) bludgeoning damage plus 7 (2d6) fire damage. If the target is a flammable\
    \ object, it ignites. If the target is a creature, the target must succeed on\
    \ a DC 13 Dexterity saving throw or ignite. Until a creature takes an action to\
    \ douse the fire, the target takes 3 (1d6) fire damage at the start of each\
    \ of its turns."
  "name": "Burning Slam"
- "desc": "The firegeist assaults the mind of one creature it can see within 30 feet\
    \ of it with the painful, humiliating memory of the firegeist's first death. The\
    \ target must make a DC 13 Wisdom saving throw. On a failure, the target takes\
    \ 14 (4d6) fire damage and is [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ for 1 minute. On a success, the target takes half the damage and isn't [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened).\
    \ While [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
    \ the creature takes 3 (1d6) fire damage at the start of each of its turns.\
    \ The target can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Burning Terror (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/elemental/token/firegeist-tob1-2023.webp"
```
^statblock

## Environment

planar