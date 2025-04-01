---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/humanoid/kobold
statblock: inline
aliases: ["Kobold Chieftain"]
---
# [Kobold Chieftain](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/kobold-chieftain-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 245*  

*This small, draconic humanoid struts as though it were ten feet tall. It wears the gilded skull of a small dragon as a helmet, and its beady eyes gleam out through the skull's sockets. It hefts its spear and shield and lets out a blood-curdling shriek, signaling the attack*.

While most kobolds are scuttling scavengers or pathetic sycophants, a few carry a spark of draconic nobility that can't be ignored. These few forge their tribes into forces to be reckoned with, rising to the rank of chieftain. A kobold chieftain stands proud, clad in war gear of fine quality and good repair. Their weapons are tended by the tribe's tinkerers, particularly evident in their springspike shields.

## Living Legend

A kobold chieftain is more than a leader, it is a symbol of the tribe's greatness. The strongest, most cunning, most ruthless of a kobold tribe embodies their connection to the revered dragons. When a chieftain sounds the call to battle, the kobolds meld into a fearless, deadly force.

```statblock
"name": "Kobold Chieftain (ToB1-2023)"
"size": "Small"
"type": "humanoid"
"subtype": "kobold"
"alignment": "Lawful Evil"
"ac": !!int "16"
"ac_class": "[studded leather](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/studded-leather-armor.md),\
  \ [shield](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/shield.md)"
"hp": !!int "110"
"hit_dice": "20d6 + 40"
"stats":
- !!int "18"
- !!int "14"
- !!int "14"
- !!int "11"
- !!int "13"
- !!int "14"
"speed": "30 ft."
"saves":
  "Charisma": !!int "5"
  "Dexterity": !!int "5"
"skillsaves":
  "Intimidation": !!int "6"
  "Stealth": !!int "4"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)"
"senses": "darkvision 60 ft., passive Perception 11"
"languages": "Common, Draconic"
"cr": "5"
"traits":
- "desc": "A melee weapon deals one extra die of its damage when the chieftain hits\
    \ with it (included in the attack)."
  "name": "Brute"
- "desc": "Dragons and kobolds within 30 feet of the chieftain can't be [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ or [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)."
  "name": "Chieftain's Presence"
- "desc": "The kobold chieftain has advantage on attack rolls against a creature if\
    \ at least one of the chieftain's allies is within 5 feet of the creature and\
    \ the ally isn't [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)."
  "name": "Pack Tactics"
- "desc": "While in sunlight, the kobold chieftain has disadvantage on attack rolls,\
    \ as well as on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on sight."
  "name": "Sunlight Sensitivity"
"actions":
- "desc": "The kobold makes three Spear or Shortbow attacks."
  "name": "Multiattack"
- "desc": "Melee or Ranged Weapon Attack: +6 to hit, reach 5 ft. or range 20/60\
    \ ft., one target. Hit: 11 (2d6 + 4) piercing damage, or 13 (2d8 + 4) piercing\
    \ damage if used with two hands to make a melee attack."
  "name": "Spear"
- "desc": "Ranged Weapon Attack: +4 to hit, range 80/320 ft., one target. Hit:\
    \ 5 (1d6 + 2) piercing damage plus 7 (2d6) poison damage, and the target must\
    \ succeed on a DC 12 Constitution saving throw or be [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 minute. A [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Shortbow"
- "desc": "The kobold chieftain shrieks a draconic battle cry. Each creature that\
    \ isn't a dragonborn or kobold within 30 feet of the chieftain must succeed on\
    \ a DC 14 Wisdom saving throw or be [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ for 1 minute. A [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success.\n\nEach dragonborn and kobold within 30 feet\
    \ of the chieftain is inspired for 1 minute. Whenever an inspired creature makes\
    \ an attack roll or saving throw, the creature can roll a d4 and add the number\
    \ rolled to the attack roll or saving throw."
  "name": "Inspiring Shriek (Recharge after Short or Long Rest)"
"reactions":
- "desc": "When the kobold chieftain is wielding its shield and is hit by a melee\
    \ attack within 5 feet of it, the chieftain can fire one of its shield spikes\
    \ at the attacker. The attacker takes 5 (2d4) piercing damage."
  "name": "Springspike Shield"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/kobold-chieftain-tob1-2023.webp"
```
^statblock

## Environment

underdark, urban