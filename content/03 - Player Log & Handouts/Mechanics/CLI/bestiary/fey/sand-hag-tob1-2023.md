---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Sand Hag"]
---
# [Sand Hag](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/sand-hag-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 229*  

*This withered crone glares malevolently, her face framed by lank, gray hair. Her malicious grin is filled with shark teeth and drool trickles from her lips.*

## Hatred of Beauty

Dressed in tattered robes and skeletally thin, sand hags are terrifying crones that haunt desert ruins and forgotten oases. Their hatred for things of beauty and peace is terrible to behold. A sand hag uses her illusions and mimicry to lure travelers into an ambush.

## False Oasis

These hags delight in tricking a caravan into an illusory oasis, killing all the riding animals and pack animals so the travelers can't flee, and then terrifying and slaughtering them one by one.

## Drain Bodies

For the slaughter of animals or humanoids, a sand hag prefers to rely on her claws, which drain the moisture from her victims. They leave the mummified remnants in postures of life—tied to a saddle or atop a guard tower—to terrify others.

```statblock
"name": "Sand Hag (ToB1-2023)"
"size": "Medium"
"type": "fey"
"alignment": "Chaotic Evil"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "120"
"hit_dice": "16d8 + 48"
"stats":
- !!int "18"
- !!int "15"
- !!int "16"
- !!int "16"
- !!int "14"
- !!int "16"
"speed": "30 ft., burrow 30 ft."
"skillsaves":
  "Deception": !!int "6"
  "Stealth": !!int "5"
  "Perception": !!int "5"
"senses": "darkvision 120 ft., passive Perception 15"
"languages": "Common, Dwarvish, Giant, Gnomish"
"cr": "6"
"traits":
- "desc": "The sand hag casts one of the following spells, requiring no material components\
    \ and using Charisma as the spellcasting ability (spell save DC 14):\n\nAt will:\
    \ [silent image](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/silent-image.md)\n\
    \n3/day each: [hallucinatory terrain](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/hallucinatory-terrain.md)\
    \ (as an action), [major image](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/major-image.md)"
  "name": "Spellcasting"
- "desc": "The sand hag has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "The sand hag can mimic animal sounds and Humanoid voices. A creature that\
    \ hears the sounds can tell they are imitations with a successful DC 16 Wisdom\
    \ ([Insight](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Insight))\
    \ check."
  "name": "Mimicry"
- "desc": "Difficult terrain composed of sand or gravel doesn't cost the hag extra\
    \ movement. In addition, while in sandy terrain, she doesn't leave tracks and\
    \ has tremorsense out to a range of 30 feet."
  "name": "Scorpion Walk"
"actions":
- "desc": "The hag makes three Claw attacks. If two Claw attacks hit one creature,\
    \ the target must succeed on a DC 14 Constitution saving throw or suffer one level\
    \ of [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion).\
    \ A creature can't suffer more than two levels of [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion)\
    \ from this effect."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 13\
    \ (2d8 + 4) slashing damage."
  "name": "Claw"
- "desc": "The sand hag covers herself and anything she is wearing or carrying with\
    \ a magical illusion that makes her look like another creature of her general\
    \ size and Humanoid shape. The illusion ends if the hag takes a bonus action to\
    \ end it or if she dies.\n\nThe changes wrought by this effect fail to hold up\
    \ to physical inspection. Otherwise, a creature must take an action to visually\
    \ inspect the illusion and succeed on a DC 20 Intelligence ([Investigation](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Investigation))\
    \ check to discern that the hag is disguised."
  "name": "Illusory Appearance"
- "desc": "The sand hag generates a blast of hot wind and sand in a 30-foot cone.\
    \ Each creature in the area must make a DC 14 Constitution saving throw. On a\
    \ failure, a creature takes 14 (4d6) slashing damage and 9 (2d8) fire damage\
    \ and is [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ for 1 minute. On a success, a creature takes half the damage and isn't [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded).\
    \ A [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success. The area is heavily obscured by airborne\
    \ sand until the start of the sand hag's next turn."
  "name": "Scouring Sirocco (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/sand-hag-tob1-2023.webp"
```
^statblock

## Environment

desert