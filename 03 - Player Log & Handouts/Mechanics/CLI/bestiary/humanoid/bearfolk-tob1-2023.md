---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/arctic
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/environment/mountain
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/bearfolk
statblock: inline
aliases: ["Bearfolk"]
---
# [Bearfolk](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/bearfolk-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 33*  

*Although it has the head of a shaggy bear, this humanoid creature wears armor and carries a battleaxe in one massive, clawed hand and a warhammer in the other. It's a solid slab of muscle that towers over most humans.*

The hulking bearfolk are intimidating creatures. Brutish and powerful, they combine features of humanoid beings and bears. Their heads are ursine with heavy jaws and sharp teeth. Dark fur covers their muscular bodies. Adult bearfolk stand at least 7 feet tall and weigh more than 600 pounds.

## Sworn to the Bear King

Bearfolk are almost universally the subjects of the Bear King. The bearfolk protect the cities of their northern kingdom and roam the wooded roads of the wilderness. The greatest number of bearfolk are concentrated around the court of the Bear King himself, with ancient bear jarls governing their unruly kin. Only a handful of renegades, exiles, and other rogue bearfolk live permanently outside this society.

## Passionate and Volatile

Boisterous and jovial, the bearfolk are a people of extremes. They celebrate with great passion and are quick to explosive anger. Settling differences with wrestling matches that leave permanent scars is common, as is seeing two bloodied bearfolk sharing a cask of mead and a raucous song after such a scuffle.

```statblock
"name": "Bearfolk (ToB1-2023)"
"size": "Medium"
"type": "humanoid"
"subtype": "bearfolk"
"alignment": "Chaotic Good"
"ac": !!int "14"
"ac_class": "[hide armor](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/hide-armor.md)"
"hp": !!int "45"
"hit_dice": "6d8 + 18"
"stats":
- !!int "19"
- !!int "14"
- !!int "16"
- !!int "8"
- !!int "12"
- !!int "9"
"speed": "40 ft."
"senses": "darkvision 60 ft., passive Perception 11"
"languages": "Common, Giant"
"cr": "3"
"traits":
- "desc": "The bearfolk has advantage on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on smell."
  "name": "Keen Smell"
"actions":
- "desc": "The bearfolk makes one Battleaxe attack, one Warhammer attack, and one\
    \ Bite attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d8\
    \ + 4) slashing damage, or 9 (1d10 + 4) slashing damage if used with two hands."
  "name": "Battleaxe"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11\
    \ (2d6 + 4) piercing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d8\
    \ + 4) bludgeoning damage, or 9 (1d10 + 4) bludgeoning damage if used with\
    \ two hands."
  "name": "Warhammer"
"bonus_actions":
- "desc": "The bearfolk triggers a berserk frenzy that lasts 1 minute. While in frenzy,\
    \ it has resistance to bludgeoning, piercing, and slashing damage and has advantage\
    \ on attack rolls. Attack rolls made against a frenzied bearfolk have advantage."
  "name": "Frenzy (Recharges after a Long or Short Rest)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/bearfolk-tob1-2023.webp"
```
^statblock

## Environment

arctic, forest, hill, mountain, urban