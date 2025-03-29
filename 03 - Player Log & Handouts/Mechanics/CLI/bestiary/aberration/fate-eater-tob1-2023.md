---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/aberration
statblock: inline
aliases: ["Fate Eater"]
---
# [Fate Eater](03 - Player Log & Handouts\Mechanics\CLI\bestiary\aberration/fate-eater-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 168*  

*Violet radiance surrounds this large pale centipede. Its flesh is translucent, and its jaws are crystalline.*

## Destiny Destroyers

Fate eaters infest remote areas of the planes, where they consume the threads of Fate itself. The beings in charge of Fate view them as vermin. Sometimes those beings engage particularly canny planar travelers either to hunt fate eaters or to help repair the damage they've done. This can be a deadly job, as the fate eaters consider the destiny of a mortal to be the tastiest of delicacies, rich in savory possibilities.

## Planar Gossips

Fate eaters can and do trade information about various dooms, fates, and outcomes, but one must have something rich in destiny to trade—or at least, juicy gossip about gods and demons.

## Visionary Flesh

Eating the properly prepared flesh of a fate eater grants the eater insight into the fate of another being.

```statblock
"name": "Fate Eater (ToB1-2023)"
"size": "Medium"
"type": "aberration"
"alignment": "Neutral"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "130"
"hit_dice": "20d8 + 40"
"stats":
- !!int "18"
- !!int "12"
- !!int "14"
- !!int "18"
- !!int "16"
- !!int "9"
"speed": "40 ft., climb 40 ft."
"saves":
  "Constitution": !!int "5"
"skillsaves":
  "Religion": !!int "7"
  "Insight": !!int "6"
  "History": !!int "7"
  "Arcana": !!int "7"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)"
"senses": "truesight 60 ft., passive Perception 13"
"languages": "telepathy 100 ft. understands all but can't speak"
"cr": "6"
"traits":
- "desc": "A creature that eats the flesh of a fate eater must make a DC 15 Constitution\
    \ saving throw. On a failure, the creature is [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 hour. On a success, the creature gains the benefits of the divination\
    \ spell."
  "name": "Visionary Flesh"
"actions":
- "desc": "The fate eater makes two Bite attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 13\
    \ (2d8 + 4) slashing damage plus 7 (2d6) necrotic damage."
  "name": "Bite"
- "desc": "The fate eater alters the fate of one creature it can see within 30 feet\
    \ of it. The creature must make a DC 15 Charisma saving throw. On a failure, the\
    \ creature takes 36 (8d8) psychic damage, and its fate is altered. Roll a d6\
    \ to determine which of the following alterations affects the creature. On a success,\
    \ the creature takes half the damage, and its fate isn't altered. A creature with\
    \ an altered fate for 1 minute or less can repeat the saving throw at the end\
    \ of each of its turns, ending the effect on itself on a success. Otherwise, a\
    \ creature with an altered fate can repeat the saving throw at the end of each\
    \ long rest, ending the effect on itself on a success."
  "name": "Alter Fate (Recharge 5-6)"
- "desc": "The creatures loses the use of one random class feature, such as Action\
    \ Surge or Channel Divinity, for 1 minute."
  "name": "1 Forgotten Training"
- "desc": "One of the creature's ability scores, chosen at random, is reduced by 2."
  "name": "2 Lost Potential"
- "desc": "The creature is [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ for 1 minute."
  "name": "3 Seeing the Alternates"
- "desc": "The creature loses proficiency in one random skill and gains proficiency\
    \ in another random skill."
  "name": "4 Shifting Memories"
- "desc": "The creature's current hp total becomes its hp maximum."
  "name": "5 Took the Lesser Path"
- "desc": "When the creature moves, it moves in a random direction for 1 minute."
  "name": "6 Untied from the Loop"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/aberration/token/fate-eater-tob1-2023.webp"
```
^statblock

## Environment

planar