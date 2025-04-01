---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1-2
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/construct
statblock: inline
aliases: ["Xanka"]
---
# [Xanka](03 - Player Log & Handouts\Mechanics\CLI\bestiary\construct/xanka-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 399*  

*This small metallic globe skitters about on many-jointed legs.*

## Cleaning Constructs

Created by gnomish tinkerers, xanka are constructs whose purpose is cleaning up their masters' messy workshops. Most xanka are built from copper, brass, or bronze, but gold, silver, and platinum varieties have been seen in the houses of nobles and rich merchants. Xanka are not built for fighting—their instinct tells them to skitter for cover when danger threatens—but they defend themselves when cornered.

## Follow Commands

These constructs understand and obey simple commands that relate to the removal of garbage. They can communicate with each other through whirs, clicks, and flashing lights, but those who have studied this communication find it is rarely more than a relaying of commands from the master between xanka to more efficiently carry out the master's wishes.

## Absorb Matter

When a xanka touches material to its globular body, it absorbs that material into itself, quickly breaking the material down into magical energy. They can use this energy to power themselves for further tasks or to protect themselves from danger by expelling the energy in a burst. Tinkerers use xanka to keep their homes and cities clear of refuse.

```statblock
"name": "Xanka (ToB1-2023)"
"size": "Small"
"type": "construct"
"alignment": "Unaligned"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "27"
"hit_dice": "6d6 + 6"
"stats":
- !!int "10"
- !!int "15"
- !!int "12"
- !!int "4"
- !!int "10"
- !!int "7"
"speed": "25 ft., climb 15 ft."
"damage_resistances": "force"
"damage_immunities": "poison, psychic"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "blindsight 120 ft., passive Perception 10"
"languages": "understands the languages of its creator but can't speak"
"cr": "1/2"
"traits":
- "desc": "Any nonmagical object that touches the xanka's central globe, any nonmagical\
    \ weapon that hits the xanka, or any nonmagical object, structure, or creature\
    \ hit by the xanka's Dismantling Leg attack begins to deteriorate. If it is a\
    \ structure or an object that isn't being worn or carried, up to a 1-foot cube\
    \ of the structure or object is destroyed.\n\nIf it is an object worn or carried\
    \ by a creature, the creature must succeed on a DC 11 Dexterity saving throw to\
    \ avoid the item being affected by the xanka's Absorb. If the object is a weapon,\
    \ the weapon takes a permanent and cumulative -1 penalty to damage rolls. If the\
    \ weapon's penalty drops to -5, the weapon is destroyed. If the object is armor\
    \ or a shield, the armor or shield takes a permanent and cumulative -1 penalty\
    \ to the AC it offers. Armor reduced to an AC of 10 or a shield that drops to\
    \ a +0 bonus is destroyed. If the target is a creature, the creature must succeed\
    \ on a DC 11 Constitution saving throw or take 2 (1d4) necrotic damage."
  "name": "Absorb"
- "desc": "The xanka doesn't require air, food, drink, or sleep."
  "name": "Construct Nature"
"actions":
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8\
    \ + 2) bludgeoning damage, and the target is subjected to the xanka's Absorb\
    \ trait."
  "name": "Dismantling Leg"
- "desc": "The xanka releases energy created from absorbed material in a burst. Each\
    \ creature within 10 feet of it must make a DC 11 Dexterity saving throw, taking\
    \ 7 (2d6) force damage on a failed save, or half as much damage on a successful\
    \ one."
  "name": "Release Energy (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/construct/token/xanka-tob1-2023.webp"
```
^statblock

## Environment

urban