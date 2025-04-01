---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/construct
statblock: inline
aliases: ["Spider Thief"]
---
# [Spider Thief](03 - Player Log & Handouts\Mechanics\CLI\bestiary\construct/spider-thief-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 342*  

*This clockwork spider creature is the size of a dog. Each of its eight sharp, sickle-like feet stabs or sinks slightly into the ground. Razor wire enwraps its body, while gyros whirl visibly in its faceless, clockwork head*.

## Wire Fighters

A spider thief never initiates combat unless ordered to, but it always defends itself against attack. Its initial attack is whirling its razor line to entangle a target. Once it snares a foe, the spider thief keeps attacking that foe until the victim stops resisting or the victim escapes from the spider's wire.

## Completely Loyal

This clockwork machine follows orders from its master even if they lead to its destruction, and it fights until destroyed or told to stand down. The machine recognizes only its creator as its master.

## Guild Tools

The spider thief got its name because of its ability to climb walls and to effortlessly cross gaps between buildings, making it an excellent accomplice for enterprising thieves. Some thieves' guilds make extensive use of them, and many freelance rogues use them as partners.

```statblock
"name": "Spider Thief (ToB1-2023)"
"size": "Small"
"type": "construct"
"alignment": "Unaligned"
"ac": !!int "13"
"ac_class": "natural armor"
"hp": !!int "66"
"hit_dice": "12d6 + 24"
"stats":
- !!int "10"
- !!int "12"
- !!int "14"
- !!int "3"
- !!int "10"
- !!int "1"
"speed": "30 ft., climb 20 ft."
"skillsaves":
  "Stealth": !!int "3"
"damage_resistances": "fire"
"damage_immunities": "poison, psychic"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 10"
"languages": "understands the languages of its creator but can't speak"
"cr": "2"
"traits":
- "desc": "The spider thief doesn't require air, food, drink, or sleep."
  "name": "Construct Nature"
- "desc": "The spider thief is immune to any spell or effect that would alter its\
    \ form."
  "name": "Immutable Form"
- "desc": "The spider thief has advantage on saving throws against spells and other\
    \ magical effects."
  "name": "Magic Resistance"
"actions":
- "desc": "The spider thief makes one Hooked Wire attack and one Sickle Claw attack,\
    \ or it makes two Sickle Claw attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 10\
    \ (2d8 + 1) slashing damage."
  "name": "Sickle Claw"
- "desc": "Melee or Ranged Weapon Attack: +3 to hit, reach 5 ft. or range 15/30\
    \ ft., one target. Hit: 6 (2d4 + 1) piercing damage, and the spider thief\
    \ pulls itself in a straight line up to 25 feet toward the target, stopping in\
    \ the nearest unoccupied space to the target. When the spider thief moves in this\
    \ way, opportunity attacks against it have disadvantage."
  "name": "Hooked Wire"
"bonus_actions":
- "desc": "The spider thief throws a hooked wire at a point on a surface, such as\
    \ the ground or wall, it can see within 30 feet of it, attaching one end of the\
    \ wire to that point. It then reels in the wire, pulling itself to an unoccupied\
    \ space within 5 feet of that point. It can bring along objects and willing creatures\
    \ as long as their total weight doesn't exceed 100 pounds. When the spider moves\
    \ in this way, opportunity attacks against it have disadvantage."
  "name": "Wire Jump"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/construct/token/spider-thief-tob1-2023.webp"
```
^statblock

## Environment

urban