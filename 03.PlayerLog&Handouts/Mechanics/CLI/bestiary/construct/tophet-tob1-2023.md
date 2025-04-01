---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/8
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/construct
statblock: inline
aliases: ["Tophet"]
---
# [Tophet](03 - Player Log & Handouts\Mechanics\CLI\bestiary\construct/tophet-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 364*  

*An enormous bronze and iron statue filled with fire towers above the ring of chanting, frenzied worshipers.*

Worshipers of fire gods use tophets to incinerate sacrifices in their flaming maws. A tophet has a large opening in the front where the flames can be seen; sometimes this is an enormous mouth, and at other times it is a large hole in the tophet's belly. Horns and expressions of anger or wide‑mouthed laughter are common.

## Eager for Sacrifices

Among fire cultists, it's widely known that when a tophet's hands are raised above its mouth, it is demanding a sacrifice to roll down its palms and into its fiery maw.

## Heed Musical Commands

Flutes and drums can be used to control the actions of a tophet during sacrifices. They have the fortunate side effect of drowning out the cries and screams of living sacrifices.

## Magical Fires

The fires within a tophet's bronze body are largely magical and fueled by sacrifices. They don't require more than a symbolic amount of wood or coal to keep burning, but they do require sacrifices of food, cloth, and living creatures to keep them under control. A tophet that is not granted a sacrifice when it demands one might go on a fiery rampage, burning down buildings, granaries, or barns until its hunger is satisfied.

```statblock
"name": "Tophet (ToB1-2023)"
"size": "Huge"
"type": "construct"
"alignment": "Neutral Evil"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "161"
"hit_dice": "14d12 + 70"
"stats":
- !!int "21"
- !!int "10"
- !!int "20"
- !!int "6"
- !!int "10"
- !!int "10"
"speed": "30 ft."
"saves":
  "Dexterity": !!int "3"
  "Strength": !!int "8"
  "Constitution": !!int "8"
"skillsaves":
  "Perception": !!int "3"
"damage_resistances": "cold"
"damage_immunities": "fire, poison, psychic"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 13"
"languages": "understands the languages of its creator but can't speak"
"cr": "8"
"traits":
- "desc": "The tophet sheds bright light in a 30-foot radius and dim light for an\
    \ additional 30 feet. Each creature in the bright light has resistance to cold\
    \ damage. At the start of each of its turns, the tophet chooses whether this light\
    \ is active."
  "name": "Burning Heart"
- "desc": "The tophet doesn't require air, food, drink, or sleep."
  "name": "Construct Nature"
- "desc": "A creature that touches the tophet or hits it with a melee attack while\
    \ within 5 feet of it takes 3 (1d6) fire damage."
  "name": "Heated Body"
"actions":
- "desc": "The tophet makes two Slam attacks. It can replace one Slam attack with\
    \ a use of Burning Belly."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 16\
    \ (2d10 + 5) bludgeoning damage plus 7 (2d6) fire damage, and the target is\
    \ [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 16) if it is a Large or smaller creature."
  "name": "Slam"
- "desc": "The tophet makes one Slam attack against a target it is grappling as it\
    \ shoves the creature into its open, flame-filled belly. If the attack hits, the\
    \ target is forced into the tophet's burning belly, and the grapple ends. While\
    \ inside the belly, the target is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ has three-quarters cover against attacks and other effects outside the belly,\
    \ and it takes 14 (4d6) fire damage at the start of each of its turns. A creature,\
    \ including the target, can take its action to pull the target free from the belly\
    \ by succeeding on a DC 16 Strength check. The creature making the attempt takes\
    \ 7 (2d6) fire damage."
  "name": "Burning Belly"
- "desc": "Flames erupt on a point the tophet can see within 100 feet of it. Each\
    \ creature within 10 feet of that point must make a DC 16 Dexterity saving throw,\
    \ taking 35 (10d6) fire damage on a failed save, or half as much damage on a\
    \ successful one."
  "name": "Gout of Flame (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/construct/token/tophet-tob1-2023.webp"
```
^statblock

## Environment

urban