---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/plant
statblock: inline
aliases: ["Mi-go"]
---
# [Mi-go](03 - Player Log & Handouts\Mechanics\CLI\bestiary\plant/mi-go-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 266*  

*This fungal, insectoid creature has stubby wings, multiple limbs, and a nightmarish head.*

The mi-go are a space-faring people of great skill and vast malevolence. They travel in large numbers between worlds, somehow covering astronomical distances in months rather than decades.

## Strange Technology

Their technology includes powerful techniques to implant mi-go elements and minds in others' bodies (or to extract them). They also have unparalleled mastery of living tissue in both plant and animal form. Mi-go merchants exchange psychic tools, surgical instruments, and engineered materials. They work these materials into fantastic objects such as void-crossing solar wings, glowing lampfruit, and purple starvines, which induce sleep.

## World Colonizers

While they have their own secrets and goals, the mi-go also serve ancient powers from between the stars. They are devoted followers of Shub-Niggurath, goddess of fecundity and growth, and take their evangelical mission seriously. They colonize entire worlds in Shub-Niggurath's name, planting and harvesting entire species according to her will.

## Brain Cylinders

The brain cylinder, a device that permits the extraction and maintenance of a living brain outside the body, is the apex of mi-go technology. Safely isolated in a mi-go cylinder, a humanoid brain can travel safely between the stars. They deploy, fill, and retrieve these cylinders according to mysterious schedules and for purposes. Indeed, most of their technology appears either revolting or simply bizarre to humanoids (plant folk are less disquieted by their functioning).

> [!note] Disquieting Technology
> 
> Though mi-go technology is strange to most creatures, the effects of the technology in the game are similar to magic items. For example, a device strapped to the chest emitting a blue field around the wearer's body that grants resistance to cold damage is functionally the same as armor of cold resistance. The identify spell fails to discern the true purpose of these pieces of technology, but a successful DC 17 Intelligence ([Arcana](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Arcana)) check during a short or long rest can reveal the purpose of a piece of mi-go technology
^disquieting-technology

```statblock
"name": "Mi-go (ToB1-2023)"
"size": "Medium"
"type": "plant"
"alignment": "Neutral Evil"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "95"
"hit_dice": "10d8 + 50"
"stats":
- !!int "16"
- !!int "19"
- !!int "21"
- !!int "25"
- !!int "15"
- !!int "13"
"speed": "30 ft., fly 60 ft."
"saves":
  "Charisma": !!int "4"
  "Strength": !!int "6"
  "Constitution": !!int "8"
"skillsaves":
  "Medicine": !!int "5"
  "Deception": !!int "7"
  "Stealth": !!int "7"
  "Perception": !!int "5"
  "Arcana": !!int "10"
"damage_resistances": "cold, radiant"
"senses": "blindsight 30 ft., darkvision 120 ft., passive Perception 15"
"languages": "Common, Void Speech"
"cr": "5"
"traits":
- "desc": "When a mi-go dies, its body crumbles into millions of spores. Each creature\
    \ within 10 feet of the mi-go must succeed on a DC 15 Dexterity saving throw or\
    \ take 14 (4d6) poison damage and be [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ until the end of its next turn."
  "name": "Deathly Spores"
- "desc": "The mi-go doesn't require air, food, drink, sleep, or ambient pressure.\
    \ It requires only minimal exposure to starlight a few times each year to sustain\
    \ itself."
  "name": "Void Traveler"
"actions":
- "desc": "The mi-go makes two Claw or Psychic Bolt attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 17\
    \ (3d8 + 4) slashing damage, and the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 15) if it is a Large or smaller creature."
  "name": "Claw"
- "desc": "Ranged Spell Attack: +10 to hit, range 120 ft., one target. Hit:\
    \ 17 (3d6 + 7) psychic damage."
  "name": "Psychic Bolt"
- "desc": "The mi-go releases hallucinogenic spores in a 30-foot cone. Each creature\
    \ in the area must make a DC 15 Dexterity saving throw. On a failure, a creature\
    \ takes 21 (6d6) poison damage and is [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ until the end of its next turn. On a success, a creature takes half the damage\
    \ and isn't [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)."
  "name": "Spore Burst (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/plant/token/mi-go-tob1-2023.webp"
```
^statblock

## Environment

planar