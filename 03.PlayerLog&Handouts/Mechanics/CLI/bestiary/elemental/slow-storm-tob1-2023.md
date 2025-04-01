---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/15
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/elemental
statblock: inline
aliases: ["Slow Storm"]
---
# [Slow Storm](03 - Player Log & Handouts\Mechanics\CLI\bestiary\elemental/slow-storm-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 333*  

*Wisps of humid wind revolve around this spiny ball. Two massive black eyes and a dark mouth are the only features visible through its static-straight quills.*

Despite its perhaps comical appearance, a slow storm is a creature of wind, lightning, and chaos, able to send minute electrical shocks into creatures that cause pain every time the creature moves. It turns the bodies of physically able creatures against them, forcing them to choose between relative inactivity or ever-increasing pain.

## Small Central Core

The nucleus of a slow storm is a sphere of ice and stone, and it is surrounded by protective, high-speed winds.

## Static Generator

A slow storm has no internal organs other than its brain, and it lives on the energy and moisture it drains from opponents. Its quills not only deflect debris but also generate static electricity that it uses when attacking.

```statblock
"name": "Slow Storm (ToB1-2023)"
"size": "Medium"
"type": "elemental"
"alignment": "Chaotic Neutral"
"ac": !!int "19"
"ac_class": "natural armor"
"hp": !!int "220"
"hit_dice": "21d8 + 126"
"stats":
- !!int "20"
- !!int "19"
- !!int "22"
- !!int "11"
- !!int "18"
- !!int "11"
"speed": "0 ft., fly 60 ft. (hover)"
"saves":
  "Dexterity": !!int "9"
  "Constitution": !!int "11"
"damage_resistances": "acid; cold; fire; bludgeoning, piercing, slashing from nonmagical\
  \ attacks"
"damage_immunities": "lightning"
"condition_immunities": "[exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
  \ [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
  \ [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)"
"senses": "blindsight 30 ft., darkvision 120 ft., passive Perception 14"
"languages": "Auran, Common"
"cr": "15"
"traits":
- "desc": "The slow storm doesn't require air, food, drink, or sleep."
  "name": "Elemental Nature"
- "desc": "The slow storm is surrounded by a 15-foot-radius wind storm. The storm\
    \ imposes disadvantage on ranged weapon attack rolls and Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks based on sight or hearing within the area. The winds extinguish open\
    \ flames and disperse fog. A flying creature in the storm must land at the end\
    \ of its turn or fall. Each creature that starts its turn in the area must succeed\
    \ on a DC 18 Dexterity saving throw or take 9 (2d8) lightning damage. The storm's\
    \ area is difficult terrain for any creature other than the slow storm."
  "name": "Eye of the Storm"
"actions":
- "desc": "The slow storm makes three Slam attacks or four Lightning Bolt attacks.\
    \ If two Slam attacks hit one creature, the target must succeed on a DC 18 Constitution\
    \ saving throw or be wracked with pain for 1 minute. While the target is wracked\
    \ with pain, minute bits of electricity dance within its body, and the target\
    \ takes 4 (1d8) lightning damage for every 5 feet it moves. The target can repeat\
    \ the saving throw at the end of each of its turns, ending the effect on itself\
    \ on a success."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 21\
    \ (3d10 + 5) bludgeoning damage plus 9 (2d8) lightning damage."
  "name": "Slam"
- "desc": "Ranged Spell Attack: +9 to hit, range 120 ft., one target. Hit: 22\
    \ (4d8 + 4) lightning damage."
  "name": "Lightning Bolt"
- "desc": "The slow storm releases built-up electricity in a 60-foot cone. Each creature\
    \ in the area must make a DC 18 Constitution saving throw, taking 54 (12d8)\
    \ lightning damage on a failed save, or half as much damage on a successful one.\
    \ A creature that fails this saving throw by 5 or more is also [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)\
    \ for 1 minute. A [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Static Shock (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/elemental/token/slow-storm-tob1-2023.webp"
```
^statblock

## Environment

desert, grassland, hill