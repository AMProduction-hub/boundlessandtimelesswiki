---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Behtu"]
---
# [Behtu](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/behtu-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 34*  

*With the face of a mandrill and the tusks of a great boar, these ferocious half-ape, half-human pygmies have demon blood flowing in their veins. Only the desperate or the suicidal travel to their volcanic temple-islands.*

Once a peaceful people, the behtu have since been corrupted by Mechuiti, the demon lord of apes, cannibalism, and torture. By feeding his blood to the behtu, he filled them with the cruelty and power of a demon, transforming them into the creatures they are today. The behtu carry his worship from island to island, subjugating, devouring, or converting all they meet.

## Temple Builders

The behtus raise shrines to Mechuiti wherever they go. Some are kept and prosper, while others fall into decay and return to the jungle.

## Ichor Drinkers

In his volcanic temples, Mechuiti's idols weep his ichorous demon blood. Behtus use the ichor to create infusions that give them inhuman strength and speed, and their leaders use it to perform a ritual that transforms simians and humans bathed in the ichor into more behtu. Behtus also etch demonic tattoos using the ichor, granting them infernal powers and protection.

## Scaly Mounts

Behtus breed demonic iguanas as war mounts (use the statistics of a giant lizard). The most powerful behtu sorcerers and druids have been known to ride large crimson drakes and small flame dragons as personal mounts.

```statblock
"name": "Behtu (ToB1-2023)"
"size": "Small"
"type": "humanoid"
"alignment": "Chaotic Evil"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "52"
"hit_dice": "8d6 + 24"
"stats":
- !!int "17"
- !!int "16"
- !!int "16"
- !!int "12"
- !!int "11"
- !!int "7"
"speed": "20 ft., climb 20 ft."
"saves":
  "Dexterity": !!int "5"
"skillsaves":
  "Athletics": !!int "5"
  "Stealth": !!int "5"
"damage_resistances": "cold, fire, lightning"
"senses": "darkvision 60 ft., passive Perception 10"
"languages": "Behtu, Common, Infernal"
"cr": "2"
"actions":
- "desc": "The behtu makes one Bite attack and one Spear attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6\
    \ + 3) piercing damage."
  "name": "Bite"
- "desc": "Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 20/60\
    \ ft., one target. Hit: 6 (1d6 + 3) piercing damage, or 7 (1d8 + 3) piercing\
    \ damage if used with two hands to make a melee attack."
  "name": "Spear"
- "desc": "The behtu exhales fire in a 15-foot cone. Each creature in that area must\
    \ make a DC 13 Dexterity saving throw, taking 21 (6d6) fire damage on a failed\
    \ save, or half as much damage on a successful one."
  "name": "Fire Breath (Recharge 6)"
- "desc": "The behtu ingests an infusion made from Mechuiti's blood. For 1 minute,\
    \ the behtu has advantage on saving throws and ability checks that use Strength\
    \ and Constitution, and its walking and climbing speeds are doubled. In addition,\
    \ it has disadvantage on saving throws and ability checks that use Intelligence\
    \ and Wisdom for the duration. A non-behtu that ingests the infusion must make\
    \ a DC 14 Constitution saving throw. On a failure, the creature takes 10 (3d6)\
    \ poison damage and is [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 minute. On a success, the creature takes half the damage and isn't [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned).\
    \ The behtu typically has 1d4 + 1 infusions in its possession."
  "name": "Ichorous Infusion"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/behtu-tob1-2023.webp"
```
^statblock

## Environment

forest