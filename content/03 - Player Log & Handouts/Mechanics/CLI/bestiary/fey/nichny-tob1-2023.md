---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Nichny"]
---
# [Nichny](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/nichny-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 284*  

*These ancient creatures resemble nothing so much as black cats dressed in sumptuous, archaic, clothing.*

## Xenophobic

The nichny are highly xenophobic and gleefully carnivorous fey who dwell in deep, primeval forests.

## True and False Prophets

Nichny have oracular powers, but they rarely share their prophecies with outsiders. Their prophecies are always delivered in triples, and legend holds that two inevitably prove true and one proves false.

## Answer Three Questions

One final legend claims that if a nichny can be bound with gold or orichalcum chains, it must answer three questions. As with their prophecies, two answers will be true and one will be a lie. All three questions must be posed before any will be answered. When the third answer is given, the nichny and the chains disappear.

> [!note] Nichny in Midgard
> 
> Known as dolia ("fate speakers") in Old Elvish, elven legend says the nichny welcomed the first elves to Midgard. They also gifted the first Emperor of the Elves with three prophecies: humans would cause a great schism and estrangement among the elves, forcing them to flee Midgard; an elfmarked child would be the doom of all elvenkind; and a third prophecy so horrific that the elves erased it with powerful magic.
^nichny-in-midgard

```statblock
"name": "Nichny (ToB1-2023)"
"size": "Medium"
"type": "fey"
"alignment": "Neutral Evil"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "127"
"hit_dice": "17d8 + 51"
"stats":
- !!int "17"
- !!int "19"
- !!int "17"
- !!int "18"
- !!int "18"
- !!int "19"
"speed": "30 ft., climb 30 ft."
"saves":
  "Dexterity": !!int "7"
"skillsaves":
  "Stealth": !!int "7"
  "Insight": !!int "7"
  "Perception": !!int "7"
  "Acrobatics": !!int "7"
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks that\
  \ aren't silvered"
"damage_immunities": "poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)"
"senses": "darkvision 60 ft., passive Perception 17"
"languages": "Elvish, Primordial, Sylvan, Void Speech"
"cr": "6"
"traits":
- "desc": "The nichny is surrounded by an aura that manipulates the luck of those\
    \ near the nichny. Each friendly creature, other than the nichny, within 10 feet\
    \ of the Nichny nichny has a +1 bonus to attack rolls and saving throws. Each\
    \ hostile creature that starts its turn within 10 feet of the nichny must succeed\
    \ on a DC 15 Wisdom saving throw or have disadvantage on attack rolls and saving\
    \ throws until the end of its turn."
  "name": "Aura of Luck"
- "desc": "The nichny has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "The nichny can spend 1 minute conversing with a creature it can see within\
    \ 30 feet of it. During this time, the creature can ask up to three questions\
    \ about the past, present, or future. At the end of the minute, the nichny then\
    \ offers two truthful answers and one false answer, each in the form of a paradox,\
    \ riddle, or cryptic rhyme."
  "name": "Soothsaying (1/Day)"
"actions":
- "desc": "The nichny makes two Claw or Luck-Stealing Bolt attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 13\
    \ (2d8 + 4) slashing damage plus 9 (2d8) force damage."
  "name": "Claw"
- "desc": "Ranged Spell Attack: +7 to hit, range 60 ft., one target. Hit: 22\
    \ (4d8 + 4) force damage, and the target has disadvantage on ability checks\
    \ and attack rolls until the end of its next turn."
  "name": "Luck-Stealing Bolt"
- "desc": "The nichny magically imbues a small stone with good luck. A creature, other\
    \ than the nichny, wearing or carrying the stone has a +1 bonus to saving throws.\
    \ The nichny can have no more than three such stones actively imbued at a time.\
    \ If it imbues a fourth, the effect on the oldest imbued stone ends. The nichny\
    \ can end the magic on any of the stones at any time (no action required)."
  "name": "Create Lucky Stone"
- "desc": "The nichny magically teleports, along with any equipment it is wearing\
    \ or carrying, up to 120 feet to an unoccupied space it can see."
  "name": "Teleport (Recharge 6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/nichny-tob1-2023.webp"
```
^statblock

## Environment

forest