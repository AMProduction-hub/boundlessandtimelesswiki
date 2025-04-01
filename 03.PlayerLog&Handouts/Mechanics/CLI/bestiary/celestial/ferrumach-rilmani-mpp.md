---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/mpp
- ttrpg-cli/monster/cr/9
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/celestial
statblock: inline
aliases: ["Ferrumach Rilmani"]
---
# [Ferrumach Rilmani](03 - Player Log & Handouts\Mechanics\CLI\bestiary\celestial/ferrumach-rilmani-mpp.md)
*Source: Morte's Planar Parade p. 44*  

Ferrumachs are the foot soldiers of the rilmani, preserving the balance between the planes through martial force. They vigilantly defend the Spire and fight at the command of aurumachs to protect the neutrality of the multiverse. Ferrumachs gleam with the sheen of bare iron. Their bodies are honed to razor edges, and from it they can fling bolts of sharpened metal.

## Rilmani

Rilmani protect the balance between the forces and philosophies of the multiverse. They seek to maintain planar equilibrium, assuring that good, evil, law, or chaos never grow too powerful or too weak. To the rilmani, each of these forces is fundamental to the multiverse's existence. Whenever one threatens to tip the balance in its favor or a plane is on the verge of collapse, the rilmani act to even the odds.

While the rilmani might be found anywhere, they're most frequently encountered on their home plane, the Outlands, where they work to ensure that no force overexerts itself on the Concordant Opposition.

Rilmani are bipedal, with bodies of living metal that ranges in appearance from cold iron to brilliant gold. Most have smooth faces with few features, and their extraordinary anatomies often act in defiance of natural forces.

```statblock
"name": "Ferrumach Rilmani (MPP)"
"size": "Medium"
"type": "celestial"
"alignment": "typically  Neutral"
"ac": !!int "18"
"ac_class": "natural armor"
"hp": !!int "136"
"hit_dice": "16d8 + 64"
"stats":
- !!int "19"
- !!int "14"
- !!int "18"
- !!int "15"
- !!int "14"
- !!int "10"
"speed": "30 ft."
"saves":
  "Strength": !!int "8"
  "Constitution": !!int "8"
"skillsaves":
  "Athletics": !!int "8"
  "Perception": !!int "6"
"damage_resistances": "psychic"
"senses": "truesight 120 ft., passive Perception 16"
"languages": "telepathy 120 ft., any two languages"
"cr": "9"
"traits":
- "desc": "The ferrumach casts one of the following spells, requiring no material\
    \ components and using Intelligence as the spellcasting ability (spell save DC\
    \ 14):\n\nAt will: [detect magic](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/detect-magic.md)\n\
    \n1/day each: [dispel magic](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dispel-magic.md),\
    \ [ice storm](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/ice-storm.md)"
  "name": "Spellcasting"
- "desc": "A creature takes 10 (3d6) slashing damage if it starts its turn grappling\
    \ or being [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ by the ferrumach."
  "name": "Bladed Edges"
- "desc": "If the ferrumach moves at least 20 feet in a straight line toward a Large\
    \ or smaller creature and ends within 5 feet of it, that creature must succeed\
    \ on a DC 16 Strength saving throw or have the [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ condition (escape DC 18) and take 10 (3d6) piercing damage."
  "name": "Skewering Charge"
"actions":
- "desc": "The ferrumach makes three Sharpened Limb or Bolt attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 9\
    \ (1d10 + 4) slashing damage plus 11 (2d10) psychic damage."
  "name": "Sharpened Limb"
- "desc": "Ranged Weapon Attack: +8 to hit, range 20/60 ft., one target. Hit:\
    \ 7 (1d6 + 4) piercing damage plus 11 (2d10) psychic damage."
  "name": "Bolt"
"source":
- "MPP"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/celestial/token/ferrumach-rilmani-mpp.webp"
```
^statblock