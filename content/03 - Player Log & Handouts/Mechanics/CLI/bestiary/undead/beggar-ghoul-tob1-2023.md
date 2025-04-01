---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1-2
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Beggar Ghoul"]
---
# [Beggar Ghoul](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/beggar-ghoul-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 200*  

*This emaciated, gray husk of a creature wears rags and picks hungrily at a sliver of bone. It moves in a crouch so low that it's almost crawling, but its eyes glow like flickering coals and it exudes a desperate ferocity with each rot-fouled breath.*

## Lesser Ghouls

Most citizens of the ghoul empire are not darakhul but lesser strains of ghouls and ghasts. Beggar ghouls are by far the weakest of these. Though they make up the majority of any military action involving the legions, they are employed as fodder, and the most wretched of them are barely suitable even for that. They eke out miserable livings by scrounging for food near the surface or by begging in the ghoul cities.

## Withered and Deprived

Thin and emaciated even for undead, beggar ghouls are shriveled versions of their standard cousins—little more than flesh-covered skeletons. While some beggar ghouls spend their entire existence in undeath as this weak strain, at least a few were once stronger ghouls who withered when they were trapped far from sources of flesh. Others were exiled from the empire without the resources to fend for themselves.

> [!note] Ghouls in Midgard
> 
> The ghoul empire maintains complex social structures and forges serious alliances, particularly among the undead princes of Morgau and Doresh. Unofficial embassies exist in Zobeck, the Ironcrag Cantons, Krakova, and Magdar. Other hidden outposts may lurk below the Seven Cities, Illyria, or beyond.
> 
> Their patience and willingness to convert enemies into followers makes lasting victories against the darakhul difficult. Three full legions of ghouls serve Emperor Nicoforus directly, and a dozen more legions of varying quality press the fight to other races of the Underworld.
^ghouls-in-midgard

```statblock
"name": "Beggar Ghoul (ToB1-2023)"
"size": "Medium"
"type": "undead"
"alignment": "Chaotic Evil"
"ac": !!int "12"
"hp": !!int "13"
"hit_dice": "3d8"
"stats":
- !!int "10"
- !!int "15"
- !!int "10"
- !!int "12"
- !!int "11"
- !!int "14"
"speed": "30 ft."
"damage_immunities": "poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 10"
"languages": "Undercommon"
"cr": "1/2"
"traits":
- "desc": "The ghoul requires no air or sleep."
  "name": "Hungry Dead Nature"
- "desc": "The beggar ghoul has advantage on attack rolls against a creature if at\
    \ least one of the beggar ghoul's allies is within 5 feet of the creature and\
    \ the ally isn't [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)."
  "name": "Pack Tactics"
- "desc": "Its Bite attack is a critical hit if the beggar ghoul bites a creature\
    \ it has surprised."
  "name": "Savage Hunger"
"actions":
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 9 (2d6\
    \ + 2) piercing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (2d4\
    \ + 2) slashing damage. If the target is a creature other than an elf or Undead,\
    \ it must succeed on a DC 10 Constitution saving throw or be [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ for 1 minute. A [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ target can repeat the saving throw at the end of each of its turns, ending the\
    \ effect on itself on a success."
  "name": "Claws"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/beggar-ghoul-tob1-2023.webp"
```
^statblock

## Environment

underdark, urban