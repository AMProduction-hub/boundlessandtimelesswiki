---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Deathwisp"]
---
# [Deathwisp](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/deathwisp-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 71*  

*A shadowy figure flickers in and out of view. Its indistinct shape betrays a sylvan ancestry, and its eyes are malevolent blue points of light.*

## Fey Undead

A deathwisp is a wraith-like spirit created in the Shadow Realm from the violent death of a shadow fey or evil fey.

## Rift Walkers

Many deathwisps remain among the shadows, but a few enter the natural world through planar rifts and gates or by walking along the shadowy roads between the worlds. Retaining only a trace of their former personality and knowledge, their lost kindness has been replaced with malice.

## Devour Breath

A deathwisp feasts on the breath of living things, and it invariably seeks to devour animals and solitary, intelligent prey. It is quite intelligent and avoids fights against greater numbers.

```statblock
"name": "Deathwisp (ToB1-2023)"
"size": "Medium"
"type": "undead"
"alignment": "Neutral Evil"
"ac": !!int "15"
"hp": !!int "82"
"hit_dice": "11d8 + 33"
"stats":
- !!int "6"
- !!int "20"
- !!int "16"
- !!int "18"
- !!int "16"
- !!int "20"
"speed": "0 ft., fly 60 ft. (hover)"
"saves":
  "Dexterity": !!int "8"
  "Wisdom": !!int "6"
  "Constitution": !!int "6"
"skillsaves":
  "Stealth": !!int "8"
  "Perception": !!int "6"
"damage_resistances": "acid; cold; fire; lightning; thunder; bludgeoning, piercing,\
  \ slashing from nonmagical attacks that aren't silvered"
"damage_immunities": "necrotic, poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
  \ [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)"
"senses": "darkvision 60 ft., passive Perception 16"
"languages": "the languages it knew in life"
"cr": "7"
"traits":
- "desc": "The deathwisp flickers in and out of sight. Ranged weapon attacks against\
    \ it are made with disadvantage."
  "name": "Flicker"
- "desc": "The deathwisp can move through other creatures and objects as if they were\
    \ difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside\
    \ a solid object."
  "name": "Incorporeal Movement"
- "desc": "While in sunlight, the deathwisp has disadvantage on attack rolls, as well\
    \ as on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on sight."
  "name": "Sunlight Sensitivity"
- "desc": "The deathwisp doesn't require air, food, drink, or sleep."
  "name": "Undead Nature"
"actions":
- "desc": "The deathwisp makes two Ghostly Pike attacks, or it can make one Ghostly\
    \ Pike attack and one Life Drain attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 16\
    \ (2d10 + 5) force damage plus 9 (2d8) necrotic damage."
  "name": "Ghostly Pike"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 23\
    \ (4d8 + 5) necrotic damage. The target must succeed on a DC 15 Constitution\
    \ saving throw or its hp maximum is reduced by an amount equal to the damage taken.\
    \ This reduction lasts until the target finishes a long rest. The target dies\
    \ if this effect reduces its hp maximum to 0."
  "name": "Life Drain"
- "desc": "The deathwisp targets a Humanoid within 10 feet of it that has been dead\
    \ for no longer than 1 minute and died violently. The target's spirit rises as\
    \ a specter in the space of its corpse or in the nearest unoccupied space. This\
    \ specter is under the deathwisp's control. The deathwisp can have no more than\
    \ twelve specters under its control at one time."
  "name": "Create Specter"
"bonus_actions":
- "desc": "While in shadows, dim light, or darkness, the deathwisp disappears into\
    \ the darkness and reappears in an unoccupied space it can see within 30 feet.\
    \ A tendril of inky smoke appears at the origin and destination when it uses this\
    \ bonus action."
  "name": "Shadow Traveler (3/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/deathwisp-tob1-2023.webp"
```
^statblock

## Environment

planar