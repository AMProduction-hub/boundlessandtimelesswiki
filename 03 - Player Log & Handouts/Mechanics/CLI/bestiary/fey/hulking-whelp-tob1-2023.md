---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/farmland
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/fey/shapechanger
statblock: inline
aliases: ["Hulking Whelp"]
---
# [Hulking Whelp](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/hulking-whelp-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 236*  

*This gray-skinned dog-like creature seems pathetically eager to please but fantastically skittish, its ears alerting at every nearby sound, and its large oval eyes following anything that passes by.*

## Emotional Giant

A hulking whelp is a tightly wound ball of emotion, extremely defensive of its personal space and terrified of the world around it. When it feels its personal space is violated, or its fragile concentration is broken, the small, quivery fey grows into a muscled beast of giant proportions.

## Calm Friend

When its emotions are under control, a hulking whelp is friendly and even helpful, although this has more to do with its guilt over past actions than a true desire to help others. In its calm form, a hulking whelp is just over three feet tall at the shoulder and weighs 50 pounds. Unleashed, it is 20 feet tall and 4,000 pounds.

```statblock
"name": "Hulking Whelp (ToB1-2023)"
"size": "Small"
"type": "fey"
"subtype": "shapechanger"
"alignment": "Chaotic Neutral"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "94"
"hit_dice": "9d12 + 36"
"stats":
- !!int "21"
- !!int "10"
- !!int "18"
- !!int "7"
- !!int "14"
- !!int "9"
"speed": "40 ft."
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks"
"senses": "passive Perception 12"
"languages": ""
"cr": "5"
"traits":
- "desc": "The hulking whelp has disadvantage on saving throws against spells and\
    \ other magical effects that reduce strong emotions, such as the [calm emotions](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/calm-emotions.md)\
    \ spell."
  "name": "Frightened Anger (Hulking Form Only)"
- "desc": "A friendly creature that has interacted peacefully with the hulking whelp\
    \ in its whelp form can try to calm it by speaking firmly and persuasively. The\
    \ hulking whelp must be able to hear the creature, who must take an action to\
    \ make a DC 15 Charisma ([Persuasion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Persuasion))\
    \ check. If the check succeeds, the hulking whelp transforms back into its whelp\
    \ form on its next turn and stops attacking. If the hulking whelp takes damage\
    \ before then, it remains in its hulking form and continues attacking."
  "name": "Pacify (Hulking Form Only)"
- "desc": "On each of the hulking whelp's turns, it attacks the nearest creature it\
    \ can see. If no creature is near enough to move to and attack, the hulking whelp\
    \ attacks an object, with preference for an object smaller than itself. If no\
    \ creature is near enough to move to and attack for two turns in a row, the hulking\
    \ whelp uses Change Shape to return to its whelp form and stops attacking."
  "name": "Unleashed Emotion (Hulking Form Only)"
"actions":
- "desc": "The hulking whelp makes two Slam attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 18\
    \ (3d8 + 5) bludgeoning damage."
  "name": "Slam"
"bonus_actions":
- "desc": "The hulking whelp transforms into a Huge, hulking canine or back into its\
    \ true whelp form, which is Fey. Its statistics, other than its size and creature\
    \ type, are the same in each form. Any equipment it is wearing or carrying isn't\
    \ transformed. It reverts to its true form if it dies."
  "name": "Change Shape"
"reactions":
- "desc": "When the hulking whelp is hit with an attack or when a creature it can\
    \ see or hear within 30 feet of it threatens to harm it, it must succeed on a\
    \ DC 12 Wisdom saving throw or transform into its hulking canine form (see the\
    \ Change Shape bonus action)."
  "name": "Defensive Transformation (Whelp Form Only)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/hulking-whelp-tob1-2023.webp"
```
^statblock

## Environment

farmland, forest