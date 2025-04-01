---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/mpp
- ttrpg-cli/monster/cr/10
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/fiend
statblock: inline
aliases: ["Maelephant"]
---
# [Maelephant](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fiend/maelephant-mpp.md)
*Source: Morte's Planar Parade p. 35, Sigil and the Outlands*  

Respected as guardians by villains across the multiverse, maelephants are Fiends with pachyderm-like heads. They can exhale toxic fumes that cause foes to temporarily forget their combat training, spellcasting abilities, and other skills.

Maelephants strike bargains with wicked spellcasters and entities of the Lower Planes, pledging to guard a site or object for decades. The Fiends fulfill their end of the bargain with unwavering loyalty, steadfastly tending to their posts per the terms of their agreement.

```statblock
"name": "Maelephant (MPP)"
"size": "Large"
"type": "fiend"
"alignment": "typically  Lawful Evil"
"ac": !!int "15"
"ac_class": "[half plate armor](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/half-plate-armor.md)"
"hp": !!int "161"
"hit_dice": "17d10 + 68"
"stats":
- !!int "19"
- !!int "10"
- !!int "18"
- !!int "10"
- !!int "16"
- !!int "12"
"speed": "40 ft."
"saves":
  "Strength": !!int "8"
  "Constitution": !!int "8"
"skillsaves":
  "Perception": !!int "7"
"damage_resistances": "acid, fire, lightning"
"damage_immunities": "poison"
"condition_immunities": "[frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 120 ft., passive Perception 17"
"languages": "Infernal"
"cr": "10"
"traits":
- "desc": "The maelephant has advantage on saving throws against spells and other\
    \ magical effects."
  "name": "Magic Resistance"
"actions":
- "desc": "The maelephant makes one Barbed Trunk attack and two Glaive attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 13\
    \ (2d8 + 4) piercing damage plus 13 (2d12) poison damage. If the target is\
    \ a Medium or smaller creature, it has the [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ condition (escape DC 14). Until this grapple ends, the target has the [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ condition. While it is grappling a creature, the maelephant can't use its barbed\
    \ trunk to attack other creatures."
  "name": "Barbed Trunk"
- "desc": "Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 15\
    \ (2d10 + 4) slashing damage."
  "name": "Glaive"
- "desc": "The maelephant expels poisonous gas from its trunk in a 60-foot cone. Each\
    \ creature in that area must make a DC 16 Constitution saving throw. On a failed\
    \ save, a creature takes 39 (6d12) poison damage and has the [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ condition. While [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ in this way, the creature loses all weapon and skill proficiencies, it can't\
    \ cast spells, it can't understand language, and it has disadvantage on Intelligence\
    \ saving throws. The target can repeat the saving throw at the end of each of\
    \ its turns, ending the effect on itself on a success. On a successful save, the\
    \ target takes half as much damage only and is immune to this maelephant's Mind\
    \ Poison for 24 hours."
  "name": "Mind Poison (Recharge 5-6)"
"source":
- "MPP"
- "SatO"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fiend/token/maelephant-mpp.webp"
```
^statblock