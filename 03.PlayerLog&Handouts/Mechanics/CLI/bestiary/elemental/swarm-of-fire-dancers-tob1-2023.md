---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/elemental
statblock: inline
aliases: ["Swarm of Fire Dancers"]
---
# [Swarm of Fire Dancers](03 - Player Log & Handouts\Mechanics\CLI\bestiary\elemental/swarm-of-fire-dancers-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 354*  

*A swirling mass of tiny, blue flames dances with the likeness of a skull embedded in each little, flickering fire.*

## Stunted Elementals

Fire dancers are tiny fire elementals. Speculation varies whether they're simply immature or somehow stunted. They may be castoffs from larger, fiery elemental beings. A single, solitary fire dancer is no more than a semi-sentient spark with a fragment of life and lofty but unrealistic ambitions. In large numbers, they're a menace.

## Unite and Grow Strong

Larger fire elementals are usually content merely to exist on their plane of origin. Fire dancers possess (and some argue are infected with) mortal qualities—they seek to reach a greater potential, which smacks of envy, ambition, and resentment. They realize that there is power in numbers and that, when united, they are a force to be reckoned with. A single fire dancer is no more threatening than a tiny candle flame, burning hot and blue. When thousands join together, though, the result is an inferno. Each fire dancer shapes itself into the likeness of a creature's (typically humanoid) skull to cause fear in its victims.

## Shared Goals

Lone fire dancers have some individuality, and like-minded fire dancers gather together in swarms to accomplish shared goals. Savvy bards, conjurers, and enchanters who summon or interact with swarms of fire dancers know to quickly determine the swarm's goal and use that to manipulate it. They must be careful to maintain the upper hand, though, for these creatures are surly allies at the best of times.

```statblock
"name": "Swarm of Fire Dancers (ToB1-2023)"
"size": "Medium"
"type": "elemental"
"alignment": "Neutral Evil"
"ac": !!int "15"
"hp": !!int "90"
"hit_dice": "12d8 + 36"
"stats":
- !!int "10"
- !!int "20"
- !!int "16"
- !!int "6"
- !!int "10"
- !!int "7"
"speed": "30 ft., fly 30 ft. (hover)"
"damage_resistances": "bludgeoning, piercing, slashing"
"damage_immunities": "fire, poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
  \ [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
  \ [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned),\
  \ [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)"
"senses": "darkvision 60 ft., passive Perception 10"
"languages": "Ignan"
"cr": "7"
"traits":
- "desc": "The swarm of fire dancers doesn't require air, food, drink, or sleep."
  "name": "Elemental Nature"
- "desc": "A creature that touches the swarm or hits it with a melee attack while\
    \ within 5 feet of it takes 5 (1d10) fire damage. In addition, the first time\
    \ the swarm enters a creature's space on a turn, that creature takes 5 (1d10)\
    \ fire damage and catches fire. Until a creature, which can include the target,\
    \ uses an action to douse the fire, the creature takes 5 (1d10) fire damage\
    \ at the start of each of its turns."
  "name": "Fire Form"
- "desc": "The swarm sheds bright light in a 30-foot radius and dim light to an additional\
    \ 30 feet."
  "name": "Illumination"
- "desc": "The swarm can occupy another creature's space and vice versa, and the swarm\
    \ can move through any opening large enough for a Tiny Elemental. The swarm can't\
    \ regain hp or gain temporary hp."
  "name": "Swarm"
- "desc": "For every 5 feet the swarm moves in water, or for every gallon of water\
    \ splashed on it, it takes 1 cold damage."
  "name": "Water Susceptibility"
"actions":
- "desc": "The swarm of fire dancers can use its Frightening Visage, if available.\
    \ It then makes two Singe attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 0 ft., one target in the swarm's\
    \ space. Hit: 22 (4d10) fire damage, or 11 (2d10) fire damage if the swarm\
    \ has half its hp or fewer."
  "name": "Singe"
- "desc": "The swarm rearranges itself into the shape of a giant, blue, flaming Humanoid\
    \ skull. Each Humanoid within 30 feet of the swarm that can see it must succeed\
    \ on a DC 16 Wisdom saving throw or be [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ for 1 minute. A [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Frightening Visage (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/elemental/token/swarm-of-fire-dancers-tob1-2023.webp"
```
^statblock

## Environment

planar