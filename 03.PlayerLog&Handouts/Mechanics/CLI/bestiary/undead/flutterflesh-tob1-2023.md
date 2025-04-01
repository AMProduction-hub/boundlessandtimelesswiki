---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/12
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Flutterflesh"]
---
# [Flutterflesh](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/flutterflesh-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 189*  

*This mass of fused corpses resembles a butterfly with wings of skin, limbs of bone, and a head formed of several different skulls. The dark magic that formed this abomination swirls around it hungrily.*

## Bound by Necromancy

Flutterfleshes are created in terrible necromantic rituals. Cultists gather in the name of a dark god, powerful lich, or crazed madman, and forever bind themselves body and soul into a single evil being. Flutterfleshes take recently severed limbs and fuse these new pieces to themselves in accordance with some unknowable aesthetic.

## Dilemma of Flesh

The most horrifying thing about a flutterflesh, however, is its devious nature. A flutterflesh offers its prey the choice to either die or lose a limb. If it accepts the limb, the flutterflesh then leaves the victim alone. One can always tell where a flutterflesh resides because so many of the locals are missing appendages.

```statblock
"name": "Flutterflesh (ToB1-2023)"
"size": "Large"
"type": "undead"
"alignment": "Chaotic Evil"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "187"
"hit_dice": "22d10 + 66"
"stats":
- !!int "11"
- !!int "18"
- !!int "17"
- !!int "12"
- !!int "16"
- !!int "10"
"speed": "10 ft., fly 60 ft."
"saves":
  "Wisdom": !!int "7"
  "Strength": !!int "4"
"skillsaves":
  "Deception": !!int "4"
  "Stealth": !!int "8"
  "Perception": !!int "7"
"damage_vulnerabilities": "radiant"
"damage_resistances": "cold; lightning; bludgeoning, piercing, slashing from nonmagical\
  \ attacks"
"damage_immunities": "necrotic, poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned),\
  \ [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)"
"senses": "darkvision 120 ft., passive Perception 17"
"languages": "Common, Darakhul"
"cr": "12"
"traits":
- "desc": "If the flutterflesh reduces a creature to 0 hp with a melee attack, it\
    \ can cut off one of the creature's limbs. If it does so, the target is reduced\
    \ to 1 hp instead."
  "name": "Merciful Exchange"
- "desc": "The flutterflesh's weapon attacks are magical. When the flutterflesh hits\
    \ with any weapon, the weapon deals an extra 2d8 necrotic damage (included in\
    \ the attack)."
  "name": "Necrotic Weapons"
- "desc": "The flutterflesh regains 10 hp at the start of its turn. If the flutterflesh\
    \ takes fire or radiant damage, this trait doesn't function at the start of the\
    \ flutterflesh's next turn. The flutterflesh dies only if it starts its turn with\
    \ 0 hp and doesn't regenerate."
  "name": "Regeneration"
- "desc": "The flutterflesh has advantage on saving throws against any effect that\
    \ turns undead."
  "name": "Turn Resistance"
- "desc": "The flutterflesh doesn't require air, food, drink, or sleep."
  "name": "Undead Nature"
"actions":
- "desc": "The flutterflesh makes three Bone Spur or Tormenting Gaze attacks. If two\
    \ Tormenting Gaze attacks hit one creature, the target must succeed on a DC 16\
    \ Wisdom saving throw or be [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ for 1 minute. A [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 17\
    \ (2d12 + 4) piercing damage plus 9 (2d8) necrotic damage, and the flutterflesh\
    \ impales the target on one of its bone spurs, grappling the target (escape DC\
    \ 16). The flutterflesh can have no more than two creatures impaled at a time."
  "name": "Bone Spur"
- "desc": "Ranged Spell Attack: +7 to hit, range 120 ft., one creature. Hit:\
    \ 21 (4d8 + 3) psychic damage."
  "name": "Tormenting Gaze"
- "desc": "The flutterflesh emits a wave of necromantic energy, hastening the journey\
    \ toward death. Each creature within 20 feet of the flutterflesh must make a DC\
    \ 16 Constitution saving throw, taking 45 (10d8) necrotic damage on a failed\
    \ save, or half as much damage on a successful one. A creature below half its\
    \ hp maximum has disadvantage on this saving throw."
  "name": "Creeping Death (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/flutterflesh-tob1-2023.webp"
```
^statblock

## Environment

any