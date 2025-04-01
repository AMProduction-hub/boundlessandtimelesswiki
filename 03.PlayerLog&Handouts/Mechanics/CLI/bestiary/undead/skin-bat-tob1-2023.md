---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1-2
- ttrpg-cli/monster/environment/mountain
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Skin Bat"]
---
# [Skin Bat](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/skin-bat-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 331*  

*A repulsive, batlike creature darts from the darkness. Its body consists entirely of rotting sheets of stolen skin. Though its large eyes are glassy and lifeless, an unmistakably evil intent glimmers within them as a toothless mouth spreads wide in hunger*.

Skin bats are undead creatures created from skin flayed from the victims of sacrificial rites. They are given a measure of unlife by a vile ritual involving immersion in Abyssal flesh vats and invocations to Camazotz and similar demon lords. They feed on the skin of living beings to replenish their own constantly rotting skin. Their acidic saliva acts as a paralytic poison and leaves ugly scars on those who survive an attack. The typical skin bat has an 8-foot wingspan. The color of their skin matches that of their prey, so a skin bat's coloration can change over time. A skin bat weighs about 15 pounds.

## Cliff and Dungeon Dwellers

Skin bats prey on the unwary but do not develop sinister plots of their own. Their flocks can be encountered in isolated areas accessible only by flight or by climbing treacherous cliffs. Skin bats can exist in any climate. In cool climes, they feed only infrequently, because the cold preserves their forms and reduces the need to replenish decaying flesh. This also explains why they are attracted to the dark depths of ageless dungeons. In wet, tropical climes where their skin decomposes rapidly, skin bats are voracious feeders by necessity.

## Accidental Treasures

Skin bats have no use for magic items or wealth, but occasionally a ring or necklace from a past victim gets embedded in their fleshy folds, where it becomes an unintended trophy.

```statblock
"name": "Skin Bat (ToB1-2023)"
"size": "Small"
"type": "undead"
"alignment": "Neutral Evil"
"ac": !!int "13"
"ac_class": "natural armor"
"hp": !!int "28"
"hit_dice": "8d6"
"stats":
- !!int "12"
- !!int "16"
- !!int "10"
- !!int "2"
- !!int "13"
- !!int "6"
"speed": "10 ft., fly 40 ft."
"skillsaves":
  "Perception": !!int "3"
"damage_immunities": "poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "blindsight 20 ft., darkvision 60 ft., passive Perception 13"
"languages": ""
"cr": "1/2"
"traits":
- "desc": "The skin bat can't use its blindsight while [deafened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Deafened)."
  "name": "Echolocation"
- "desc": "The skin bat doesn't require air or sleep."
  "name": "Hungry Dead Nature"
"actions":
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4\
    \ + 3) piercing damage, and the target must succeed on a DC 10 Constitution saving\
    \ throw or be [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ until the end of its next turn. On a success, the target can't be [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ in this way by the skin bat again for 24 hours.\n\nIn addition, the skin bat\
    \ attaches to the target. While attached, the skin bat can't attack, and at the\
    \ start of each of the bat's turns, the target takes 5 (1d4 + 3) piercing damage.\
    \ The attached bat moves with the target whenever the target moves, requiring\
    \ none of the bat's movement. It can detach itself by spending 5 feet of its movement\
    \ on its turn. A creature, including the target, can use its action to detach\
    \ the skin bat by succeeding on a DC 11 Strength check."
  "name": "Bite"
"reactions":
- "desc": "When the skin bat is reduced to below half its hp maximum while underground\
    \ or outside at night, it releases a high-frequency cry similar to that of an\
    \ injured bat, attracting other bats to it. On initiative count 20 of the next\
    \ round, 1d6 bats arrive and aid the skin bat. These bats aren't under the skin\
    \ bat's control, but they protect it to the best of their abilities, attacking\
    \ those that harm the skin bat."
  "name": "Attract Bats (1/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/skin-bat-tob1-2023.webp"
```
^statblock

## Environment

mountain, underdark