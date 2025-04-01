---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/fiend/demon
statblock: inline
aliases: ["Apau Perape Demon"]
---
# [Apau Perape Demon](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fiend/apau-perape-demon-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 82*  

*Sharp teeth fill this large, demonic ape's mouth. Its long, muscular arms stretch to the ground, ending in wickedly curved claws.*

## Servants of Fire

These black-furred gorilla demons serve only Mechuiti, the demon lord of fire and apes. Their final loyalty is unshakable, though sometimes they serve others for a time. They have no fear of fire, gleefully setting villages and crops aflame if their master is snubbed or insulted.

## Fearless Attackers

The apau perape are fearless and savage, living for battle. Once in combat, their morale never breaks. Like their master, they have an insatiable hunger and leave no dead behind, consuming even the bones.

## Eyes of Fire

When this demon is angered, its eyes glow a deep, disturbing red, unlike any natural ape.

```statblock
"name": "Apau Perape Demon (ToB1-2023)"
"size": "Large"
"type": "fiend"
"subtype": "demon"
"alignment": "Chaotic Evil"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "95"
"hit_dice": "10d10 + 40"
"stats":
- !!int "21"
- !!int "18"
- !!int "19"
- !!int "10"
- !!int "12"
- !!int "15"
"speed": "30 ft., climb 30 ft."
"saves":
  "Dexterity": !!int "7"
  "Wisdom": !!int "4"
  "Constitution": !!int "7"
"skillsaves":
  "Intimidation": !!int "5"
  "Stealth": !!int "7"
  "Perception": !!int "4"
"damage_vulnerabilities": "cold"
"damage_resistances": "fire; lightning; bludgeoning, piercing, slashing from nonmagical\
  \ attacks"
"damage_immunities": "poison"
"condition_immunities": "[frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 120 ft., passive Perception 14"
"languages": "Abyssal, telepathy 120 ft."
"cr": "6"
"traits":
- "desc": "When the apau perape takes piercing damage or slashing damage, a spray\
    \ of caustic blood spurts from the wound. Each creature within 5 feet of the apau\
    \ perape must succeed on a DC 15 Constitution saving throw or become infected\
    \ with the Mechuiti's ichor disease and be [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ until the disease is cured. Every 24 hours that elapse, the target must repeat\
    \ the saving throw, reducing its hp maximum by 5 (2d4) on a failure. The disease\
    \ is cured on a success. This reduction lasts until the disease is cured. The\
    \ creature dies if the disease reduces its hp maximum to 0."
  "name": "Diseased Ichor"
- "desc": "The apau perape has advantage on saving throws against spells and other\
    \ magical effects."
  "name": "Magic Resistance"
"actions":
- "desc": "The apau perape makes one Bite attack and two Claw attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 12\
    \ (2d6 + 5) piercing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 14\
    \ (2d8 + 5) slashing damage."
  "name": "Claw"
- "desc": "The apau perape releases a terrifying, flame-coated roar in a 30-foot cone.\
    \ Each creature in that area must make a DC 15 Dexterity saving throw. On a failure,\
    \ a creature takes 31 (9d6) fire damage and is [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ until the end of its next turn. On a success, a creature takes half the damage\
    \ and isn't [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)."
  "name": "Fiery Roar (Recharge 6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fiend/token/apau-perape-demon-tob1-2023.webp"
```
^statblock

## Environment

forest, planar