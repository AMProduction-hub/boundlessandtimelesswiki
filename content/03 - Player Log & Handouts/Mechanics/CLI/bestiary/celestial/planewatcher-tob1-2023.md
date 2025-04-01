---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/10
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/celestial
statblock: inline
aliases: ["Planewatcher"]
---
# [Planewatcher](03 - Player Log & Handouts\Mechanics\CLI\bestiary\celestial/planewatcher-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 293*  

*The brilliant lasso tightened around the eldritch monster as the faceless winged creature dragged it across a hellish landscape.*

A planewatcher is sworn to protect the order of the boundaries between worlds. These angelic creatures fearlessly track down people and monsters who cross the boundaries of the planes and drag them back to where they came from, willingly or otherwise. Each planewatcher is bound to a single plane of existence.

## Friend or Foe

Planewatchers are dedicated to their purpose, regardless of morality. Heroes may find themselves beseeching a planewatcher for help to battle an interplanar foe, or find themselves fighting one while on a planar mission. Planewatchers track down trespassers based on the perceived threat to the multiverse.

## Unlikely Allies

Star drakes protect the Material Plane in much the same way planewatchers protect their respective planes. Because of this, the Material Plane has fewer planewatchers than other planes, and the two beings can work in concert to maintain the natural order of the multiverse.

```statblock
"name": "Planewatcher (ToB1-2023)"
"size": "Medium"
"type": "celestial"
"alignment": "Lawful Neutral"
"ac": !!int "18"
"ac_class": "[plate](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/plate-armor.md)"
"hp": !!int "136"
"hit_dice": "16d8 + 64"
"stats":
- !!int "18"
- !!int "18"
- !!int "18"
- !!int "17"
- !!int "18"
- !!int "20"
"speed": "30 ft., climb 90 ft."
"saves":
  "Charisma": !!int "9"
  "Wisdom": !!int "8"
"skillsaves":
  "Athletics": !!int "8"
  "Insight": !!int "8"
  "Perception": !!int "8"
  "Survival": !!int "8"
"damage_resistances": "radiant; bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "truesight 120 ft., passive Perception 18"
"languages": "all, telepathy 120 ft."
"cr": "10"
"traits":
- "desc": "The planewatcher has advantage on saving throws against spells and other\
    \ magical effects."
  "name": "Magic Resistance"
- "desc": "The planewatcher can pinpoint the location of creatures not native to the\
    \ plane the planewatcher currently occupies and planar portals within 60 feet\
    \ of it, and the planewatcher can sense the general direction of such creatures\
    \ and portals within 1 mile of it."
  "name": "Planar Sense"
- "desc": "The planewatcher is immune to any spell or effect that would force it to\
    \ leave its current plane, unless it wants to leave."
  "name": "Plane Bound"
- "desc": "The planewatcher always knows the direction and distance to any creature\
    \ that dispels, breaks, or otherwise avoids the geas of the promise it made via\
    \ Planar Ultimatum, provided the planewatcher and the creature are on the same\
    \ plane of existence. While grappling such a creature, it can cast the [banishment](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/banishment.md)\
    \ spell as a bonus action (spell save DC 17) on that creature."
  "name": "Word-Bound"
"actions":
- "desc": "The planewatcher makes one Radiant Lasso attack and two Enervating Blast\
    \ attacks, or it makes three Enervating Blast attacks. It can replace two attacks\
    \ with a use of Planar Ultimatum."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 30 ft., one target. Hit: 22\
    \ (4d6 + 4) radiant damage, and the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 16) if the planewatcher isn't already grappling a creature. Until\
    \ this grapple ends, the target is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ can't tell a lie, and can't teleport or be transported to another plane of existence\
    \ unless the planewatcher wills it."
  "name": "Radiant Lasso"
- "desc": "Melee or Ranged Spell Attack: +9 to hit, range 60 ft., one target.\
    \ Hit: 23 (4d8 + 5) force damage, and the target has disadvantage on Strength\
    \ and Dexterity checks until the end of its next turn."
  "name": "Enervating Blast"
- "desc": "The planewatcher demands one creature [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ by it to return to the creature's home plane within 24 hours. If the creature\
    \ doesn't swear to do so, it must make a DC 17 Constitution saving throw, taking\
    \ 45 (10d8) radiant damage on a failed save, or half as much damage on a successful\
    \ one If the creature swears to return, it becomes affected by the [geas](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/geas.md)\
    \ spell for 30 days, which compels the creature to return to its home plane as\
    \ soon as possible."
  "name": "Planar Ultimatum"
"bonus_actions":
- "desc": "The planewatcher pulls a creature [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ by it up to 25 feet straight toward it."
  "name": "Reel"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/celestial/token/planewatcher-tob1-2023.webp"
```
^statblock

## Environment

planar