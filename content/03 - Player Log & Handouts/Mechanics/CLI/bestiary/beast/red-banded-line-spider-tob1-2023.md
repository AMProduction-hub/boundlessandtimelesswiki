---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1-4
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Red-Banded Line Spider"]
---
# [Red-Banded Line Spider](03 - Player Log & Handouts\Mechanics\CLI\bestiary\beast/red-banded-line-spider-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 345*  

*Bands of red swirl along the abdomen of this small, black spider.*

Red-banded line spiders are named for both the deep red swirls on their abdomens, unique to each spider, and for their peculiar hunting technique. The largest ones hunt in the dark canopy of temperate and subtropical forests.

## Hand-Sized Hunters

These furry, brown spiders are not enormous monsters, but they are big enough to be alarming. A typical one is as big as a human hand with fingers spread wide, but some grow as large as small dogs.

## Webbed Line

Line spiders don't spin webs but instead perch and watch for prey. When prey wanders near, the spider launches a line of webbing to snare it, then pounces unerringly along that line to deliver a deep bite. Their potent venom can incapacitate creatures much larger than themselves, and they quickly devour flesh with their powerful jaws.

## City Dwellers

Line spiders are often found in cities, and their size makes them a good replacement for a garroter crab in certain forms of divination. They're favorites among exotic pet dealers—usually with their venom sacs removed, sometimes not. Goblins, kobolds, and some humans use them rather than cats to control a mouse or rat infestation, and they make reasonably good pets if they're kept well-fed. If they get hungry, line spiders may devour other small pets or even their owners.

```statblock
"name": "Red-Banded Line Spider (ToB1-2023)"
"size": "Tiny"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "13"
"hp": !!int "15"
"hit_dice": "6d4"
"stats":
- !!int "4"
- !!int "16"
- !!int "10"
- !!int "1"
- !!int "10"
- !!int "2"
"speed": "30 ft., climb 30 ft."
"skillsaves":
  "Stealth": !!int "5"
  "Perception": !!int "2"
"damage_immunities": "psychic"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)"
"senses": "darkvision 60 ft., passive Perception 12"
"languages": ""
"cr": "1/4"
"traits":
- "desc": "If the spider deals poison damage to a creature that is [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
    \ the target takes an extra 2 (1d4) poison damage."
  "name": "Reactive Venom"
- "desc": "The spider can climb difficult surfaces, including upside down and on ceilings,\
    \ without needing to make an ability check."
  "name": "Spider Climb"
- "desc": "The spider ignores movement restrictions caused by webbing."
  "name": "Web Walker"
"actions":
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 1 piercing\
    \ damage plus 5 (2d4) poison damage, and the target must succeed on a DC 10\
    \ Constitution saving throw or be [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ until the end of its next turn."
  "name": "Bite"
"bonus_actions":
- "desc": "The spider throws a length of webbing at a point on a surface, such as\
    \ the ground or wall, it can see within 30 feet of it, attaching one end of the\
    \ webbing to that point. It then reels in the webbing, pulling itself to an unoccupied\
    \ space within 5 feet of that point. When the spider moves in this way, opportunity\
    \ attacks against it have disadvantage. If the spider pulled itself at least 15\
    \ feet straight toward a creature, it has advantage on the next Bite attack it\
    \ makes against that creature before the start of its next turn."
  "name": "Swingline"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/beast/token/red-banded-line-spider-tob1-2023.webp"
```
^statblock

## Environment

forest, urban