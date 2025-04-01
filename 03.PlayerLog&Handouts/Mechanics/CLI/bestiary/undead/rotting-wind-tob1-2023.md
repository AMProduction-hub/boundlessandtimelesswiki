---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/farmland
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Rotting Wind"]
---
# [Rotting Wind](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/rotting-wind-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 311*  

*A noxious wind brings a chilling gust to the air, turning nearby foliage to rot.*

## Air of Tombs

A rotting wind is an undead creature made up of the foul air and grave dust sloughed off by innumerable undead creatures within lost tombs and grand necropolises.

## Scouts for Undead Armies

A rotting wind carries the foul stench of death upon it, sometimes flying before undead armies and tomb legions or circling around long-extinct cities and civilizations.

## Withering Crops

Rotting winds sometimes drift mindlessly across a moor or desert, blighting all life they find and leaving only famine and death in their wake. This is especially dangerous when they drift across fields full of crops. They can destroy an entire harvest in minutes.

```statblock
"name": "Rotting Wind (ToB1-2023)"
"size": "Large"
"type": "undead"
"alignment": "Neutral Evil"
"ac": !!int "15"
"hp": !!int "110"
"hit_dice": "13d10 + 39"
"stats":
- !!int "14"
- !!int "20"
- !!int "16"
- !!int "7"
- !!int "12"
- !!int "10"
"speed": "0 ft., fly 60 ft. (hover)"
"damage_immunities": "necrotic, poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
  \ [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
  \ [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)"
"senses": "blindsight 60 ft. (blind beyond this radius), passive Perception 11"
"languages": ""
"cr": "6"
"traits":
- "desc": "The rotting wind can enter a hostile creature's space and stop there. It\
    \ can move through a space as narrow as 1 inch wide without squeezing."
  "name": "Air Form"
- "desc": "The rotting wind is [invisible](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Invisible)."
  "name": "Invisibility"
- "desc": "The rotting wind radiates an aura of poison and decay that slowly pollutes\
    \ the area within 30 feet of it. Each hour the rotting wind stays in a place,\
    \ nonmagical plants in the aura begin to wither, and water in the aura becomes\
    \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned).\
    \ Nonmagical plants in the aura for 24 hours die. A creature that drinks water\
    \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ by the aura must succeed on a DC 14 Constitution saving throw or contract the\
    \ tomb rot disease (see the Tomb Rot trait). Creatures immune to the [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ condition are immune to this disease."
  "name": "Poisonous Aura"
- "desc": "A creature infested with this disease manifests symptoms 1d4 days after\
    \ infection, which include muscle weakness and rotten-smelling breath as its body\
    \ rots from the inside out. Until the disease is cured, at the end of each long\
    \ rest, the infected creature must succeed on a DC 14 Constitution saving throw\
    \ or take 10 (3d6) necrotic damage and suffer one level of [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion).\
    \ This [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion)\
    \ lasts until the creature finishes a long rest after the disease is cured. A\
    \ creature that succeeds on two saving throws recovers from the disease."
  "name": "Tomb Rot"
- "desc": "The rotting wind doesn't require air, food, drink, or sleep."
  "name": "Undead Nature"
"actions":
- "desc": "The rotting wind makes two Wind of Decay attacks. If both attacks hit one\
    \ creature, the target must succeed on a DC 14 Constitution saving throw or contract\
    \ the tomb rot disease (see the Tomb Rot trait)."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 0 ft., one target in the rotting\
    \ wind's space. Hit: 12 (2d6 + 5) bludgeoning damage plus 10 (3d6) necrotic\
    \ damage."
  "name": "Wind of Decay"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/rotting-wind-tob1-2023.webp"
```
^statblock

## Environment

farmland, urban