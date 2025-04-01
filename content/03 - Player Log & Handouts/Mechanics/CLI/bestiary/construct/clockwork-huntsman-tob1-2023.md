---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/construct
statblock: inline
aliases: ["Clockwork Huntsman"]
---
# [Clockwork Huntsman](03 - Player Log & Handouts\Mechanics\CLI\bestiary\construct/clockwork-huntsman-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 62*  

*The mechanical soldier is clad in flat-black armor, and beneath its breastplate, gears tick and whir.*

## Slave Hunters

These metal huntsmen were once the province of corrupt aristocrats, running down escaped slaves and tracking prey in hunting expeditions. Their masters may vary, but the clockwork huntsmen still perform when called upon. In some places, they operate only on the command of the secret police, hunting down persons of interest wanted for questioning. Huntsmen may operate alone, but usually they seek their quarry in a group of two or three. Because they are unsleeping and tireless, few can hide from them long without magical assistance.

## Despised Machines

Clockwork huntsmen stand nearly six feet tall and weigh 400 pounds. They are painted matte black with mithral trim and occasionally outfitted with armor or a black steel blade for added intimidation. Common folk detest them; all but their keepers and commanders shun them.

## Obedient to Orders

Bound with specific instructions, clockwork huntsmen patrol, stand sentry, or remain unmoving as ordered, always paying attention, alert to their surroundings. Clockwork huntsmen are unrelenting and single-minded in their missions, focusing on particular targets—priests, spellcasters, or heavily armored intruders, as directed. Oblivious to injury, clockwork huntsmen attack until destroyed or ordered to stand down.

```statblock
"name": "Clockwork Huntsman (ToB1-2023)"
"size": "Medium"
"type": "construct"
"alignment": "Unaligned"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "99"
"hit_dice": "18d8 + 18"
"stats":
- !!int "17"
- !!int "14"
- !!int "12"
- !!int "4"
- !!int "10"
- !!int "1"
"speed": "40 ft."
"saves":
  "Dexterity": !!int "4"
  "Strength": !!int "5"
"skillsaves":
  "Perception": !!int "4"
  "Survival": !!int "4"
"damage_immunities": "poison, psychic"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 14"
"languages": "understands Common but can't speak"
"cr": "3"
"traits":
- "desc": "The clockwork huntsman doesn't require air, food, drink, or sleep."
  "name": "Construct Nature"
- "desc": "The mechanism that powers the huntsman explodes when the construct is destroyed,\
    \ projecting superheated steam and shrapnel. Each creature within 5 feet of the\
    \ huntsman when it is destroyed must make a DC 13 Dexterity saving throw, taking\
    \ 10 (3d6) fire damage on a failed save, or half as much damage on a successful\
    \ one."
  "name": "Explosive Core"
- "desc": "The clockwork huntsman is immune to any spell or effect that would alter\
    \ its form."
  "name": "Immutable Form"
- "desc": "The clockwork huntsman has advantage on saving throws against spells and\
    \ other magical effects."
  "name": "Magic Resistance"
"actions":
- "desc": "The clockwork huntsman makes one Slam attack and two Longsword attacks.\
    \ It can replace its Slam attack with a Net Cannon attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8\
    \ + 3) slashing damage."
  "name": "Longsword"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10\
    \ (2d6 + 3) bludgeoning damage."
  "name": "Slam"
- "desc": "Ranged Weapon Attack: +4 to hit, range 10/20 ft., one target. Hit:\
    \ If the target is a Large or smaller creature, it is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained).\
    \ A mechanism within the clockwork huntsman's chest can fire a net with a 20-foot\
    \ trailing cable anchored within its chest. A creature, including the [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ creature, can take its action to free the [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ creature by succeeding on a DC 10 Strength check. Alternatively, dealing 5 slashing\
    \ damage to the net (AC 10) frees the creature."
  "name": "Net Cannon (4/Day)"
"bonus_actions":
- "desc": "The clockwork huntsman pulls a creature [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ by its net up to 15 feet straight toward it."
  "name": "Reel"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/construct/token/clockwork-huntsman-tob1-2023.webp"
```
^statblock

## Environment

urban