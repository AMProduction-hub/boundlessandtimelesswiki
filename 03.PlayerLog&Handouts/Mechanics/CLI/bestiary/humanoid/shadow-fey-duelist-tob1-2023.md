---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/elf
statblock: inline
aliases: ["Shadow Fey Duelist"]
---
# [Shadow Fey Duelist](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/shadow-fey-duelist-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 159*  

*The pale-skinned elf wears a gleaming breastplate and tight-fitting clothing. He moves like the wind, evading blows with effortless skill. When he stops and smiles, his blade is slick with crimson*.

Shadow fey duelists are elite warriors, often of noble lineage. Swift and sure beyond compare, duelists are often taller and more wiry than others of their kind. Their armor, clothing, and weapons are of exquisite make, fashioned from only the finest materials, as befits their station.

## Deadly Nobles

A nobleman or woman of the shadow fey is not to be taken lightly—many courtiers or politicians are deadly with their slim blades, and they are known to distill virulent poisons. Often a skilled duelist serves as a champion for her liege, standing in the noble's stead in challenges or serving as an elite bodyguard.

```statblock
"name": "Shadow Fey Duelist (ToB1-2023)"
"size": "Medium"
"type": "humanoid"
"subtype": "elf"
"alignment": "Lawful Evil"
"ac": !!int "17"
"ac_class": "[studded leather](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/studded-leather-armor.md)"
"hp": !!int "117"
"hit_dice": "18d8 + 36"
"stats":
- !!int "13"
- !!int "20"
- !!int "14"
- !!int "13"
- !!int "12"
- !!int "16"
"speed": "30 ft."
"saves":
  "Charisma": !!int "6"
  "Dexterity": !!int "8"
  "Constitution": !!int "5"
"skillsaves":
  "Deception": !!int "6"
  "Stealth": !!int "8"
  "Perception": !!int "4"
  "Acrobatics": !!int "8"
"senses": "darkvision 60 ft., passive Perception 14"
"languages": "Common, Elvish, Umbral"
"cr": "6"
"traits":
- "desc": "Opportunity attacks made against the duelist have disadvantage. If the\
    \ duelist is [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)\
    \ at the start of its turn, it can immediately stand without costing movement."
  "name": "Duelist's Mobility"
- "desc": "The shadow fey has advantage on saving throws against being [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
    \ and magic can't put it to sleep."
  "name": "Fey Ancestry"
- "desc": "While in sunlight, the shadow fey has disadvantage on attack rolls, as\
    \ well as on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on sight."
  "name": "Sunlight Sensitivity"
"actions":
- "desc": "The shadow fey duelist makes two Rapier attacks and one Dagger attack."
  "name": "Multiattack"
- "desc": "Melee or Ranged Weapon Attack: +8 to hit, reach 5 ft. or range 20/60\
    \ ft., one target. Hit: 7 (1d4 + 5) piercing damage plus 14 (4d6) poison\
    \ damage, and if the target is a creature, it must succeed on a DC 14 Constitution\
    \ saving throw or become [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 minute. A [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Dagger"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 9 (1d8\
    \ + 5) piercing damage."
  "name": "Rapier"
"bonus_actions":
- "desc": "While in shadows, dim light, or darkness, the shadow fey disappears into\
    \ the darkness and reappears in an unoccupied space it can see within 30 feet.\
    \ A tendril of inky smoke appears at the origin and destination when it uses this\
    \ bonus action."
  "name": "Shadow Traveler (3/Day)"
"reactions":
- "desc": "The shadow fey duelist adds 3 to its AC against one melee attack that would\
    \ hit it. To do so, the duelist must see the attacker and be wielding a melee\
    \ weapon."
  "name": "Parry"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/shadow-fey-duelist-tob1-2023.webp"
```
^statblock

## Environment

any, urban