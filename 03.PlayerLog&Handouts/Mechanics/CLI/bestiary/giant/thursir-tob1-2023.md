---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/arctic
- ttrpg-cli/monster/environment/mountain
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/giant
statblock: inline
aliases: ["Thursir"]
---
# [Thursir](03 - Player Log & Handouts\Mechanics\CLI\bestiary\giant/thursir-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 210*  

*The giant's hair and beard are plaited with rings and other bits of decorative stone and metal, and it carries a large, rune-inscribed hammer.*

## Forge Masters

Greedy and aggressively competitive, thursir dwell in vast caverns under frozen mountains where they labor to forge chains, armor, and massive engines of war. Smaller than many giants, thursir have a natural affinity for metalworking. Armor or weapons forged by a thursir giant are of the highest quality, and other giants often seek thursir smiths to outfit their people in times of strife.

## Enormous Appetites

When not toiling at the forge, these giants entertain themselves with gluttonous feasts and boisterous wrestling competitions, or they raid human settlements for food and valuables.

## Divided Society

Female thursir rarely leave thursir dwellings, tending the family and hearth and performing much of a community's labor, while male thursir spend their time crafting, metalworking, and going to war. However, female thursir have the most affinity for magic and make up the bulk of the thursir's priesthood and spellcasters. Priestesses hold especially high standing in thursir society and often operate as valued advisors to clan leadership or accompany the most powerful units of warriors into battle, tending wounds and boosting morale.

```statblock
"name": "Thursir (ToB1-2023)"
"size": "Large"
"type": "giant"
"alignment": "Unaligned"
"ac": !!int "13"
"ac_class": "[chain shirt](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/chain-shirt.md)"
"hp": !!int "114"
"hit_dice": "12d10 + 48"
"stats":
- !!int "19"
- !!int "10"
- !!int "18"
- !!int "13"
- !!int "15"
- !!int "11"
"speed": "40 ft."
"saves":
  "Constitution": !!int "6"
"skillsaves":
  "Athletics": !!int "6"
  "Perception": !!int "4"
"senses": "darkvision 60 ft., passive Perception 14"
"languages": "Common, Dwarvish, Giant"
"cr": "3"
"traits":
- "desc": "The thursir has advantage on saving throws against being [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)."
  "name": "Cast Iron Stomach"
- "desc": "The alignment of an thursir is neutral evil (50%) or lawful evil (50%)."
  "name": "Alignment"
"actions":
- "desc": "Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 13\
    \ (2d8 + 4) bludgeoning damage, or 15 (2d10 + 4) bludgeoning damage if used\
    \ with two hands to make a melee attack."
  "name": "Warhammer"
- "desc": "Ranged Weapon Attack: +6 to hit, range 60/240 ft., one target. Hit:\
    \ 15 (2d10 + 4) bludgeoning damage."
  "name": "Rock"
"bonus_actions":
- "desc": "The thursir touches a weapon, painting the thurs rune on the weapon in\
    \ the thursir's blood. When the thursir hits with the weapon while the rune is\
    \ active, the weapon deals an extra 9 (2d8) lightning damage, and the target\
    \ can't take reactions until the start of its next turn. The rune lasts for 1\
    \ minute."
  "name": "Runic Blood (3/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/giant/token/thursir-tob1-2023.webp"
```
^statblock

## Environment

arctic, mountain, underdark