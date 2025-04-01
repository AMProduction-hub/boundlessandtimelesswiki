---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/elf
statblock: inline
aliases: ["Shadow Fey Forest Hunter"]
---
# [Shadow Fey Forest Hunter](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/shadow-fey-forest-hunter-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 161*  

*The shadows flicker slightly, the only warning before a hail of arrows erupts from the concealed elf hidden in the gloom.*

Dressed in exquisitely wrought mail and leather jerkins, forest hunters are even more lithe and graceful than most shadow fey.

## Shadow Stalkers

Forest hunters roam the deep woods connected to the Plane of Shadow, as well as the forests' dark reflections within the Plane of Shadow. They are skilled trackers and stalkers, hunting animals and more dangerous game. Many forest hunters serve in the Wild Hunt. A hunter that has at one time ridden at the Lord of the Hunt 's side is afforded great respect, even fear, because of the common belief that such a hunter can implore the Lord of the Hunt to notice an enemy.

```statblock
"name": "Shadow Fey Forest Hunter (ToB1-2023)"
"size": "Medium"
"type": "humanoid"
"subtype": "elf"
"alignment": "Lawful Evil"
"ac": !!int "15"
"ac_class": "[chain shirt](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/chain-shirt.md)"
"hp": !!int "104"
"hit_dice": "19d8 + 19"
"stats":
- !!int "12"
- !!int "18"
- !!int "12"
- !!int "11"
- !!int "12"
- !!int "16"
"speed": "30 ft."
"saves":
  "Charisma": !!int "6"
  "Dexterity": !!int "7"
  "Constitution": !!int "4"
"skillsaves":
  "Stealth": !!int "10"
  "Perception": !!int "4"
  "Survival": !!int "4"
"senses": "darkvision 60 ft., passive Perception 14"
"languages": "Common, Elvish, Umbral"
"cr": "5"
"traits":
- "desc": "If the forest hunter is subjected to an effect that allows it to make a\
    \ Dexterity saving throw to take only half the damage, the hunter instead takes\
    \ no damage if it succeeds on the saving throw, and only half the damage if it\
    \ fails."
  "name": "Evasion"
- "desc": "The shadow fey has advantage on saving throws against being [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
    \ and magic can't put it to sleep."
  "name": "Fey Ancestry"
- "desc": "The forest hunter has advantage on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ and Wisdom ([Survival](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Survival))\
    \ checks to find and track Beasts and Humanoids."
  "name": "Forest and Urban Hunter"
- "desc": "If the forest hunter moves at least 10 feet straight toward a target after\
    \ hitting the target with a Longbow attack, the forest hunter can make one Dagger\
    \ attack against the target as a bonus action."
  "name": "Charging Archer"
- "desc": "While in sunlight, the shadow fey has disadvantage on attack rolls, as\
    \ well as on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on sight."
  "name": "Sunlight Sensitivity"
"actions":
- "desc": "The shadow fey makes two Dagger or Longbow attacks."
  "name": "Multiattack"
- "desc": "Melee or Ranged Weapon Attack: +7 to hit, reach 5 ft., one target.\
    \ Hit: 6 (1d4 + 4) piercing damage plus 10 (3d6) poison damage."
  "name": "Dagger"
- "desc": "Ranged Weapon Attack: +7 to hit, range 150/600 ft., one target. Hit:\
    \ 8 (1d8 + 4) piercing damage plus 10 (3d6) poison damage."
  "name": "Longbow"
"bonus_actions":
- "desc": "While in shadows, dim light, or darkness, the shadow fey disappears into\
    \ the darkness and reappears in an unoccupied space it can see within 30 feet.\
    \ A tendril of inky smoke appears at the origin and destination when it uses this\
    \ bonus action."
  "name": "Shadow Traveler (3/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/shadow-fey-forest-hunter-tob1-2023.webp"
```
^statblock

## Environment

any, forest