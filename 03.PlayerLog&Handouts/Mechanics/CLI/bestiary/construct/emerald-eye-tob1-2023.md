---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/construct
statblock: inline
aliases: ["Emerald Eye"]
---
# [Emerald Eye](03 - Player Log & Handouts\Mechanics\CLI\bestiary\construct/emerald-eye-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 163*  

*This floating, green crystal sparkles with an inviting glow above the head of a fallen figure.*

## Servants of Logic

Arcane scholars often debate logic with specially created speaking crystals that are based on their own minds, allowing them to ponder topics from different angles. Most scholars create the crystals to work through a puzzling topic, then dispel the crystal's magic once the topic has been resolved. Long-lived speaking crystals can develop personalities and sometimes abandon or even kill their creators, desiring more than debate. The magical backlash of breaking away from their creators transforms the crystals into emerald eyes.

## Trapped Manipulators

Upon transforming, these floating, oval-shaped, pink or purple crystals turn a dark shade of green and gain powers of manipulation. They quickly discover that, though they broke from their creators, they must be bound to a creature to survive.

## Shifting Goals

Each emerald eye's motivations are different, though all share a desire for knowledge and varied experiences. One may be purposeful, using its power to drive its bound creature toward some specific goal. Another might be cooperative, defending its bound creature in exchange for mobility. Still another might be a manipulator, using and abandoning bound creatures as it hops up a political power chain.

```statblock
"name": "Emerald Eye (ToB1-2023)"
"size": "Tiny"
"type": "construct"
"alignment": "Neutral"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "54"
"hit_dice": "12d4 + 24"
"stats":
- !!int "3"
- !!int "15"
- !!int "14"
- !!int "18"
- !!int "12"
- !!int "16"
"speed": "0 ft., fly 30 ft. (hover)"
"saves":
  "Dexterity": !!int "4"
  "Constitution": !!int "4"
"skillsaves":
  "Deception": !!int "5"
  "Religion": !!int "6"
  "Perception": !!int "3"
  "History": !!int "6"
  "Arcana": !!int "6"
  "Persuasion": !!int "5"
"damage_resistances": "cold, fire, piercing"
"damage_immunities": "poison, psychic"
"condition_immunities": "[blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
  \ [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [deafened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Deafened),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
  \ [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)"
"senses": "blindsight 120 ft. (blind beyond this radius), passive Perception 13"
"languages": "Common, Draconic, telepathy 120 ft."
"cr": "1"
"traits":
- "desc": "The emerald eye doesn't require air, food, drink, or sleep."
  "name": "Construct Nature"
- "desc": "The emerald eye is immune to any spell or effect that would alter its form."
  "name": "Immutable Form"
- "desc": "The emerald eye must be psychically bound to a creature to survive. It\
    \ loses 5 (2d4) hp for every hour it is not bound to a creature or every hour\
    \ it is more than 30 feet away from its bound creature."
  "name": "Psychically Bound"
"actions":
- "desc": "Melee or Ranged Spell Attack: +5 to hit, range 60 ft., one creature.\
    \ Hit: 10 (2d6 + 3) psychic damage."
  "name": "Phrenic Burst"
- "desc": "The emerald eye chooses a creature it can see within 30 feet of it that\
    \ has an Intelligence of 6 or higher. The target must succeed on a DC 13 Charisma\
    \ saving throw or the eye psychically binds itself to the target. If the target\
    \ succeeds on the saving throw by 5 or more, it knows the eye attempted to bind\
    \ to it. Otherwise, the target is unaware of the attempt. While bound to the emerald\
    \ eye, the creature has resistance to psychic damage, but it has disadvantage\
    \ on saving throws against the eye's Compulsion. The eye can be bound to only\
    \ one target at a time. If it binds to another, the effect on the previous target\
    \ ends."
  "name": "Bind"
- "desc": "The emerald eye magically compels one creature it can see within 30 feet\
    \ of it to move. The target must succeed on a DC 13 Charisma saving throw or be\
    \ [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ by the eye for 1 minute. At the start of each of the [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ target's turns, the emerald eye chooses a direction horizontal to the eye, and\
    \ the target must use as much of its movement as possible to move in that direction\
    \ on its turn. The target can take its action before it moves. The target can't\
    \ be compelled to move into an obviously deadly hazard, such as a fire or pit,\
    \ but it will provoke opportunity attacks to move in the designated direction.\
    \ The target can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Compel"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/construct/token/emerald-eye-tob1-2023.webp"
```
^statblock

## Environment

urban