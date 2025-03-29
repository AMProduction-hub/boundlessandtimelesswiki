---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/plant
statblock: inline
aliases: ["Deathcap Myconid"]
---
# [Deathcap Myconid](03 - Player Log & Handouts\Mechanics\CLI\bestiary\plant/deathcap-myconid-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 280*  

*This fungal creature's head extends up and out in an orange and red cap with white spots. A vicious-looking fanged maw dominates its face.*

## Mushroom Farmers

These sentient mushroom folk tend the forests of fungi in the underworld and are allies of the darakhul. Despite their ominous name, deathcap myconids are chiefly farmers. They cultivate dozens of species of mushrooms anywhere they have water, dung, and a bit of earth or slime in the underworld deeps. For this reason, other races rarely attack them. The ghouls do not eat them, and they cannot be made into darakhul.

## Toxic Spores

Although deathcaps are mostly peaceful, their spores are toxic and sleep-inducing. They make excellent allies in combat because their abilities tend to punish attackers, but they aren't especially lethal on their own. They use their poison and slumber spores to full effect against living creatures and typically flee from constructs and undead. They count on their allies to fend off the most powerful foes.

## Clones

Deathcap myconids live in communal groups of related clones. They reproduce asexually, and an elder and its offspring can be nearly identical in all but age. These clone groups are called deathcap rings. Myconids build no huts or towns, but their groups are defined by their crops and general appearance. Indeed, many sages claim that the deathcaps are merely the fruiting, mobile bodies of the forests they tend, which is why they fight so ferociously to defend their forests of giant fungi.

```statblock
"name": "Deathcap Myconid (ToB1-2023)"
"size": "Medium"
"type": "plant"
"alignment": "Neutral Evil"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "90"
"hit_dice": "12d8 + 36"
"stats":
- !!int "14"
- !!int "10"
- !!int "16"
- !!int "10"
- !!int "11"
- !!int "9"
"speed": "20 ft."
"senses": "darkvision 60 ft., passive Perception 10"
"languages": ""
"cr": "4"
"traits":
- "desc": "The deathcap takes 10 radiant damage when it starts its turn in sunlight.\
    \ While in sunlight, it has disadvantage on attack rolls and ability checks."
  "name": "Sunlight Hypersensitivity"
"actions":
- "desc": "The myconid can use its Eject Spores. It then makes two Spore-Coated Fist\
    \ attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6\
    \ + 2) bludgeoning damage plus 10 (3d6) poison damage."
  "name": "Spore-Coated Fist"
- "desc": "The myconid ejects one of the following types of spores at one creature\
    \ it can see within 15 feet of it.\n\n- Deathcap Spores. The target must succeed\
    \ on a DC 13 Constitution saving throw or be [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 minute. It can repeat the saving throw at the end of each of its turns,\
    \ ending the effect on itself on a success.  \n- Slumber Spores. The target\
    \ must succeed on a DC 13 Constitution saving throw or fall [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)\
    \ for 1 minute. The target wakes up if it takes damage or if another creature\
    \ takes an action to shake it awake.  "
  "name": "Eject Spores"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/plant/token/deathcap-myconid-tob1-2023.webp"
```
^statblock

## Environment

underdark