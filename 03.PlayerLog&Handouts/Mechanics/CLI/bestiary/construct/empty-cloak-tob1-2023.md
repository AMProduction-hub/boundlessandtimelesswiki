---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1-2
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/construct
statblock: inline
aliases: ["Empty Cloak"]
---
# [Empty Cloak](03 - Player Log & Handouts\Mechanics\CLI\bestiary\construct/empty-cloak-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 164*  

*This dark cloth of black and purple, stitched with silver and golden threads, resembles a garment of elvish make. Smoke sometimes billows under the hood.*

## Silent Motion

A billowing empty cloak glides through the air, either under its own power or on the shoulders of its master. Its movement appears odd somehow, as though it moves slightly out of step with the frame bearing it.

## Guards

Created by the shadow fey as unobtrusive guardians, empty cloaks are often paired with animated armor or other constructs like monolith footmen, and made to look like a display piece.

## Shadow Servants

Shadow fey nobles sometimes wear an empty cloak as their own clothing, using it to cover a hasty retreat or to assist in a kidnapping.

```statblock
"name": "Empty Cloak (ToB1-2023)"
"size": "Medium"
"type": "construct"
"alignment": "Neutral"
"ac": !!int "13"
"ac_class": "natural armor"
"hp": !!int "45"
"hit_dice": "10d8"
"stats":
- !!int "18"
- !!int "14"
- !!int "10"
- !!int "10"
- !!int "10"
- !!int "1"
"speed": "0 ft., fly 40 ft."
"saves":
  "Dexterity": !!int "4"
  "Constitution": !!int "2"
"skillsaves":
  "Stealth": !!int "4"
  "Perception": !!int "2"
"damage_vulnerabilities": "fire"
"damage_resistances": "bludgeoning"
"damage_immunities": "poison, psychic"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 12"
"languages": "understands Elvish and Umbral but can't speak"
"cr": "1/2"
"traits":
- "desc": "The empty cloak doesn't require air, food, drink, or sleep."
  "name": "Construct Nature"
- "desc": "The empty cloak has advantage on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks."
  "name": "Diligent Sentinel"
- "desc": "Made mostly of shadow, the empty cloak bursts into pieces then dissipates\
    \ when a creature scores a critical hit against it."
  "name": "Shadow Construction"
- "desc": "The empty cloak can occupy a Medium or smaller creature's space and vice\
    \ versa. It has advantage on attack rolls against any creature in the same space\
    \ as it."
  "name": "Wrapping Embrace"
"actions":
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d8\
    \ + 4) slashing damage."
  "name": "Razor Cloak"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft, one target. Hit: 6 (1d4\
    \ + 4) bludgeoning damage."
  "name": "Shadow Slam"
- "desc": "Ranged Weapon Attack: +4 to hit, range 20/60 ft., one Large or smaller\
    \ creature. Hit: The target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 14). Until this grapple ends, the target is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ by tendrils of shadow. A creature, including the [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ creature, can take its action to free the [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ creature by succeeding on a DC 14 Strength check. The tendrils of shadow can\
    \ be attack and destroyed (AC 12; hp 10; vulnerability to radiant damage; immunity\
    \ to necrotic, poison, and psychic damage)."
  "name": "Shadow Snare"
"bonus_actions":
- "desc": "When a creature the cloak can see attacks a creature in the cloak's space,\
    \ the cloak can briefly wrap itself around the creature in its space. The creature\
    \ in its space takes only half the damage from the attack, and the cloak takes\
    \ the other half."
  "name": "Protective Embrace"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/construct/token/empty-cloak-tob1-2023.webp"
```
^statblock

## Environment

urban