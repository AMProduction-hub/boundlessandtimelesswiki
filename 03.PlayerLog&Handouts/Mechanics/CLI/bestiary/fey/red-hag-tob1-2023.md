---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/environment/coastal
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Red Hag"]
---
# [Red Hag](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/red-hag-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 228*  

*The red-skinned woman steps forward, sunlight glinting in her raven hair as red magic swirls around her.*

An elder race—older than the elves, and as old as the dragons, they claim—red hags are the most cunning and longest-lived of the hags, with a lifespan of more than a thousand years.

## Beautiful and Strong

Unlike many of their hag kin, red hags are not horrid to look upon, and most are considered comely in their own right. Few know anything about them, and the red hags do little to enlighten scholars, preferring seclusion.

## Tied to Nature

Red hags have a deep connection with all elements of nature, and they often make their homes in deep forests, in caves, or alongside coastlines.

## Blood Magic

Because of their connection to nature, red hags often serve as druids. Within their druidic circles they practice blood sacrifices and perform ritualistic blood magic—both to slake their craving for humanoid blood, but also as a means to venerate goddesses of dark magic. The ancient hags all answer to a hierarchy with the most powerful spellcasters at the top.

> [!note] Red Hags in Midgard
> 
> Red hags are more sociable among their own kind than other hags are, and they sometimes live in small communities in remote areas. In ancient times, they settled together in larger clusters and ruled small cities of mixed populations—especially in Old Verrayne. Their current leader is Blood Mother Margase, an ancient druid.
> 
> Their greatest city, Talitheos, an island metropolis of vast wealth and magical knowledge, sunk during the cataclysm, and the hags have been seeking its ruins ever since.
^red-hags-in-midgard

```statblock
"name": "Red Hag (ToB1-2023)"
"size": "Medium"
"type": "fey"
"alignment": "Neutral Evil"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "136"
"hit_dice": "16d8 + 64"
"stats":
- !!int "19"
- !!int "16"
- !!int "18"
- !!int "18"
- !!int "21"
- !!int "15"
"speed": "30 ft., swim 30 ft."
"skillsaves":
  "Deception": !!int "5"
  "Insight": !!int "8"
  "Perception": !!int "8"
  "Arcana": !!int "10"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 18"
"languages": "Common, Druidic, Giant, Sylvan"
"cr": "7"
"traits":
- "desc": "The red hag casts one of the following spells, requiring no material components\
    \ and using Wisdom as the spellcasting ability (spell save DC 16):\n\nAt will:\
    \ [animal friendship](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/animal-friendship.md),\
    \ [druidcraft](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/druidcraft.md),\
    \ [entangle](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/entangle.md)\n\
    \n1/day: [control water](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/control-water.md),\
    \ [freedom of movement](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/freedom-of-movement.md)\n\
    \n3/day: [cure wounds](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/cure-wounds.md),\
    \ [dispel magic](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dispel-magic.md),\
    \ [lesser restoration](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/lesser-restoration.md)"
  "name": "Spellcasting"
- "desc": "The red hag can breathe air and water."
  "name": "Amphibious"
- "desc": "The red hag can pinpoint the location of creatures that aren't Constructs\
    \ or Undead within 60 feet of her and can sense the general direction of such\
    \ creatures within 1 mile of her."
  "name": "Blood Sense"
- "desc": "The red hag has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "The red hag can communicate with Beasts as if they shared a language."
  "name": "Speak with Beasts"
"actions":
- "desc": "The hag makes two Claw attacks or three Blood Bolt attacks. She can replace\
    \ one attack with a use of Spellcasting."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 13\
    \ (2d8 + 4) slashing damage plus 9 (2d8) necrotic damage."
  "name": "Claw"
- "desc": "Ranged Spell Attack: +8 to hit, range 60 ft., one target. Hit: 14\
    \ (2d8 + 5) necrotic damage. If the target is a creature with blood, it must\
    \ succeed on a DC 16 Constitution saving throw or be [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ until the end of its next turn."
  "name": "Blood Bolt"
- "desc": "The red hag drains blood from nearby creatures. Each creature that isn't\
    \ a Construct or Undead within 20 feet of the red hag must make a DC 16 Constitution\
    \ saving throw, taking 35 (10d6) necrotic damage on a failed save, or half as\
    \ much damage on a successful one. If at least one creature fails the saving throw,\
    \ the next spell the red hag casts is cast as if the spell used a spell slot two\
    \ levels higher than the spell's lowest level."
  "name": "Siphon Blood (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/red-hag-tob1-2023.webp"
```
^statblock

## Environment

coastal, forest, underdark