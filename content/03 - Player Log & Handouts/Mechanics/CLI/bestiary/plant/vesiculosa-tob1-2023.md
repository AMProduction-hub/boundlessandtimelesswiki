---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/11
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/size/gargantuan
- ttrpg-cli/monster/type/plant
statblock: inline
aliases: ["Vesiculosa"]
---
# [Vesiculosa](03 - Player Log & Handouts\Mechanics\CLI\bestiary\plant/vesiculosa-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 385*  

*A glittering pool stands among lush and verdant fruiting plants.*

## Underground Oasis

A vesiculosa is a huge, burrowing pitcher plant that dwells in deserts and oases, spurring nearby growth and luring in prey with soporific scents and tainted water. A vesiculosa's body is buried in the ground, with only its roots in the open in ropy tangles. It leaves the mouth of its water-filled central pitcher open on the surface of the ground, looking like a small oasis. When creatures fall to its sleep-inducing water, the vesiculosa uses its roots to pull them into the soil, waiting for them to die before feasting on the nutrients left by the decaying flesh.

## Rich Sapphire Heartvine

A vesiculosa's heartvine resembles a lump of sapphire and is highly prized by alchemists. It can be reached with an hour or two of hard digging once the plant has been killed.

```statblock
"name": "Vesiculosa (ToB1-2023)"
"size": "Gargantuan"
"type": "plant"
"alignment": "Unaligned"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "232"
"hit_dice": "16d20 + 64"
"stats":
- !!int "20"
- !!int "15"
- !!int "19"
- !!int "2"
- !!int "14"
- !!int "2"
"speed": "0 ft., burrow 20 ft."
"skillsaves":
  "Perception": !!int "6"
"damage_resistances": "bludgeoning, fire, piercing"
"condition_immunities": "[blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
  \ [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [deafened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Deafened),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)"
"senses": "tremorsense 60 ft., passive Perception 16"
"languages": ""
"cr": "11"
"traits":
- "desc": "While the vesiculosa remains motionless and partially submerged on the\
    \ surface of sand or soil, it is indistinguishable from a small oasis or pond.\
    \ The vesiculosa's pitcher produces enough water for plants to grow around it,\
    \ provided the vesiculosa remains in the area for an extended period of time.\
    \ A creature that eats a fruit from a plant growing in the vesiculosa's water\
    \ is affected by the Sweet Water trait as if it drank the water."
  "name": "Oasis Appearance"
- "desc": "When a creature that can smell the vesiculosa's sweet fragrance starts\
    \ its turn within 30 feet of the vesiculosa, the creature must succeed on a DC\
    \ 16 Wisdom saving throw or be [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ for 1 minute. While [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
    \ the creature must move on its turn toward the vesiculosa by the safest available\
    \ route to get within 5 feet of the plant and drink its water. If a creature's\
    \ saving throw is successful or the effect ends for it, the creature is immune\
    \ to the vesiculosa's Sweet Fragrance for the next 24 hours."
  "name": "Sweet Fragrance"
- "desc": "A creature that drinks water from the vesiculosa's pitcher regains 5 2d4\
    \ hp, reduces its [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion)\
    \ level by 1, and must succeed on a DC 16 Constitution saving throw or fall [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)\
    \ for 10 minutes. An [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)\
    \ creature wakes up if it takes damage or if another creature takes an action\
    \ to shake it awake. Drinking the water provides a creature enough nourishment\
    \ to sustain it for one day."
  "name": "Sweet Water"
"actions":
- "desc": "The vesiculosa makes four Root or Spit Sweet Water attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +9 to hit, reach 10 ft., one creature. Hit:\
    \ 18 (3d8 + 5) bludgeoning damage, and the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 16). Until the grapple ends, the target is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained).\
    \ The vesiculosa has four roots, each of which can grapple only one target."
  "name": "Root"
- "desc": "Ranged Weapon Attack: +6 to hit, range 20/60 ft., one creature. Hit:\
    \ 18 (3d10 + 2) bludgeoning damage, and the target must succeed on a DC 16 Constitution\
    \ saving throw or fall [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)\
    \ for 1 minute. The target wakes up if it takes damage or if another creature\
    \ takes an action to shake it awake."
  "name": "Spit Sweet Water"
"bonus_actions":
- "desc": "One creature [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ by the vesiculosa is knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
    \ dragged into the ground, and buried just below the surface, ending the grapple.\
    \ The buried creature is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ and unable to breathe or stand up. A creature, including the buried creature,\
    \ can take its action to free the buried creature by succeeding on a DC 16 Strength\
    \ check. This bonus action doesn't wake a creature that is [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)\
    \ from the vesiculosa's Sweet Water trait or Spit Sweet Water action."
  "name": "Bury"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/plant/token/vesiculosa-tob1-2023.webp"
```
^statblock

## Environment

desert