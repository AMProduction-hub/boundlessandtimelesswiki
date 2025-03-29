---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1-2
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/construct
statblock: inline
aliases: ["Clockwork Beetle"]
---
# [Clockwork Beetle](03 - Player Log & Handouts\Mechanics\CLI\bestiary\construct/clockwork-beetle-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 60*  

*Gleaming metal and whirring gears make up the form of this elaborate mechanical insect the size of a housecat.*

## Bejeweled Familiars

Forged by talented jewelers and sold to gear-mages and aristocrats, clockwork beetles are highly prized as familiars. Although normally created in the form of metal beetles, their appearance can vary greatly. Some resemble incandescent ladybugs while others have razor-sharp horns reminiscent of deadly stag beetles. Some are fashioned as darkling beetles with prehensile antennae, and even weevil-like designs have been spotted. In the southern deserts, scarab beetle patterns are particularly prized.

## Hidden Timers

The most talented gear-mages occasionally design a clockwork beetle with a hidden countdown clock that silently ticks down over years or even decades. When the counter expires, it triggers a mechanical metamorphosis, causing the beetle to rapidly transform into a completely different clockwork creature—a wondrous surprise known only to the original designer.

## Freed But Foolish

Clockwork beetle swarms form when several of the creatures break free of their creators and bond together in a noisy mass of clattering, mechanical parts. Severed from the bonds of their creators, the swarm lacks the telepathy of singular clockwork beetles and has a reduced mental capacity.

```statblock
"name": "Clockwork Beetle (ToB1-2023)"
"size": "Tiny"
"type": "construct"
"alignment": "Unaligned"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "20"
"hit_dice": "8d4"
"stats":
- !!int "8"
- !!int "16"
- !!int "10"
- !!int "4"
- !!int "12"
- !!int "7"
"speed": "30 ft., fly 50 ft."
"saves":
  "Dexterity": !!int "5"
"skillsaves":
  "Stealth": !!int "5"
"damage_immunities": "poison, psychic"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 11"
"languages": "understands the languages of its creator but can't speak"
"cr": "1/2"
"traits":
- "desc": "The clockwork beetle doesn't require air, food, drink, or sleep."
  "name": "Construct Nature"
- "desc": "The clockwork beetle is immune to any spell or effect that would alter\
    \ its form."
  "name": "Immutable Form"
- "desc": "The clockwork beetle can magically transmit simple messages and images\
    \ to its owner, provided the owner is within 100 feet of it."
  "name": "Limited Telepathy"
- "desc": "The clockwork beetle has advantage on saving throws against spells and\
    \ other magical effects."
  "name": "Magic Resistance"
"actions":
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6\
    \ + 3) piercing damage, and the target must make a DC 10 Constitution saving\
    \ throw, taking 5 (2d4) poison damage on a failed save, or half as much damage\
    \ on a successful one."
  "name": "Bite"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/construct/token/clockwork-beetle-tob1-2023.webp"
```
^statblock

## Environment

urban