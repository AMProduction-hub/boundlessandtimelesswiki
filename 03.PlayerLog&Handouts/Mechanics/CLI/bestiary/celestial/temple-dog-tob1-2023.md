---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/celestial
statblock: inline
aliases: ["Temple Dog"]
---
# [Temple Dog](03 - Player Log & Handouts\Mechanics\CLI\bestiary\celestial/temple-dog-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 359*  

*Looking like a mix between a large dog and a lion, the creature glares at everyone who passes the threshold of the temple it guards.*

A temple dog is an imposing guardian used by various deities to protect their temples. They are fiercely loyal and territorial. Often depicted in temple statuary, the creature has a largely canine body, soft but short hair, a thick hairy tail, and a mane like a lion's around a dog's face with a short snout.

## Divine Colors

Coloration and other features of the temple dog vary to match the deity who created it, and sometimes a temple dog's coloration is quite fanciful. Greenish-bronze temple dogs are known, as are those the color of cinnabar or lapis. Even coats resembling fired ceramic of an orange hue have been seen guarding some temples. These unusual casts make it easy for a temple dog to be mistaken for statuary.

## Travel with Priests

As a temple protector, it rarely leaves the grounds of the temple to which it has been attached, but temple dogs do accompany priests or allies of the temple during travel. The temple dog cannot speak, but it understands the words and needs of those it accompanies. Temple dogs are notorious for biting their prey, then shaking the victim senseless in their massive jaws.

```statblock
"name": "Temple Dog (ToB1-2023)"
"size": "Medium"
"type": "celestial"
"alignment": "Any Good alignment"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "97"
"hit_dice": "15d8 + 30"
"stats":
- !!int "18"
- !!int "14"
- !!int "15"
- !!int "8"
- !!int "14"
- !!int "10"
"speed": "30 ft."
"saves":
  "Charisma": !!int "3"
  "Wisdom": !!int "5"
  "Constitution": !!int "5"
"skillsaves":
  "Perception": !!int "5"
"damage_resistances": "radiant; bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 15"
"languages": "understands Celestial and Common but can't speak"
"cr": "5"
"traits":
- "desc": "The temple dog has advantage on saving throws against spells and other\
    \ magical effects."
  "name": "Magic Resistance"
- "desc": "The temple dog has advantage on initiative rolls while in its temple or\
    \ within 30 feet of a priest of its deity."
  "name": "Protector's Instincts"
- "desc": "The temple dog's Bite attacks are magical. When it hits with a Bite attack,\
    \ the Bite deals an extra 2d6 radiant damage (included in the attack)."
  "name": "Radiant Jaws"
- "desc": "If the temple dog moves at least 15 feet straight toward a target and then\
    \ hits it with a Bite attack on the same turn, that target must succeed on a DC\
    \ 15 Strength saving throw or be pushed up to 10 feet away from the temple dog.\
    \ If the target is pushed, the temple dog can move up to 10 feet straight toward\
    \ the target without provoking opportunity attacks."
  "name": "Rushing Bite"
"actions":
- "desc": "The temple dog makes two Bite attacks. If both attacks hit a Medium or\
    \ smaller target, the temple dog sinks in its teeth, shaking its head violently,\
    \ and the target must succeed on a DC 15 Strength saving throw or take 9 (2d8)\
    \ slashing damage and be [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 15). Until this grapple ends, the target is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ and temple dog can't Bite another target."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 8 (1d8\
    \ + 4) piercing damage plus 7 (2d6) radiant damage."
  "name": "Bite"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/celestial/token/temple-dog-tob1-2023.webp"
```
^statblock

## Environment

planar, urban