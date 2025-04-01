---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/arctic
- ttrpg-cli/monster/environment/coastal
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Mahoru"]
---
# [Mahoru](03 - Player Log & Handouts\Mechanics\CLI\bestiary\monstrosity/mahoru-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 260*  

*A white fin cut the surface of the water as the serpentine creature approached. Its wolfish head burst from the surface, revealing a body covered in fine, white fur.*

## Valuable Teeth and Fur

A mahoru's heavy jaws are filled with triangular, serrated teeth adept at tearing flesh and sundering bone. Their white fur is prized for its warmth and waterproof qualities. Their pectoral fins feature stubby, claw-tipped paws. Mahoru is a totem beast for many northern tribes. Some make arrowheads and tooth-studded clubs with the beast's fangs.

## Iceberg Hunters

Mahoru prowl northern coasts and estuaries, hunting among the fragmenting pack ice each summer. They lurk beneath the surface, catching swimmers or lurching up onto the ice to break or tilt it and send prey tumbling into the water. When necessary, they stalk beaches and riverbanks in search of carrion or unwary victims.

## Work in Pairs and Packs

Mahoru work together in mated pairs to corral everything from fish and seals to larger prey like kayaking humanoids and even polar bears. They gnaw at ice bridges and the frozen surface of lakes and rivers to create fragile patches that plunge unwary victims into waiting jaws.

```statblock
"name": "Mahoru (ToB1-2023)"
"size": "Large"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "105"
"hit_dice": "14d10 + 28"
"stats":
- !!int "18"
- !!int "19"
- !!int "14"
- !!int "3"
- !!int "12"
- !!int "7"
"speed": "10 ft., swim 60 ft."
"skillsaves":
  "Stealth": !!int "6"
  "Perception": !!int "3"
"senses": "darkvision 60 ft., passive Perception 13"
"languages": ""
"cr": "3"
"traits":
- "desc": "The mahoru can breathe air and water."
  "name": "Amphibious"
- "desc": "The mahoru has advantage on melee attack rolls against any creature that\
    \ doesn't have all of its hp."
  "name": "Blood Frenzy"
- "desc": "The mahoru has advantage on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on sight or smell."
  "name": "Keen Sight and Smell"
- "desc": "The mahoru has advantage on attack rolls against a creature if at least\
    \ one of the mahoru's allies is within 5 feet of the creature and the ally isn't\
    \ [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)."
  "name": "Pack Tactics"
"actions":
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 20\
    \ (3d10 + 4) slashing damage. If the mahoru scores a critical hit, the target\
    \ must succeed on a DC 14 Strength saving throw or the mahoru bites off one of\
    \ the target's limbs. A creature is immune to this effect if it is immune to slashing\
    \ damage."
  "name": "Bite"
- "desc": "The mahoru roars while above water or emits a loud, low thrum while underwater.\
    \ Each creature within 30 feet of the mahoru that can hear the roar or thrum must\
    \ succeed on a DC 14 Wisdom saving throw or be [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ for 1 minute. A [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success. A creature that fails the saving throw by\
    \ 5 or more is also [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ until the end of its next turn. If a creature's saving throw is successful or\
    \ the effect ends for it, the creature is immune to the Roar of all mahoru for\
    \ the next 24 hours."
  "name": "Roar"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/monstrosity/token/mahoru-tob1-2023.webp"
```
^statblock

## Environment

arctic, coastal, underwater