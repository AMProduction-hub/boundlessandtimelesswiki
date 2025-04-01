---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/8
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/giant
statblock: inline
aliases: ["Degenerate Titan"]
---
# [Degenerate Titan](03 - Player Log & Handouts\Mechanics\CLI\bestiary\giant/degenerate-titan-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 362*  

*This giant retains a look of daunting power despite its stooped bearing, tattered clothing, and pieces of slapdash armor strapped on wherever it fits.*

## Haunt Ruins

The degenerate descendants of ancient titans haunt the ruins where their cities once flourished. These descendants hunt for any living thing to eat, including each other, and sometimes chase after herds of goats or other animals for miles. While they are easily distracted, they always find their way home unerringly.

## Insane and Moody

Degenerate titans are prone to erratic actions and unexpected mood shifts. They are fiercely territorial creatures who worship the still-active magical devices of their cities and any surviving statuary as if the statues were gods. Their lairs are filled with items scavenged from the city. These collections are a hodge-podge of dross and delight, as the degenerate titans are not intelligent enough to discern treasure from trash.

## Primal Power

Degenerate titans cannot command magical words of power like their ancestors, but they retain a connection to the natural world, allowing them to tap into the earth's latent mystic power to generate strange geomancy. These devolved misfits may have lost most of their former gifts, but what remains are primal powers that tap, without subtlety or skill, into the fundamental building blocks of the world.

```statblock
"name": "Degenerate Titan (ToB1-2023)"
"size": "Huge"
"type": "giant"
"alignment": "Chaotic Evil"
"ac": !!int "12"
"ac_class": "armor scraps"
"hp": !!int "161"
"hit_dice": "14d12 + 70"
"stats":
- !!int "21"
- !!int "6"
- !!int "20"
- !!int "6"
- !!int "12"
- !!int "7"
"speed": "40 ft."
"skillsaves":
  "Intimidation": !!int "4"
  "Perception": !!int "4"
"senses": "darkvision 60 ft., passive Perception 14"
"languages": "Giant"
"cr": "8"
"traits":
- "desc": "The degenerate titan has advantage on saving throws against spells and\
    \ other magical effects."
  "name": "Magic Resistance"
"actions":
- "desc": "The degenerate titan can use its Reality‑Bending Shout. It then makes three\
    \ Greatclub attacks or two Rock attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 18\
    \ (3d8 + 5) bludgeoning damage."
  "name": "Greatclub"
- "desc": "Ranged Weapon Attack: +8 to hit, range 60/240 ft., one target. Hit:\
    \ 27 (4d10 + 5) bludgeoning damage."
  "name": "Rock"
- "desc": "The degenerate titan utters a scream that vibrates the fabric of reality\
    \ around one creature it can see within 30 feet of it. The titan can attempt to\
    \ end one magical effect of its choice of 3rd level or lower on the target. This\
    \ effect works like the [dispel magic](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dispel-magic.md)\
    \ spell, except the titan must always make an ability check. The titan's ability\
    \ check for this is +4."
  "name": "Reality-Bending Shout"
- "desc": "The degenerate titan slams its fists onto the ground, creating a shockwave\
    \ in a 60-foot line that is 10 feet wide. Each creature in the line must make\
    \ a 16 Dexterity saving throw. On a failure, a creature takes 35 (10d6) force\
    \ damage and is flung 20 feet away from the titan and knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
    \ as the earth buckles and tosses the creature. On a success, a creature takes\
    \ half the damage and isn't flung or knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone).\
    \ If a flung creature strikes a solid surface, the creature takes 3 (1d6) bludgeoning\
    \ damage for every 10 feet it was flung. If the creature is flung at another creature,\
    \ that creature must succeed on a DC 16 Dexterity saving throw or take the same\
    \ damage and be knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Earthstrike (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/giant/token/degenerate-titan-tob1-2023.webp"
```
^statblock

## Environment

any