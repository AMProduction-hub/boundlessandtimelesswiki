---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/environment/farmland
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Dissimortuum"]
---
# [Dissimortuum](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/dissimortuum-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 106*  

*This twisted humanoid has gray flesh and black claws that drip blood. A bone mask is bound to its head by strips of putrid flesh, and a third arm hangs from the right side of the creature's body, its hand clutching a large sack stained with blood.*

## Plague Bringers

Dissimortuum are undead monstrosities constructed by necromancers to spread the undead plague, slowly but surely. These creatures are rare but tenacious. A dissimortuum obeys orders from the necromancer whose magic created it. When a dissimortuum kills, it collects body parts from its victims and keeps them in a sack that it carries with its third arm at all times. The monster sets down its sack of trophies only when pressed in combat, to make the most of its extra limb.

## Constructing Dissimortuum

Even when not following instructions, a dissimortuum seeks to create more of its own kind. The creature wanders graveyards, battlefields, and slums, searching for the gruesome components it needs to construct a mask and body for its undead offspring. The process is slow, taking up to a month to make a single mask, but a dissimortuum has plenty of time. The new creation is independent and not under the control of its maker or of the necromancer that might have created its maker.

> [!note] Dissimortuum's Cursed Mask
> 
> The dissimortuum's mask is nigh indestructible. When the creature is destroyed, its mask usually survives and breaks free. On its own, the object emits a faint magical aura with mixed enchantment and necromantic properties. It is a tempting souvenir, but any humanoid or giant foolish enough to don the mask is immediately wracked by pain and takes 7 (`2d6`) necrotic damage. The creature must succeed on a DC 15 Wisdom saving throw or become dominated by the mask. The domination arrives slowly. The creature acts normally for a day or two, but then the creature notices periods of time that cannot be accounted for. During these unremembered times, the creature gathers the grisly components needed to build a new body for the dissimortuum. This process takes a week, after which the creature is freed from domination as the dissimortuum arises anew and dons its mask once more.
^dissimortuums-cursed-mask

```statblock
"name": "Dissimortuum (ToB1-2023)"
"size": "Medium"
"type": "undead"
"alignment": "Chaotic Evil"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "112"
"hit_dice": "15d8 + 45"
"stats":
- !!int "14"
- !!int "10"
- !!int "16"
- !!int "8"
- !!int "11"
- !!int "18"
"speed": "30 ft., climb 30 ft."
"saves":
  "Constitution": !!int "6"
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "necrotic, poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 10"
"languages": "the languages of its creator"
"cr": "7"
"traits":
- "desc": "The dissimortuum can climb difficult surfaces, including upside down on\
    \ ceilings, without needing to make an ability check."
  "name": "Spider Climb"
- "desc": "The dissimortuum doesn't require air, food, drink, or sleep."
  "name": "Undead Nature"
"actions":
- "desc": "The dissimortuum makes three Claw attacks. It can replace one Claw attack\
    \ with a use of Terrifying Mask."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 15\
    \ (3d8 + 2) slashing damage."
  "name": "Claw"
- "desc": "Each non-Undead creature within 60 feet of the dissimortuum that can see\
    \ it must succeed on a DC 15 Wisdom saving throw or be [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ for 1 minute. A [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ creature can repeat the saving throw, ending the effect on itself on a success.\
    \ If a target's saving throw is successful or the effect ends for it, the target\
    \ becomes immune to the dissimortuum's Terrifying Mask for the next 24 hours."
  "name": "Terrifying Mask"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/dissimortuum-tob1-2023.webp"
```
^statblock

## Environment

farmland, urban