---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1-4
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/humanoid/erina
statblock: inline
aliases: ["Erina"]
---
# [Erina](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/erina-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 166*  

*This small humanoid has a slightly pointed face with bright, brown eyes and a black, snout-like nose. Its skin is covered in short, tan fur, and its head, shoulders, and back have smoothed-down quills.*

Erinas, or hedgehog folk, are a small, communal people.

## Burrowed Villages

Natural diggers at heart, erinas live in shallow networks of tunnels and chambers they excavate themselves. Enemies who attack the peaceful erinas become confused and lost in the mazelike tunnels. On their own ground, the erinas can easily evade, outmaneuver, or surround invaders. They lure intruders into choke points where the enemy can be delayed while noncombatants and valuables are hustled to safety through other tunnels. Such choke points are often protected or held by erina defenders, the largest and hardiest of their kind.

## Scroungers and Gatherers

Erinas are naturally curious. They tend to explore an area by tunneling beneath it and popping up at interesting points. They dislike farming and live mainly on the bounty of the land surrounding their homes. In cities, they subsist on what they can find, and they have a knack for finding whatever they need.

```statblock
"name": "Erina (ToB1-2023)"
"size": "Small"
"type": "humanoid"
"subtype": "erina"
"alignment": "Neutral"
"ac": !!int "12"
"ac_class": "[leather armor](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/leather-armor.md)"
"hp": !!int "22"
"hit_dice": "4d6 + 8"
"stats":
- !!int "9"
- !!int "12"
- !!int "14"
- !!int "13"
- !!int "10"
- !!int "11"
"speed": "20 ft., burrow 20 ft."
"damage_resistances": "poison"
"senses": "darkvision 60 ft., passive Perception 10"
"languages": "Common, Erina"
"cr": "1/4"
"traits":
- "desc": "The erina has advantage on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on smell."
  "name": "Keen Smell"
- "desc": "The erina has advantage on saving throws against poison."
  "name": "Hardy"
- "desc": "A creature that touches the erina or hits it with a melee attack while\
    \ within 5 feet of it takes 2 (1d4) piercing damage. In addition, a creature\
    \ [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ by or grappling the erina takes 2 (1d4) piercing damage at the start of the\
    \ erina's turn."
  "name": "Spines"
"actions":
- "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4\
    \ + 1) slashing damage"
  "name": "Dagger"
- "desc": "Ranged Weapon Attack: +3 to hit, range 30/120 ft., one target. Hit:\
    \ 3 (1d4 + 1) bludgeoning damage."
  "name": "Sling"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/erina-tob1-2023.webp"
```
^statblock

## Environment

forest, grassland