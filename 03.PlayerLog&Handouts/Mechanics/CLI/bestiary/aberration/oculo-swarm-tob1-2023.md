---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/aberration
statblock: inline
aliases: ["Oculo Swarm"]
---
# [Oculo Swarm](03 - Player Log & Handouts\Mechanics\CLI\bestiary\aberration/oculo-swarm-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 288*  

*This collection of hundreds of eyes floats along, trailing ganglia and dripping caustic fluid that sizzles when it hits the ground.*

## Failed Experiment

Oculo swarms came about from failed experiments to create living scrying sensors. Once set loose, these horrors attain a form of distributed self-awareness. Exactly what motivates them is unknown, except that they are driven to survive.

## Flesh Stealers

A weakened oculo swarm can reinvigorate itself by tearing fresh eyes from almost any type of living creature. If a badly depleted oculo swarm escapes from battle, it attacks lone creatures or weak groups until the mass of gore-spattered eyeballs is replenished. The more dismembered eyeballs the swarm contains, the more powerful it becomes.

## Single Eye Scouts

The entire swarm sees what any single member sees. Before attacking or even entering a potentially dangerous area, individual eyes scout ahead for prospective victims or dangerous foes. Though harmless and easily destroyed, these lone eyes provide plenty of information to the oculo swarm before perishing.

> [!note] Oculo Swarms in Midgard
> 
> Bemmean wizards have been known to employ oculo swarms as lie detectors during negotiations. An oculo instinctively reads eye movements, and it can communicate what it sees to the wizard by moving in a specific way or by changing the color of its irises. If negotiations go poorly, the mage gives the swarm permission to add a fresh pair of eyes to its number.
^oculo-swarms-in-midgard

```statblock
"name": "Oculo Swarm (ToB1-2023)"
"size": "Large"
"type": "aberration"
"alignment": "Neutral Evil"
"ac": !!int "15"
"hp": !!int "82"
"hit_dice": "11d10 + 22"
"stats":
- !!int "10"
- !!int "20"
- !!int "14"
- !!int "8"
- !!int "15"
- !!int "17"
"speed": "5 ft., fly 40 ft. (hover)"
"skillsaves":
  "Stealth": !!int "7"
  "Insight": !!int "6"
  "Perception": !!int "6"
"damage_resistances": "bludgeoning, piercing, slashing"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
  \ [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
  \ [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)"
"senses": "darkvision 60 ft., passive Perception 16"
"languages": "understands Common but can't speak"
"cr": "4"
"traits":
- "desc": "The oculo swarm has advantage on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on sight and on saving throws against being [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded).\
    \ In addition, if the swarm isn't [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
    \ creatures attacking it can't benefit from traits and features that rely on a\
    \ creature's allies distracting or surrounding the swarm, such as the Pack Tactics\
    \ trait or Sneak Attack class feature."
  "name": "Hundreds of Eyes"
- "desc": "The swarm can occupy another creature's space and vice versa, and the swarm\
    \ can move through any opening large enough for a Tiny eyeball. The swarm can't\
    \ regain hp or gain temporary hp."
  "name": "Swarm"
"actions":
- "desc": "The oculo swarm makes two Extract Eye attacks. If both attacks hit one\
    \ creature, the target must succeed on a DC 13 Strength saving throw or the swarm\
    \ removes one of its eyes. While missing half or fewer of its total number of\
    \ eyes, the target has disadvantage on attack rolls and Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on sight. While missing more than half its total number of\
    \ eyes, the target is [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ until its sight is restored. If the target's eye is recovered from the defeated\
    \ swarm, it can be reattached with a successful DC 12 Wisdom ([Medicine](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Medicine))\
    \ check, provided the eye is reattached within 1 hour of the target losing the\
    \ eye."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 0 ft., one creature in the swarm's\
    \ space. Hit: 18 (4d8) piercing damage, or 9 (2d8) piercing damage if the\
    \ swarm has half of its hp or fewer."
  "name": "Extract Eye"
- "desc": "The swarm's many eyes suddenly turn in different directions. Each creature\
    \ within 10 feet of the oculo swarm must make a DC 13 Charisma saving throw. On\
    \ a failure, a creature takes 21 (6d6) psychic damage and is disoriented until\
    \ the end of its next turn. On a success, a creature takes half the damage and\
    \ isn't disoriented. A disoriented creature is [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ and moves in a random direction when it moves."
  "name": "Disorienting Gaze (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/aberration/token/oculo-swarm-tob1-2023.webp"
```
^statblock

## Environment

any, urban