---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1-2
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/construct
statblock: inline
aliases: ["Clockwork Watchman"]
---
# [Clockwork Watchman](03 - Player Log & Handouts\Mechanics\CLI\bestiary\construct/clockwork-watchman-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 64*  

*This mechanical being's body is composed of brass and iron, bedecked in a loose uniform of the city watch. Its movements are slow but steady.*

## Lightly Armored Servants

Clockwork watchmen are more solidly built versions of common clockwork scullions (servant creations in wealthy households that are incapable of combat). Proper clockwork watchmen are built with iron parts instead of tin and given keener senses. Many have small bits of armor covering their joints and vital parts.

## Constant Rounds

They endlessly patrol the city day and night, pausing only to receive maintenance and new boots.

## Shouts & Stutters

Their speech is slow and halting, but their distinctive shouts and whistles bring human guards at a run.

```statblock
"name": "Clockwork Watchman (ToB1-2023)"
"size": "Medium"
"type": "construct"
"alignment": "Unaligned"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "44"
"hit_dice": "8d8 + 8"
"stats":
- !!int "14"
- !!int "12"
- !!int "12"
- !!int "5"
- !!int "10"
- !!int "1"
"speed": "30 ft."
"saves":
  "Constitution": !!int "3"
"skillsaves":
  "Athletics": !!int "4"
  "Perception": !!int "4"
"damage_immunities": "poison, psychic"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 14"
"languages": "Common"
"cr": "1/2"
"traits":
- "desc": "The clockwork watchman doesn't require air, food, drink, or sleep."
  "name": "Construct Nature"
- "desc": "The clockwork watchman is immune to any spell or effect that would alter\
    \ its form."
  "name": "Immutable Form"
- "desc": "The clockwork watchman has advantage on saving throws against spells and\
    \ other magical effects."
  "name": "Magic Resistance"
"actions":
- "desc": "Melee Weapon Attack: +4 to hit, reach 10 ft., one target. Hit: 7\
    \ (1d10 + 2) slashing damage."
  "name": "Halberd"
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6\
    \ + 2) bludgeoning damage."
  "name": "Slam"
- "desc": "Ranged Weapon Attack: +3 to hit, range 10/20 ft., one target. Hit:\
    \ If the target is a Large or smaller creature, it is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained).\
    \ A mechanism within the clockwork watchman's chest can fire a net with a 20-foot\
    \ trailing cable anchored within the watchman's chest. A creature, including the\
    \ [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ creature, can take its action to free the [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ creature by succeeding on a DC 10 Strength check. Alternatively, dealing 5 slashing\
    \ damage to the net (AC 10) frees the creature."
  "name": "Net Cannon (4/Day)"
"bonus_actions":
- "desc": "The clockwork watchman pulls a creature [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ by its net up to 15 feet straight toward it."
  "name": "Reel"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/construct/token/clockwork-watchman-tob1-2023.webp"
```
^statblock

## Environment

urban