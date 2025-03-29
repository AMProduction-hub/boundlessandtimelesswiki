---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/aberration
statblock: inline
aliases: ["Arboreal Grappler"]
---
# [Arboreal Grappler](03 - Player Log & Handouts\Mechanics\CLI\bestiary\aberration/arboreal-grappler-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 24*  

*Long, simian arms snake through the trees like furred serpents, dangling from a shaggy, striped ape in the leafy canopy above and trying to snare those below.*

An arboreal grappler is a malformed creation of the gods, a primate whose limbs warped into long, muscular tentacles covered in shaggy, red fur.

## Carry Prey to the Heights

Arboreal grapplers use their long limbs to snatch and drag prey behind them as they use their powerful forelimbs to ascend to the highest canopy. Victims are constricted until their struggles cease and then are devoured. The grapplers' flexible tentacles are ill-suited for terrestrial movement; they must drag themselves clumsily across open ground too wide to swing across.

## Clans in the Canopy

Arboreal grappler tribes build family nests decorated with bones and prized relics of past hunts. These nests are built high in the jungle canopy, typically 80 feet or more above the ground. Clans of 40 or more spread across crude villages atop the trees; in such large settlements, a third of the population are juveniles. These nests are difficult to spot from the ground; a DC 20 Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception)) check is required. A creature observing an arboreal grappler as it climbs into or out of a nest has advantage on the check.

## Carnivorous Elf Hunters

Grapplers are carnivorous and prefer humanoid flesh, elves in particular. Scholars suggest this arises from hatred as much as from hunger, citing records of various humanoids hunting arboreal grapplers millennia ago.

```statblock
"name": "Arboreal Grappler (ToB1-2023)"
"size": "Medium"
"type": "aberration"
"alignment": "Neutral Evil"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "90"
"hit_dice": "12d8 + 36"
"stats":
- !!int "16"
- !!int "16"
- !!int "16"
- !!int "6"
- !!int "10"
- !!int "6"
"speed": "10 ft., climb 40 ft."
"skillsaves":
  "Stealth": !!int "5"
  "Acrobatics": !!int "5"
"senses": "darkvision 60 ft., passive Perception 10"
"languages": ""
"cr": "4"
"traits":
- "desc": "The arboreal grappler doesn't provoke opportunity attacks when it climbs\
    \ out of an enemy's reach."
  "name": "Boscage Brachiation"
- "desc": "The arboreal grappler can move at its full speed when dragging a Medium\
    \ or smaller creature it has [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)."
  "name": "Mobile Grappler"
- "desc": "The arboreal grappler can climb difficult surfaces, including upside down\
    \ on ceilings, without needing to make an ability check."
  "name": "Spider Climb"
"actions":
- "desc": "The arboreal grappler makes one Bite attack and two Tentacle attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one creature. Hit: 6\
    \ (1d6 + 3) piercing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +5 to hit, reach 10 ft., one target. Hit: 10\
    \ (2d6 + 3) bludgeoning damage, and the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 13). Until this grapple ends, the target is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained).\
    \ The arboreal grappler has two tentacles, each of which can grapple only one\
    \ target."
  "name": "Tentacle"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/aberration/token/arboreal-grappler-tob1-2023.webp"
```
^statblock

## Environment

forest