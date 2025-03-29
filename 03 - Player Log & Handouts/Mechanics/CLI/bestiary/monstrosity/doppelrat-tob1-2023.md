---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Doppelrat"]
---
# [Doppelrat](03 - Player Log & Handouts\Mechanics\CLI\bestiary\monstrosity/doppelrat-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 109*  

*Within seconds, the startled rat became four, and then the four multiplied into sixteen rats.*

The result of a clone spell gone awry, a doppelrat uses short-lived duplicates to overwhelm its adversaries. An easy battle against a single rat can quickly spiral out of control as the doppelrat clones itself into a swarm—the original rat hides while combat rages. Doppelrats settle in large city alleys and sewers after they have killed or driven off normal rats and natural predators. Doppelrats can sense others of their kind among standard rats, which helps ensure the longevity of their species.

## Stillborn Clones

Those who survive a doppelrat's bite suffer from a frightening disease, sloughing off a stillborn clone each day as their own vitality fades.

## Clone and Run

In combat, doppelrats spawn as many clones as they can, then flee or hide while the copied rats swarm foes. Only a keen-eyed opponent can discern the original from all the clones.

## City Bounties

In cities with known doppelrat lairs, magistrates hire spellcasters to scour alleys and sewers and obliterate any rats they find. Shady spellcasters who capture a live doppelrat have blackmailed such magistrates by promising to rescue the town from the rats for an exorbitant fee.

```statblock
"name": "Doppelrat (ToB1-2023)"
"size": "Tiny"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "13"
"hp": !!int "45"
"hit_dice": "10d4 + 20"
"stats":
- !!int "2"
- !!int "17"
- !!int "14"
- !!int "2"
- !!int "13"
- !!int "2"
"speed": "30 ft., climb 15 ft., swim 15 ft."
"saves":
  "Dexterity": !!int "5"
"skillsaves":
  "Stealth": !!int "5"
"senses": "darkvision 60 ft., passive Perception 11"
"languages": ""
"cr": "2"
"traits":
- "desc": "While in combat, at the start of each of its turns, the doppelrat rapidly\
    \ creates duplicates of itself as an automatic defense mechanism. These duplicates\
    \ immediately form into a swarm of rats in the doppelrat's space, acting as allies\
    \ of the doppelrat and obeying its body language commands. The swarm acts on the\
    \ doppelrat's turn, and the doppelrat can use its reaction to move up to its speed\
    \ with the swarm, provided it is in the swarm's space when the swarm moves. The\
    \ swarm remains for 1 minute, until the doppelrat dies, or until the doppelrat\
    \ dismisses it as a bonus action. The doppelrat can have no more than two swarms\
    \ of rats under its control at a time."
  "name": "Arcane Doubling"
- "desc": "While the doppelrat is in the space of a swarm it created with Arcane Doubling,\
    \ it is indiscernible from the other rats and has total cover. A creature must\
    \ take an action to visually inspect the swarm and succeed on a DC 15 Intelligence\
    \ ([Investigation](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Investigation))\
    \ check to find the doppelrat among its duplicates. Once a creature succeeds on\
    \ this check, the doppelrat loses total cover against attacks and spells from\
    \ that creature and that creature's allies until the doppelrat starts its turn\
    \ in the same space as one of its swarms."
  "name": "Hidden Original"
- "desc": "Characterized by the growing and sloughing off of tumors shaped like the\
    \ infected creature, horrific doppeling is a disease that infects creatures attacked\
    \ by doppelrats. Until the disease is cured, the creature is [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned).\
    \ At the end of each long rest, the infected creature must succeed on a DC 13\
    \ Constitution saving throw or shed a tumor that looks like a Tiny version of\
    \ itself. Though disturbing, the tumor is merely a mass of shed skin and fat that\
    \ decays as normal. The disease is cured after the creature succeeds on two saving\
    \ throws."
  "name": "Horrific Doppeling"
- "desc": "The doppelrat has advantage on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on smell."
  "name": "Keen Smell"
"actions":
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4\
    \ + 3) piercing damage, and the target must succeed on a DC 13 Constitution saving\
    \ throw or contract the horrific doppeling disease (see the Horrific Doppeling\
    \ trait)."
  "name": "Bite"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/monstrosity/token/doppelrat-tob1-2023.webp"
```
^statblock

## Environment

urban