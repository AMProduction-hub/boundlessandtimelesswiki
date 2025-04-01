---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/mpp
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/dragon
statblock: inline
aliases: ["Time Dragon Wyrmling"]
---
# [Time Dragon Wyrmling](03 - Player Log & Handouts\Mechanics\CLI\bestiary\dragon/time-dragon-wyrmling-mpp.md)
*Source: Morte's Planar Parade p. 51*  

These sleek dragons harness the power of time to manipulate the past, present, and future. Time dragon wyrmlings are born with shining scales and have horns that are barely more than nubs. As they master the flow of time, their horns grow with branching, rainbow-hued veins suggestive of time's paths and possibilities. Ancient time dragons can create temporal gates connected to specific times and places in the multiverse. Using these, they and allied creatures can travel anywhere in time to affect fate-determining moments or to banish threats beyond the flow of time. As a result of their ability to travel between ages, time dragons often seem unstuck from the usual flow of time and have a flexible view of what is, what was, and what will be.

Time dragons prize historical records, objects representative of lost cultures, and treasures from long-gone creators. They are fascinated by time-manipulation magic and forgotten knowledge. Those who stumble upon a time dragon's hoard might find invaluable historical information from eras past.

```statblock
"name": "Time Dragon Wyrmling (MPP)"
"size": "Medium"
"type": "dragon"
"alignment": "typically  Neutral"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "75"
"hit_dice": "10d8 + 30"
"stats":
- !!int "19"
- !!int "10"
- !!int "17"
- !!int "17"
- !!int "13"
- !!int "17"
"speed": "30 ft., climb 30 ft., fly 60 ft."
"saves":
  "Charisma": !!int "6"
  "Dexterity": !!int "3"
  "Wisdom": !!int "4"
  "Constitution": !!int "6"
"skillsaves":
  "Stealth": !!int "6"
  "Perception": !!int "7"
  "History": !!int "9"
  "Arcana": !!int "6"
"senses": "blindsight 10 ft., darkvision 120 ft., passive Perception 17"
"languages": "Draconic plus any two languages"
"cr": "5"
"actions":
- "desc": "The dragon makes three Rend attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 7\
    \ (1d6 + 4) slashing damage plus 3 (1d6) force damage."
  "name": "Rend"
- "desc": "The dragon exhales a wave of shimmering light in a 15-foot cone. Nonmagical\
    \ objects and vegetation in that area that aren't being worn or carried crumble\
    \ to dust. Each creature in that area must make a DC 14 Constitution saving throw.\
    \ On a failed save, a creature takes 27 (6d8) force damage and is magically\
    \ weakened as it is desynchronized from the time stream. While the creature is\
    \ in this state, attack rolls against it have advantage. On a successful save,\
    \ a creature takes half as much damage only. A weakened creature can repeat the\
    \ saving throw at the end of each of its turns, ending the effect on itself on\
    \ a success."
  "name": "Time Breath (Recharge 5-6)"
"source":
- "MPP"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/dragon/token/time-dragon-wyrmling-mpp.webp"
```
^statblock