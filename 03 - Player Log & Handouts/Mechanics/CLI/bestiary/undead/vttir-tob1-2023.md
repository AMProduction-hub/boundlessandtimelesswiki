---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Vættir"]
---
# [Vættir](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/vttir-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 378*  

*The creature's blue-black skin is stretched taut over its bones, and its lips are drawn back in a cruel grimace. It holds a bronze axe high over its head, and its eyes glow an icy blue.*

## Servants of the Land

Servants of the land, vættir haunt those who disrespect the wild or ancient laws and traditions. Regardless of where they're found, vættir always wear ancient mail and carry bronze axes.

## Jealous and Wrathful

A wrathful vættir rises from its burial mound when its grave goods are stolen or when it is disrespected. Vættir jealously guard both honor and treasures, and they may be relentless enemies over matters as small as an accidental word or a single coin.

## Dangerous Helpers

Vættirs will answer a summons for aid by descendants or nearby villages. Summoned vættir wander into longhouses or taverns and sit down beside those who call them, ready to serve. However, there's always a price, and a vættir's help is often more than bargained for.

```statblock
"name": "Vættir (ToB1-2023)"
"size": "Medium"
"type": "undead"
"alignment": "Lawful Evil"
"ac": !!int "15"
"ac_class": "[chain shirt](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/chain-shirt.md)"
"hp": !!int "97"
"hit_dice": "13d8 + 39"
"stats":
- !!int "20"
- !!int "14"
- !!int "16"
- !!int "10"
- !!int "12"
- !!int "14"
"speed": "30 ft."
"saves":
  "Dexterity": !!int "4"
  "Wisdom": !!int "3"
"damage_immunities": "necrotic, poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., truesight 30 ft., passive Perception 11"
"languages": "the languages it knew in life"
"cr": "4"
"traits":
- "desc": "The vættir can pinpoint the location of creatures wearing or carrying one\
    \ of the vættir's personal items or grave goods within 60 feet of it, and the\
    \ vættir can sense the general direction of its personal items and grave goods\
    \ within 1 mile of it."
  "name": "Grave Goods Sense"
- "desc": "A destroyed vættir gains a new body in 24 hours, regaining all its hp and\
    \ becoming active again. The new body forms in a random unoccupied space within\
    \ 100 feet of where it fell. This trait doesn't function if the vættir is put\
    \ to rest (typically by returning its remains to its burial mound)."
  "name": "Rejuvenation"
- "desc": "While in sunlight, the vættir has disadvantage on attack rolls, as well\
    \ as on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on sight."
  "name": "Sunlight Sensitivity"
- "desc": "The vættir doesn't require air, food, drink, or sleep."
  "name": "Undead Nature"
"actions":
- "desc": "The vættir can use its Disorienting Gaze. It then makes two Vættir's Greataxe\
    \ or Necrotic Bolt attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11\
    \ (1d12 + 5) slashing damage plus 4 (1d8) necrotic damage."
  "name": "Vættir's Greataxe"
- "desc": "Ranged Spell Attack: +4 to hit, range 120 ft., one target. Hit: 15\
    \ (3d8 + 2) necrotic damage."
  "name": "Necrotic Bolt"
- "desc": "The vættir locks eyes with one creature it can see within 30 feet of it.\
    \ The target must succeed on a DC 15 Charisma saving throw or be [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ for 1 minute. While [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated),\
    \ the creature moves in a random direction when it moves. An [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success. If a creature's saving throw is successful\
    \ or the effect ends for it, the creature is immune to the vættir's Disorienting\
    \ Gaze for the next 24 hours."
  "name": "Disorienting Gaze"
- "desc": "The vættir spews forth a 15‑foot cone of putrid gas. Each creature in the\
    \ area must make a DC 15 Constitution saving throw. On a failure, a creature takes\
    \ 21 (6d6) poison damage and is [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 minute. On a success, a creature takes half the damage and isn't [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned).\
    \ A [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Corpse Breath (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/vaettir-tob1-2023.webp"
```
^statblock

## Environment

any