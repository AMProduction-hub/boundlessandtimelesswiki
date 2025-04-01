---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/8
- ttrpg-cli/monster/environment/coastal
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Deep One Archimandrite"]
---
# [Deep One Archimandrite](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/deep-one-archimandrite-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 73*  

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
"name": "Deep One Archimandrite (ToB1-2023)"
"size": "Large"
"type": "humanoid"
"alignment": "Chaotic Evil"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "153"
"hit_dice": "18d10 + 54"
"stats":
- !!int "20"
- !!int "16"
- !!int "17"
- !!int "12"
- !!int "17"
- !!int "19"
"speed": "40 ft., swim 40 ft."
"saves":
  "Charisma": !!int "7"
  "Dexterity": !!int "6"
  "Wisdom": !!int "6"
"skillsaves":
  "Perception": !!int "6"
  "Arcana": !!int "4"
"damage_vulnerabilities": "fire"
"damage_resistances": "cold, thunder"
"senses": "darkvision 240 ft., passive Perception 16"
"languages": "Common, Void Speech"
"cr": "8"
"traits":
- "desc": "The deep one archimandrite casts one of the following spells, requiring\
    \ no material components and using Charisma as the spellcasting ability (spell\
    \ save DC 15):\n\nAt will: [bless](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/bless.md),\
    \ [guidance](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/guidance.md),\
    \ [suggestion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/suggestion.md),\
    \ [thaumaturgy](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/thaumaturgy.md)\n\
    \n1/day each: [augury](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/augury.md),\
    \ [lightning bolt](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/lightning-bolt.md),\
    \ [spirit guardians](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/spirit-guardians.md)\n\
    \n3/day each: [charm person](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/charm-person.md),\
    \ [command](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/command.md),\
    \ [sleep](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/sleep.md)"
  "name": "Spellcasting"
- "desc": "The deep one archimandrite can breathe air and water."
  "name": "Amphibious"
- "desc": "If a deep one archimandrite takes 15 or more damage from a single attack,\
    \ it has advantage on all attack rolls and gains a +4 bonus to all damage rolls\
    \ until the end of its next turn. For the duration, it can make one Unholy Trident\
    \ attack as a bonus action on its turn."
  "name": "Frenzied Rage"
"actions":
- "desc": "The deep one archimandrite makes one Claw attack and one Unholy Trident\
    \ attack, or it makes three Jolt attacks. It can replace one attack with a use\
    \ of Spellcasting."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 18\
    \ (3d8 + 5) slashing damage."
  "name": "Claws"
- "desc": "Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 14\
    \ (2d8 + 5) piercing damage plus 13 (2d12) necrotic damage."
  "name": "Unholy Trident"
- "desc": "Melee or Ranged Spell Attack: +7 to hit, reach 5 ft. or range 60 ft.,\
    \ one target. Hit: 14 (3d6 + 4) lightning damage, and the target's speed is\
    \ reduced by 10 until the end of its next turn."
  "name": "Jolt"
- "desc": "With a ringing shout, the archimandrite magically calls 1d4 reef sharks\
    \ or 1 swarm of quippers, provided the archimandrite is at least partially submerged\
    \ in a body of water that can contain the creatures. The called creatures arrive\
    \ in 1d4 rounds, acting as allies of the archimandrite and obeying its spoken\
    \ commands. The creatures remain for 1 hour, until the archimandrite dies, or\
    \ until the archimandrite dismisses them as a bonus action. Each deep one within\
    \ 1 mile of the archimandrite can hear this call, though these deep ones are under\
    \ no magical compulsion to make their way toward the archimandrite."
  "name": "Call of the Archimandrite (1/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/deep-one-archimandrite-tob1-2023.webp"
```
^statblock

## Environment

coastal, underwater