---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/8
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/dragon
statblock: inline
aliases: ["Rust Drake"]
---
# [Rust Drake](03 - Player Log & Handouts\Mechanics\CLI\bestiary\dragon/rust-drake-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 145*  

*This rust-covered dragon could easily be mistaken for a pile of scrap metal.*

## Shedding Rust

Aside from fangs and claws like iron spikes, this dragon-like creature seems to be nothing more than a collection of rust. Each beating of its wings brings a shower of flakes.

## Warped Metallics

Many sages claim that rust dragons are a perversion of nature's order obtained either by the corruption of a metallic dragon's egg or the transformation of such a dragon by way of a ritual. Others disagree and propose another theory about a malady that affects the skin of young metallic dragons and ferrous drakes alike. So far, no one has discovered the truth about their origins.

## Filthy Scrap Metal Eaters

These foul creatures feed on rust and are known as disease carriers.

```statblock
"name": "Rust Drake (ToB1-2023)"
"size": "Medium"
"type": "dragon"
"alignment": "Chaotic Evil"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "161"
"hit_dice": "19d8 + 76"
"stats":
- !!int "20"
- !!int "15"
- !!int "19"
- !!int "12"
- !!int "8"
- !!int "8"
"speed": "30 ft., fly 80 ft."
"skillsaves":
  "Stealth": !!int "5"
  "Perception": !!int "5"
"damage_vulnerabilities": "acid"
"damage_immunities": "poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 15"
"languages": "Common, Draconic"
"cr": "8"
"traits":
- "desc": "A creature infected with this disease manifests symptoms 1d4 days after\
    \ infection, which include painful muscle spasms, particularly in the jaw. At\
    \ the end of each long rest, the infected creature must succeed on a DC 15 Constitution\
    \ saving throw or be [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ for 1 hour and have its Dexterity score reduced by 1d4. This reduction lasts\
    \ until the disease is cured. If the disease reduces the creature's Dexterity\
    \ to 0, the creature dies. A creature that succeeds on two saving throws recovers\
    \ from the disease."
  "name": "Rust Drake Lockjaw"
"actions":
- "desc": "The drake makes one Bite attack and two Tail Swipe attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 18\
    \ (3d8 + 5) piercing damage, and the target must succeed on a DC 15 Constitution\
    \ save or contract the rust drake lockjaw disease (see the Rust Drake Lockjaw\
    \ trait)."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 14\
    \ (2d8 + 5) bludgeoning damage."
  "name": "Tail Swipe"
- "desc": "The rust drake vomits forth a 15-foot cone of rusted metal. Each creature\
    \ in the area must make a DC 15 Dexterity saving throw, taking 22 (5d8) slashing\
    \ damage and 22 (5d8) poison damage on a failed save, or half as much damage\
    \ on a successful one. In addition, each creature that failed the saving throw\
    \ must succeed on a DC 15 Constitution saving throw or contract the rust drake\
    \ lockjaw disease (see the Rust Drake Lockjaw trait)."
  "name": "Vomit Scrap (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/dragon/token/rust-drake-tob1-2023.webp"
```
^statblock

## Environment

urban