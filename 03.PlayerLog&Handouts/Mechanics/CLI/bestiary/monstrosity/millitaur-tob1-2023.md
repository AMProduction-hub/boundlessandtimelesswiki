---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Millitaur"]
---
# [Millitaur](03 - Player Log & Handouts\Mechanics\CLI\bestiary\monstrosity/millitaur-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 267*  

*A purplish-black segmented worm the size of a horse, with hundreds of legs, black multifaceted eyes, and powerful mandibles wields a pair of stone axes.*

Millitaurs roam jungles and woodlands, especially wherever dense undergrowth rots beneath the canopy and piles high. Leaves and plant matter provide much of the millitaur diet, but they also are good hunters and supplement with squirrel, monkey, gnome, and goblin.

## Poisonous Drool

As formidable as they appear, millitaurs are the preferred prey of some dragons and jungle giants, and tosculi often hunt them for use as slaves and pack animals. In defense, they've developed a mild poison. Millitaur handaxes often drip with this substance, smeared on from the beast's mandibles. They use their axes for breaking up mulch for easier digestion, as well as for hunting and self-defense.

## Alchemists and Brewers

Millitaurs are capable alchemists and brew their own unique beverages, potions, and alchemical substances, using the various materials and substances provided by the plants and animals found in their jungle homes. When away from their burrows, millitaurs carry a handful of flasks for self defense, to ward off intruders, or to trade with respectful humanoids traveling near their territory.

## Clicking Speech

Millitaurs communicate via body language, antennae movements, scent, and clicking sounds. Although they have no voice boxes, millitaurs can make sounds by artfully clicking and grinding their mandibles, and they mimic the sounds of Common in a peculiar popping tone. They can be good sources for local information so long as they are treated with respect and their territory is not encroached.

```statblock
"name": "Millitaur (ToB1-2023)"
"size": "Large"
"type": "monstrosity"
"alignment": "Neutral"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "85"
"hit_dice": "10d10 + 30"
"stats":
- !!int "17"
- !!int "14"
- !!int "16"
- !!int "8"
- !!int "16"
- !!int "10"
"speed": "40 ft., burrow 20 ft., climb 30 ft."
"skillsaves":
  "Acrobatics": !!int "4"
"damage_resistances": "poison, slashing"
"condition_immunities": "[prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)"
"senses": "darkvision 60 ft., tremorsense 30 ft., passive Perception 13"
"languages": "Common, Millitaur"
"cr": "3"
"actions":
- "desc": "The millitaur makes two Handaxe attacks."
  "name": "Multiattack"
- "desc": "Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 20/60\
    \ ft., one target. Hit: 10 (2d6 + 3) slashing damage plus 3 (1d6) poison\
    \ damage."
  "name": "Handaxe"
- "desc": "The millitaur hastily combines alchemical substances into a poisonous concoction\
    \ and throws it at a point the millitaur can see within 30 feet. Each creature\
    \ within 15 feet of that point must make a DC 13 Dexterity saving throw. On a\
    \ failure, a creature takes 14 (4d6) poison damage and is [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 minute. On a success, a creature takes half the damage and isn't [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned).\
    \ A [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ creature can make a DC 13 Constitution saving throw at the end of each of its\
    \ turns, ending the effect on itself on a success."
  "name": "Poisonous Flask (Recharge 5-6)"
- "desc": "The millitaur administers a healing tonic to a willing creature within\
    \ 5 feet of it. The target magically regains 7 2d6 hp and is freed from any\
    \ disease or poison."
  "name": "Healing Tonic (2/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/monstrosity/token/millitaur-tob1-2023.webp"
```
^statblock

## Environment

forest