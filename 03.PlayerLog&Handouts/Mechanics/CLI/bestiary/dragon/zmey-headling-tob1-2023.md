---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/swamp
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/dragon
statblock: inline
aliases: ["Zmey Headling"]
---
# [Zmey Headling](03 - Player Log & Handouts\Mechanics\CLI\bestiary\dragon/zmey-headling-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 404*  

*Crashing through the forest, this three-headed dragon stands upright, its long tail thrashing from side to side as it walks.*

Hunting beneath the canopy of the forest, lurking below the surfaces of lakes, and guarding caves concealing great treasure and mystery, the zmey has two roles—vicious terror and nature's protector.

## Claws of the Forest

Single-mindedly destructive, the zmey keeps the heart of the forest free from interlopers. Rumors suggest the heart of an ancient forest itself can control the actions of these lesser dragons, while others believe zmeys have pacts with certain druid circles.

## Voracious Headlings

A zmey's head doesn't die when severed from its body. Within days, it becomes a miniature zmey, developing into a full-grown zmey after two months. Voracious appetite fuels this growth. Coating the head or headling in the first month of life prevents this growth.

```statblock
"name": "Zmey Headling (ToB1-2023)"
"size": "Medium"
"type": "dragon"
"alignment": "Chaotic Evil"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "105"
"hit_dice": "14d8 + 42"
"stats":
- !!int "16"
- !!int "10"
- !!int "17"
- !!int "8"
- !!int "16"
- !!int "8"
"speed": "30 ft., swim 20 ft."
"damage_resistances": "cold, fire"
"condition_immunities": "[paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)"
"senses": "darkvision 60 ft., passive Perception 13"
"languages": "Common, Draconic, Sylvan"
"cr": "5"
"traits":
- "desc": "The zmey headling can breathe air and water."
  "name": "Amphibious"
- "desc": "The zmey headling regains 10 hp at the start of its turn. If the zmey headling\
    \ takes acid or fire damage, this trait doesn't function at the start of its next\
    \ turn. The zmey headling dies if it starts its turn with 0 hp and doesn't regenerate."
  "name": "Regeneration"
"actions":
- "desc": "The zmey headling makes one Bite attack and two Claw attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 16\
    \ (2d12 + 3) piercing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 10\
    \ (2d6 + 3) slashing damage."
  "name": "Claw"
- "desc": "The zmey headling exhales fire in a 30-foot cone. Each creature in that\
    \ area must make a DC 14 Dexterity saving throw, taking 28 (8d6) fire damage\
    \ on a failed save, or half as much damage on a successful one. The headling can\
    \ choose for this breath to not harm plants or Plant creatures."
  "name": "Fire Breath (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/dragon/token/zmey-headling-tob1-2023.webp"
```
^statblock

## Environment

forest, swamp