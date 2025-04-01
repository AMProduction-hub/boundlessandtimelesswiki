---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/celestial
statblock: inline
aliases: ["Uraeus"]
---
# [Uraeus](03 - Player Log & Handouts\Mechanics\CLI\bestiary\celestial/uraeus-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 373*  

*A sleek serpent wends through the air, held aloft on bronze-feathered wings. The flying cobra flares its hood and hisses, hurling a spray of orange sparks from its fanged mouth.*

Uraeuses resemble vibrantly colored cobras. The serpent's scales are the rich, gold-flecked blue of lapis lazuli and its eyes gleam white. However, its most distinguishing feature is its pair of feathery, bronze wings. It glides gracefully through the air with a deliberate vigilance that reveals its intelligence. A uraeus grows up to three feet long, and weighs around five pounds.

## Divine Protectors

Uraeuses are celestial creatures that carry a spark of divine fire within them, and they thirst for purpose when they arrive on the Material Plane. Whether the creature was deliberately summoned or found its way to the Material Plane through other means, a uraeus is created to protect. Once it finds a worthy charge, it devotes its fiery breath and searing venom to protecting that ward. A uraeus is fanatically loyal to the creature it protects. Only gross mistreatment or vicious evil can drive a uraeus to break its bond and leave.

```statblock
"name": "Uraeus (ToB1-2023)"
"size": "Tiny"
"type": "celestial"
"alignment": "Lawful Neutral"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "40"
"hit_dice": "9d4 + 18"
"stats":
- !!int "6"
- !!int "15"
- !!int "14"
- !!int "10"
- !!int "14"
- !!int "9"
"speed": "30 ft., fly 60 ft."
"saves":
  "Charisma": !!int "1"
  "Wisdom": !!int "4"
"skillsaves":
  "Perception": !!int "4"
"damage_resistances": "radiant; bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "fire, poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "blindsight 10 ft., passive Perception 14"
"languages": "understands Celestial and Common but can't speak"
"cr": "2"
"traits":
- "desc": "The uraeus doesn't provoke opportunity attacks when it flies out of an\
    \ enemy's reach."
  "name": "Flyby"
- "desc": "The uraeus has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
"actions":
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6\
    \ + 2) piercing damage plus 9 (2d8) poison damage, and the target must succeed\
    \ on a DC 12 Constitution saving throw or be [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 minute. While [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
    \ the target takes 3 (1d6) fire damage at the start of each of its turns. A\
    \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Bite"
- "desc": "Ranged Weapon Attack: +4 to hit, range 20/60 ft., one target. Hit:\
    \ 16 (4d6 + 2) fire damage."
  "name": "Spit Fire"
- "desc": "The uraeus exhales a 15-foot cone of fire. Each creature in the area must\
    \ make a DC 12 Dexterity saving throw, taking 10 (3d6) fire damage on a failed\
    \ save, or half as much damage on a successful one."
  "name": "Searing Breath (Recharge 5-6)"
"bonus_actions":
- "desc": "The uraeus forms a magical bond with a willing creature within 5 feet of\
    \ it. While bonded, the uraeus and its ward know the distance and direction to\
    \ each other and the general state of each other's health, even if the two are\
    \ on different planes of existence. The bond lasts until the uraeus or its ward\
    \ dies, until the uraeus ends it as a bonus action, or until the uraeus uses this\
    \ bonus action to create a bond with another creature."
  "name": "Ward Bond"
"reactions":
- "desc": "When the uraeus's bonded ward takes damage, the uraeus prevents the ward\
    \ from taking the damage and loses hp equal to that amount instead, regardless\
    \ of the type of damage dealt."
  "name": "Bonded Savior"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/celestial/token/uraeus-tob1-2023.webp"
```
^statblock

## Environment

any, planar