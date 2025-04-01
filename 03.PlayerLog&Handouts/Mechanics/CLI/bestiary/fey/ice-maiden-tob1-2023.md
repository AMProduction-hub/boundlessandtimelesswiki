---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/arctic
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Ice Maiden"]
---
# [Ice Maiden](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/ice-maiden-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 238*  

*This alluring beauty has flesh and hair as white as snow and eyes as blue as glacial ice.*

## Born of the Ice

Ice maidens are the daughters of powerful creatures of the cold, such as the Snow Queen, frost giants, and thursir. A few result from pleas by pregnant women lost in the snows, desperate to save their children. Fraughashar often raise these infants as ice maidens.

## Solitary Lives

Most ice maidens live solitary existences save for a servant or two under their thrall. They're lonely creatures, desperate for love but condemned to know companionship only through their magical kiss. If genuine love ever fills an ice maiden's heart, she melts into nothingness.

## Killing Dilemma

An ice maiden's hunger for affection and contact leads her to harm those she approaches, which only drives her harder to seek warmth and love. An ice maiden can become a dryad or even a humanoid if she keeps a lover's heart warm for a full year.

```statblock
"name": "Ice Maiden (ToB1-2023)"
"size": "Medium"
"type": "fey"
"alignment": "Lawful Evil"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "84"
"hit_dice": "13d8 + 26"
"stats":
- !!int "12"
- !!int "17"
- !!int "15"
- !!int "19"
- !!int "13"
- !!int "20"
"speed": "30 ft."
"saves":
  "Charisma": !!int "8"
  "Constitution": !!int "5"
"skillsaves":
  "Deception": !!int "8"
  "Stealth": !!int "6"
  "Persuasion": !!int "8"
"damage_vulnerabilities": "fire"
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "cold"
"senses": "darkvision 60 ft., passive Perception 11"
"languages": "Common, Giant, Sylvan"
"cr": "6"
"traits":
- "desc": "A creature that starts its turn within 15 feet of the ice maiden must succeed\
    \ on a DC 16 Constitution saving throw or take 3 (1d6) cold damage. Unprotected,\
    \ nonmagical flames within 15 feet of the maiden are extinguished, and water freezes\
    \ if it remains within 15 feet of the maiden for at least 1 minute."
  "name": "Chilling Presence"
- "desc": "The ice maiden can move across icy and snowy surfaces without needing to\
    \ make an ability check. Additionally, difficult terrain composed of ice or snow\
    \ doesn't cost her extra movement."
  "name": "Ice Walk"
- "desc": "The ice maiden has advantage on saving throws against spells and other\
    \ magical effects."
  "name": "Magic Resistance"
- "desc": "The ice maiden can see through areas obscured by snow or fog without penalty."
  "name": "Snow Sight"
"actions":
- "desc": "The ice maiden makes two Ice Blade or Ice Bolt attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7 (1d8\
    \ + 3) slashing damage plus 14 (4d6) cold damage."
  "name": "Ice Blade"
- "desc": "Ranged Spell Attack: +8 to hit, range 60 ft., one target. Hit: 19\
    \ (4d6 + 5) cold damage."
  "name": "Ice Bolt"
- "desc": "The ice maiden kisses a willing Humanoid, freezing the target's heart.\
    \ The target has immunity to cold damage, but it is [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ by the ice maiden until the maiden ends the effect (no action required) or until\
    \ the target is kissed by a creature that loves it. The [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ target obeys the maiden's verbal commands. If the target suffers any harm from\
    \ the maiden or her allies, or if it receives a suicidal command, it can make\
    \ a DC 16 Wisdom saving throw, ending the effect on itself on a success. The maiden\
    \ can have no more than three Humanoids [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ at a time."
  "name": "Kiss of the Frozen Heart"
- "desc": "The ice maiden blasts wintry weather on a point she can see within 60 feet\
    \ of her. Each creature within 15 feet of that point must make a DC 16 Dexterity\
    \ saving throw. On a failure, a creature takes 28 (8d6) cold damage and is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ by ice until the end of its next turn. On a success, a creature takes half the\
    \ damage and isn't [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained).\
    \ The area then becomes icy, difficult terrain for 1 minute."
  "name": "Icy Embrace (Recharge 5-6)"
"bonus_actions":
- "desc": "The ice maiden teleports, along with any equipment she is wearing or carrying,\
    \ up to 30 feet to an unoccupied space she can see. The origin and destination\
    \ spaces must contain snow or ice."
  "name": "Snow Step"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/ice-maiden-tob1-2023.webp"
```
^statblock

## Environment

arctic