---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/mpp
- ttrpg-cli/monster/cr/22
- ttrpg-cli/monster/size/gargantuan
- ttrpg-cli/monster/type/
statblock: inline
aliases: ["Planar Incarnate"]
---
# [Planar Incarnate](03 - Player Log & Handouts\Mechanics\CLI\bestiary/planar-incarnate-mpp.md)
*Source: Morte's Planar Parade p. 41*  

The Upper and Lower Planes are fundamental manifestations of good and evil, law and chaos. In the most dire and fateful circumstances, these planes can manifest primal embodiments of their might. These expressions of a plane's power are called planar incarnates, and they appear as roiling energies with features distinct to the plane that created it. They protect their home from destructive or otherwise antithetical forces, then merge back into their plane of origin.

Planar incarnates are akin to natural disasters that work to protect and further the virtues and vices of the planes they originate upon. Those from the Lower Planes might appear as roiling waves of fiendish flames or other sinister forms, while those from the Upper Planes often appear as blooms of light and wild growth or similarly majestic shapes. On the rare occasions that planar incarnates appear on another plane, they might take either form or appear as unique manifestations of the philosophies they embody.

```statblock
"name": "Planar Incarnate (MPP)"
"size": "Gargantuan"
"alignment": "Any alignment"
"ac": !!int "20"
"ac_class": "natural armor"
"hp": !!int "333"
"hit_dice": "18d20 + 144"
"stats":
- !!int "27"
- !!int "10"
- !!int "26"
- !!int "15"
- !!int "20"
- !!int "20"
"speed": "40 ft., fly 40 ft."
"skillsaves":
  "Perception": !!int "12"
"damage_immunities": "necrotic; poison; radiant; bludgeoning, piercing, slashing from\
  \ nonmagical attacks"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
  \ [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned),\
  \ [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)"
"senses": "truesight 120 ft., passive Perception 22"
"languages": "all"
"cr": "22"
"traits":
- "desc": "If the incarnate fails a saving throw, it can choose to succeed instead."
  "name": "Legendary Resistance (3/Day)"
- "desc": "The incarnate has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "An incarnate on the Upper Planes is a Celestial. An incarnate on the Lower\
    \ Planes is a Fiend."
  "name": "Planar Form"
- "desc": "The incarnate deals double damage to objects and structures."
  "name": "Siege Monster"
"actions":
- "desc": "The incarnate makes two Slam or Energy Bolt attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +15 to hit, reach 15 ft., one target. Hit: 27\
    \ (3d12 + 8) force damage."
  "name": "Slam"
- "desc": "Ranged Spell Attack: +12 to hit, range 120 ft., one target. Hit:\
    \ 32 (5d12) necrotic damage if the incarnate is a Fiend or radiant damage if\
    \ the incarnate is a Celestial."
  "name": "Energy Bolt"
- "desc": "The incarnate exhales concentrated energy native to its plane in a 60-foot\
    \ cone. Each creature in that area must make a DC 23 Constitution saving throw.\
    \ On a failed save, a creature takes 52 (8d12) necrotic damage if the incarnate\
    \ is a Fiend or radiant damage if the incarnate is a Celestial, and the creature\
    \ has the [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ condition until the end of the incarnate's next turn. On a successful save,\
    \ a creature takes half as much damage only."
  "name": "Planar Exhalation (Recharge 5-6)"
"reactions":
- "desc": "The incarnate can take up to three reactions per round but only one per\
    \ turn."
  "name": ""
- "desc": "In response to being hit by an attack roll, the incarnate turns its magical\
    \ gaze toward one creature it can see within 120 feet of itself and commands it\
    \ to combust. The target must succeed on a DC 20 Wisdom saving throw or take 16\
    \ (3d10) fire damage."
  "name": "Searing Gaze"
- "desc": "Immediately after a creature the incarnate sees ends its turn, the incarnate\
    \ teleports up to 60 feet to an unoccupied space it can see."
  "name": "Teleport"
"source":
- "MPP"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/token/planar-incarnate-mpp.webp"
```
^statblock