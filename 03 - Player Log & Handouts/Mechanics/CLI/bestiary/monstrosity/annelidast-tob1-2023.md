---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/12
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/environment/mountain
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Annelidast"]
---
# [Annelidast](03 - Player Log & Handouts\Mechanics\CLI\bestiary\monstrosity/annelidast-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 21*  

*The massive worm erupted from the earth, crushing all near it and scooping up the remains.*

An annelidast is a gigantic worm that slumbers for decades at a time in the bowels of the earth, where the rock itself radiates primordial magic. Over millennia, they have grown lead-plated carapaces to shield themselves from the magic.

## Unique Predation

Each century, an annelidast wakes and travels to the surface to feed. The worm eats through baleen-like teeth that help it filter feed through the earth as it travels underground, but this method of eating requires it to pulverize larger surface prey before consumption.

## Sleeping Plague

The annelidast's exterior is saturated with the primordial magic of its deep-earth home. When an annelidast nears waking, it burrows toward the surface in a dreamlike state, following vibrations in the earth made by living creatures. As it lies just beneath the surface rousing from its slumber, the primordial magic infusing it radiates outward and sickens creatures living there, making them easier prey when it fully wakes.

```statblock
"name": "Annelidast (ToB1-2023)"
"size": "Huge"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "18"
"ac_class": "natural armor"
"hp": !!int "184"
"hit_dice": "16d12 + 80"
"stats":
- !!int "26"
- !!int "10"
- !!int "20"
- !!int "1"
- !!int "10"
- !!int "4"
"speed": "40 ft., burrow 30 ft."
"saves":
  "Wisdom": !!int "4"
  "Constitution": !!int "9"
"damage_resistances": "lightning"
"damage_immunities": "bludgeoning, poison from nonmagical attacks"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "tremorsense 120 ft., passive Perception 10"
"languages": ""
"cr": "12"
"traits":
- "desc": "The annelidast doesn't require air."
  "name": "Deep Earth Dweller"
- "desc": "A creature that starts its turn within 30 feet of the annelidast must succeed\
    \ on a DC 17 Constitution saving throw or take 7 (2d6) poison damage. A creature\
    \ that finishes a long rest within 1,000 feet of the annelidast must succeed on\
    \ a DC 17 Constitution saving throw or develop tumors across its body and become\
    \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ until the tumors are removed by the [greater restoration](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/greater-restoration.md)\
    \ spell or similar magic."
  "name": "Primordial Aura"
- "desc": "The annelidast can burrow through solid rock at half its burrow speed and\
    \ leaves a 10-foot-diameter tunnel in its wake."
  "name": "Tunneler"
"actions":
- "desc": "The annelidast makes three Slam attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 21\
    \ (2d12 + 8) bludgeoning damage, and if the target is a creature, it must succeed\
    \ on a DC 17 Strength saving throw or be pushed up to 15 feet away from the annelidast.\
    \ A creature [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ by the annelidast automatically succeeds on this saving throw."
  "name": "Slam"
- "desc": "The annelidast launches most of its massive bulk into the air and crashes\
    \ down on the ground in a 20-foot line that is 10 feet wide. It then retracts\
    \ itself into a space along that line and can occupy the space of one or more\
    \ Large or smaller creatures. Each creature in the line must make a DC 17 Dexterity\
    \ saving throw. On a failure, a creature takes 45 (7d12) bludgeoning damage,\
    \ is knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
    \ and is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ while it shares a space with the annelidast, as it is pinned beneath the annelidast's\
    \ body. On a success, a creature takes half the damage, isn't knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
    \ and is pushed out of the annelidast's space into an unoccupied space of the\
    \ creature's choice within 5 feet of the annelidast. A creature, including the\
    \ [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ creature, can take its action to free the [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ creature by succeeding on a DC 17 Strength check. If the annelidast burrows\
    \ along the surface of the earth at least 20 feet before using this action, creatures\
    \ in the line have disadvantage on the saving throw."
  "name": "Crush (Recharge 5-6)"
"reactions":
- "desc": "When the annelidast takes damage, it can make one Slam attack against a\
    \ creature [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ by it."
  "name": "Defensive Recoil"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/monstrosity/token/annelidast-tob1-2023.webp"
```
^statblock

## Environment

desert, forest, grassland, hill, mountain, underdark, urban