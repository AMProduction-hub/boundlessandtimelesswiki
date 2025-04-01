---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fiend/devil
statblock: inline
aliases: ["Salt Devil"]
---
# [Salt Devil](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fiend/salt-devil-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 100*  

*The creature's skin sparkles with fine salt crystals as it brandishes a scimitar and jagged claws.*

## Sparkly Crystals

Salt devils have sharp, crystalline teeth, sparkling skin studded with fine salt crystals, and long claws that leave jagged, burning wounds. They can also fight with salt‑encrusted blades seemingly forged from thin air.

## Servants of Mammon

Salt devils claim to serve the devil-god Mammon. They often ally with gnolls and slavers with whom they seek out oases to use as ambush sites or just to poison the water.

## Slavers and Corruptors

Salt devils create slave markets and salt mines, where they thrive on the misery of those indentured into their service. They often forge alliances with mortals when partners are needed for an endeavor, and they are less grasping and greedy than one might expect of Mammon's servants, preferring to encourage corruption in others.

```statblock
"name": "Salt Devil (ToB1-2023)"
"size": "Medium"
"type": "fiend"
"subtype": "devil"
"alignment": "Lawful Evil"
"ac": !!int "13"
"ac_class": "natural armor"
"hp": !!int "93"
"hit_dice": "11d8 + 44"
"stats":
- !!int "18"
- !!int "13"
- !!int "18"
- !!int "13"
- !!int "14"
- !!int "15"
"speed": "30 ft."
"saves":
  "Charisma": !!int "5"
  "Dexterity": !!int "4"
  "Constitution": !!int "7"
"skillsaves":
  "Stealth": !!int "4"
  "Perception": !!int "5"
"damage_resistances": "acid; cold; bludgeoning, piercing, slashing from nonmagical\
  \ attacks that aren't silvered"
"damage_immunities": "fire, poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 120 ft., passive Perception 15"
"languages": "Common, Gnoll, Infernal, telepathy 120 ft."
"cr": "6"
"traits":
- "desc": "Magical darkness doesn't impede the salt devil's darkvision."
  "name": "Devil's Sight"
- "desc": "The salt devil has advantage on saving throws against spells and other\
    \ magical effects."
  "name": "Magic Resistance"
- "desc": "A creature that touches the salt devil or hits it with a melee attack while\
    \ within 5 feet of it takes 3 (1d6) slashing damage."
  "name": "Salt-Encrusted Hide"
"actions":
- "desc": "The salt devil makes two Scimitar attacks and one Water-Draining Claw attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 7 (1d6\
    \ + 4) slashing damage."
  "name": "Scimitar"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 6 (1d4\
    \ + 4) slashing damage. If the target is a creature that isn't a Construct or\
    \ Undead, it must make a DC 15 Constitution saving throw, taking 14 (4d6) necrotic\
    \ damage on a failed save, or half as much damage on a successful one. Plants,\
    \ Oozes, and creatures with the Amphibious, Water Breathing, or Water Form traits\
    \ have disadvantage on this saving throw. If the saving throw fails by 5 or more,\
    \ the target also suffers one level of [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion)."
  "name": "Water-Draining Claw"
- "desc": "The salt devil magically teleports, along with any equipment it is wearing\
    \ or carrying, up to 120 feet to an unoccupied space it can see."
  "name": "Teleport (3/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fiend/token/salt-devil-tob1-2023.webp"
```
^statblock

## Environment

desert, planar