---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Angler Worm"]
---
# [Angler Worm](03 - Player Log & Handouts\Mechanics\CLI\bestiary\monstrosity/angler-worm-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 20*  

*As patient as a fisherman, the angler worm lights a beacon in the darkness and waits for its next meal.*

## Silk Snares

The angler worm burrows into the ceilings of caves and tunnels, where it creates snares from strong silk threads coated with sticky mucus. It then lures prey into its snares while remaining safely hidden, emerging only to feed. With dozens of snares, food always comes to the angler worm eventually.

```statblock
"name": "Angler Worm (ToB1-2023)"
"size": "Huge"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "104"
"hit_dice": "11d12 + 33"
"stats":
- !!int "14"
- !!int "5"
- !!int "16"
- !!int "3"
- !!int "14"
- !!int "1"
"speed": "20 ft., climb 20 ft."
"damage_immunities": "poison"
"condition_immunities": "[blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
  \ [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [deafened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Deafened),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)"
"senses": "tremorsense 60 ft., passive Perception 12"
"languages": ""
"cr": "4"
"traits":
- "desc": "The angler worm has advantage on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on vibrations."
  "name": "Keen Touch"
- "desc": "The angler worm ignores movement restrictions caused by its snares or the\
    \ snares of other angler worms."
  "name": "Snare Walker"
- "desc": "The angler worm can climb difficult surfaces, including upside down on\
    \ ceilings, without needing to make an ability check."
  "name": "Spider Climb"
- "desc": "With 10 minutes of work, the angler worm can create a web of nearly transparent\
    \ snares in a 20-foot cube. The web must be anchored between two solid masses\
    \ or layered across a floor, wall, or ceiling. A web of snares layered over a\
    \ flat surface has a depth of 5 feet. The web is difficult terrain, and the snares\
    \ forming it are nearly transparent, requiring a successful DC 15 Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ check to notice them.\n\nA creature that starts its turn in the web of snares\
    \ or enters the web during its turn must succeed on a DC 13 Dexterity saving throw\
    \ or be [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ by the sticky snares. A creature [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ by the snares can use its action to free itself by succeeding on a DC 13 Strength\
    \ check."
  "name": "Transparent Trap"
"actions":
- "desc": "The angler worm makes two Bite attacks or one Bite attack and one Coils\
    \ attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 9\
    \ (2d6 + 2) piercing damage plus 3 (1d6) acid damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +4 to hit, reach 10 ft., one creature. Hit:\
    \ 12 (3d6 + 2) bludgeoning damage, and the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 13). Until this grapple ends, the target is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ by the angler worm, it can't breathe, it takes 10 (3d6) bludgeoning damage\
    \ at the start of each of the angler worm's turns, and the angler worm can't use\
    \ its Coils on another target."
  "name": "Coils"
- "desc": "The angler worm creates an orb of faint, blue light on a point it can see\
    \ within 20 feet of it. The light glows until the start of the worm's next turn.\
    \ When a creature that isn't an angler worm starts its turn within 60 feet of\
    \ the orb and can see the light, it must succeed on a DC 13 Wisdom saving throw\
    \ or be [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ until the start of its next turn. While [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
    \ the creature must take the Dash action and move toward the light by the most\
    \ direct route, trying to get within 5 feet of the light. It doesn't avoid opportunity\
    \ attacks, but before moving into damaging terrain, such as lava or a pit, the\
    \ creature can repeat the saving throw, ending the effect on itself on a success.\
    \ If the [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ creature enters the worm's snares, it has disadvantage on the saving throw to\
    \ avoid being [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)."
  "name": "Ethereal Lure (Recharge 4-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/monstrosity/token/angler-worm-tob1-2023.webp"
```
^statblock

## Environment

underdark