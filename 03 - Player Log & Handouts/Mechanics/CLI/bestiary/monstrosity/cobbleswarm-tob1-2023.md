---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Cobbleswarm"]
---
# [Cobbleswarm](03 - Player Log & Handouts\Mechanics\CLI\bestiary\monstrosity/cobbleswarm-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 67*  

*The paving stones underfoot suddenly lurch and tumble over one another. Thousands of tiny limbs, pincers, and stingers break from the stony surface and frantically scuttle forward.*

A cobbleswarm is made up of tiny, crablike creatures with smooth, stony shells. Individually they are referred to as cobbles. The creatures vary in size, shape, and color, but all have six segmented legs, a whiplike stinger, and a single eye.

## Paving Stone Mimics

When the eye is closed and the limbs are pulled under the shell, cobbles are nearly indistinguishable from lifeless paving stones. Victims of cobbleswarms are caught unaware when the floor beneath them suddenly writhes and shifts, and dozens of eyes appear where there should be none.

## Trap Affinity

Cobbleswarms have a rudimentary understanding of traps. They often hide in places where their Shift and Tumble ability can slide intruders into pits or across trapped areas. Kobold tribes prize them for this reason.

```statblock
"name": "Cobbleswarm (ToB1-2023)"
"size": "Medium"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "36"
"hit_dice": "8d8"
"stats":
- !!int "12"
- !!int "11"
- !!int "11"
- !!int "5"
- !!int "12"
- !!int "5"
"speed": "30 ft."
"damage_resistances": "bludgeoning, piercing, slashing"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
  \ [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
  \ [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)"
"senses": "passive Perception 11"
"languages": ""
"cr": "2"
"traits":
- "desc": "While the cobbleswarm remains motionless, it is indistinguishable from\
    \ normal stones."
  "name": "False Appearance"
- "desc": "Whenever the cobbleswarm moves into a creature's space or starts its turn\
    \ in another creature's space, the creature must succeed on a DC 13 Dexterity\
    \ saving throw or fall [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone).\
    \ A [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)\
    \ creature must succeed on a DC 13 Dexterity ([Acrobatics](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Acrobatics))\
    \ check to stand up in a space occupied by the swarm."
  "name": "Shifting Floor"
- "desc": "The cobbleswarm can occupy another creature's space and vice versa, and\
    \ the swarm can move through any opening large enough for a Tiny stone. The swarm\
    \ can't regain hp or gain temporary hp."
  "name": "Swarm"
"actions":
- "desc": "Melee Weapon Attack: +3 to hit, reach 0 ft., one target in the swarm's\
    \ space. Hit: 15 (6d4) piercing damage, or 7 (3d4) piercing damage if the\
    \ swarm has half its hp or fewer."
  "name": "Stings"
"bonus_actions":
- "desc": "The cobbleswarm pushes a [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)\
    \ creature in its space up to 5 feet away from it."
  "name": "Shift and Tumble"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/monstrosity/token/cobbleswarm-tob1-2023.webp"
```
^statblock

## Environment

underdark, urban