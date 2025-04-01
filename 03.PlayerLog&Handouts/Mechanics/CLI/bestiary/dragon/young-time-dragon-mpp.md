---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/mpp
- ttrpg-cli/monster/cr/11
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/dragon
statblock: inline
aliases: ["Young Time Dragon"]
---
# [Young Time Dragon](03 - Player Log & Handouts\Mechanics\CLI\bestiary\dragon/young-time-dragon-mpp.md)
*Source: Morte's Planar Parade p. 51*  

These sleek dragons harness the power of time to manipulate the past, present, and future. Time dragon wyrmlings are born with shining scales and have horns that are barely more than nubs. As they master the flow of time, their horns grow with branching, rainbow-hued veins suggestive of time's paths and possibilities. Ancient time dragons can create temporal gates connected to specific times and places in the multiverse. Using these, they and allied creatures can travel anywhere in time to affect fate-determining moments or to banish threats beyond the flow of time. As a result of their ability to travel between ages, time dragons often seem unstuck from the usual flow of time and have a flexible view of what is, what was, and what will be.

Time dragons prize historical records, objects representative of lost cultures, and treasures from long-gone creators. They are fascinated by time-manipulation magic and forgotten knowledge. Those who stumble upon a time dragon's hoard might find invaluable historical information from eras past.

```statblock
"name": "Young Time Dragon (MPP)"
"size": "Large"
"type": "dragon"
"alignment": "typically  Neutral"
"ac": !!int "18"
"ac_class": "natural armor"
"hp": !!int "210"
"hit_dice": "20d10 + 100"
"stats":
- !!int "20"
- !!int "12"
- !!int "20"
- !!int "20"
- !!int "15"
- !!int "17"
"speed": "40 ft., climb 40 ft., fly 80 ft."
"saves":
  "Charisma": !!int "7"
  "Dexterity": !!int "5"
  "Wisdom": !!int "6"
  "Constitution": !!int "9"
"skillsaves":
  "Stealth": !!int "9"
  "Perception": !!int "10"
  "History": !!int "13"
  "Arcana": !!int "9"
"senses": "blindsight 30 ft., darkvision 120 ft., passive Perception 20"
"languages": "Draconic plus any four languages"
"cr": "11"
"actions":
- "desc": "The dragon makes three Rend attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 12\
    \ (2d6 + 5) slashing damage plus 7 (2d6) force damage."
  "name": "Rend"
- "desc": "The dragon exhales a wave of shimmering light in a 30-foot cone. Nonmagical\
    \ objects and vegetation in that area that aren't being worn or carried crumble\
    \ to dust. Each creature in that area must make a DC 17 Constitution saving throw.\
    \ On a failed save, a creature takes 31 (7d8) force damage and is magically\
    \ weakened as it is desynchronized from the time stream. While the creature is\
    \ in this state, attack rolls against it have advantage. On a successful save,\
    \ a creature takes half as much damage only. A weakened creature can repeat the\
    \ saving throw at the end of each of its turns, ending the effect on itself after\
    \ it succeeds on two of these saves."
  "name": "Time Breath (Recharge 5-6)"
"source":
- "MPP"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/dragon/token/young-time-dragon-mpp.webp"
```
^statblock