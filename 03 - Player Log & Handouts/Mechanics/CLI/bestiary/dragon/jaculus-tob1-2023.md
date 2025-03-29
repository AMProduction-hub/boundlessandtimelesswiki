---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/dragon
statblock: inline
aliases: ["Jaculus"]
---
# [Jaculus](03 - Player Log & Handouts\Mechanics\CLI\bestiary\dragon/jaculus-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 241*  

*This small dragon has feathered wings on its forearms and clings with powerful claws to a tree.*

The jaculus (plural jaculi) is a draconic predator similar to a small wyvern that roams the forest and jungle looking for valuable objects it can add to its hoard. Also called the javelin snake, a jaculus loves shiny or reflective items, and it is clever enough to identify items of real value. It will fight and kill to take items it desires, which it stashes inside hollow trees far from any forest trail.

## Leapers

Jaculi are far better jumpers than flyers. They climb faster than they fly, and they use their wings to flap clumsily back into the trees only when necessary.

## Teamwork Thievery

Jaculi are among the least intelligent of the dragons, but they're still smarter than most humans. They're known to pursue cunning and complicated plots to build their hoards. Many traditional tales tell of jaculi in the southern forests working as teams to separate merchants and other travelers from their wealth, figuring out ways to abscond with gems and jewelry before the owners even know they've been robbed. Some jaculi may feign docility or even pretend to be friendly and helpful, but wise travelers know that the creatures drop such ruses as soon as they can steal what they're seeking.

```statblock
"name": "Jaculus (ToB1-2023)"
"size": "Small"
"type": "dragon"
"alignment": "Neutral Evil"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "65"
"hit_dice": "10d6 + 30"
"stats":
- !!int "14"
- !!int "18"
- !!int "17"
- !!int "13"
- !!int "13"
- !!int "13"
"speed": "20 ft., climb 20 ft., fly 10 ft."
"saves":
  "Charisma": !!int "3"
  "Dexterity": !!int "6"
"skillsaves":
  "Stealth": !!int "6"
  "Perception": !!int "3"
  "Acrobatics": !!int "6"
"damage_resistances": "acid, lightning"
"senses": "blindsight 10 ft., darkvision 60 ft., passive Perception 13"
"languages": "Common, Draconic"
"cr": "3"
"traits":
- "desc": "If the jaculus moves at least 10 feet straight toward a target and then\
    \ hits it with a Bite attack on the same turn, the target takes an extra 4 (1d8)\
    \ piercing damage. If the target is a creature, it must succeed on a DC 13 Strength\
    \ saving throw or be knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Spearhead"
- "desc": "The jaculus's long jump is up to 20 feet and its high jump is up to 10\
    \ feet, with or without a running start."
  "name": "Standing Leap"
"actions":
- "desc": "The jaculus makes one Bite attack and two Claw attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d8\
    \ + 4) piercing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7 (1d6\
    \ + 4) slashing damage."
  "name": "Claws"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/dragon/token/jaculus-tob1-2023.webp"
```
^statblock

## Environment

forest