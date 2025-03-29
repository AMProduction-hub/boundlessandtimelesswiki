---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/dragon
statblock: inline
aliases: ["Elder Shadow Drake"]
---
# [Elder Shadow Drake](03 - Player Log & Handouts\Mechanics\CLI\bestiary\dragon/elder-shadow-drake-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 143*  

*A large dragon with black scales and shadowy wings emerges from the darkness. Its red eyes glare bright as coals, and it speaks in a deep monotone.*

## Solitary Lairs

They haunt dark and lonely places, such as deep caves, dense forests, shadowy ruins, and many wild locations in the Plane of Shadow. They are long-lived for drakes, often reaching 250 years of age, and mate rarely, abandoning their eggs shortly before hatching.

## Fade Into Shadows

An elder shadow drake naturally fades from view in areas of dim light or darkness, becoming invisible until it attacks or is bathed in sunlight.

```statblock
"name": "Elder Shadow Drake (ToB1-2023)"
"size": "Large"
"type": "dragon"
"alignment": "Chaotic Evil"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "114"
"hit_dice": "12d10 + 48"
"stats":
- !!int "22"
- !!int "13"
- !!int "18"
- !!int "8"
- !!int "9"
- !!int "13"
"speed": "20 ft., fly 60 ft."
"saves":
  "Charisma": !!int "4"
  "Dexterity": !!int "4"
  "Constitution": !!int "7"
"skillsaves":
  "Stealth": !!int "7"
  "Perception": !!int "5"
"damage_vulnerabilities": "radiant"
"damage_immunities": "cold"
"senses": "darkvision 120 ft., passive Perception 15"
"languages": "Common, Draconic, Umbral"
"cr": "7"
"traits":
- "desc": "The drake has advantage on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks made while in dim light or darkness, and magical darkness doesn't impede\
    \ the drake's darkvision."
  "name": "Shadow Sight"
"actions":
- "desc": "The elder shadow drake makes one Bite attack and two Tail Slap attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 17\
    \ (2d10 + 6) piercing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 15\
    \ (2d8 + 6) bludgeoning damage."
  "name": "Tail Slap"
- "desc": "The drake magically turns [invisible](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Invisible)\
    \ until it attacks, uses Shadow Step, or starts its turn in sunlight, or until\
    \ its [concentration](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Concentration)\
    \ ends (as if [concentrating](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Concentration)\
    \ on a spell). Any equipment the drake wears or carries is [invisible](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Invisible)\
    \ with it. The drake must be in dim light or darkness to use this action."
  "name": "Invisibility"
- "desc": "The elder shadow drake spits a ball of black liquid on a point the dragon\
    \ can see within 60 feet of it. The ball bursts into a 20-foot-radius sphere of\
    \ black mist centered on that point for 1 minute. Each creature in the mist when\
    \ it appears must make a DC 15 Constitution saving throw, taking 42 (12d6) cold\
    \ damage on a failed save, or half as much damage on a successful one. The mist\
    \ spreads around corners, and its area is magical darkness. No natural light can\
    \ illuminate the mist. If any of the mist overlaps with an area of light created\
    \ by a spell of 1st level or lower, the spell creating the light is dispelled."
  "name": "Stygian Breath (Recharge 5-6)"
"bonus_actions":
- "desc": "The drake teleports, along with any equipment it is wearing or carrying,\
    \ up to 60 feet to an unoccupied space it can see. The origin and destination\
    \ spaces must be in dim light or darkness."
  "name": "Shadow Step"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/dragon/token/elder-shadow-drake-tob1-2023.webp"
```
^statblock

## Environment

forest, underdark