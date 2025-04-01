---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/arctic
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Swarm of Wolf Spirits"]
---
# [Swarm of Wolf Spirits](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/swarm-of-wolf-spirits-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 358*  

*A pack of ghostly wolves appears in a swirl of greenish fog, coalescing from the fog itself.*

When a pack of wolves dies of hunger or chill in the deep winter, sometimes the pack leader's rage at a cruel death—or the summoning call of a necromancer—brings the entire pack back to the mortal world as a slavering pack of greenish, translucent apparitions that glides swiftly over snow and ice, or even rivers and lakes.

## Dozen-Eyed Hunters

At night such a swarm can appear as little more than a mass of swirling mist, but when it prepares to attack, the mist condenses into a dozen or more snarling wolf heads with glowing red eyes that trail off into tendrils of fog. A wolf spirit swarm does not eat, but the urge to hunt and kill is as strong as ever.

## Absorb Their Kill

Most such swarms serve powerful undead, warlocks, noctiny, or orcish shamans as guardians and enforcers, terrifying horses and henchmen alike. The souls of those slain by the pack are said to join it.

## Howl Before Combat

Hirelings, mounts, and familiars often panic at the sound of a spirit pack's chilling howl. Packs of wolf spirits are canny enough to always howl for a time before rushing a herd or encampment.

```statblock
"name": "Swarm of Wolf Spirits (ToB1-2023)"
"size": "Large"
"type": "undead"
"alignment": "Neutral Evil"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "104"
"hit_dice": "16d10 + 16"
"stats":
- !!int "14"
- !!int "18"
- !!int "12"
- !!int "4"
- !!int "10"
- !!int "12"
"speed": "50 ft., fly 50 ft. (hover)"
"saves":
  "Dexterity": !!int "7"
  "Wisdom": !!int "3"
"skillsaves":
  "Stealth": !!int "7"
  "Perception": !!int "3"
"damage_resistances": "acid, bludgeoning, fire, lightning, necrotic, piercing, slashing,\
  \ thunder"
"damage_immunities": "cold, poison"
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
"senses": "darkvision 120 ft., passive Perception 13"
"languages": "understands Common but can't speak"
"cr": "6"
"traits":
- "desc": "The swarm of wolf spirits can move through other creatures and objects\
    \ as if they were difficult terrain. It takes 5 (1d10) force damage if it ends\
    \ its turn inside an object."
  "name": "Incorporeal Movement"
- "desc": "The swarm can occupy another creature's space and vice versa. The swarm\
    \ can't regain hp or gain temporary hp."
  "name": "Swarm"
- "desc": "The swarm of wolf spirits doesn't require air, food, drink, or sleep."
  "name": "Undead Nature"
"actions":
- "desc": "The swarm of wolf spirits makes two Spectral Bites attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 0 ft., one creature in the swarm's\
    \ space. Hit: 14 (4d6) cold damage plus 9 (2d8) necrotic damage, or 7 (2d6)\
    \ cold damage plus 4 (1d8) necrotic damage if the swarm has half of its hp or\
    \ fewer."
  "name": "Spectral Bites"
- "desc": "The swarm of wolf spirits howls, causing cold fear to course through those\
    \ that hear it. Each creature within 15 feet that can hear the howl must make\
    \ a DC 15 Constitution saving throw. On a failure, a creature takes 35 (10d6)\
    \ cold damage and is [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ for 1 minute. On a success, a creature takes half the damage and isn't [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened).\
    \ A creature that fails the saving throw by 5 or more also suffers one level of\
    \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion).\
    \ A [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ creature can make a DC 15 Wisdom saving throw at the end of each of its turns,\
    \ ending the effect on itself on a success."
  "name": "Chilling Howl (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/swarm-of-wolf-spirits-tob1-2023.webp"
```
^statblock

## Environment

arctic