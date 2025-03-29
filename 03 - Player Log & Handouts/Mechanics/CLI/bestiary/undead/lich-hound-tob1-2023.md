---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Lich Hound"]
---
# [Lich Hound](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/lich-hound-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 253*  

*Half bone, half purple fire, this deathly hound releases an eerie howl that echoes with the voices of the damned.*

## Fiery Bones

Bright white skulls with a heavy jaw and thick, robust skeletal bodies define the ferocious lich hounds. Their eyes burn green or blue, and their tongues resemble black fire. Fueled by necromantic power, these creatures are loyal servants of undead high priests or liches.

## Echoing Howls

Even on their own, lich hounds are relentless hunters, pursuing their prey with powerful senses and a keen ability to find the living wherever the creatures may hide. Lich hound howls fade into and out of normal hearing, with strangely shifted pitch and echoes.

## Murdered Celestials

The dark process of creating a lich hound involves a perverse ritual of first summoning a celestial canine and binding it to the Material Plane. The hound's future master then murders the trapped beast. Only then can the creature be animated in all its unholy glory. Houndlike celestials have long been outraged by the creation of lich hounds, and every few centuries, they band together to rid the world of those practicing this particular dark magic. Inevitably some knowledge survives this purge, leaving lich hounds a constant, painful reality for the celestials.

```statblock
"name": "Lich Hound (ToB1-2023)"
"size": "Medium"
"type": "undead"
"alignment": "Neutral Evil"
"ac": !!int "14"
"hp": !!int "85"
"hit_dice": "10d8 + 40"
"stats":
- !!int "10"
- !!int "18"
- !!int "18"
- !!int "6"
- !!int "10"
- !!int "16"
"speed": "30 ft., fly 50 ft."
"saves":
  "Charisma": !!int "5"
  "Wisdom": !!int "2"
"skillsaves":
  "Perception": !!int "4"
  "Acrobatics": !!int "6"
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "poison"
"condition_immunities": "[exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 14"
"languages": "understands Common and Darakhul but can't speak"
"cr": "4"
"traits":
- "desc": "The lich hound can pinpoint the location of creatures that aren't Constructs\
    \ or Undead within 60 feet of it and can sense the general direction of such creatures\
    \ within 1 mile of it."
  "name": "Blood Sense"
- "desc": "The lich hound has advantage on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on hearing or smell."
  "name": "Keen Hearing and Smell"
- "desc": "The lich hound doesn't require air, food, drink, or sleep."
  "name": "Undead Nature"
"actions":
- "desc": "The lich hound can use its Eerie Howl. It then makes two Bite attacks.\
    \ If both attacks hit one creature, the target must succeed on a DC 14 Constitution\
    \ saving throw or take 7 (2d6) slashing damage and be [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ until the end of its next turn."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11\
    \ (2d6 + 4) piercing damage. If the target is a creature, it must succeed on\
    \ a DC 14 Strength saving throw or be knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Bite"
- "desc": "The lich hound releases an eerie howl that fades in and out and echoes\
    \ strangely. Each creature within 30 feet of the lich hound must succeed on a\
    \ DC 14 Wisdom saving throw or be [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ for 1 minute. A creature can repeat the saving throw at the end of each of its\
    \ turns, ending the effect on itself on a success. If a creature's saving throw\
    \ is successful or the effect ends for it, the creature is immune to the lich\
    \ hound's Eerie Howl for the next 24 hours."
  "name": "Eerie Howl"
"bonus_actions":
- "desc": "The lich hound magically shifts from the Material Plane to the Ethereal\
    \ Plane, or vice versa."
  "name": "Ethereal Jaunt"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/lich-hound-tob1-2023.webp"
```
^statblock

## Environment

any, planar