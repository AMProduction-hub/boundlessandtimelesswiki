---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/8
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Bone Collective"]
---
# [Bone Collective](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/bone-collective-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 39*  

*Thousands of tiny bones coalesce into a humanoid form, then disperse in a clattering swarm the next moment. The bones rustle as the creature moves, a sound like sand sliding down a dune.*

## Spies and Sneaks

Bone collectives are not primarily fighters, preferring to spy and skulk. However, when cornered, they fight fearlessly, seeking to strip the flesh from their foes. They wear robes or cloaks to pass as humanoid, as they know that most creatures find them disturbing.

## Commanders and Servants of Undeath

Bone collectives' long finger bones and hooked claws help them ascend and control zombie mounts, and their magic allows them to control small groups of undead. This undead affinity occasionally leads them to serve as spies or spymasters for necromancers, darakhul, vampires, or liches.

## Feed on Society

Bone collectives join societies around them, whether human, goblin, or ghoul. They prey on the living and the dead, to replenish lost bones. They produce a reddish venom that drains the luster of life from victims. Those who survive can describe the horrifying red smile of the collective's venom‑coated fangs.

```statblock
"name": "Bone Collective (ToB1-2023)"
"size": "Small"
"type": "undead"
"alignment": "Chaotic Evil"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "120"
"hit_dice": "16d6 + 64"
"stats":
- !!int "10"
- !!int "20"
- !!int "18"
- !!int "14"
- !!int "10"
- !!int "16"
"speed": "30 ft."
"saves":
  "Dexterity": !!int "8"
"skillsaves":
  "Deception": !!int "6"
  "Stealth": !!int "11"
  "Perception": !!int "3"
  "Arcana": !!int "5"
"damage_resistances": "bludgeoning, piercing, slashing"
"damage_immunities": "necrotic, poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
  \ [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
  \ [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)"
"senses": "darkvision 120 ft., passive Perception 13"
"languages": "Common, Darakhul (can't speak in shapeless form)"
"cr": "8"
"traits":
- "desc": "The bone collective casts the [animate dead](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/animate-dead.md)\
    \ spell as an action, requiring no material components and using Charisma as the\
    \ spellcasting ability (spell save DC 14).\n\n3/day each: [animate dead](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/animate-dead.md)"
  "name": "Spellcasting (3/Day; Humanoid Form Only)"
- "desc": "The collective's individual bones are connected via a hive mind. It can\
    \ telepathically communicate with any of its individual bones within 50 miles\
    \ of it, and it can't be surprised. If the collective is reduced to half its hp\
    \ or fewer, its Intelligence score is reduced to 1, it can't cast spells, it immediately\
    \ changes to its shapeless form, and it can't take on a Humanoid form."
  "name": "Collective Mind"
- "desc": "The bone collective can wield weapons and hold, grasp, push, pull, or interact\
    \ with objects that might otherwise require a Humanoid form to accomplish."
  "name": "Grasping Limbs (Humanoid Form Only)"
- "desc": "The bone collective can occupy another creature's space and vice versa,\
    \ and the swarm can move through any opening large enough for a Tiny bone."
  "name": "Swarm (Shapeless Form Only)"
- "desc": "The bone collective doesn't require air, food, drink, or sleep."
  "name": "Undead Nature"
- "desc": "When the bone collective hits a [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ creature with a Bite or Piercing Bones attack, the target's Charisma score is\
    \ reduced by 1d4. The target is [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ if this reduces its Charisma to 0. The reduction lasts until the target finishes\
    \ a long rest."
  "name": "Wyrmblood Venom"
"actions":
- "desc": "The bone collective makes two Claw attacks, or one Claw attack and one\
    \ Bite attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 31\
    \ (4d12 + 5) piercing damage, and the target must succeed on a DC 16 Constitution\
    \ saving throw or become [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 minute. The target can repeat the saving throw at the end of each of its\
    \ turns, ending the effect on itself on a success."
  "name": "Bite (Humanoid Form Only)"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 25\
    \ (3d12 + 5) slashing damage."
  "name": "Claw (Humanoid Form Only)"
- "desc": "Melee Weapon Attack: +8 to hit, reach 0 ft., one creature in the collective's\
    \ space. Hit: 52 (8d12) piercing damage, or 26 (4d12) piercing damage if\
    \ the collective has half its hp or fewer."
  "name": "Piercing Bones (Shapeless Form Only)"
"bonus_actions":
- "desc": "The bone collective can shape itself into a Small Humanoid or back into\
    \ a shapeless form of Tiny bones. Its statistics are the same in each form, and\
    \ it can't regain hp or gain temporary hp. It can't take on a Humanoid form if\
    \ it is occupying the space of another creature."
  "name": "Shape Swarm"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/bone-collective-tob1-2023.webp"
```
^statblock

## Environment

urban