---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/elf
statblock: inline
aliases: ["Shadow Fey Enchantress"]
---
# [Shadow Fey Enchantress](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/shadow-fey-enchantress-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 160*  

*This ravishing shadow fey woman moves with alluring grace. Her voice rings like a bell, and in her hearing, worldly cares and sorrows melt away.*

Beyond even great physical beauty, the sheer presence of a shadow fey enchantress can lay the most stalwart foes low. Almost universally female, Enchantresses are beautiful beyond compare.

## Enchanting Shadows

Enchantresses are also powerful spellcasters who infuse their words and manner with the beguiling power of shadow to turn enemies against one another with a few words and a deadly smile. They augment the force of their minds with fey-wrought blades, infusing their weapons with power that shreds their victims' psyche as well as their flesh.

```statblock
"name": "Shadow Fey Enchantress (ToB1-2023)"
"size": "Medium"
"type": "humanoid"
"subtype": "elf"
"alignment": "Lawful Evil"
"ac": !!int "16"
"ac_class": "[breastplate](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/breastplate.md)"
"hp": !!int "123"
"hit_dice": "19d8 + 38"
"stats":
- !!int "10"
- !!int "15"
- !!int "14"
- !!int "12"
- !!int "17"
- !!int "18"
"speed": "30 ft."
"saves":
  "Charisma": !!int "7"
  "Dexterity": !!int "5"
  "Wisdom": !!int "6"
"skillsaves":
  "Deception": !!int "7"
  "Stealth": !!int "5"
  "Perception": !!int "6"
  "Arcana": !!int "4"
  "Persuasion": !!int "7"
"senses": "darkvision 60 ft., passive Perception 16"
"languages": "Common, Elvish, Umbral"
"cr": "7"
"traits":
- "desc": "The enchantress casts one of the following spells, requiring no material\
    \ components and using Charisma as the spellcasting ability (spell save DC 15):\n\
    \nAt will: [command](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/command.md),\
    \ [message](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/message.md)\n\
    \n1/day: [confusion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/confusion.md),\
    \ [dominate person](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dominate-person.md),\
    \ [greater invisibility](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/greater-invisibility.md),\
    \ [hold monster](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/hold-monster.md),\
    \ [phantasmal killer](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/phantasmal-killer.md)\n\
    \n3/day: [charm person](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/charm-person.md),\
    \ [enthrall](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/enthrall.md),\
    \ [fear](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/fear.md), [hold\
    \ person](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/hold-person.md),\
    \ [hypnotic pattern](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/hypnotic-pattern.md)"
  "name": "Spellcasting"
- "desc": "The enchantress has advantage on saving throws against being [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
    \ and magic can't put her to sleep."
  "name": "Fey Ancestry"
- "desc": "The enchantress's weapon attacks are magical. When she hits with any weapon,\
    \ the weapon deals an extra 4d6 psychic damage (included in the attack)."
  "name": "Phrenic Weapons"
- "desc": "While in sunlight, the shadow fey has disadvantage on attack rolls, as\
    \ well as on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on sight."
  "name": "Sunlight Sensitivity"
"actions":
- "desc": "The shadow fey enchantress makes two Rapier attacks. She can replace one\
    \ attack with a use of Spellcasting."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d8\
    \ + 2) piercing damage plus 14 (4d6) psychic damage."
  "name": "Rapier"
- "desc": "Ranged Spell Attack: +7 to hit, range 120 ft., one target. Hit: 11\
    \ (2d6 + 4) cold damage plus 9 (2d8) necrotic damage."
  "name": "Shadow Bolt"
- "desc": "The enchantress speaks sweet words to a creature she can see within 60\
    \ feet of her and that can hear her. The creature must succeed on a DC 15 Charisma\
    \ saving throw or be [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ for 1 minute. While [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ in this way, the creature has disadvantage on Wisdom and Charisma saving throws\
    \ against spells cast by the enchantress."
  "name": "Beguiling Whispers (Recharge 5-6)"
- "desc": "For 1 minute, the enchantress can utter a special command or warning whenever\
    \ a nonhostile creature that she can see within 30 feet of her makes an attack\
    \ roll or a saving throw. The creature can add a d4 to its roll, provided it\
    \ can hear and understand the enchantress. A creature can benefit from only one\
    \ Leadership die at a time. This effect ends if the enchantress is [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)."
  "name": "Leadership (Recharges after a Short or Long Rest)"
"bonus_actions":
- "desc": "While in shadows, dim light, or darkness, the shadow fey disappears into\
    \ the darkness and reappears in an unoccupied space it can see within 30 feet.\
    \ A tendril of inky smoke appears at the origin and destination when it uses this\
    \ bonus action."
  "name": "Shadow Traveler (3/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/shadow-fey-enchantress-tob1-2023.webp"
```
^statblock

## Environment

any, urban