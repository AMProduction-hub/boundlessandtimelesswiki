---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/12
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/celestial
statblock: inline
aliases: ["Hundun"]
---
# [Hundun](03 - Player Log & Handouts\Mechanics\CLI\bestiary\celestial/hundun-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 237*  

*A toothless mouth adorns the headless shoulders of this oversized, four-armed, doughy humanoid. Colors and half-formed phantasmal shapes appear and vanish around it, to the creature's obvious delight.*

## Creative Chaos

Wise yet child-like creatures of chaos, hunduns are four-armed, headless humanoids that embody spontaneous creation and the confusion that precedes enlightenment. Taking delight in creation of all kinds, they bring change to the staid and stagnant, spin revelation from confusion, and inspire moments of great creation—from works of art to new nations and faiths, and even the formation of planets and planes.

## Nonsense Speech

Although not mindless, hunduns rarely seem to act out of conscious thought; however, their actions seem wise and are usually benevolent. They communicate only in nonsense words but have no trouble communicating among themselves or acting in coordination with other celestials.

## Flesh of Creation

Hundun blood is a powerful catalyst, and their spittle is a potent drug. Each hundun's heart is an Egg of Worlds—an artifact that can give birth to new concepts, powers, or even worlds. Obviously, the hundun must die for its heart to be used this way, but this is a sacrifice one might make willingly under the right circumstances.

```statblock
"name": "Hundun (ToB1-2023)"
"size": "Large"
"type": "celestial"
"alignment": "Chaotic Good"
"ac": !!int "18"
"ac_class": "natural armor"
"hp": !!int "154"
"hit_dice": "18d10 + 54"
"stats":
- !!int "20"
- !!int "14"
- !!int "16"
- !!int "4"
- !!int "20"
- !!int "18"
"speed": "40 ft., fly 40 ft. (hover)"
"saves":
  "Charisma": !!int "8"
  "Wisdom": !!int "9"
  "Constitution": !!int "7"
"skillsaves":
  "Athletics": !!int "9"
  "Insight": !!int "9"
  "Perception": !!int "9"
"damage_resistances": "lightning; radiant; thunder; bludgeoning, piercing, slashing\
  \ from nonmagical attacks"
"damage_immunities": "acid, psychic"
"condition_immunities": "[blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
  \ [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [deafened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Deafened),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
  \ [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned),\
  \ [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)"
"senses": "blindsight 60 ft. (blind beyond this radius), passive Perception 19"
"languages": "understands Celestial and Primordial, but can't speak intelligibly"
"cr": "12"
"traits":
- "desc": "The hundun casts one of the following spells, requiring no material components\
    \ and using Wisdom as the spellcasting ability (spell save DC 17):\n\nAt will:\
    \ [create or destroy water](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/create-or-destroy-water.md),\
    \ [dancing lights](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dancing-lights.md),\
    \ [minor illusion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/minor-illusion.md),\
    \ [prestidigitation](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/prestidigitation.md)\n\
    \n1/day each: [creation](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/creation.md)\
    \ (as an action), [plant growth](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/plant-growth.md)\n\
    \n3/day each: [Evard's black tentacles](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/evards-black-tentacles.md),\
    \ [fabricate](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/fabricate.md)\
    \ (as an action), [Otto's irresistible dance](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/ottos-irresistible-dance.md)"
  "name": "Spellcasting"
- "desc": "The hundun is immune to any effect that would sense its emotions or read\
    \ its thoughts, as well as any divination spell that it refuses. Wisdom ([Insight](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Insight))\
    \ checks made to ascertain the hundun's intentions or sincerity have disadvantage."
  "name": "Inscrutable"
- "desc": "The hundun has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "The hundun's Slam attacks are magical. When the hundun hits with a Slam\
    \ attack, the attack deals an extra 2d6 radiant damage (included in the attack)."
  "name": "Radiant Fists"
"actions":
- "desc": "The hundun can use its Motivating Babble. It then makes four Slam attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 12\
    \ (2d6 + 5) bludgeoning damage plus 7 (2d6) radiant damage."
  "name": "Slam"
- "desc": "The hundun babbles incoherently at one creature it can see within 60 feet\
    \ of it. The target must succeed on a DC 17 Wisdom saving throw or suffer one\
    \ of the following effects until the end of its next turn. Roll a d4 to determine\
    \ which effect happens."
  "name": "Motivating Babble"
- "desc": "The target is distracted with a flood of new ideas and has disadvantage\
    \ on attack rolls and saving throws."
  "name": "1 Distracted"
- "desc": "The target's mind fills with solutions to many of its problems, reducing\
    \ its burden on itself. Its speed is increased by half, and its jump distance\
    \ is doubled."
  "name": "2 Enlightened"
- "desc": "The target is inspired by new ideas and has advantage on attack rolls and\
    \ saving throws."
  "name": "3 Inspired"
- "desc": "The target's speed is reduced to 0 and it must use its next action to write\
    \ itself a note, tie a small knot, or create some other physical reminder of the\
    \ great idea that just struck it."
  "name": "4 Struck with Genius"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/celestial/token/hundun-tob1-2023.webp"
```
^statblock

## Environment

any