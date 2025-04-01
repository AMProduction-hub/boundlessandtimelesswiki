---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Rat King"]
---
# [Rat King](03 - Player Log & Handouts\Mechanics\CLI\bestiary\monstrosity/rat-king-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 300*  

*A great knot of scabrous rats scrabbles together as a mass, with skulls, bones, and flesh entangled in the whole. Teeth, eyes, and fur all flow as a single disturbing rat swarm walking on two legs.*

## Fused at the Tail

A rat king forms when dozens of rats twist their tails together in a thick knot of bone and lumpy cartilage—and offer praise to the rat demon Chittr'k'k (see*Creature Codex*). Its numbers and powers grow quickly

## Rule Sewers and Slums

The rat king is a cunning creature that stalks city sewers, boneyards, and slums. Some even command entire thieves' guilds or hordes of beggars that give it obeisance. They grow larger and more powerful over time until discovered.

## Plague and Dark Magic

The rat king is the result of plague infused with twisted magic, and a malignant ceremony that creates one is called "Enthroning the Rat King." Rats afflicted with virulent leavings of dark magic rites or twisted experiments become bound to one another. As more rats add to the mass, the creature's intelligence and force of will grow.

```statblock
"name": "Rat King (ToB1-2023)"
"size": "Medium"
"type": "monstrosity"
"alignment": "Chaotic Evil"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "76"
"hit_dice": "9d8 + 36"
"stats":
- !!int "6"
- !!int "16"
- !!int "18"
- !!int "11"
- !!int "15"
- !!int "16"
"speed": "30 ft., burrow 20 ft."
"skillsaves":
  "Stealth": !!int "6"
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
  \ [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)"
"senses": "darkvision 60 ft., passive Perception 12"
"languages": "Common, Thieves' cant"
"cr": "5"
"traits":
- "desc": "The rat king has advantage on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on smell."
  "name": "Keen Smell"
- "desc": "The rat king radiates a magical aura of misfortune. A creature that starts\
    \ its turn within 15 feet of the rat king must succeed on a DC 14 Charisma saving\
    \ throw or have disadvantage on attack rolls and saving throws until the start\
    \ of its next turn."
  "name": "Plague of Ill Omen"
"actions":
- "desc": "The rat king makes two Bite attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 10\
    \ (2d6 + 3) piercing damage plus 7 (2d6) poison damage. If the target is a\
    \ creature, it must succeed on a DC 14 Constitution saving throw or suffer one\
    \ level of [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion)\
    \ and become infected with a disease. Until the disease is cured, at the end of\
    \ each long rest, the creature must repeat the saving throw. On a failure, the\
    \ creature suffers another level of [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion).\
    \ The [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion)\
    \ lasts until the creature finishes a long rest after the disease is cured. A\
    \ creature that succeeds on two saving throws recovers from the disease."
  "name": "Bite"
- "desc": "The rat king magically calls 2d4 rats, 1d4 giant rats, or 1 swarm of\
    \ rats. The rats arrive in 1d4 rounds, acting as allies of the rat king and\
    \ obeying its spoken commands. The rats remain for 1 hour, until the rat king\
    \ dies, or until the rat king dismisses them as a bonus action."
  "name": "Call Rats (1/Day)"
"reactions":
- "desc": "When a friendly rat, giant rat, or swarm of rats starts its turn within\
    \ 5 feet of the rat king, the rat king can absorb it. If the rat king does so,\
    \ the target dies, and the rat king gains temporary hp equal to the target's remaining\
    \ hp."
  "name": "Absorption"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/monstrosity/token/rat-king-tob1-2023.webp"
```
^statblock

## Environment

urban