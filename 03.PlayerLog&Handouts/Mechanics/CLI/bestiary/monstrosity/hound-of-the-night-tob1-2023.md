---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Hound of the Night"]
---
# [Hound of the Night](03 - Player Log & Handouts\Mechanics\CLI\bestiary\monstrosity/hound-of-the-night-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 235*  

*This enormous black hound pants in the moonlight, wisps of steam rising from its muzzle, as it follows its elvish master.*

## Fey Bloodhounds

Hounds of the night are bred by the shadow fey for use as hunting companions and guardians, and they excel at both tasks. Far more intelligent than other hounds, they are difficult to evade once they are on a quarry's trail, because they can think their way past problems that would throw their lesser kin off the trail. Their shadow fey masters claim that hounds of the night can smell a shadow on running water and can sniff out a ghost passing through a wall.

## Cousins to Winter

Somewhere in their early existence as a breed, some enterprising hunter interbred them with winter wolves. Every trace of their white fur is long gone, but the cold breath of those dread canines remains.

## Dimensional Stepping

Hounds of night excel at distracting prey while some of their pack teleport away to achieve some larger goal, such as dragging off a treasure or overwhelming a spellcaster in the back ranks.

```statblock
"name": "Hound of the Night (ToB1-2023)"
"size": "Large"
"type": "monstrosity"
"alignment": "Neutral"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "112"
"hit_dice": "15d10 + 30"
"stats":
- !!int "20"
- !!int "16"
- !!int "14"
- !!int "7"
- !!int "14"
- !!int "10"
"speed": "30 ft."
"saves":
  "Dexterity": !!int "6"
  "Wisdom": !!int "5"
  "Constitution": !!int "5"
"skillsaves":
  "Intimidation": !!int "3"
  "Stealth": !!int "6"
  "Perception": !!int "5"
"damage_vulnerabilities": "fire"
"damage_immunities": "cold"
"senses": "darkvision 60 ft., passive Perception 15"
"languages": "understands Elvish and Umbral but can't speak"
"cr": "5"
"traits":
- "desc": "The hound of the night has advantage on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on smell. If it is tracking a Fey, Giant, or Humanoid whose\
    \ scent it knows, the hound can continue tracking that creature if the creature\
    \ moves into the Border Ethereal or teleports, provided the creature isn't in\
    \ the Border Ethereal for more than 1 minute or that the creature doesn't teleport\
    \ more than 100 feet at a time."
  "name": "Fey Scent"
"actions":
- "desc": "The hound of the night makes two Bite attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 14\
    \ (2d8 + 5) piercing damage plus 4 (1d8) cold damage, and the target must\
    \ succeed on a DC 14 Strength saving throw or be knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Bite"
- "desc": "The hound exhales frost in a 15-foot cone. Each creature in the area must\
    \ make a DC 14 Dexterity saving throw, taking 27 (6d8) cold damage on a failed\
    \ save, or half as much damage on a successful one."
  "name": "Frost Breath (Recharge 5-6)"
- "desc": "The hound magically teleports, along with any equipment it is wearing or\
    \ carrying, up to 60 feet to an unoccupied space it can see. Before or after teleporting,\
    \ the hound can make one Bite attack."
  "name": "Teleport (Recharge 4-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/monstrosity/token/hound-of-the-night-tob1-2023.webp"
```
^statblock

## Environment

forest, planar