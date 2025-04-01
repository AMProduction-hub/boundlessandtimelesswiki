---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Sand Silhouette"]
---
# [Sand Silhouette](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/sand-silhouette-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 312*  

*A person made of sand emerges from the dune, a sandstorm of wailing souls swirling around it.*

Sand silhouettes are spirits of those who died in desperation in sandy ground, buried during sandstorms, thrown into dry wells, or the victims of a dune collapse.

## Sand Bodies

If disturbed or agitated, these restless souls cause the sand around them to swirl and form into a loose vortex that vaguely resembles their physical body in life. They can control these shapes as they controlled their physical bodies.

## Traceless Movement

Sand silhouettes glide through the sand without leaving a trace or creating any telltale sign of their approach, which makes it easy for them to surprise even cautious travelers with sudden attacks from below.

```statblock
"name": "Sand Silhouette (ToB1-2023)"
"size": "Medium"
"type": "undead"
"alignment": "Neutral Evil"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "105"
"hit_dice": "14d8 + 42"
"stats":
- !!int "18"
- !!int "12"
- !!int "17"
- !!int "7"
- !!int "12"
- !!int "10"
"speed": "30 ft., burrow 30 ft."
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "necrotic, poison"
"condition_immunities": "[exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., tremorsense 60 ft., passive Perception 11"
"languages": "The languages it knew in life"
"cr": "6"
"traits":
- "desc": "The sand silhouette has advantage on Dexterity ([Stealth](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Stealth))\
    \ checks made to hide in desert terrain."
  "name": "Sand Camouflage"
- "desc": "The sand silhouette can move through a space as narrow as 1 inch wide without\
    \ squeezing."
  "name": "Sand Form"
- "desc": "The sand silhouette can burrow through nonmagical, loose sand without disturbing\
    \ the material it is moving through."
  "name": "Sand Glide"
- "desc": "The sand silhouette doesn't require air, food, drink, or sleep."
  "name": "Undead Nature"
- "desc": "For every 5 feet the sand silhouette moves in water, or for every gallon\
    \ of water splashed on it, it takes 2 (1d4) cold damage. In addition, the silhouette\
    \ takes 10 cold damage when it starts its turn at least partially submerged in\
    \ water."
  "name": "Water Hypersusceptibility"
"actions":
- "desc": "The sand silhouette makes two Slam attacks. If both attacks hit a Medium\
    \ or smaller target, the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 15), and the silhouette uses its Engulf on the target."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 14\
    \ (3d6 + 4) bludgeoning damage plus 3 (1d6) necrotic damage."
  "name": "Slam"
- "desc": "The sand silhouette engulfs a Medium or smaller creature [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ by it. The engulfed target is [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ and [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ and it must succeed on a DC 15 Constitution saving throw at the start of each\
    \ of the sand silhouette's turns or take 10 (3d6) necrotic damage. If the sand\
    \ silhouette moves, the engulfed target moves with it. The sand silhouette can\
    \ have only one creature engulfed at a time."
  "name": "Engulf"
- "desc": "The sand silhouette creates a storm of whirling sand and wailing souls\
    \ around itself. The storm is a 10-foot radius, 30-foot-tall cylinder centered\
    \ on the silhouette and moves with the silhouette for 1 minute, until it ends\
    \ the storm as a bonus action, or until its [concentration](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Concentration)\
    \ ends (as if [concentrating](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Concentration)\
    \ on a spell). The sandstorm's area is lightly obscured, and a creature that starts\
    \ its turn in the sandstorm's area or enters it for the first time on a turn must\
    \ succeed on a DC 15 Wisdom saving throw or take 3 (1d6) necrotic damage and\
    \ be [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ for 1 minute. An engulfed creature automatically succeeds on this saving throw.\
    \ A [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Haunted Haboob (3/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/sand-silhouette-tob1-2023.webp"
```
^statblock

## Environment

desert