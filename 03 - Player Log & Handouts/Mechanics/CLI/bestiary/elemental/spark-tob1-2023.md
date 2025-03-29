---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/elemental
statblock: inline
aliases: ["Spark"]
---
# [Spark](03 - Player Log & Handouts\Mechanics\CLI\bestiary\elemental/spark-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 337*  

*This mote of electrical energy floats menacingly, erupting in a shower of sparks and tendrils of lightning. When it disappears, it leaves only the whiff of ozone.*

## Born in Storms

When a great storm rips across a world in the Material Plane, it sometimes tears loose the fabric of reality, releasing sentient creatures composed entirely of elemental energy. Occasionally when a spark forms, an oppositely charged mate is created at the same time. When this happens, the two always stay within 300 feet of one another.

## Seek Hosts

Fueled by its frenetic thought patterns and erratic actions, a spark jolts through its new world to find a physical body, drawn by an urge to know form. Some spellcasters deliberately seek out sparks for symbiosis. Spellcasters devoted to deities or study of the elements may reach an agreement with sparks, allowing the elementals to ride within their bodies for the sparks' lifetime. Sparks rarely survive longer than a year, even within a symbiotic relationship with a mortal form. When they expire, they wink out and return to the elemental planes.

```statblock
"name": "Spark (ToB1-2023)"
"size": "Tiny"
"type": "elemental"
"alignment": "Chaotic Neutral"
"ac": !!int "15"
"hp": !!int "104"
"hit_dice": "16d4 + 64"
"stats":
- !!int "4"
- !!int "20"
- !!int "18"
- !!int "10"
- !!int "12"
- !!int "17"
"speed": "10 ft., fly 60 ft. (hover)"
"saves":
  "Dexterity": !!int "8"
"damage_resistances": "thunder; bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "lightning"
"condition_immunities": "[exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
  \ [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
  \ [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)"
"senses": "darkvision 60 ft., passive Perception 11"
"languages": "Common, Primordial"
"cr": "7"
"traits":
- "desc": "The spark doesn't require air, food, drink, or sleep."
  "name": "Elemental Nature"
"actions":
- "desc": "The spark makes three Electric Touch attacks."
  "name": "Multiattack"
- "desc": "Melee Spell Attack: +6 to hit, reach 5 ft., one target. Hit: 16 (3d8\
    \ + 3) lightning damage."
  "name": "Electric Touch"
- "desc": "One Humanoid that the spark can see within 5 feet of it must succeed on\
    \ a DC 14 Charisma saving throw or be inhabited by the spark. The spark then disappears,\
    \ fusing with the target's nervous system, and the target is [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ and loses control of its body. The spark now controls the body but doesn't deprive\
    \ the target of awareness. The spark can't be targeted by any attack, spell, or\
    \ other effect, and it retains its alignment, Intelligence, Wisdom, Charisma,\
    \ immunity to being [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
    \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
    \ or [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious),\
    \ and its Electric Touch attack. It otherwise uses the inhabited target's statistics,\
    \ but doesn't gain access to the target's knowledge, class features, or proficiencies.\n\
    \nEvery 24 hours that elapse, the target must succeed on a DC 14 Constitution\
    \ saving throw or take 7 (2d6) lightning damage, and its hp maximum is reduced\
    \ by that amount. This reduction lasts until the target finishes a long rest after\
    \ the spark no longer inhabits it. The target dies if this reduces its hp maximum\
    \ to 0. Each time the spark makes an Electric Touch attack and at the end of each\
    \ long rest, the target can make a DC 14 Charisma saving throw, expelling the\
    \ spark on a success. Alternatively, the spark can exit the target's body as a\
    \ bonus action or can be forced out by an effect like the [protection from energy](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/protection-from-energy.md)\
    \ spell. The target is immune to this spark's Inhabit for 24 hours after succeeding\
    \ on the saving throw or after the spark is expelled.\n\nA willing target retains\
    \ full function of its body, doesn't need to make a Constitution saving throw\
    \ every 24 hours, has immunity to lightning damage, and can communicate with the\
    \ spark telepathically. If the spark inhabits a willing target, it takes its turn\
    \ at the same time as the target, but the spark can attack only as a reaction\
    \ to a creature moving within 5 feet of the target or as a reaction to the target\
    \ attacking a creature within 5 feet of it."
  "name": "Inhabit"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/elemental/token/spark-tob1-2023.webp"
```
^statblock

## Environment

grassland, planar