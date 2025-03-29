---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/coastal
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Deep One Priest"]
---
# [Deep One Priest](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/deep-one-priest-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 72*  

*These fishlike folk have enormous eyes, a wide mouth, and almost no chin.*

## Elder Gods

In their fully grown form, the deep ones are an ocean-dwelling race that worships elder gods such as Father Dagon and Mother Hydra, and they dwell in deep water darkness. In some areas, they intermarry with coastal humans to create human-deep one hybrids.

## Coastal Raiders

The deep ones keep to themselves in isolated coastal villages and settlements in the deep ocean for long periods, and then, at the command of their patron gods, turn suddenly into strong, relentless raiders, seizing territory, slaves, and wealth all along the coasts. Some deep ones have even founded small kingdoms lasting generations in backwater reaches or distant, chilled seas.

## Demand Sacrifices

They demand tolls from mariners frequently; those who do not leave tribute at certain islands or along certain straits find the fish escape their nets, or the storms shatter their hulls and drown their sailors. Some seafaring nations have found it more profitable to ally themselves with the deep ones; this is the first step in their patient plans to dominate and rule.

## Ocean Change

A deep one born to a human family resembles a human child, but the person transforms into an adult deep one between the ages of 16 and 30. Such deep ones then hear the siren call of their elder god masters and oceanic cousins, which eventually supplants the love the person might feel for family and friends on land.

> [!note] Gods of the Deep Ones
> 
> The deep ones are faithful servants of horrific powers inimical to all life on land. Father Dagon is a god of fertility, fish, and the strength of the deep ocean and is an evil lord of storm and waves. Mother Hydra is his consort, a goddess of immense strength and size, spawning entire schools of fish at once. She is mistress of the great kraken and toothsome krake spawn, who are her children and servitors. Both deities plot conquest through a long program of forced interbreeding and eldritch meddling with human bloodlines.
> 
> In addition, many deep ones follow Shar-Ngolyeth, a long-lost deity referred to as That Which Lurks Beneath the Waves. This kraken and her krake spawn offspring are close allies to the deep ones, but they are largely indifferent to Dagon and Hydra.
^gods-of-the-deep-ones

```statblock
"name": "Deep One Priest (ToB1-2023)"
"size": "Medium"
"type": "humanoid"
"alignment": "Chaotic Evil"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "105"
"hit_dice": "14d8 + 42"
"stats":
- !!int "18"
- !!int "14"
- !!int "16"
- !!int "12"
- !!int "12"
- !!int "16"
"speed": "30 ft., swim 30 ft."
"saves":
  "Charisma": !!int "5"
  "Wisdom": !!int "3"
  "Constitution": !!int "5"
"skillsaves":
  "Athletics": !!int "6"
  "Deception": !!int "5"
  "Perception": !!int "3"
"damage_vulnerabilities": "fire"
"damage_resistances": "cold"
"senses": "darkvision 120 ft., passive Perception 13"
"languages": "Common, Void Speech"
"cr": "4"
"traits":
- "desc": "The deep one priest casts one of the following spells, requiring no material\
    \ components and using Charisma as the spellcasting ability (spell save DC 13):\n\
    \nAt will: [guidance](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/guidance.md),\
    \ [thaumaturgy](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/thaumaturgy.md)\n\
    \n1/day each: [spirit guardians](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/spirit-guardians.md)\n\
    \n3/day each: [command](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/command.md),\
    \ [sleep](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/sleep.md)"
  "name": "Spellcasting"
- "desc": "The deep one priest can breathe air and water."
  "name": "Amphibious"
- "desc": "If a deep one priest takes 10 or more damage from a single attack, it has\
    \ advantage on melee attack rolls and gains a +4 bonus to melee damage rolls until\
    \ the end of its next turn."
  "name": "Frenzied Rage"
- "desc": "The deep one priest can spend 5 minutes giving a speech in a rolling, droning\
    \ voice that fascinates listeners. At the end of the speech, each creature that\
    \ heard it must succeed on a DC 13 Wisdom saving throw or forget the events of\
    \ the past 10 minutes or keep no memory of the events of the next 5 minutes (the\
    \ priest's choice). On a successful saving throw, a creature is immune to the\
    \ priest's Voice of the Deeps for the next 24 hours."
  "name": "Voice of the Deeps"
"actions":
- "desc": "The deep one priest makes one Claws attack and one Jolting Touch attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 13\
    \ (2d8 + 4) slashing damage."
  "name": "Claws"
- "desc": "Melee Spell Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6\
    \ + 3) lightning damage, and the target's speed is reduced by 10 until the end\
    \ of its next turn."
  "name": "Jolting Touch"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/deep-one-priest-tob1-2023.webp"
```
^statblock

## Environment

coastal, underwater