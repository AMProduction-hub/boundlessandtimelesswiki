---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/8
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/construct
statblock: inline
aliases: ["Feyward Tree"]
---
# [Feyward Tree](03 - Player Log & Handouts\Mechanics\CLI\bestiary\construct/feyward-tree-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 186*  

*Dark, bark-like rust encrusts the trunk of this metal tree, and its dull metallic leaves rustle with the sound of sharp metal.*

## Cold Iron Trees

These ferrous constructs are cold-forged in a process taking several years, as bits of rust and other oxidation are cultivated one layer at a time into bark and branches. In this way, the artificers create massive, twisted trunks resembling real, gnarled trees. Green-tinged leaves of beaten cold iron are welded in place by the master craftsmen, and trained warmages bring the construct to life through intense magical rituals rumored to take a full turn of seasons.

## Fey Destroyers

The feyward tree unswervingly obeys the commands of its creators, guarding key points of entry across fey rivers and streams, abandoned sacred groves deep in the forest, suspected faerie rings, or possible elf encampments. Many are released deep in elvish woods with orders to attack any fey on sight. These trees are rarely, if ever, heard from again. Whether they leave a bloody trail of flayed elves in their wake or some fey counter-measure neutralizes them is unknown.

## Growing Numbers

Each year, the feywardens order the construction and release of a handful of feyward trees, trusting in the destructive nature of the constructs. The feywardens leave nothing to chance, flooding fey forests with the constructs over decades.

```statblock
"name": "Feyward Tree (ToB1-2023)"
"size": "Huge"
"type": "construct"
"alignment": "Unaligned"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "126"
"hit_dice": "12d12 + 48"
"stats":
- !!int "25"
- !!int "10"
- !!int "18"
- !!int "3"
- !!int "11"
- !!int "6"
"speed": "20 ft."
"saves":
  "Charisma": !!int "1"
  "Dexterity": !!int "3"
  "Wisdom": !!int "3"
"skillsaves":
  "Perception": !!int "3"
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks that\
  \ aren't adamantine"
"damage_immunities": "lightning, poison, psychic"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 13"
"languages": "understands the languages of its creator but can't speak"
"cr": "8"
"traits":
- "desc": "If the feyward tree takes cold damage, it has disadvantage on attack rolls\
    \ and its speed is halved until the end of its next turn."
  "name": "Aversion to Cold"
- "desc": "The feyward tree doesn't require air, food, drink, or sleep."
  "name": "Construct Nature"
- "desc": "The feyward tree's Razor-Leafed Branch attacks are magical. When the tree\
    \ hits with its Razor-Leafed Branch, the branch deals an extra 9 (2d8) force\
    \ damage (included in the attack)."
  "name": "Enchanted Leaves"
- "desc": "The feyward tree is immune to any spell or effect that would alter its\
    \ form."
  "name": "Immutable Form"
- "desc": "Whenever the feyward tree is subjected to lightning damage, it takes no\
    \ damage and instead regains a number of hp equal to the lightning damage dealt."
  "name": "Lightning Absorption"
- "desc": "The feyward tree has advantage on saving throws against spells and other\
    \ magical effects."
  "name": "Magic Resistance"
- "desc": "A creature within 15 feet of a feyward tree that moves away from it provokes\
    \ an opportunity attack even if the creature takes the Disengage action."
  "name": "Warden's Reach"
"actions":
- "desc": "The feyward tree makes two Razor-Leafed Branch attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +10 to hit, reach 15 ft., one target. Hit: 16\
    \ (2d8 + 7) slashing damage plus 9 (2d8) force damage."
  "name": "Razor-Leafed Branch"
- "desc": "The feyward tree launches a barrage of razor-sharp cold iron leaves from\
    \ its branches. Each creature within 20 feet of the tree must make a DC 15 Dexterity\
    \ saving throw, taking 28 (8d6) slashing damage on a failed save, or half as\
    \ much damage on a successful one."
  "name": "Flaying Leaves (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/construct/token/feyward-tree-tob1-2023.webp"
```
^statblock

## Environment

forest