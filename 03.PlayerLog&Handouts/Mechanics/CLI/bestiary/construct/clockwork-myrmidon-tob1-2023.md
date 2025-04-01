---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/construct
statblock: inline
aliases: ["Clockwork Myrmidon"]
---
# [Clockwork Myrmidon](03 - Player Log & Handouts\Mechanics\CLI\bestiary\construct/clockwork-myrmidon-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 63*  

*This hulking brass and iron creature resembles a giant suit of plate armor. A constant growl issues from its midsection. Its squat head wears an angry expression, and it moves with powerful, determined grace*.

## Elite Machines

Clockwork myrmidons are heavily armored at their joints and at most vital parts. They are much too valuable to undertake patrols or menial labor, and are unleashed only for dangerous situations that clockwork watchmen cannot handle.

## Single Targets

A clockwork myrmidon defends itself but does not initiate combat unless so directed by its master. When it does enter battle, a clockwork myrmidon is unrelenting and single-minded. It attacks one particular target until that foe surrenders, escapes, or is defeated. Unless given other instructions, a clockwork myrmidon attacks whatever enemy is closest to it. A clockwork myrmidon attacks until destroyed or ordered to stand down.

## Alchemical Tricks

A clockwork myrmidon is always outfitted with alchemical fire, acids, grease, and other special devices. An alchemist is required to keep one running well.

```statblock
"name": "Clockwork Myrmidon (ToB1-2023)"
"size": "Large"
"type": "construct"
"alignment": "Unaligned"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "136"
"hit_dice": "16d10 + 48"
"stats":
- !!int "20"
- !!int "14"
- !!int "16"
- !!int "6"
- !!int "10"
- !!int "1"
"speed": "30 ft."
"saves":
  "Dexterity": !!int "5"
  "Strength": !!int "8"
"skillsaves":
  "Athletics": !!int "8"
  "Perception": !!int "6"
"damage_immunities": "poison, psychic"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 16"
"languages": "understands Common but can't speak"
"cr": "6"
"traits":
- "desc": "The clockwork myrmidon's alchemical flame reservoir explodes when the construct\
    \ is destroyed, spraying nearby creatures with burning fuel. Each creature within\
    \ 10 feet of the myrmidon when it is destroyed must make a DC 16 Dexterity saving\
    \ throw, taking 14 (4d6) fire damage on a failed save, or half as much damage\
    \ on a successful one. This explosion doesn't occur if the clockwork myrmidon\
    \ has already fired its alchemical flame jet four times."
  "name": "Alchemical Fireball"
- "desc": "The clockwork myrmidon doesn't require air, food, drink, or sleep."
  "name": "Construct Nature"
- "desc": "The clockwork myrmidon is immune to any spell or effect that would alter\
    \ its form."
  "name": "Immutable Form"
- "desc": "The clockwork myrmidon has advantage on saving throws against spells and\
    \ other magical effects."
  "name": "Magic Resistance"
"actions":
- "desc": "The clockwork myrmidon makes one Slam attack and two Heavy Pick attacks.\
    \ It can replace both Heavy Pick attacks with a use of its Alchemical Flame Jet."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 14\
    \ (2d8 + 5) piercing damage."
  "name": "War Pick"
- "desc": "Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 11\
    \ (1d12 + 5) bludgeoning damage."
  "name": "Slam"
- "desc": "The clockwork myrmidon spews a jet of alchemical fire in a 30-foot line\
    \ that is 5 feet wide. Each creature in the line must make a DC 16 Dexterity saving\
    \ throw, taking 14 (4d6) fire damage on a failed save, or half as much damage\
    \ on a successful one."
  "name": "Alchemical Flame Jet (4/Day)"
"bonus_actions":
- "desc": "The clockwork myrmidon's chest fires a spray of alchemical grease on a\
    \ point on the ground within 30 feet of it. The grease covers a 10-foot square\
    \ centered on that point, and the area is difficult terrain. Each creature standing\
    \ in the area must succeed on a DC 16 Dexterity saving throw or fall [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone).\
    \ A creature that enters the area or ends its turn there must also succeed on\
    \ a DC 16 Dexterity saving throw or fall [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Grease Spray (4/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/construct/token/clockwork-myrmidon-tob1-2023.webp"
```
^statblock

## Environment

urban