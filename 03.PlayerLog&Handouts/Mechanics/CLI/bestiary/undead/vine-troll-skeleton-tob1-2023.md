---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/9
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Vine Troll Skeleton"]
---
# [Vine Troll Skeleton](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/vine-troll-skeleton-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 330*  

*Moss and flowering vines cover the hulking skeleton.*

## Corrupted Earth Magic

Vine troll skeletons guard duskthorn dryad glades and the sacred circles of druids; others serve the vila or even moss lurker colonies as guardians. In each case, they were created by corrupted earth magic for a purpose, and that energy empowers great strength and endurance—but little in the way of wits.

## Constant Regrowth

The vines holding the skeleton together regenerate quickly. This powerful magic allows vine troll skeletons to reattach severed limbs. Just like with their living cousins, only fire or acid can destroy vine troll skeletons, rendering the living vines harmless.

## Bound to a Tree's Heart

Vine troll skeletons are direct offshoots of the main vine wrapped around a duskthorn dryad 's tree, a treant, or a weeping treant. They are created by enchanting a dead troll's heart and fusing that heart with the vines of a duskthorn dryad or with the heartwood of a tree or treant, calling on magic similar to that involved in binding a dryad to her tree. Killing the duskthorn dryad or destroying the heart at the center of the parent tree kills the skeleton bound to that heart. Because of this, vine troll skeletons are single-minded defenders of their parent tree or duskthorn dryad.

```statblock
"name": "Vine Troll Skeleton (ToB1-2023)"
"size": "Large"
"type": "undead"
"alignment": "Unaligned"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "153"
"hit_dice": "18d10 + 54"
"stats":
- !!int "20"
- !!int "12"
- !!int "16"
- !!int "6"
- !!int "8"
- !!int "5"
"speed": "30 ft."
"saves":
  "Constitution": !!int "7"
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "poison"
"condition_immunities": "[deafened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Deafened),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 9"
"languages": "understands all languages it knew in life but can't speak"
"cr": "9"
"traits":
- "desc": "The vine troll skeleton regains 5 hp at the start of its turn. If the skeleton\
    \ takes acid or fire damage, this trait doesn't function at the start of the skeleton's\
    \ next turn. The skeleton dies only if it starts its turn with 0 hp and doesn't\
    \ regenerate or if its bound tree is destroyed (see Tree Bound trait)."
  "name": "Regeneration"
- "desc": "The vine troll skeleton is magically bound to a duskthorn dryad, tree,\
    \ or treant, and the skeleton must stay within 1 mile of it. If the skeleton's\
    \ bound duskthorn dryad, tree, or treant dies, the skeleton is immediately destroyed\
    \ and doesn't regenerate."
  "name": "Tree Bound"
- "desc": "The vine troll skeleton doesn't require air, food, drink, or sleep."
  "name": "Undead Nature"
"actions":
- "desc": "The skeleton makes one Bite attack and two Claw attacks, or it makes three\
    \ Poisoned Thorn attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 21\
    \ (3d10 + 5) piercing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 19\
    \ (4d6 + 5) slashing damage."
  "name": "Claw"
- "desc": "Ranged Weapon Attack: +5 to hit, range 20/60 ft., one target. Hit:\
    \ 8 (2d6 + 1) piercing damage plus 10 (3d6) poison damage."
  "name": "Poisoned Thorn"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/vine-troll-skeleton-tob1-2023.webp"
```
^statblock

## Environment

forest