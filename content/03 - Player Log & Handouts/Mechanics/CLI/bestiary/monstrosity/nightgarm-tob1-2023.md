---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/arctic
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Nightgarm"]
---
# [Nightgarm](03 - Player Log & Handouts\Mechanics\CLI\bestiary\monstrosity/nightgarm-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 285*  

*This red-furred lupine creature has a too-wide mouth and blood-soaked claws.*

Created in a ritual performed over a pregnant worg, nightgarms are always born female and are followers of the Great Wolf.

## Wide-Jawed Lupines

Nightgarms resemble red-furred worgs with wide mouths, half-formed fingers, and comfort with bipedal and quadrupedal movement. They can hold items in their front paws, and their jaws can open to swallow especially large creatures.

## Mother of Falsehearts

If a nightgarm eats a humanoid corpse whole, it gives birth nine hours later to a duplicate of the victim, known as a falseheart (see the Falseheart Template sidebar). Falsehearts are loyal to the nightgarm that birthed them and retain enough of the victim's memories and capabilities to integrate into society as the victim.

> [!note] Falseheart Template
> 
> The corpse of any Humanoid can become a falseheart if eaten whole by a nightgarm. When a Humanoid becomes a falseheart, it retains its statistics, except as described below.
> 
> **Type.** The Humanoid's type changes to Monstrosity
> 
> **Alignment.** The falseheart's alignment changes to chaotic evil.
> 
> **New Trait Convincing Copy.** A creature very familiar with the Humanoid the falseheart replaced can tell the falseheart is an imitation with a successful DC 20 Wisdom ([Insight](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Insight)) check.
> 
> **New Trait Keen Smell.** The falseheart has advantage on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception)) checks that rely on smell.
> 
> **New Trait Mother's Love.** The falseheart is magically bound to the nightgarm that birthed it, following the nightgarm's telepathic commands.
^falseheart-template

```statblock
"name": "Nightgarm (ToB1-2023)"
"size": "Large"
"type": "monstrosity"
"alignment": "Chaotic Evil"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "152"
"hit_dice": "16d10 + 64"
"stats":
- !!int "20"
- !!int "14"
- !!int "18"
- !!int "10"
- !!int "15"
- !!int "16"
"speed": "40 ft."
"skillsaves":
  "Stealth": !!int "5"
  "Perception": !!int "5"
"damage_vulnerabilities": "radiant; bludgeoning, piercing, slashing by silvered weapons"
"damage_resistances": "lightning, thunder"
"senses": "darkvision 60 ft., passive Perception 15"
"languages": "Common, Giant, Goblin, telepathy 60 ft."
"cr": "6"
"traits":
- "desc": "The nightgarm ignores the range restriction on its telepathy when communicating\
    \ with a falseheart it has birthed. The nightgarm and its falseheart don't need\
    \ to be on the same plane of existence."
  "name": "Telepathic Bond"
"actions":
- "desc": "The nightgarm makes one Bite attack and two Claw attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 16\
    \ (2d10 + 5) piercing damage. If the target is a Medium or smaller creature,\
    \ it must succeed on a DC 15 Strength saving throw or be swallowed. A swallowed\
    \ creature is [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ and [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ it has total cover against attacks and other effects outside the nightgarm,\
    \ and it takes 10 (3d6) acid damage at the start of each of the nightgarm's\
    \ turns. The nightgarm can have only one creature swallowed at a time. If the\
    \ nightgarm takes 20 damage or more on a single turn from the swallowed creature,\
    \ the nightgarm must succeed on a DC 14 Constitution saving throw at the end of\
    \ that turn or regurgitate the creature, which falls [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)\
    \ in a space within 5 feet of the nightgarm. If the nightgarm dies, a swallowed\
    \ creature is no longer [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ by her and can escape from the corpse by using 10 feet of movement, exiting\
    \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 12\
    \ (2d6 + 5) slashing damage."
  "name": "Claw"
- "desc": "The nightgarm magically calls 2d4 wolves or 2 dire wolves. The wolves\
    \ arrive in 1d4 rounds, acting as allies of the nightgarm and obeying her telepathic\
    \ commands. The wolves remain for 1 hour, until the nightgarm dies, or until the\
    \ nightgarm dismisses them as a bonus action."
  "name": "Lupine Howl (1/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/monstrosity/token/nightgarm-tob1-2023.webp"
```
^statblock

## Environment

arctic, forest