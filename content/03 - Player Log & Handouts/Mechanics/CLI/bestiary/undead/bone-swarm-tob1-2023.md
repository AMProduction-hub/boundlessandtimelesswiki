---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/10
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/environment/mountain
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Bone Swarm"]
---
# [Bone Swarm](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/bone-swarm-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 41*  

*Dank winds sweep up skeletons, both humanoid and animal. They blow forward, reaching out for living creatures like a clawed hand of bone. A scattering of bones rolls across the ground, then rises into the air, billowing like a sheet*.

## Swarms of Fallen

On rare occasions, the pugnacious spirits of fallen undead join together, bonded by a common craving: to feel alive again. They gather up their bones from life, as well as any other bones they come across, and form bone swarms.

## Nomadic Undead

These swarms ravage the countryside wresting life from living creatures, grabbing livestock, humanoids, and even dragons, digging in their claws in an attempt to cling to life. Bone swarms with one or more sets of jaws wail constantly in their sorrow, interrupting their cries with snippets of rational, but scattered speech declaiming their woes and despair.

## Cliff and Pit Dwellers

Bone swarms gather near cliffs, crevasses, and pits in the hope of forcing a victim or an entire herd of animals to fall to its death, creating more shattered bones to add to their mass.

```statblock
"name": "Bone Swarm (ToB1-2023)"
"size": "Large"
"type": "undead"
"alignment": "Chaotic Evil"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "198"
"hit_dice": "36d10"
"stats":
- !!int "22"
- !!int "18"
- !!int "10"
- !!int "9"
- !!int "15"
- !!int "20"
"speed": "20 ft., fly 60 ft."
"saves":
  "Charisma": !!int "9"
  "Dexterity": !!int "8"
  "Wisdom": !!int "6"
"skillsaves":
  "Stealth": !!int "8"
  "Perception": !!int "6"
  "Acrobatics": !!int "8"
"damage_vulnerabilities": "bludgeoning"
"damage_resistances": "piercing, slashing from nonmagical attacks"
"damage_immunities": "poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
  \ [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
  \ [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)"
"senses": "darkvision 60 ft., passive Perception 16"
"languages": "Common, Void Speech"
"cr": "10"
"traits":
- "desc": "The swarm can occupy another creature's space and vice versa, and the swarm\
    \ can move through any opening large enough for a Tiny human skull. The swarm\
    \ can't regain hp or gain temporary hp."
  "name": "Swarm"
- "desc": "The bone swarm doesn't require air, food, drink, or sleep."
  "name": "Undead Nature"
"actions":
- "desc": "The bone swarm makes two Swirling Bones attacks. It can replace one Swirling\
    \ Bones attack with one Death's Embrace attack, if available."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +10 to hit, reach 0 ft., one creature in the swarm's\
    \ space. Hit: 36 (8d8) bludgeoning, 36 (8d8) piercing, or 36 (8d8) slashing\
    \ damage (the bone swarm's choice), or 18 (4d8) bludgeoning, 8 (4d8) piercing,\
    \ or 8 (4d8) slashing damage (the bone swarm's choice) if the swarm has half\
    \ of its hp or fewer."
  "name": "Swirling Bones"
- "desc": "Melee Weapon Attack: +10 to hit, reach 0 ft., one creature in the swarm's\
    \ space. Hit: The target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 16) if it is a Large or smaller creature. Until this grapple ends,\
    \ the creature is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ and any attack against the bone swarm has a 50 percent chance of hitting the\
    \ [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ creature instead. The bone swarm can have only one creature [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ at a time. The [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ creature has advantage on ability checks made to escape the grapple when the\
    \ bone swarm has half of its hp or fewer."
  "name": "Death's Embrace (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/bone-swarm-tob1-2023.webp"
```
^statblock

## Environment

hill, mountain, urban