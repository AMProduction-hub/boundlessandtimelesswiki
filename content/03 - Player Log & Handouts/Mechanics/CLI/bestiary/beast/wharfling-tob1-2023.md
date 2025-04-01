---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1-8
- ttrpg-cli/monster/environment/coastal
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Wharfling"]
---
# [Wharfling](03 - Player Log & Handouts\Mechanics\CLI\bestiary\beast/wharfling-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 395*  

*The hairless canine scurries along the pier, dripping with water and carrying a fish in its jaws. Its finned claws click on the planks as a fishmonger yells from behind it.*

## Waterborne Packs

Wharflings are hairless, aquatic canines with large, webbed feet and oversized mouths. Adept fish catchers, wharflings establish dens near the shores of oceans, lakes, and rivers, and they often move in family groups of three or more.

## Thieving Gits

Those who have been bitten by a wharfling rightly fear their needle-like teeth, but most coastal communities hate the animal more for its propensity for theft. Their lairs are filled with stolen metal trinkets.

## Beach Swarms

Periodically, wharflings congregate in huge numbers and tear along the shoreline for miles before returning to their dens. Why they gather this way is unknown, but most locals know to avoid the shore on these nights.

```statblock
"name": "Wharfling (ToB1-2023)"
"size": "Tiny"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "10"
"hit_dice": "4d4"
"stats":
- !!int "4"
- !!int "14"
- !!int "10"
- !!int "2"
- !!int "12"
- !!int "8"
"speed": "30 ft., climb 10 ft., swim 30 ft."
"skillsaves":
  "Sleight of Hand": !!int "4"
  "Perception": !!int "3"
"senses": "darkvision 60 ft., passive Perception 13"
"languages": ""
"cr": "1/8"
"traits":
- "desc": "The wharfling can breathe air and water."
  "name": "Amphibious"
"actions":
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4\
    \ + 2) piercing damage. Instead of dealing damage, the wharfling can steal one\
    \ item the target is wearing or carrying, provided the item weighs no more than\
    \ 10 pounds, isn't a weapon, and isn't wrapped around or firmly attached to the\
    \ target, such as a shirt or armor."
  "name": "Pilfering Bite"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/beast/token/wharfling-tob1-2023.webp"
```
^statblock

## Environment

coastal, underwater