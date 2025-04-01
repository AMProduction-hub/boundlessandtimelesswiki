---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/8
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/elemental
statblock: inline
aliases: ["Chronalmental"]
---
# [Chronalmental](03 - Player Log & Handouts\Mechanics\CLI\bestiary\elemental/chronalmental-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 56*  

*A chronalmental is difficult to pin down, and it may appear as a large man-shaped absence in the air that reveals first a field of stars, then a contorted rainbow of colored bands, then a brilliant white light, strobing in and out of existence.*

## Fluid as Time

Shifting between the past, present, and future, chronalmentals are formed from temporal energy. They flow like sand in an hourglass and exist between the ticks of a clock. The first chronalmentals were forged from extra time left over from the beginning of the universe. Many served as shock troopers in unfathomable wars between angels and fiends or gods and ancient titans. Most were lost between seconds or abandoned to drift in the Astral Plane or in the void between the stars.

## Stewards of Calamity

Locations of historical significance—both past and future—attract chronalmentals. They have a fondness for battlefields and other sites of strife. Because they are drawn to noteworthy places, chronalmentals have a reputation as harbingers of calamity, and their presence may incite panic among scholars, priests, and sages.

## Environmental Chaos

Whatever the terrain, the environment behaves strangely around the chronalmental. Collapsed walls might suddenly rise, seedlings become massive trees, and fallen soldiers relive their dying moments. These changes occur randomly, a side effect of a chronalmental's presence. Things return to normal when they depart.

```statblock
"name": "Chronalmental (ToB1-2023)"
"size": "Large"
"type": "elemental"
"alignment": "Neutral"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "142"
"hit_dice": "15d10 + 60"
"stats":
- !!int "14"
- !!int "20"
- !!int "19"
- !!int "9"
- !!int "13"
- !!int "6"
"speed": "30 ft."
"damage_immunities": "poison; bludgeoning, piercing, slashing from nonmagical attacks"
"condition_immunities": "[exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
  \ [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)"
"senses": "darkvision 60 ft., passive Perception 11"
"languages": "Celestial, Infernal"
"cr": "8"
"traits":
- "desc": "The chronalmental doesn't require air, food, drink, or sleep."
  "name": "Elemental Nature"
- "desc": "When a chronalmental is subjected to a [slow](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/slow.md)\
    \ spell, [haste](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/haste.md)\
    \ spell, or similar effect, it automatically succeeds on any saving throws required\
    \ by the spell or effect and regains 13 3d8 hp."
  "name": "Temporal Body"
"actions":
- "desc": "The chronalmental makes three Slam attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 16\
    \ (2d10 + 5) bludgeoning damage."
  "name": "Slam"
- "desc": "The chronalmental steals time from one creature it can see within 30 feet\
    \ of it, drawing the stolen time into itself. The target must make a DC 16 Wisdom\
    \ saving throw. On a failure, the target's speed is halved, and it can take either\
    \ an action or a bonus action on its turn, but not both for 1 minute. Then, the\
    \ chronalmental's position in the initiative order increases by 10, its speed\
    \ increases by 30 feet, and when it takes the Multiattack action, it can make\
    \ one additional Slam attack. The target can repeat the saving throw at the end\
    \ of each of its turns, ending the effects on itself and the chronalmental on\
    \ a success."
  "name": "Steal Time (1/Day)"
- "desc": "The chronalmental sends one creature it can see within 30 feet of it outside\
    \ of the flow of time, shunting the creature to a tiny demiplane. The target must\
    \ succeed on a DC 16 Wisdom saving throw or be [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)\
    \ and magically shunted outside of time for 1 minute. The creature disappears\
    \ for the duration, returning to the space it previously occupied, or the nearest\
    \ unoccupied space, when the effect ends. At the end of each of its turns, the\
    \ target can repeat the saving throw, ending the effect on itself on a success."
  "name": "Displace (Recharge 5-6)"
"reactions":
- "desc": "When a creature the chronalmental can see moves within 5 feet of it, the\
    \ chronalmental can teleport, along with any equipment it is wearing or carrying,\
    \ to an unoccupied space within 60 feet that it occupied within the past minute."
  "name": "Step Between Seconds (Recharge 4-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/elemental/token/chronalmental-tob1-2023.webp"
```
^statblock

## Environment

planar