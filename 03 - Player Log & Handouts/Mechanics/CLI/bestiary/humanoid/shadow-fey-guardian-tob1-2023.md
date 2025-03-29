---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/humanoid/elf
statblock: inline
aliases: ["Shadow Fey Guardian"]
---
# [Shadow Fey Guardian](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/shadow-fey-guardian-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 162*  

*A hulking brute, this elvish figure towers over his fellows and wields massive weapons. Patches of his body are swallowed by inky blackness that writhes and crawls, and his eyes are hollow black pits.*

Shadow fey guardians are massive creatures trained and bred for battle. They appear as massive versions of shadow fey, but the stuff of shadow corrupts them even more than their brethren, expanding their size and power to an ogreish strength. Patches of shadow swallow parts of their body and crawl about, revealing and obscuring more by inches at a time. They stand nearly 10 feet tall and weigh over 700 pounds.

## Loyal Protectors

Guardians are fanatically loyal to their superiors. Employed as house guards or even personal bodyguards for important shadow fey, guardians are unshakable in their duty. The shadow reaches into their minds and souls, so that not even powerful magic can bend their hearts or break their resolve. Guardians are independent thinkers, but they discharge their duty with single-minded dedication.

```statblock
"name": "Shadow Fey Guardian (ToB1-2023)"
"size": "Large"
"type": "humanoid"
"subtype": "elf"
"alignment": "Neutral Evil"
"ac": !!int "15"
"ac_class": "[chain shirt](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/chain-shirt.md)"
"hp": !!int "110"
"hit_dice": "13d10 + 39"
"stats":
- !!int "18"
- !!int "14"
- !!int "16"
- !!int "6"
- !!int "14"
- !!int "8"
"speed": "30 ft."
"saves":
  "Strength": !!int "6"
  "Constitution": !!int "5"
"skillsaves":
  "Athletics": !!int "6"
  "Perception": !!int "4"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)"
"senses": "darkvision 60 ft., passive Perception 14"
"languages": "Common, Elvish, Umbral"
"cr": "4"
"traits":
- "desc": "The shadow fey guardian has advantage on saving throws against being [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
    \ and magic can't put it to sleep."
  "name": "Fey Ancestry"
- "desc": "The guardian has advantage on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks, and magical darkness doesn't impede the guardian's darkvision."
  "name": "Shadow's Vigil"
- "desc": "While in sunlight, the shadow fey has disadvantage on attack rolls, as\
    \ well as on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on sight."
  "name": "Sunlight Sensitivity"
"actions":
- "desc": "The shadow fey guardian makes two Pike or Javelin attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 15\
    \ (2d10 + 4) piercing damage."
  "name": "Pike"
- "desc": "Melee or Ranged Weapon Attack: +6 to hit, reach 5 ft. or range 30/120\
    \ ft., one target. Hit: 11 (2d6 + 4) piercing damage."
  "name": "Javelin"
"bonus_actions":
- "desc": "While in shadows, dim light, or darkness, the shadow fey disappears into\
    \ the darkness and reappears in an unoccupied space it can see within 30 feet.\
    \ A tendril of inky smoke appears at the origin and destination when it uses this\
    \ bonus action."
  "name": "Shadow Traveler (2/Day)"
"reactions":
- "desc": "When a friendly creature the shadow fey guardian can see within 5 feet\
    \ of it is the target of an attack, the guardian can impose disadvantage on the\
    \ attack roll. To do so, the guardian must see the attacker and be wielding a\
    \ melee weapon."
  "name": "Protective Interference"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/shadow-fey-guardian-tob1-2023.webp"
```
^statblock

## Environment

any, urban