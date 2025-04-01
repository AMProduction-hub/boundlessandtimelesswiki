---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/22
- ttrpg-cli/monster/environment/arctic
- ttrpg-cli/monster/size/gargantuan
- ttrpg-cli/monster/type/giant
statblock: inline
aliases: ["Jotun"]
---
# [Jotun](03 - Player Log & Handouts\Mechanics\CLI\bestiary\giant/jotun-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 209*  

*The earth shudders with every footfall of this massive giant.*

## Foes of the Gods

Tall enough to look a titan in the eye and strong enough to wrestle a dragon, jotun giants are the lords of giantkind and the immortal enemies of the gods. Their enormous halls are carved in mountains and glaciers throughout the north. As foes of the northern gods, jotun giants plot to regain their former status as lords of creation. Many know ancient secrets and snippets of antediluvian arcane lore, and the most powerful among them straddle the line between mortal and demigod.

## Contests and Challenges

Like many giants, jotun enjoy a challenge. Only the mightiest heroes can challenge a jotun's might in physical combat, and most resort to cunning or trickery to defeat a jotun. However, jotun giants are no fools and catch on to trickery quickly.

```statblock
"name": "Jotun (ToB1-2023)"
"size": "Gargantuan"
"type": "giant"
"alignment": "Chaotic Neutral"
"ac": !!int "20"
"ac_class": "natural armor"
"hp": !!int "370"
"hit_dice": "20d20 + 160"
"stats":
- !!int "30"
- !!int "8"
- !!int "26"
- !!int "18"
- !!int "20"
- !!int "14"
"speed": "60 ft."
"saves":
  "Charisma": !!int "9"
  "Wisdom": !!int "12"
  "Constitution": !!int "15"
"skillsaves":
  "Nature": !!int "11"
  "Stealth": !!int "6"
  "History": !!int "11"
  "Arcana": !!int "11"
"damage_immunities": "cold; bludgeoning, piercing, slashing from nonmagical attacks"
"senses": "darkvision 120 ft., passive Perception 15"
"languages": "Common, Giant"
"cr": "22"
"traits":
- "desc": "The jotun casts one of the following spells, requiring no material components\
    \ and using Wisdom as the spellcasting ability (spell save DC 20):\n\nAt will:\
    \ [earthquake](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/earthquake.md),\
    \ [speak with animals](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/speak-with-animals.md)\n\
    \n1/day: [divination](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/divination.md)\n\
    \n3/day: [bestow curse](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/bestow-curse.md),\
    \ [gust of wind](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/gust-of-wind.md)"
  "name": "Spellcasting"
- "desc": "The jotun's ability scores and hp maximum can't be reduced except by means\
    \ of a [wish](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/wish.md)\
    \ spell."
  "name": "Demigod's Vitality"
- "desc": "The jotun's weapon attacks are magical. When the jotun hits with any weapon,\
    \ the weapon deals an extra 6d8 cold damage (included in the attack)."
  "name": "Icy Weapons"
- "desc": "The jotun has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "The jotun is immune to any spell or effect that would force it to leave\
    \ the Material Plane, unless the jotun wants to leave. It has disadvantage on\
    \ saving throws against effects that would return it to the Material Plane from\
    \ another plane of existence."
  "name": "Material Bound"
- "desc": "While the jotun remains motionless in nonmagical, natural terrain, it has\
    \ advantage on Dexterity ([Stealth](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Stealth))\
    \ checks."
  "name": "Too Big to Notice"
"actions":
- "desc": "The jotun can use its Frightful Presence. It then makes three Greatclub\
    \ or Rock attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +17 to hit, reach 15 ft., one target. Hit: 28\
    \ (4d8 + 10) bludgeoning damage plus 27 (6d8) cold damage."
  "name": "Greatclub"
- "desc": "Ranged Weapon Attack: +17 to hit, range 60/240 ft., one target. Hit:\
    \ 32 (4d10 + 10) bludgeoning damage plus 27 (6d8) cold damage."
  "name": "Rock"
- "desc": "Each creature of the jotun's choice within 120 feet of the jotun and aware\
    \ of it must succeed on a DC 20 Wisdom saving throw or become [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ for 1 minute. A creature can repeat the saving throw at the end of each of its\
    \ turns, ending the effect on itself on a success. If a creature's saving throw\
    \ is successful or the effect ends for it, the creature is immune to the jotun's\
    \ Frightful Presence for the next 24 hours."
  "name": "Frightful Presence"
- "desc": "The jotun swings its ice-coated greatclub in a wide arc. Each creature\
    \ within 20 feet of the jotun must make a DC 23 Dexterity saving throw. On a failure,\
    \ a creature takes 36 (8d8) bludgeoning damage and 54 (12d8) cold damage and\
    \ is pushed up to 15 feet away from the jotun and knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone).\
    \ On a success, a creature takes half the damage and isn't pushed or knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Icy Sweep (Recharge 5-6)"
"reactions":
- "desc": "If a rock or similar object is hurled at the jotun, the jotun can, with\
    \ a successful DC 10 Dexterity saving throw, catch the missile and take no bludgeoning\
    \ damage from it."
  "name": "Rock Catching"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/giant/token/jotun-tob1-2023.webp"
```
^statblock

## Environment

arctic