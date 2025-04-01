---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/elf
statblock: inline
aliases: ["Elvish Veteran Archer"]
---
# [Elvish Veteran Archer](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/elvish-veteran-archer-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 410*  

The elvish veteran archer is a stealthy hunter that quietly slips through the wood, watching for game or intruders. While capable with a sword, the elvish archer's true skill lies with the longbow. When unseen, the archer can launch a volley of arrows at its foes with deadly results.

```statblock
"name": "Elvish Veteran Archer (ToB1-2023)"
"size": "Medium"
"type": "humanoid"
"subtype": "elf"
"alignment": "Any alignment"
"ac": !!int "16"
"ac_class": "[studded leather](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/studded-leather-armor.md)"
"hp": !!int "66"
"hit_dice": "12d8 + 12"
"stats":
- !!int "11"
- !!int "18"
- !!int "12"
- !!int "11"
- !!int "13"
- !!int "11"
"speed": "30 ft."
"skillsaves":
  "Nature": !!int "2"
  "Stealth": !!int "5"
  "Perception": !!int "5"
  "Survival": !!int "3"
"senses": "passive Perception 15"
"languages": "Common, Elvish"
"cr": "3"
"traits":
- "desc": "The elvish veteran archer has advantage on Wisdom ([Survival](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Survival))\
    \ checks to track Beasts and on Intelligence ([Nature](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Nature))\
    \ checks to recall information about Beasts."
  "name": "Beast Hunter"
- "desc": "The elvish veteran archer has advantage on saving throws against being\
    \ [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
    \ and magic can't put the archer to sleep."
  "name": "Fey Ancestry"
- "desc": "The elvish veteran archer has advantage on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on hearing or sight."
  "name": "Keen Hearing and Sight"
- "desc": "A longbow deals one extra die of its damage when the archer hits with it\
    \ (included in the attack). In addition, when the archer makes a ranged attack\
    \ with a longbow, it doesn't have disadvantage on the attack roll from being within\
    \ 5 feet of a hostile creature, though it may still have disadvantage from other\
    \ sources."
  "name": "Point Blank Hunter"
"actions":
- "desc": "The elvish veteran archer makes three Shortsword attacks or two Longbow\
    \ attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7 (1d6\
    \ + 4) piercing damage."
  "name": "Shortsword"
- "desc": "Ranged Weapon Attack: +6 to hit, range 150/600 ft., one target. Hit:\
    \ 13 (2d8 + 4) piercing damage. Instead of dealing damage, the archer can pin\
    \ part of the target's clothing or body to the ground or to a nearby wall or tree.\
    \ If it does so, the target is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained).\
    \ A creature, including the target, can take its action to remove the arrow and\
    \ free the [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ target by succeeding on a DC 14 Strength check."
  "name": "Longbow"
- "desc": "The elvish veteran archer fires a flurry of arrows in a 15-foot cone. Each\
    \ creature in the cone must make a DC 14 Dexterity saving throw, taking 18 (4d8)\
    \ piercing damage on a failed save, or half as much damage on a successful one."
  "name": "Arrow Spray (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/elvish-veteran-archer-tob1-2023.webp"
```
^statblock

## Environment

forest