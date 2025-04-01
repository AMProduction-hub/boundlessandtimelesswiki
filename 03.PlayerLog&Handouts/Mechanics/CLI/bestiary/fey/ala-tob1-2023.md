---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/8
- ttrpg-cli/monster/environment/farmland
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Ala"]
---
# [Ala](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/ala-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 13*  

*Alas are born from galls that grow on treant trunks. Within this parasitic pocket, an ala sickens the treant and consumes its life force. When the treant dies, the ala is born in a black whirlwind*.

## Daughters of the Whirlwind

Alas have windblown hair and wear smoky black rags, but their true form is that of a whirlwind, which can always be seen by šestaci, those men and women with six digits on each hand. In flight or in battle, an ala takes on a form with the upper body of a hag and a whirling vortex of air in place of hips and legs. When an ala enters a house in human form, the whole building groans in protest, as if it had been struck by a powerful storm wind. Alas live in the hollows of trees that were struck by lightning. They are most active when thunder rocks the forest, and when they travel, hail or thunderstorms spawn around them.

## Enormous Appetites

The huge-mouthed alas have voracious appetites. In the wild, they devour wolves, bears, and badgers. They prefer to hunt in settled areas, however, because they favor the taste of innocents above all else. Unsavory humanoids may beg an ala's favor (or divert its wrath) with gifts of bound captives.

## Energized by Storms

In battle, an ala is constantly on the move, weaving between foes like the wind. It tears at its foes with claws and a poisonous bite, or throws wicked lightning bolts and hailstorms from afar. Woe betides the hero who confronts an ala while a storm rages overhead—such storms energize the ala and make its lightning stronger. Because alas wield lightning with such mastery, some sages associate them with the god of lightning.

```statblock
"name": "Ala (ToB1-2023)"
"size": "Medium"
"type": "fey"
"alignment": "Chaotic Evil"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "127"
"hit_dice": "15d8 + 60"
"stats":
- !!int "20"
- !!int "16"
- !!int "18"
- !!int "10"
- !!int "16"
- !!int "8"
"speed": "30 ft., fly 40 ft."
"skillsaves":
  "Athletics": !!int "8"
  "Stealth": !!int "6"
  "Perception": !!int "9"
"damage_immunities": "lightning, poison, thunder"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 19"
"languages": "Common, Draconic"
"cr": "8"
"traits":
- "desc": "The ala doesn't provoke an opportunity attack when it flies out of an enemy's\
    \ reach."
  "name": "Flyby"
- "desc": "The ala's poison infuses its flesh. A creature that touches the ala or\
    \ hits it with a melee attack while within 5 feet of it takes 7 (2d6) poison\
    \ damage."
  "name": "Poisonous Flesh"
- "desc": "If the ala is outside and an electrical storm is within 1 mile of it, creatures\
    \ have disadvantage on their saving throws against the ala's Lightning's Kiss."
  "name": "Storm's Strength"
"actions":
- "desc": "The ala makes one Bite attack and two Claw attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 9 (1d8\
    \ + 5) piercing damage plus 7 (2d6) poison damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 8 (1d6\
    \ + 5) slashing damage plus 7 (2d6) poison damage."
  "name": "Claw"
- "desc": "The ala launches a bolt of lightning at up to three targets it can see\
    \ within 30 feet of it. Each target must make a DC 16 Dexterity saving throw,\
    \ taking 28 (8d6) lightning damage on a failed save, or half as much damage\
    \ on a successful one."
  "name": "Lightning's Kiss (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/ala-tob1-2023.webp"
```
^statblock

## Environment

farmland, forest