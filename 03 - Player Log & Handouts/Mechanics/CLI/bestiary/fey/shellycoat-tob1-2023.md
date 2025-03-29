---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/swamp
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Shellycoat"]
---
# [Shellycoat](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/shellycoat-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 325*  

*Despite being short and squat, this creature's relationship with a troll is undeniable. The kinship is most notable in the long arms and thick, pebbly hide.*

## Long Handed and Toad-like

The shellycoat is a warped and spiteful creature also called the Iamh fada, or "long hands." They are frequently referred to as bridge trolls. Despite being fey, they are distantly related to true trolls. Unlike those tall, lanky creatures, a shellycoat is dwarfish and toad-like, with short, bent, legs and especially long arms with swollen, distended joints. It can further dislocate and stretch these joints to alarming lengths.

## Bridges and Pools

The shellycoat can be found in abandoned wells or behind waterfalls, in deep tide pools, or beneath the ice of frozen ponds, but their preferred haunt has always been under bridges. They are most active during nighttime and on heavily overcast days, because of their mortal dread of sunlight. A shellycoat's favored tactic is to lie in wait under the water, ice, or bridge and surprise its prey. It strikes outward or upward from its hiding place to snatch passersby, livestock, and lone travelers or fishermen. Prey is dragged down to the shadows and water to be robbed and devoured.

## Shining Garments

Shellycoats always fashioned themselves coats, cloaks, or shirts of colored pebbles, glass, and polished river shells. These adornments are crude but beautiful and sometimes magical.

```statblock
"name": "Shellycoat (ToB1-2023)"
"size": "Medium"
"type": "fey"
"alignment": "Neutral Evil"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "52"
"hit_dice": "7d8 + 21"
"stats":
- !!int "17"
- !!int "16"
- !!int "16"
- !!int "13"
- !!int "9"
- !!int "7"
"speed": "30 ft., swim 20 ft."
"skillsaves":
  "Stealth": !!int "4"
  "Perception": !!int "1"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)"
"senses": "darkvision 60 ft., passive Perception 11"
"languages": "Giant, Sylvan"
"cr": "2"
"traits":
- "desc": "The shellycoat can breathe air and water."
  "name": "Amphibious"
- "desc": "The shellycoat has advantage on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on hearing."
  "name": "Keen Hearing"
- "desc": "The shellycoat can see through areas obscured by fog, smoke, and steam\
    \ without penalty."
  "name": "Hazesight"
- "desc": "The shellycoat regains 3 hp at the start of its turn. If the shellycoat\
    \ takes acid or fire damage, this trait doesn't function at the start of the shellycoat's\
    \ next turn. The shellycoat dies only if it starts its turn with 0 hp and doesn't\
    \ regenerate."
  "name": "Regeneration"
- "desc": "The shellycoat has advantage on Dexterity ([Stealth](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Stealth))\
    \ checks made to hide while at least partially submerged in water."
  "name": "Water Camouflage"
- "desc": "If the shellycoat remains in nonmagical sunlight for 1 minute, it becomes\
    \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified)\
    \ at the end of that minute."
  "name": "Sunlight Petrification"
"actions":
- "desc": "The shellycoat makes one Bite attack and one Claw attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6\
    \ + 3) piercing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +5 to hit, reach 15 ft., one target. Hit: 12\
    \ (2d8 + 3) slashing damage, and the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 13) if it is a Large or smaller creature. Until this grapple ends,\
    \ the creature is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained).\
    \ The shellycoat has two claws, each of which can grapple only one creature."
  "name": "Claw"
- "desc": "While in contact with water, the shellycoat can create a 20-foot-radius\
    \ sphere of fog centered on a point it can see within 60 feet of it for 1 minute.\
    \ The sphere spreads around corners, and its area is heavily obscured. A creature\
    \ that enters the fog for the first time on a turn or starts its turn there must\
    \ succeed on a DC 13 Constitution saving throw or be [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ and unable to breathe, unless it can breathe water, for 1 minute. The creature\
    \ can repeat the saving throw at the end of each of its turns, ending the effect\
    \ on itself on a success."
  "name": "Shellycoat's Fog (1/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/shellycoat-tob1-2023.webp"
```
^statblock

## Environment

forest, swamp, underwater