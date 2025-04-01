---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/mpp
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/size/small-or-medium
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Society of Sensation Muse"]
---
# [Society of Sensation Muse](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/society-of-sensation-muse-mpp.md)
*Source: Morte's Planar Parade p. 61, Sigil and the Outlands*  

The muses of the Society of Sensation are performers who enthrall crowds with spectacle and minor sensory experiences. When threatened, they beguile their foes, placating their enemies with magical displays.

```statblock
"name": "Society of Sensation Muse (MPP)"
"size": "Small or Medium"
"type": "humanoid"
"alignment": "Any alignment"
"ac": !!int "14"
"ac_class": "[leather armor](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/leather-armor.md)"
"hp": !!int "44"
"hit_dice": "8d8 + 8"
"stats":
- !!int "8"
- !!int "16"
- !!int "12"
- !!int "15"
- !!int "14"
- !!int "17"
"speed": "30 ft."
"saves":
  "Charisma": !!int "5"
  "Dexterity": !!int "5"
"skillsaves":
  "Stealth": !!int "5"
  "Insight": !!int "4"
  "Perception": !!int "4"
  "Performance": !!int "7"
"senses": "passive Perception 14"
"languages": "Common plus two more languages"
"cr": "3"
"traits":
- "desc": "The muse casts one of the following spells, using Charisma as the spellcasting\
    \ ability (spell save DC 13):\n\nAt will: [dancing lights](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dancing-lights.md)\n\
    \n1/day each: [comprehend languages](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/comprehend-languages.md),\
    \ [hypnotic pattern](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/hypnotic-pattern.md)"
  "name": "Spellcasting"
"actions":
- "desc": "The muse makes two Beguiling Resonance attacks."
  "name": "Multiattack"
- "desc": "Melee or Ranged Spell Attack: +5 to hit, reach 5 ft. or range 90 ft.,\
    \ one target. Hit: 9 (2d8) psychic damage. If the target is a creature, it\
    \ must succeed on a DC 13 Charisma saving throw or have disadvantage on the next\
    \ attack roll it makes until the end of its next turn."
  "name": "Beguiling Resonance"
"bonus_actions":
- "desc": "Each creature within 30 feet of the muse must make a DC 13 Wisdom saving\
    \ throw. On a failed save, the creature has the [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ condition for 1 minute. On a successful save, the creature becomes immune to\
    \ any muse's Enchanting Presence for 24 hours.\n\nWhenever the muse deals damage\
    \ to the [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ creature, the [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ creature can repeat the saving throw, ending the effect on itself on a success."
  "name": "Enchanting Presence"
"source":
- "MPP"
- "SatO"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/society-of-sensation-muse-mpp.webp"
```
^statblock