---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/9
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fiend/demon
statblock: inline
aliases: ["Malakbel Demon"]
---
# [Malakbel Demon](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fiend/malakbel-demon-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 85*  

*Within a blinding wave of heat and glare walks a long-limbed, misshapen form. The creature scorches everything in its path as it strides forward.*

What most people recall most vividly from an encounter with a malakbel is the blinding light and blistering heat surrounding it. Rippling distortion obscures the creature's body, which is roughly the size and shape of an adult human.

## Demonic Messengers

Malakbel demons are contradictory creatures. They are both messengers and destroyers who carry the words of demon lords or even dark gods to the mortal realm. Paradoxically, once their message is delivered, they often leave none of its hearers alive to spread the tale.

## Where Virtue Cannot Look

The malakbel is the embodiment of all that is forbidden and destructive. Despite its vital role as a messenger, its destructive nature always comes to the fore. A malakbel descends upon settlements and travelers with the merciless and relentless onslaught of the raging sun, burning all it sees to cinders before vanishing like heat shimmers at dusk.

```statblock
"name": "Malakbel Demon (ToB1-2023)"
"size": "Medium"
"type": "fiend"
"subtype": "demon"
"alignment": "Chaotic Evil"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "102"
"hit_dice": "12d8 + 48"
"stats":
- !!int "14"
- !!int "17"
- !!int "19"
- !!int "13"
- !!int "16"
- !!int "20"
"speed": "40 ft."
"saves":
  "Dexterity": !!int "7"
  "Wisdom": !!int "7"
"skillsaves":
  "Perception": !!int "7"
"damage_resistances": "cold; lightning; bludgeoning, piercing, slashing from nonmagical\
  \ attacks"
"damage_immunities": "fire, poison, radiant"
"condition_immunities": "[blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "truesight 30 ft., passive Perception 17"
"languages": "Abyssal, telepathy 120 ft."
"cr": "9"
"traits":
- "desc": "The malakbel sheds searing, bright light in a 30-foot radius and dim light\
    \ for an additional 30 feet. At the start of each of the malakbel's turns, each\
    \ creature in the bright light shed by the malakbel takes 11 (2d10) radiant\
    \ damage. If any of the bright light overlaps with an area of darkness created\
    \ by a spell of 3rd level or lower, the spell creating the darkness is dispelled."
  "name": "Blistering Radiance"
- "desc": "Ranged attacks against the malakbel are made with disadvantage."
  "name": "Distortion"
- "desc": "The malakbel has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
"actions":
- "desc": "The malakbel makes two Scorching Blast attacks."
  "name": "Multiattack"
- "desc": "Melee or Ranged Spell Attack: +9 to hit, reach 5 ft. or range 120 ft.,\
    \ one target. Hit: 18 (3d8 + 5) fire damage."
  "name": "Scorching Blast"
- "desc": "The malakbel intensifies the heat and light it sheds to withering levels.\
    \ Each creature in the bright light shed by the malakbel's Blistering Radiance\
    \ trait must make a DC 16 Constitution saving throw. On a failure, a creature\
    \ takes 13 (3d8) fire damage and 22 (4d10) radiant damage and suffers one\
    \ level of [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion).\
    \ On a success, a creature takes half the damage and doesn't suffer [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion)."
  "name": "Searing Flare (Recharge 5-6)"
- "desc": "The malakbel magically teleports, along with any equipment it is wearing\
    \ or carrying, up to 100 feet to an unoccupied space it can see."
  "name": "Teleport"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fiend/token/malakbel-demon-tob1-2023.webp"
```
^statblock

## Environment

planar, urban