---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/farmland
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Swarm of Sluaghs"]
---
# [Swarm of Sluaghs](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/swarm-of-sluaghs-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 357*  

*This tiny humanlike creature has a torso that trails away in place of legs, eyes that are black voids, and long, pale arms ending in sharp claws.*

## Cowards Alone

These tiny, malevolent fey dwell in darkness. Alone they are cowards, but they are rarely encountered alone. They are most active during the winter, especially during winter's long nights. They usually speak to their victims as they attack, but those shouts are little more than whispers to the ears of their prey.

## Chilling Touch

Sluaghs feed by draining their prey of warmth with their chilling claws. They devour small animals if nothing more appetizing is available, though they prefer humanoid prey. Their victims have unnaturally cold skin with a pale, blue tint. Swarms of sluaghs serve hags, devils, trollkin, and evil fey who know the blood rituals to summon and direct them. Shadow fey and drow send them against other elves, often targeting the defenders of elven settlements.

## Legless Flocks

Sluaghs are tiny, gaunt humanoid creatures the size of a weasel. They have no legs; instead their torso tapers off in a disquieting way. Though they can fly, they can also pull themselves quickly across the ground with their arms. They are always draped in black, though their actual skin and hair are pale white. They have sharp claws and fangs, and their eyes are entirely black. In masses, they somewhat resemble a flock of strange birds.

```statblock
"name": "Swarm of Sluaghs (ToB1-2023)"
"size": "Medium"
"type": "fey"
"alignment": "Chaotic Evil"
"ac": !!int "13"
"hp": !!int "54"
"hit_dice": "12d8"
"stats":
- !!int "6"
- !!int "16"
- !!int "11"
- !!int "6"
- !!int "13"
- !!int "10"
"speed": "30 ft., fly 50 ft."
"skillsaves":
  "Stealth": !!int "5"
"damage_vulnerabilities": "fire"
"damage_resistances": "bludgeoning, piercing, slashing"
"damage_immunities": "cold"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
  \ [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
  \ [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)"
"senses": "darkvision 60 ft., passive Perception 11"
"languages": "Common, Sylvan"
"cr": "3"
"traits":
- "desc": "While in sunlight, the swarm of sluaghs has disadvantage on attack rolls,\
    \ ability checks, and saving throws."
  "name": "Sunlight Weakness"
- "desc": "The swarm can occupy another creature's space and vice versa, and the swarm\
    \ can move through any opening large enough for a Tiny fey. The swarm can't regain\
    \ hp or gain temporary hp."
  "name": "Swarm"
"actions":
- "desc": "Melee Weapon Attack: +5 to hit, reach 0 ft., one creature in the swarm's\
    \ space. Hit: 28 (8d6) cold damage, or 14 (4d6) cold damage if the swarm\
    \ has half of its hp or fewer. The target must succeed on a DC 13 Constitution\
    \ saving throw or be unable to regain hp for 1 minute. The target can repeat the\
    \ saving throw at the end of each of its turns, ending the effect on itself on\
    \ a success."
  "name": "Chilling Touch"
"bonus_actions":
- "desc": "While in dim light or darkness, the swarm of sluaghs takes the Hide action."
  "name": "Shadow Stealth"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/swarm-of-sluaghs-tob1-2023.webp"
```
^statblock

## Environment

farmland, forest