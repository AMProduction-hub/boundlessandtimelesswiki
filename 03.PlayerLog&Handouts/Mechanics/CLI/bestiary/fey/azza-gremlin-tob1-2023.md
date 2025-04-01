---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1-4
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Azza Gremlin"]
---
# [Azza Gremlin](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/azza-gremlin-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 222*  

*These tiny, hairless, rail-thin creatures crackle with static electricity. Arcs of lightning snap between their long ears.*

## Lightning Lovers

Azza gremlins live among storm clouds, lightning-based machinery, and other places with an abundance of lightning.

## Magnetic Flight

Although wingless, their light bodies are perfectly attuned to electromagnetic fields, giving them buoyancy and flight. They love playing in thunderstorms and riding lightning bolts between the clouds or between clouds and the ground. They feed off lightning and love to see its effects on other creatures.

## Work with Spellcasters

Although they aren't much more than hazardous pests by themselves, more malicious creatures and spellcasters that use lightning as a weapon work with azza gremlins to amplify their own destructiveness. Azza gremlins stand 12 to 18 inches tall and weigh approximately 8 pounds.

```statblock
"name": "Azza Gremlin (ToB1-2023)"
"size": "Small"
"type": "fey"
"alignment": "Neutral"
"ac": !!int "14"
"hp": !!int "7"
"hit_dice": "2d6"
"stats":
- !!int "5"
- !!int "18"
- !!int "10"
- !!int "12"
- !!int "13"
- !!int "16"
"speed": "10 ft., fly 40 ft. (hover)"
"damage_immunities": "lightning, thunder"
"senses": "darkvision 120 ft., passive Perception 11"
"languages": "Common, Primordial"
"cr": "1/4"
"traits":
- "desc": "A creature that touches the azza gremlin or hits it with a metal weapon\
    \ while within 5 feet of it receives a discharge of lightning. The creature must\
    \ succeed on a DC 10 Constitution saving throw or attract lightning for 1 minute.\
    \ For the duration, attacks that deal lightning damage have advantage against\
    \ the affected creature, the creature has disadvantage on saving throws against\
    \ spells and effects that deal lightning damage, and if the creature takes lightning\
    \ damage, it is [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ until the end of its next turn. An affected creature can repeat the saving throw\
    \ at the end of each of its turns, ending the effect on itself on a success."
  "name": "Contagious Lightning"
"actions":
- "desc": "Melee or Ranged Spell Attack: +5 to hit, reach 5 ft. or range 30 ft.,\
    \ one creature. Hit: 6 (1d6 + 3) lightning damage, and the target must succeed\
    \ on a DC 10 Constitution saving throw or be affected by Contagious Lightning."
  "name": "Lightning Jolt"
"reactions":
- "desc": "The azza gremlin can travel instantly along any bolt of lightning. When\
    \ a bolt of lightning strikes or an effect deals lightning damage within 30 feet\
    \ of the gremlin, it can teleport to an unoccupied space within 5 feet of where\
    \ the lightning struck or dealt damage."
  "name": "Ride the Bolt"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/azza-gremlin-tob1-2023.webp"
```
^statblock

## Environment

grassland