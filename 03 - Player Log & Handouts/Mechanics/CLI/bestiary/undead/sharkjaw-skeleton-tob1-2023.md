---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/environment/coastal
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Sharkjaw Skeleton"]
---
# [Sharkjaw Skeleton](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/sharkjaw-skeleton-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 329*  

*A skeletal humanoid made entirely of shark's jaws steps out from the water, dripping strands of seaweed.*

Made from numerous, interlocking shark's jaws, these horrors are animated through foul magic into a large, vaguely humanoid shape. Sahuagin priests animate them to guard sepulchers of bones. These sharkjaw skeletons lie among great piles of bones, waiting to rise up and attack any uninvited souls who invade the sanctity of sahuagin holy sites. Others guard pirate treasures or ancient shipwrecks.

## Undead Automaton

Sharkjaw skeletons do nothing without orders from their creator, and they follow those instructions explicitly. A sharkjaw skeleton's creator can give it new commands while near the skeleton. Otherwise, a sharkjaw skeleton follows its last instructions to the best of its ability and to the exclusion of all else, though it fights back if attacked.

```statblock
"name": "Sharkjaw Skeleton (ToB1-2023)"
"size": "Large"
"type": "undead"
"alignment": "Lawful Evil"
"ac": !!int "13"
"ac_class": "natural armor"
"hp": !!int "45"
"hit_dice": "6d10 + 12"
"stats":
- !!int "16"
- !!int "10"
- !!int "15"
- !!int "6"
- !!int "8"
- !!int "4"
"speed": "30 ft., swim 30 ft."
"skillsaves":
  "Stealth": !!int "2"
  "Perception": !!int "1"
"damage_vulnerabilities": "bludgeoning"
"damage_immunities": "cold, poison"
"condition_immunities": "[exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "blindsight 30 ft., darkvision 60 ft., passive Perception 11"
"languages": "understands the languages of its creator but can't speak"
"cr": "1"
"traits":
- "desc": "The sharkjaw skeleton doesn't require air, food, drink, or sleep."
  "name": "Undead Nature"
"actions":
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10\
    \ (2d6 + 3) piercing damage. If the target is a Large or smaller creature, it\
    \ is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 13). The skeleton can grapple up to two targets at a time."
  "name": "Bite"
- "desc": "The sharkjaw skeleton devours a Medium or smaller creature [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ by it. The grapple ends, the devoured target is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ in the skeleton's many jaws, and the target takes 7 (2d6) piercing damage\
    \ at the start of each of the skeleton's turns. If the skeleton moves, the devoured\
    \ target moves with it. The skeleton can devour only one target at a time. A creature,\
    \ including the devoured target, can take its action to pry the devoured target\
    \ out of the skeleton's many jaws by succeeding on a DC 13 Strength check."
  "name": "Devouring Embrace"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/sharkjaw-skeleton-tob1-2023.webp"
```
^statblock

## Environment

coastal, underwater