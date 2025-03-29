---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/15
- ttrpg-cli/monster/environment/badlands
- ttrpg-cli/monster/size/gargantuan
- ttrpg-cli/monster/type/aberration
statblock: inline
aliases: ["Mordant Snare"]
---
# [Mordant Snare](03 - Player Log & Handouts\Mechanics\CLI\bestiary\aberration/mordant-snare-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 276*  

*The ground rumbles and a gigantic starfish with eleven arms rises from the earth, grasping at nearby prey.*

Mordant snares were created by war mages of ancient times. Each resembles an immense, eleven-armed starfish weighing eight tons, and yet a mordant snare is never obvious. Instead, it controls a dozen humanoids shuffling about aimlessly, paying little attention to their surroundings.

## Starfish Puppet Masters

Snares bury themselves under loose soil to attack creatures walking above them. After killing a humanoid, they inject acid into the victim's body that liquefies organs and muscle while leaving the skeleton, tendons, and skin intact. With the body thus hollowed out and refilled with acid and filaments, the mordant snare can control it from below like a puppet.

## Brains Preferred

The mordant snare prefers intelligent food and hunts until an area is empty of sustenance. A village can suffer tremendous losses or even be wiped out before discovering the cause. However, a mordant snare is intelligent enough to know that escaped victims may come back with friends, shovels, and weapons, ready for battle. When this occurs, the snare abandons its puppets, burrows deeper underground, and seeks a new home.

## Cooperative Killers

Mordant snares are few in number and cannot reproduce. Since the secret of their creation was lost long ago, eventually they will disappear. Until then, they cooperate with each other when in the same areas, using puppets to lure victims to one another.

```statblock
"name": "Mordant Snare (ToB1-2023)"
"size": "Gargantuan"
"type": "aberration"
"alignment": "Chaotic Evil"
"ac": !!int "18"
"ac_class": "natural armor"
"hp": !!int "248"
"hit_dice": "16d20 + 80"
"stats":
- !!int "23"
- !!int "16"
- !!int "21"
- !!int "15"
- !!int "14"
- !!int "6"
"speed": "10 ft., burrow 30 ft."
"skillsaves":
  "Deception": !!int "8"
"damage_resistances": "bludgeoning from nonmagical attacks"
"damage_immunities": "acid"
"condition_immunities": "[prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)"
"senses": "darkvision 60 ft., tremorsense 60 ft., passive Perception 12"
"languages": "Common, Primordial, telepathy 60 ft."
"cr": "15"
"traits":
- "desc": "The mordant snare has advantage on saving throws against spells and other\
    \ magical effects."
  "name": "Magic Resistance"
- "desc": "A mordant snare can spend 8 hours draining a dead Humanoid of its fluids\
    \ and internal organs, replacing them with the snare's acid and filaments. The\
    \ Humanoid's body then becomes a puppet controlled by the snare. Mordant puppets\
    \ share a telepathic link with the snare, and each puppet uses the statistics\
    \ of a zombie. The puppets can't move more than 30 feet away from the snare. The\
    \ mordant snare can have no more than twelve puppets under its control at one\
    \ time.\n\nWhen a puppet is destroyed, each creature within 5 feet of the puppet\
    \ must succeed on a DC 18 Dexterity saving throw or take 9 (2d8) acid damage.\
    \ If the mordant snare dies, all puppets it controls immediately crumble into\
    \ desiccated husks as the animating acid and filaments leave them."
  "name": "Mordant Puppets"
"actions":
- "desc": "The mordant snare makes one Bite attack and four Tentacle attacks, or it\
    \ makes four Acid Spike attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 17\
    \ (2d10 + 6) piercing damage plus 18 (4d8) acid damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +11 to hit, reach 20 ft., one target. Hit: 15\
    \ (2d8 + 6) bludgeoning damage, and the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 18) if it is a Large or smaller creature. The mordant snare has eleven\
    \ tentacles, each of which can grapple only one target."
  "name": "Tentacle"
- "desc": "Ranged Weapon Attack: +8 to hit, range 30/120 ft., one target. Hit:\
    \ 10 (2d6 + 3) piercing damage plus 13 (3d8) acid damage."
  "name": "Acid Spike"
- "desc": "While underground, the mordant snare covers itself in dirt, sand, or other\
    \ material and lurks just below the surface. The mordant snare is indistinguishable\
    \ from the ground around it while motionless and covered in this way. When a creature\
    \ enters the mordant snare's space, the snare can make one Tentacle attack against\
    \ the creature as a reaction, removing the covering material."
  "name": "Hidden Trap"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/aberration/token/mordant-snare-tob1-2023.webp"
```
^statblock

## Environment

badlands