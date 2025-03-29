---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/10
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/construct
statblock: inline
aliases: ["Algorith"]
---
# [Algorith](03 - Player Log & Handouts\Mechanics\CLI\bestiary\construct/algorith-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 14*  

*Sometimes called folding angels, algoriths are lawful beings made from sheer force, pure math, and universal physical laws.*

## Creatures of Pure Reason

Algoriths are the border guards of the Conceptual Realms, warding subjective beings from the Realms of the Absolute. Eternal, remorseless, and unceasingly vigilant, they guard against the monstrosities that lurk in the multiverse's most obscure dimensions. They seek out and eliminate chaos even from the abodes of the gods.

## Foes of Chaos

They visit mortal realms when chaos threatens to unravel a location or when the skeins of fate are tangled. On some occasions, an algorith will serve a god of Law or answer the summons of a skein witch. Algoriths fight with conjured blades of force. They can also summon universal energy that deconstructs randomness, weakening enemies or reducing them to finely ordered crystalline dust.

## Social but Mysterious

In groups, algoriths move and fight in silent coordination. Only tiny variations in the formulas etched into their skins identify one algorith from another. Five is a number of extreme importance to all algoriths, but few are willing (or able) to explain why to anyone who isn't an algorith. Algoriths may have castes, ranks, or commanders, but no mortal has decoded the mathematical blazons adorning their flesh. The algoriths themselves refuse to discuss these formulas with those who do not comprehend them.

```statblock
"name": "Algorith (ToB1-2023)"
"size": "Medium"
"type": "construct"
"alignment": "Lawful Neutral"
"ac": !!int "18"
"ac_class": "natural armor"
"hp": !!int "153"
"hit_dice": "18d8 + 72"
"stats":
- !!int "21"
- !!int "14"
- !!int "19"
- !!int "13"
- !!int "16"
- !!int "18"
"speed": "40 ft., fly 40 ft."
"saves":
  "Charisma": !!int "8"
  "Dexterity": !!int "6"
  "Wisdom": !!int "7"
  "Constitution": !!int "8"
"skillsaves":
  "Athletics": !!int "9"
  "Investigation": !!int "5"
  "Insight": !!int "7"
  "Perception": !!int "7"
"damage_resistances": "acid, cold, lightning"
"damage_immunities": "poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 17"
"languages": "Celestial, Common, Draconic, Infernal"
"cr": "10"
"traits":
- "desc": "The algorith casts one of the following spells, requiring no material components\
    \ and using Charisma as the spellcasting ability (spell save DC 16):\n\nAt will:\
    \ [bless](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/bless.md),\
    \ [detect magic](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/detect-magic.md),\
    \ [dimension door](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dimension-door.md),\
    \ [dispel magic](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dispel-magic.md)\n\
    \n1/day each: [commune](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/commune.md)\
    \ (as an action), [wall of force](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/wall-of-force.md)"
  "name": "Spellcasting"
- "desc": "The algorith doesn't require air, food, drink, or sleep."
  "name": "Construct Nature"
- "desc": "The algorith is immune to any spell or effect that would alter its form."
  "name": "Immutable Form"
"actions":
- "desc": "The algorith makes three Logic Razor attacks, or it makes two Logic Razor\
    \ attacks and uses Spellcasting."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 21\
    \ (3d10 + 5) force damage."
  "name": "Logic Razor"
- "desc": "The algorith projects null energy in a 30-foot cone. Each creature in the\
    \ area must make a DC 16 Dexterity saving throw. On a failure, a creature takes\
    \ 33 (6d10) force damage and any spell of 4th level or lower on the creature\
    \ ends, as if it had been the target of a [dispel magic](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dispel-magic.md)\
    \ spell. On a success, a creature takes half the damage and spells on it don't\
    \ end."
  "name": "Cone of Negation (Recharge 5-6)"
- "desc": "The algorith summons and throws a tiny rune of law at a point it can see\
    \ within 100 feet. The rune explodes on impact. Each creature within 30 feet of\
    \ where the rune landed must make a DC 16 Dexterity saving throw. On a failure,\
    \ a creature takes 27 (5d10) force damage and is [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)\
    \ until the end of its next turn. On a success, a creature takes half the damage\
    \ and isn't [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)."
  "name": "Reality Bomb (5/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/construct/token/algorith-tob1-2023.webp"
```
^statblock

## Environment

planar