---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/environment/badlands
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Sand Spider"]
---
# [Sand Spider](03 - Player Log & Handouts\Mechanics\CLI\bestiary\beast/sand-spider-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 346*  

*Two speckled, tan legs erupt from the sand, plunging forward with murderous speed. The legs are quickly followed by the body of a large, orange and tan furred spider.*

## Drag Prey into Tunnels

Sand spiders lurk beneath the arid plains and dry grasslands. These carnivores hunt desert dwellers and plains travelers by burrowing into loose sand so they are completely hidden from view. When prey walks over their trap, the spider lunges up from hiding, snares the prey, and drags it down beneath the sand, where it can wrap the prey in webbing before quickly stabbing it to death.

## Spider Packs

More terrifying than a lone sand spider is a group of sand spiders hunting together. They build connected lair networks called clusters, containing one female and two or three males. They work together with one sand spider attacking to draw attention, and the others attacking from trapdoors in the opposite direction, behind the skirmish line.

```statblock
"name": "Sand Spider (ToB1-2023)"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "135"
"hit_dice": "18d10 + 36"
"stats":
- !!int "20"
- !!int "17"
- !!int "14"
- !!int "4"
- !!int "12"
- !!int "4"
"speed": "30 ft., burrow 20 ft."
"skillsaves":
  "Stealth": !!int "6"
  "Perception": !!int "4"
"senses": "darkvision 60 ft., tremorsense 60 ft., passive Perception 14"
"languages": ""
"cr": "7"
"traits":
- "desc": "The sand spider has advantage on Dexterity ([Stealth](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Stealth))\
    \ checks made to hide in sandy terrain."
  "name": "Sand Camouflage"
"actions":
- "desc": "The sand spider makes one Bite attack and two Impaling Leg attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one creature. Hit: 10\
    \ (1d10 + 5) piercing damage plus 10 (3d6) poison damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 12\
    \ (2d6 + 5) piercing damage. If the target is a Medium or smaller creature,\
    \ it must succeed on a DC 16 Strength saving throw or be [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 16). Until this grapple ends, the target is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ and takes 7 (2d6) piercing damage at the start of each of its turns, and the\
    \ sand spider can't use the same Impaling Leg on another target. The sand spider\
    \ has four Impaling Legs."
  "name": "Impaling Leg"
"reactions":
- "desc": "When the sand spider is burrowed just below the surface of sand and a Medium\
    \ or smaller creature enters the space on the surface just above where it is burrowed,\
    \ the sand spider makes one Impaling Leg attack against the creature, bursting\
    \ from the sand and revealing itself in the process. The target has disadvantage\
    \ on the saving throw to avoid being [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)."
  "name": "Trapdoor Ambush"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/beast/token/sand-spider-tob1-2023.webp"
```
^statblock

## Environment

badlands, desert, grassland