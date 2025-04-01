---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/farmland
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/construct
statblock: inline
aliases: ["Gnarljak"]
---
# [Gnarljak](03 - Player Log & Handouts\Mechanics\CLI\bestiary\construct/gnarljak-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 212*  

*A bear trap springs to clacking life, ready to tear flesh.*

## Hopping Motion

All steel and springs, a gnarljak is easily mistaken for a simple bear trap when lying dormant. But once it starts hopping in pursuit of a target, it reveals its animated nature and its only motivation: destruction of living things.

## Endless Snapping

Gnarljaks are mindless. They do not grow tired. They exist only to pull creatures to the ground and chew through them, then turn around and chew through them again.

## Defensive Traps

Some try to use gnarljaks to guard treasures or booby-trap approaches to important locations, but their indiscriminate biting makes them quite dangerous to their owners as well. Certain monsters, such as redcaps and shadow fey, use gnarljaks with some regularity, and gnomes are very fond of making them part of a standard tunnel defense.

```statblock
"name": "Gnarljak (ToB1-2023)"
"size": "Small"
"type": "construct"
"alignment": "Unaligned"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "88"
"hit_dice": "16d6 + 32"
"stats":
- !!int "13"
- !!int "21"
- !!int "15"
- !!int "2"
- !!int "14"
- !!int "1"
"speed": "30 ft."
"saves":
  "Strength": !!int "4"
"skillsaves":
  "Stealth": !!int "8"
  "Perception": !!int "5"
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "poison, psychic"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "blindsight 60 ft. (blind beyond this radius), passive Perception 15"
"languages": ""
"cr": "6"
"traits":
- "desc": "The gnarljak doesn't require air, food, drink, or sleep."
  "name": "Construct Nature"
- "desc": "While the gnarljak remains motionless, it is indistinguishable from a normal\
    \ bear trap."
  "name": "False Appearance"
"actions":
- "desc": "The gnarljak makes one Gnawing Bite attack and two Chain Tail attacks,\
    \ or it makes three Chain Tail attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 14\
    \ (2d8 + 5) piercing damage, and the gnarljak attaches to the target. While\
    \ attached, the gnarljak can't make Gnawing Bite attacks, and at the start of\
    \ each of the gnarljak's turns, the target takes 14 (2d8 + 5) piercing damage.\n\
    \nThe attached gnarljak moves with the target whenever the target moves, requiring\
    \ none of the gnarljak's movement. It can detach itself by spending 5 feet of\
    \ its movement on its turn. A creature, including the target, can use its action\
    \ to detach the gnarljak by succeeding on a DC 16 Strength check."
  "name": "Gnawing Bite"
- "desc": "Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 12\
    \ (2d6 + 5) bludgeoning damage."
  "name": "Chain Tail"
"bonus_actions":
- "desc": "When within 10 feet of the ground, structure, wall, or other solid surface,\
    \ the gnarljak can secure its tail spike on a point in the surface within 10 feet\
    \ of it. While secured, the gnarljak can't be knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
    \ it can't move more than 10 feet from that point, and its Chain Tail attack's\
    \ reach is reduced to 5 feet. If the gnarljak is attached to a creature while\
    \ its tail is secured, the creature is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ until the gnarljak is no longer attached to it."
  "name": "Secure Tail"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/construct/token/gnarljak-tob1-2023.webp"
```
^statblock

## Environment

farmland, forest, urban