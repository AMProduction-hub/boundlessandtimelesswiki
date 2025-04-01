---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/humanoid/erina
statblock: inline
aliases: ["Erina Defender"]
---
# [Erina Defender](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/erina-defender-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 166*  

*This small humanoid has a slightly pointed face with bright, brown eyes and a black, snout-like nose. Its skin is covered in short, tan fur, and its head, shoulders, and back have smoothed-down quills.*

Erinas, or hedgehog folk, are a small, communal people.

## Burrowed Villages

Natural diggers at heart, erinas live in shallow networks of tunnels and chambers they excavate themselves. Enemies who attack the peaceful erinas become confused and lost in the mazelike tunnels. On their own ground, the erinas can easily evade, outmaneuver, or surround invaders. They lure intruders into choke points where the enemy can be delayed while noncombatants and valuables are hustled to safety through other tunnels. Such choke points are often protected or held by erina defenders, the largest and hardiest of their kind.

## Scroungers and Gatherers

Erinas are naturally curious. They tend to explore an area by tunneling beneath it and popping up at interesting points. They dislike farming and live mainly on the bounty of the land surrounding their homes. In cities, they subsist on what they can find, and they have a knack for finding whatever they need.

```statblock
"name": "Erina Defender (ToB1-2023)"
"size": "Small"
"type": "humanoid"
"subtype": "erina"
"alignment": "Neutral"
"ac": !!int "15"
"ac_class": "[chain shirt](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/chain-shirt.md)"
"hp": !!int "44"
"hit_dice": "8d6 + 16"
"stats":
- !!int "11"
- !!int "14"
- !!int "14"
- !!int "13"
- !!int "12"
- !!int "11"
"speed": "20 ft., burrow 20 ft."
"skillsaves":
  "Athletics": !!int "4"
  "Perception": !!int "3"
"damage_resistances": "poison"
"senses": "darkvision 60 ft., passive Perception 13"
"languages": "Common, Erina"
"cr": "1"
"traits":
- "desc": "The erina has advantage on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on smell."
  "name": "Keen Smell"
- "desc": "The erina has advantage on saving throws against poison."
  "name": "Hardy"
- "desc": "A creature that touches the erina or hits it with a melee attack while\
    \ within 5 feet of it takes 5 (2d4) piercing damage. In addition, a creature\
    \ [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ by or grappling the erina takes 5 (2d4) piercing damage at the start of the\
    \ erina's turn."
  "name": "Spines"
"actions":
- "desc": "The erina defender makes two Shortsword or Shortbow attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6\
    \ + 2) piercing damage."
  "name": "Shortsword"
- "desc": "Ranged Weapon Attack: +4 to hit, range 80/320 ft., one target. Hit:\
    \ 5 (1d6 + 2) piercing damage."
  "name": "Shortbow"
"reactions":
- "desc": "When a friendly creature the erina defender can see within 5 feet of it\
    \ is the target of an attack, the defender can impose disadvantage on the attack\
    \ roll. To do so, the defender must see the attacker and be wielding a melee weapon."
  "name": "Protective Interference"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/erina-defender-tob1-2023.webp"
```
^statblock

## Environment

forest, grassland