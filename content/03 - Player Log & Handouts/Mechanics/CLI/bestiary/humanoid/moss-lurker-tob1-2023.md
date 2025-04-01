---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Moss Lurker"]
---
# [Moss Lurker](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/moss-lurker-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 278*  

*Somewhat like the cruel crossbreed of troll and gnome, this creature has a long, greenish beard and hair. Its hide is peaty amber, and a vaguely fungal scent surrounds it.*

Like their trollish relatives, moss lurkers have large, often grotesque noses. Their claws are bright red when unsheathed, and their teeth tend toward the long and snaggly. They wear simple clothes of homespun wool or leather, or go naked in the summer. Their hats are sometimes festooned with toadstools or ferns as primitive camouflage.

## Large Rocks and Poisoned Gifts

Moss lurkers have a fondness for throwing large stones at enemies. Some stones even seem too large for the lurker to heft. They also enjoy poisoning food and drink then offering it to creatures lost in the forest.

```statblock
"name": "Moss Lurker (ToB1-2023)"
"size": "Small"
"type": "humanoid"
"alignment": "Chaotic Neutral"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "45"
"hit_dice": "10d6 + 10"
"stats":
- !!int "14"
- !!int "14"
- !!int "12"
- !!int "12"
- !!int "10"
- !!int "10"
"speed": "30 ft."
"saves":
  "Dexterity": !!int "4"
  "Strength": !!int "4"
"skillsaves":
  "Stealth": !!int "4"
  "Perception": !!int "2"
"damage_immunities": "poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "blindsight 60 ft., passive Perception 12"
"languages": "Giant, Sylvan, Trollkin"
"cr": "1"
"traits":
- "desc": "A moss lurker has advantage on Dexterity ([Stealth](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Stealth))\
    \ checks made to hide in forested terrain."
  "name": "Forest Camouflage"
- "desc": "The moss lurker has advantage on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on hearing or smell."
  "name": "Keen Hearing and Smell"
- "desc": "A moss lurker can spend 1 minute stirring one of its red claws in a drink\
    \ or cooked meal, contaminating the food or drink. A creature that eats or drinks\
    \ the contaminated food or drink must succeed on a DC 12 Constitution saving throw\
    \ or be [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 hour. A creature that fails this saving throw by 5 or more is also [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)\
    \ while [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ in this way. The creature wakes up if it takes damage or if another creature\
    \ takes an action to shake it awake."
  "name": "Poisoned Gifts"
"actions":
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6\
    \ + 2) slashing damage plus 7 (2d6) poison damage, and the target must succeed\
    \ on a DC 12 Constitution saving throw or be [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ until the end of its next turn."
  "name": "Poisoned Claw"
- "desc": "Ranged Weapon Attack: +4 to hit, range 20/60 ft., one target. Hit:\
    \ 7 (2d4 + 2) bludgeoning damage. If the target is at least 10 feet below the\
    \ moss lurker, such as at the base of a cliff where the moss lurker stands, the\
    \ target must succeed on a DC 12 Strength saving throw or take 1d4 bludgeoning\
    \ damage for every 10 feet the rock fell before hitting the target, to a maximum\
    \ of 10d4."
  "name": "Throw Stone"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/moss-lurker-tob1-2023.webp"
```
^statblock

## Environment

forest, underdark