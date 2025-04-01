---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/8
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Arcane Guardian"]
---
# [Arcane Guardian](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/arcane-guardian-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 338*  

*A luminous green mist swirls into the form of an ancient warrior. Dented armor and a ragged cloak enshroud the warrior's skeletal body, and its grinning skull leers out from an open helm.*

Some spectral guardians were not warriors in life, but powerful spellcasters.

## Worn Finery

Composed of faintly glowing green vapor, the arcane guardian is a skeletal being encased in ancient armor or noble's finery. The cloth is worn and tattered, spiraling away into mist at the edges, and the creature glides with the faintest whisper of sound.

## Eternal Disgrace

The arcane guardian is the spirit of an ancient warrior or noble, bound to serve in death as it failed to do in life. A broken oath, an act of cowardice, or a curse laid down by the gods for a terrible betrayal leaves an indelible mark on a soul. After the cursed creature's death, its spirit rises in a place closely related to its disgrace. Compelled by the crushing weight of its deeds, the arcane guardian knows no rest or peace.

```statblock
"name": "Arcane Guardian (ToB1-2023)"
"size": "Medium"
"type": "undead"
"alignment": "Neutral Evil"
"ac": !!int "14"
"hp": !!int "127"
"hit_dice": "15d8 + 60"
"stats":
- !!int "6"
- !!int "18"
- !!int "18"
- !!int "11"
- !!int "16"
- !!int "18"
"speed": "0 ft., fly 60 ft."
"saves":
  "Dexterity": !!int "7"
  "Wisdom": !!int "6"
"damage_resistances": "acid; fire; lightning; thunder; bludgeoning, piercing, slashing\
  \ from nonmagical attacks"
"damage_immunities": "cold, necrotic, poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
  \ [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)"
"senses": "blindsight 10 ft., darkvision 60 ft., passive Perception 13"
"languages": "understands the languages it knew in life but can't speak"
"cr": "8"
"traits":
- "desc": "The arcane guardian casts one of the following spells, requiring no material\
    \ components and using Charisma as the spellcasting ability (spell save DC 15):\n\
    \nAt will: [dancing lights](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dancing-lights.md),\
    \ [fog cloud](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/fog-cloud.md),\
    \ [minor illusion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/minor-illusion.md)\n\
    \n1/day each: [Bigby's hand](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/bigbys-hand.md)\n\
    \n3/day each: [fear](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/fear.md),\
    \ [slow](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/slow.md)"
  "name": "Spellcasting"
- "desc": "The arcane guardian is bound to a tomb, castle ruins, or other place related\
    \ to the disgrace in life that caused it to rise as a arcane guardian in death.\
    \ If the guardian starts its turn more than 1 mile from its bound location, it\
    \ loses its Spectral Blade action until it returns to the region. If it remains\
    \ outside the region, it automatically teleports back to its bound location after\
    \ 24 hours, regardless of distance."
  "name": "Disgrace Bound"
- "desc": "The arcane guardian can move through other creatures and objects as if\
    \ they were difficult terrain. It takes 5 (1d10) force damage if it ends its\
    \ turn inside an object."
  "name": "Incorporeal Movement"
- "desc": "The arcane guardian doesn't require air, food, drink, or sleep."
  "name": "Undead Nature"
"actions":
- "desc": "The arcane guardian makes three Spectral Burst attacks. It can replace\
    \ one attack with a use of Spellcasting."
  "name": "Multiattack"
- "desc": "Melee or Ranged Spell Attack: +7 to hit, reach 5 ft. or range 120 ft.,\
    \ one target. Hit: 9 (1d10 + 4) force damage plus 9 (2d8) necrotic damage."
  "name": "Spectral Burst"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/arcane-guardian-tob1-2023.webp"
```
^statblock

## Environment

any, urban