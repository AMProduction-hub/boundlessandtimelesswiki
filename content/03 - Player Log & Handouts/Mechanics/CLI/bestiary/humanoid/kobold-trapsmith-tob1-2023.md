---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/humanoid/kobold
statblock: inline
aliases: ["Kobold Trapsmith"]
---
# [Kobold Trapsmith](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/kobold-trapsmith-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 246*  

*This kobold is bedecked in satchels, pouches, sacks, and bandoliers. All of these are bursting with tools, bits of scrap, wire, cogs, and twine. Impossibly large eyes blink through the lenses of its goggles*.

Some kobolds hatch a bit cleverer than their counterparts. These sharp-witted creatures feel driven to fiddle with the world, and those that don't meet an early demise through accident or violence often take up tinkering. Trapsmiths make a kobold lair into a deadly gauntlet of hidden pain.

## Improvisers

Trapsmiths are adept at improvising on-the-fly. They can use whatever spare parts are at hand to create simple thieves' tools or construct makeshift traps to fling at foes.

## Shifting Peril

Trapsmiths aren't warriors and avoid direct confrontation with enemies that aren't mired in traps or engaged with other foes. If the trapsmith senses that invaders in its lair are likely to get past its traps, it tries to hide or escape. A trapsmith delights in laying traps and snares behind invaders, along tunnels and paths they've already cleared and believe to be safe, then luring them back through its handiwork.

```statblock
"name": "Kobold Trapsmith (ToB1-2023)"
"size": "Small"
"type": "humanoid"
"subtype": "kobold"
"alignment": "Lawful Neutral"
"ac": !!int "14"
"ac_class": "[leather armor](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/leather-armor.md)"
"hp": !!int "54"
"hit_dice": "12d6 + 12"
"stats":
- !!int "7"
- !!int "16"
- !!int "12"
- !!int "16"
- !!int "13"
- !!int "8"
"speed": "30 ft."
"skillsaves":
  "Stealth": !!int "5"
"senses": "darkvision 60 ft., passive Perception 11"
"languages": "Common, Draconic"
"cr": "2"
"traits":
- "desc": "The kobold trapsmith can use any Tiny objects at hand to pick locks and\
    \ disarm traps, as if any such object was part of a set of thieves' tools. It\
    \ is proficient in using Tiny objects in this way. In addition, the trapsmith\
    \ has advantage on ability checks to pick locks and disarm traps."
  "name": "Improvised Tools"
- "desc": "The kobold trapsmith has advantage on attack rolls against a creature if\
    \ at least one of the trapsmith's allies is within 5 feet of the creature and\
    \ the ally isn't [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)."
  "name": "Pack Tactics"
- "desc": "While in sunlight, the kobold trapsmith has disadvantage on attack rolls,\
    \ as well as on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on sight."
  "name": "Sunlight Sensitivity"
"actions":
- "desc": "The trapsmith uses Makeshift Trap then makes one Dagger or Spare Part attack."
  "name": "Multiattack"
- "desc": "Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 20/60\
    \ ft., one target. Hit: 5 (1d4 + 3) piercing damage."
  "name": "Dagger"
- "desc": "Ranged Weapon Attack: +5 to hit, range 20/60 ft., one target. Hit:\
    \ 6 (1d6 + 3) bludgeoning damage or slashing damage (the trapsmith's choice)."
  "name": "Spare Part"
- "desc": "The kobold trapsmith cobbles together a quick trap with materials at hand\
    \ and throws it at a point on the ground it can see within 30 feet of it. The\
    \ trapsmith chooses one of the following traps. Each creature in the trap's area\
    \ must succeed on a DC 13 Dexterity saving throw or suffer the trap's effects.\n\
    \n- Bursting Much-Heavy Net. Each creature that fails the saving throw within\
    \ 10 feet of where the trap lands takes 10 (3d6) bludgeoning damage and is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ for 1 minute. A creature can take an action to free the [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ creature by succeeding on a DC 13 Strength check.  \n- Spikes-on-Spikes.\
    \ Each creature within 10 feet of where the trap lands takes 10 (4d4) piercing\
    \ damage and the area within 10 feet of the point is difficult terrain for 1 minute.\
    \  \n- Spring-Loaded Whirly Blades. Each creature that fails the saving throw\
    \ within 10 feet of where the trap lands takes 14 (4d6) slashing damage and\
    \ its speed is reduced by 10 feet until the end of its next turn.  \n- Static-Generating\
    \ Thingamabob. Each creature that fails the saving throw within 5 feet of where\
    \ the trap lands takes 9 (2d8) lightning damage and is [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)\
    \ until the end of its next turn.  "
  "name": "Makeshift Trap"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/kobold-trapsmith-tob1-2023.webp"
```
^statblock

## Environment

underdark, urban