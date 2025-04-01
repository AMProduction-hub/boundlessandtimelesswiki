---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/coastal
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/dragon
statblock: inline
aliases: ["Drakon"]
---
# [Drakon](03 - Player Log & Handouts\Mechanics\CLI\bestiary\dragon/drakon-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 147*  

*These winged snakes are coastal beasts and sometimes confused with true dragons or wyverns. They are neither, but quite deadly in their own right.*

## Searing Acid and Dissolving Gaze

The gaze of these winged snakes can paralyze and dissolve their victims. Drakon fangs do not deliver venom; volatile acid constantly burbles up from a drakon's stomach and enhances its attacks. A caustic drool clings to creatures they bite, and drakons can also belch clouds of searing vapor. Their lairs reek with acidic vapors and droplets of searing liquid.

## Coastal Beasts

Drakons lair along warm, largely uninhabited coasts, where they explore the shores and the coastal shelf, spending as much time above the waves as under them. Fortunately, they rarely travel far inland.

```statblock
"name": "Drakon (ToB1-2023)"
"size": "Large"
"type": "dragon"
"alignment": "Unaligned"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "105"
"hit_dice": "14d10 + 28"
"stats":
- !!int "14"
- !!int "19"
- !!int "15"
- !!int "2"
- !!int "12"
- !!int "10"
"speed": "30 ft., fly 60 ft., swim 40 ft."
"skillsaves":
  "Stealth": !!int "7"
  "Perception": !!int "4"
"damage_resistances": "acid"
"condition_immunities": "[paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)"
"senses": "darkvision 60 ft., passive Perception 14"
"languages": ""
"cr": "5"
"traits":
- "desc": "The drakon can breathe air and water."
  "name": "Amphibious"
- "desc": "When a creature that can see the drakon's eyes starts its turn within 30\
    \ feet of the drakon, the drakon can force it to make a DC 13 Constitution saving\
    \ throw if the drakon isn't [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ and can see the creature. On a failed save, the creature takes 3 (1d6) acid\
    \ damage, its hp maximum is reduced by an amount equal to the acid damage it takes,\
    \ and it is [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ until the start of its next turn. This reduction lasts until the creature finishes\
    \ a long rest. The creature dies if this effect reduces its hp maximum to 0.\n\
    \nUnless surprised, a creature can avert its eyes to avoid the saving throw at\
    \ the start of its turn. If the creature does so, it can't see the drakon until\
    \ the start of its next turn, when it can avert its eyes again. If the creature\
    \ looks at the drakon in the meantime, it must immediately make the save."
  "name": "Dissolving Gaze"
"actions":
- "desc": "The drakon makes one Bite attack and one Tail attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11\
    \ (2d6 + 4) piercing damage plus 10 (4d4) acid damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 8\
    \ (1d8 + 4) bludgeoning damage."
  "name": "Tail"
- "desc": "The drakon exhales acidic vapors in a 15-foot cone. Each creature in that\
    \ area must make a DC 13 Constitution saving throw, taking 28 (8d6) acid damage\
    \ on a failed save, or half as much damage on a successful one."
  "name": "Acid Breath (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/dragon/token/drakon-tob1-2023.webp"
```
^statblock

## Environment

coastal