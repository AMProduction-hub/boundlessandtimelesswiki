---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Dau"]
---
# [Dau](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/dau-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 69*  

*A constant shimmer surrounds this short, winged creature. Staring at it is eye-watering and confusing, like a distant desert mirage, though it's scant yards away.*

## Desert Mirage Fey

Daus are creatures of haze and illusion. They stand three feet tall, with sandy skin, and are surrounded by a shimmering aura like a heat haze. They are flighty, physically weak, and unfocused, but agile in body and wit.

## Lazy and Bored

Their ability to magically provide for themselves in most material ways tends to make daus lazy and hedonistic. As a result, daus are often friendly and eager for company. They invite friends and strangers alike to rest in their lairs, partake in their feasts, and share their stories.

## Sticklers for Etiquette

However, a dau's hospitality turns to cruelty when guests breach its intricate rules of etiquette.

```statblock
"name": "Dau (ToB1-2023)"
"size": "Small"
"type": "fey"
"alignment": "Chaotic Neutral"
"ac": !!int "13"
"hp": !!int "49"
"hit_dice": "9d6 + 18"
"stats":
- !!int "7"
- !!int "17"
- !!int "14"
- !!int "14"
- !!int "17"
- !!int "16"
"speed": "20 ft., fly 60 ft. (hover)"
"skillsaves":
  "Deception": !!int "5"
  "Stealth": !!int "5"
  "Insight": !!int "5"
  "Perception": !!int "5"
"senses": "darkvision 60 ft., passive Perception 15"
"languages": "Deep Speech, Primordial, Sylvan, telepathy 60 ft."
"cr": "4"
"traits":
- "desc": "The dau casts one of the following spells, requiring no material components\
    \ and using Charisma as the spellcasting ability (spell save DC 13):\n\nAt will:\
    \ [detect thoughts](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/detect-thoughts.md),\
    \ [minor illusion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/minor-illusion.md)\n\
    \n1/day each: [programmed illusion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/programmed-illusion.md),\
    \ [project image](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/project-image.md)\n\
    \n3/day each: [invisibility](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/invisibility.md),\
    \ [major image](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/major-image.md)"
  "name": "Spellcasting"
- "desc": "The dau has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
"actions":
- "desc": "The dau makes two Slam attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one creature. Hit: 6\
    \ (1d6 + 3) bludgeoning damage plus 10 (3d6) necrotic damage, and the dau\
    \ regains hp equal to the necrotic damage dealt. The target must succeed on a\
    \ DC 13 Constitution saving throw or its hp maximum is reduced by an amount equal\
    \ to the necrotic damage dealt. This reduction lasts until the creature finishes\
    \ a long rest. The creature dies if this effect reduces its hp maximum to 0."
  "name": "Slam"
"reactions":
- "desc": "When a creature the dau can see within 30 feet of it attacks the dau or\
    \ targets it with a spell, the dau replaces itself with an illusory duplicate\
    \ and teleports to any unoccupied space that it can see within 30 feet. The dau\
    \ isn't affected by the attack or spell, and the illusory duplicate is destroyed."
  "name": "Mirror Dodge"
- "desc": "When the dau casts a spell that creates an illusion of an object, the dau\
    \ temporarily transforms that illusion into a physical, nonmagical object. The\
    \ temporary object lasts 10 minutes, after which it reverts to being an illusion\
    \ (or vanishes, if the duration of the original illusion expires). During that\
    \ time, the illusion has all the physical properties of the object it represents,\
    \ but it doesn't have any of the object's magical properties. The dau must touch\
    \ the illusion to trigger this transformation, and the object can be no larger\
    \ than 5 cubic feet."
  "name": "Tangible Illusion (1/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/dau-tob1-2023.webp"
```
^statblock

## Environment

desert