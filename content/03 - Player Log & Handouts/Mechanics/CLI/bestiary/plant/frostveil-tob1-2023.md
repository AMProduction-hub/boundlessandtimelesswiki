---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/arctic
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/plant
statblock: inline
aliases: ["Frostveil"]
---
# [Frostveil](03 - Player Log & Handouts\Mechanics\CLI\bestiary\plant/frostveil-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 193*  

*"They took the sled dogs first, and later the seal-skinner set to guard them. We'd hear a confused, muffled cry in the wind and then we'd find them—a raven harvest, cold and stiff on the ice. Next time, we hid ourselves and watched, and we saw them floating through the air like kites. A wisp of blowing snow that never dispersed, a billowing, snowflake sail moving with sinister purpose. The 'cloak of death' our guide called it."*

Whipped through the air by snowstorms and resembling a spider's web dangling with delicate ice crystals, these silently gliding, beautiful killers are semi-sentient plants adapted to the merciless cold of the north.

## Cloak of Death

Flat nodes shaped like large snowflakes connect the frostveil's netlike body and trailing tails of transparent fibers. Gossamer tendrils stream behind and between the flying snowflakes, ready to grab and entangle any warm-blooded creature the frostveil detects.

## Seek Warmth

Each starlike node contains crude sensory organs, able to detect warmth as meager as a living creature's breath and steer the gliding web toward it.

## Spirit Spores

Northern shamans say the dance of the frostveils is beautiful when lit by the northern lights and a powerful omen. With great care, shamans sometimes harvest frostveils for their frozen spore-shards, which grant potent visions of the spirit world when melted on the tongue.

```statblock
"name": "Frostveil (ToB1-2023)"
"size": "Medium"
"type": "plant"
"alignment": "Unaligned"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "67"
"hit_dice": "9d8 + 27"
"stats":
- !!int "20"
- !!int "20"
- !!int "16"
- !!int "1"
- !!int "11"
- !!int "1"
"speed": "10 ft., fly 15 ft. (hover)"
"skillsaves":
  "Stealth": !!int "7"
"damage_vulnerabilities": "fire"
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "cold"
"condition_immunities": "[blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
  \ [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [deafened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Deafened),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)"
"senses": "blindsight 120 ft., passive Perception 10"
"languages": ""
"cr": "4"
"traits":
- "desc": "A creature that touches the frostveil or hits it with a melee attack while\
    \ within 5 feet of it takes 4 (1d8) acid damage."
  "name": "Chilling Acidic Body"
- "desc": "While engulfing a creature, the frostveil takes only half the damage dealt\
    \ to it (rounded down), and the engulfed creature takes the other half."
  "name": "Damage Transfer"
- "desc": "While the frostveil remains motionless, it is indistinguishable from a\
    \ formation of frost and ice."
  "name": "False Appearance"
- "desc": "In windy conditions, the frostveil's flying speed increases to 30 feet.\
    \ In a wind of moderate or greater speed (at least 10 miles per hour), its flying\
    \ speed increases to 60 feet."
  "name": "Windborne"
"actions":
- "desc": "The frostveil makes two Frozen Tendril attacks. If both attacks hit a Medium\
    \ or smaller target, the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 15), and the frostveil uses Snowy Engulf on it."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 9\
    \ (1d8 + 5) bludgeoning damage plus 3 (1d6) cold damage."
  "name": "Frozen Tendril"
- "desc": "The frostveil engulfs a Medium or smaller creature [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ by it. The engulfed target is [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ and [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ and it must succeed on a DC 15 Constitution saving throw at the start of each\
    \ of the frostveil's turns or take 4 (1d8) acid damage and 3 (1d6) cold damage.\
    \ If the frostveil moves, the engulfed target moves with it. The frostveil can\
    \ have only one creature engulfed at a time."
  "name": "Snowy Engulf"
- "desc": "The frostveil releases a puff of psychotropic spores around itself. Each\
    \ creature within 10 feet of the frostveil must make a DC 15 Constitution saving\
    \ throw. On a failure, a creature takes 21 (6d6) cold damage and is [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ for 1 minute. On a success, a creature takes half the damage and isn't [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated).\
    \ When an [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ creature moves, it moves in a random direction. An [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Spirit Spores (Recharge 6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/plant/token/frostveil-tob1-2023.webp"
```
^statblock

## Environment

arctic