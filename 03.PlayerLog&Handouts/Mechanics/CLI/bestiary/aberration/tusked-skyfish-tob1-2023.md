---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/aberration
statblock: inline
aliases: ["Tusked Skyfish"]
---
# [Tusked Skyfish](03 - Player Log & Handouts\Mechanics\CLI\bestiary\aberration/tusked-skyfish-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 372*  

*This creature looks like an enormous flying jellyfish, with long, wicked tusks curving from its gaping mouth and tentaclewhiskers trailing behind it.*

## Alchemical Flotation

These aerial jellyfish waft through the air like balloons, suspended by internal alchemical reactions. This mode of movement takes them vertically when they wish or allows them to drift with the winds. They can reach altitudes of 30,000 feet.

## Shocking Tendrils

Tusked skyfish catch slow-moving or inattentive prey in their tentacles, and they sometimes fish in shallow lakes and streams. They can suppress their natural electrical charge, allowing them to manipulate objects or interact with other creatures safely.

## Slow Mounts

When fitted with special, electricity-resistant saddles, tusked skyfish can be ridden without harming their riders, although their slow speed makes them most suitable for casual excursions or unhurried long-distance travel. Genies, their offspring, and their servitors seem to find tusked skyfish congenial beasts of burden.

```statblock
"name": "Tusked Skyfish (ToB1-2023)"
"size": "Large"
"type": "aberration"
"alignment": "Unaligned"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "102"
"hit_dice": "12d10 + 36"
"stats":
- !!int "19"
- !!int "12"
- !!int "17"
- !!int "3"
- !!int "14"
- !!int "10"
"speed": "5 ft., fly 20 ft. (hover)"
"damage_immunities": "lightning"
"senses": "darkvision 60 ft., passive Perception 12"
"languages": ""
"cr": "4"
"traits":
- "desc": "A creature that touches the skyfish or hits it with a melee attack while\
    \ within 5 feet of it takes 3 (1d6) lightning damage. In addition, a creature\
    \ that starts its turn beneath the skyfish while the skyfish is hovering takes\
    \ 3 (1d6) lightning damage, provided the creature is within 15 feet of the skyfish."
  "name": "Electrified Tendrils"
- "desc": "While grappling a creature, the tusked skyfish can move at its full speed,\
    \ carrying the [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ creature along with it."
  "name": "Mobile Grappler"
"actions":
- "desc": "The tusked skyfish makes one Gore attack and one Electrified Tentacles\
    \ attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 13\
    \ (2d8 + 4) piercing damage."
  "name": "Gore"
- "desc": "Melee Weapon Attack: +6 to hit, reach 10 ft., one creature. Hit:\
    \ 14 (3d6 + 4) bludgeoning damage, and the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 13) if it is a Medium or smaller creature. Until this grapple ends,\
    \ the target is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ and takes 14 (4d6) lightning damage at the start of each of its turns, and\
    \ the skyfish can't use its Electrified Tentacles on another target."
  "name": "Electrified Tentacles"
- "desc": "The tusked skyfish sprays foul‑smelling liquid in a 20-foot line that is\
    \ 5 feet wide. Each creature in that line must make a DC 13 Constitution saving\
    \ throw. On a failure, a creature takes 21 (6d6) poison damage and is [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 minute. On a success, a creature takes half the damage and isn't [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned).\
    \ If the saving throw fails by 5 or more, the creature falls [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)\
    \ while [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ in this way. The [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)\
    \ creature wakes up if it takes damage or if another creature takes an action\
    \ to shake it awake. A [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Stench Spray (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/aberration/token/tusked-skyfish-tob1-2023.webp"
```
^statblock

## Environment

desert, grassland