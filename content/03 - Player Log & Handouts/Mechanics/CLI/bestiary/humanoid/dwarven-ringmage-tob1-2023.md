---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/environment/arctic
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/dwarf
statblock: inline
aliases: ["Dwarven Ringmage"]
---
# [Dwarven Ringmage](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/dwarven-ringmage-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 409*  

Curves are seldom seen in the stacked blocks and precise geometric forms of dwarven architecture. Devoid of angles and planes with no beginning and no end, circles are a mystery and hold power. Dwarven ringmages are those dwarves who have mastered the art of tapping into that power, imbuing it into metal rings and their spellcasting. Rings and circles are sacred to them, and they read omens in the cycle of seasons, the shape of flowers, and in a storm's first rain drops.

```statblock
"name": "Dwarven Ringmage (ToB1-2023)"
"size": "Medium"
"type": "humanoid"
"subtype": "dwarf"
"alignment": "Any alignment"
"ac": !!int "16"
"ac_class": "[breastplate](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/breastplate.md)"
"hp": !!int "136"
"hit_dice": "21d8 + 42"
"stats":
- !!int "10"
- !!int "14"
- !!int "15"
- !!int "18"
- !!int "12"
- !!int "9"
"speed": "30 ft."
"saves":
  "Wisdom": !!int "4"
  "Intelligence": !!int "7"
  "Constitution": !!int "5"
"skillsaves":
  "History": !!int "7"
  "Arcana": !!int "7"
"damage_resistances": "poison"
"senses": "darkvision 60 ft., passive Perception 11"
"languages": "Common, Dwarvish"
"cr": "7"
"traits":
- "desc": "The dwarven ringmage casts one of the following spells, requiring no material\
    \ components and using Intelligence as the spellcasting ability (spell save DC\
    \ 15):\n\nAt will: [color spray](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/color-spray.md),\
    \ [mage hand](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/mage-hand.md),\
    \ [true strike](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/true-strike.md)\n\
    \n1/day each: [greater invisibility](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/greater-invisibility.md),\
    \ [wall of stone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/wall-of-stone.md)\n\
    \n3/day each: [expeditious retreat](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/expeditious-retreat.md),\
    \ [fly](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/fly.md), [haste](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/haste.md)"
  "name": "Spellcasting"
- "desc": "The dwarven ringmage has advantage on saving throws against poison."
  "name": "Dwarven Resilience"
"actions":
- "desc": "The dwarven ringmage can use its Ring Magic. It then makes three Ring Staff\
    \ attacks. It can replace one attack with a use of Spellcasting."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d6\
    \ + 2) bludgeoning damage plus 10 (3d6) acid, cold, fire, lightning, or thunder\
    \ damage (the ringmage's choice)."
  "name": "Ring Staff"
- "desc": "The dwarven ringmage draws circles of magic in the air and sends them toward\
    \ one creature it can see within 30 feet of it, causing one of the following effects:\n\
    \n- Rings of Binding. The target must succeed on a DC 15 Strength saving throw\
    \ or be [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ by magical rings until the end of its next turn.  \n- Rings of Bravery.\
    \ The target can't be [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ and has advantage on melee weapon attack rolls until the end of its next turn.\
    \  \n- Rings of Protection. The target has a +2 bonus to its Armor Class until\
    \ the end of its next turn.  \n- Rings of Retribution. When any creature hits\
    \ the target before the start of the ringmage's next turn, the creature takes\
    \ 4 (1d8) acid, cold, fire, lightning, or thunder damage (the ringmage's choice).\
    \  "
  "name": "Ring Magic"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/dwarven-ringmage-tob1-2023.webp"
```
^statblock

## Environment

arctic, urban