---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/environment/swamp
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/aberration
statblock: inline
aliases: ["Bagiennik"]
---
# [Bagiennik](03 - Player Log & Handouts\Mechanics\CLI\bestiary\aberration/bagiennik-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 31*  

*With webbed claws, bulbous eyes, and two nostril-slits that ooze an oily black substance, the creature is not quite hideous—but it might be, if most of it wasn't concealed by a thick coating of muck and mud.*

## Bathing Uglies

When a bagiennik is alone, it spends its time bathing in local springs, rivers, and marshes. The creature sifts through the muck and silt, extracting substances that enhance its oily secretions. If anything disturbs the creature during its languorous bathing sessions, it angrily retaliates. Once a bagiennik has bathed for four hours, it seeks a target for mischief or charity.

## Unpredictable Moods

One never knows what to expect with a bagiennik. The same creature might aid an injured traveler one day, smear that person with corrosive, acidic oil the next day, and then extend tender care to the burned victim of its own psychotic behavior. If the creature feels beneficent, it heals injured animals or even diseased or injured villagers. If a bagiennik visits a settlement, the ill and infirm approach it cautiously while everyone else hides to avoid provoking its wrath. When a bagiennik leaves its bath in an angry mood, it raves and seeks out animals or humanoids to coat with its acidic oil. If a victim falls, the foul‑tempered bagiennik often applies healing oil to stabilize them, grumbling all the while.

## Acid Oils

Collecting a dead bagiennik's black oils must be done within an hour of the creature's death. A successful DC 15 Wisdom ([Medicine](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Medicine)) check yields one vial of acid, or two vials if the result was 20 or higher. A bagiennik can use these chemicals either to heal or to harm, but no alchemist or healer has figured out how to reproduce the healing effects. Other than their acidic effect, the secretions lose all potency within moments of being removed from a bagiennik.

```statblock
"name": "Bagiennik (ToB1-2023)"
"size": "Medium"
"type": "aberration"
"alignment": "Chaotic Neutral"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "75"
"hit_dice": "10d8 + 30"
"stats":
- !!int "16"
- !!int "18"
- !!int "16"
- !!int "9"
- !!int "16"
- !!int "11"
"speed": "30 ft., swim 40 ft."
"skillsaves":
  "Perception": !!int "5"
"senses": "darkvision 60 ft., passive Perception 15"
"languages": "Common"
"cr": "3"
"actions":
- "desc": "The bagiennik makes two Claw attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 13\
    \ (2d8 + 4) slashing damage."
  "name": "Claw"
- "desc": "The bagiennik sprays acid on one creature it can see within 30 feet of\
    \ it, creating a puddle of oil beneath the creature. The target must make a DC\
    \ 13 Dexterity saving throw. On a failure, the creature takes 18 (4d8) acid\
    \ damage and is knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone).\
    \ On a success, the creature takes half the damage and isn't knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone).\
    \ The slippery oil covers the ground in a 5-foot square centered on the point\
    \ where the target was standing for 1 minute. A creature that enters the oily\
    \ area or ends its turn there must succeed on a DC 13 Dexterity saving throw or\
    \ fall [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Acid Spray"
- "desc": "The bagiennik applies healing oil to a creature it can see within 5 feet\
    \ of it. The target magically regains 7 2d6 hp and is freed from any disease\
    \ or poison. The target must then succeed on a DC 13 Constitution saving throw\
    \ or its speed is halved and it takes a -2 penalty to AC and Dexterity saving\
    \ throws for 1 minute."
  "name": "Healing Oil (3/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/aberration/token/bagiennik-tob1-2023.webp"
```
^statblock

## Environment

forest, hill, swamp