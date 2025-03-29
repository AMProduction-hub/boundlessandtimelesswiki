---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Swarm of Manabane Scarabs"]
---
# [Swarm of Manabane Scarabs](03 - Player Log & Handouts\Mechanics\CLI\bestiary\beast/swarm-of-manabane-scarabs-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 355*  

*These clicking, turquoise-colored beetles have faintly luminescent golden glyphs on their backs, which grow brighter as they slowly draw near.*

Manabane scarabs are vermin infused with the ancient magic of fallen desert empires.

## Devour Magic

Whether from gnawing on the flesh of the undead or nesting in areas rife with lingering enchantment, these beetles have developed a taste for the power of magic even as its power has marked them. The graven glyphs on their carapaces resemble the priestly cuneiform of long-dead kingdoms, and the more magical energy they consume, the brighter they glow. Manabane scarabs pursue magic without hesitation or fear, tirelessly seeking to drain it for sustenance.

```statblock
"name": "Swarm of Manabane Scarabs (ToB1-2023)"
"size": "Medium"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "82"
"hit_dice": "11d8 + 33"
"stats":
- !!int "3"
- !!int "16"
- !!int "16"
- !!int "1"
- !!int "13"
- !!int "2"
"speed": "20 ft., burrow 10 ft., climb 20 ft., fly 10 ft."
"skillsaves":
  "Stealth": !!int "5"
  "Perception": !!int "3"
"damage_resistances": "bludgeoning, piercing, slashing"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
  \ [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
  \ [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)"
"senses": "blindsight 10 ft., darkvision 30 ft., tremorsense 30 ft., passive Perception\
  \ 13"
"languages": ""
"cr": "4"
"traits":
- "desc": "The swarm of manabane scarabs can't be affected or detected by spells of\
    \ 2nd level or lower unless it wishes to be. It has advantage on saving throws\
    \ against all other spells and magical effects."
  "name": "Limited Magic Immunity"
- "desc": "The swarm of manabane scarabs senses magic within 120 feet of it at will.\
    \ This trait otherwise works like the [detect magic](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/detect-magic.md)\
    \ spell but isn't itself magical."
  "name": "Sense Magic"
- "desc": "The swarm can occupy another creature's space and vice versa, and the swarm\
    \ can move through any opening large enough for a Tiny insect. The swarm can't\
    \ regain hp or gain temporary hp."
  "name": "Swarm"
"actions":
- "desc": "Melee Weapon Attack: +5 to hit, reach 0 ft., one creature in the swarm's\
    \ space. Hit: 28 (8d6) piercing damage, or 14 (4d6) piercing damage if the\
    \ swarm has half of its hit points or fewer, and the swarm can attempt to end\
    \ one random magical effect of 2nd level or lower on the target. This effect works\
    \ like the [dispel magic](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dispel-magic.md)\
    \ spell, except the swarm must always make an ability check. Its ability check\
    \ for this is +5."
  "name": "Bites"
"bonus_actions":
- "desc": "The swarm drains the magic from one magic item in its space that isn't\
    \ being worn or carried. A magic item with charges loses 1d4 charges, an item\
    \ with limited uses per day loses one daily use, and a single-use item, such as\
    \ a potion or spell scroll is destroyed. All other magic items have their effects\
    \ suppressed for 1 minute. A drained item regains its magic after 1 hour."
  "name": "Drain Magic Item"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/beast/token/swarm-of-manabane-scarabs-tob1-2023.webp"
```
^statblock

## Environment

desert