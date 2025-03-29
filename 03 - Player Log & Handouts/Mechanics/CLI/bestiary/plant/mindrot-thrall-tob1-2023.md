---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/badlands
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/plant
statblock: inline
aliases: ["Mindrot Thrall"]
---
# [Mindrot Thrall](03 - Player Log & Handouts\Mechanics\CLI\bestiary\plant/mindrot-thrall-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 270*  

*A heavily cloaked figure reeks of decay, spreading a floating cloud of spores with every step.*

## Fungal Rot

Mindrot fungus is an intelligent hive-mind parasite that consumes creatures from the inside out. When inhaled, mindrot spores enter the brain through the bloodstream. As the fungus grows, it dissolves the host's body and slowly replaces the creature's flesh with its own. The fungus's first target is the motor function of the brain. It takes control of the creature's movement while the victim is still alive and conscious, leaving the victim trapped within its own body. Indeed, sensory awareness may be the last function that the fungus attacks. Eventually, even the victim's skin and muscle are replaced with fungal fibers. At that point, the affected creature no longer looks like its former self. Such a newly born mindrot thrall conceals its alarming appearance under heavy robes or cloaks so it can travel without causing alarm.

## Spore Blisters

A thrall's skin is taut and waxy. Blisters form just beneath the surface, and when they grow as large as a child's fist they burst, releasing a spray of spores. It seeks to infect as many new victims as possible during the few weeks that it survives in humanoid form. At the end of that time, the thrall shrivels to a dried, vaguely humanoid husk. Even a dead mindrot thrall remains dangerous. Its half-formed spore blisters can remain infectious for months.

## Dimensional Horrors

Wizards hypothesize the fungus was brought to the mortal world's wastelands by a shambling horror crossing through a dimensional portal. The remoteness of the wasteland is likely why the mindrot fungus hasn't destroyed whole cities, though someday it might find a more fertile breeding ground.

```statblock
"name": "Mindrot Thrall (ToB1-2023)"
"size": "Medium"
"type": "plant"
"alignment": "Neutral"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "82"
"hit_dice": "11d8 + 33"
"stats":
- !!int "15"
- !!int "14"
- !!int "17"
- !!int "11"
- !!int "14"
- !!int "6"
"speed": "30 ft."
"saves":
  "Constitution": !!int "5"
"damage_immunities": "acid, poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "tremorsense 30 ft., passive Perception 12"
"languages": "understands Common but can't speak"
"cr": "3"
"traits":
- "desc": "A creature that starts its turn within 5 feet of a mindrot thrall must\
    \ succeed on a DC 13 Constitution saving throw or become infected with the mindrot\
    \ disease."
  "name": "Fungal Aura"
- "desc": "A creature infected with this disease manifests symptoms in 1d4 days\
    \ after infection, which include migraines and muscle weakness. Until the disease\
    \ is cured, at the end of each long rest, the infected creature must succeed on\
    \ a DC 13 Constitution saving throw or take 9 (2d8) acid damage, and its hp\
    \ maximum is reduced by that amount. This reduction lasts until the creature finishes\
    \ a long rest after the disease is cured. The creature dies if the disease reduces\
    \ its hp maximum to 0. One day after the creature dies, it rises as a mindrot\
    \ thrall. A creature that succeeds on two saving throws recovers from the disease."
  "name": "Mindrot"
"actions":
- "desc": "The mindrot thrall makes two Claw attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 9 (2d6\
    \ + 2) slashing damage."
  "name": "Claw"
- "desc": "The thrall exhales a blast of acidic spores from its rotten lungs in a\
    \ 15-foot cone. Each creature in the area must make a DC 13 Dexterity saving throw.\
    \ On a failure, a creature takes 18 (4d8) acid damage and is infected with the\
    \ mindrot disease (see the Mindrot trait). On a success, a creature takes half\
    \ the damage and isn't infected."
  "name": "Spore Breath (Recharge 4-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/plant/token/mindrot-thrall-tob1-2023.webp"
```
^statblock

## Environment

badlands, underdark