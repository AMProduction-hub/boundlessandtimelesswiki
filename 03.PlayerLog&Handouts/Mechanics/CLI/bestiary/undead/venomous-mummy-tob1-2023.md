---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Venomous Mummy"]
---
# [Venomous Mummy](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/venomous-mummy-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 279*  

*This shambling corpse warrior is draped in stained linen wrappings. Green liquid drips from rents in the fabric.*

## Servant of the Scorpion Goddess

These mummies are crafted by the faithful of a goddess of poison and scorpions to guard holy sites and tombs and to serve as agents of the goddess's retribution. Should the goddess's faithful feel themselves slighted by an individual or a community, they perform dangerous rituals to awaken these creatures from the crypts of her temples. Venomous mummies delight in wreaking deadly vengeance against those who disrespect the goddess.

## Death to Blasphemers

In most cases, retribution is limited to people who actually undertook acts of blasphemy. However, if the priests determine that an entire community has grown heretical, they may set mummies loose against the entire populace.

## Deadly Smoke

Though fire destroys many undead, burning a venomous mummy releases a toxic smoke.

```statblock
"name": "Venomous Mummy (ToB1-2023)"
"size": "Medium"
"type": "undead"
"alignment": "Lawful Evil"
"ac": !!int "11"
"ac_class": "natural armor"
"hp": !!int "58"
"hit_dice": "9d8 + 18"
"stats":
- !!int "16"
- !!int "8"
- !!int "15"
- !!int "7"
- !!int "10"
- !!int "14"
"speed": "20 ft."
"saves":
  "Wisdom": !!int "2"
"damage_vulnerabilities": "fire"
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "necrotic, poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 10"
"languages": "the languages it knew in life"
"cr": "3"
"traits":
- "desc": "If the venomous mummy takes fire damage, each creature within 10 feet of\
    \ it must make a DC 12 Constitution saving throw as its venom-soaked wraps emit\
    \ a poisonous smoke. On a failure, a creature takes 7 (2d6) poison damage and\
    \ is [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ until the end of its next turn. On a success, a creature takes half the damage\
    \ and isn't [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned).\
    \ The smoke fills a 10-foot-radius sphere centered on the mummy. The sphere spreads\
    \ around corners, and its area is lightly obscured. It lasts until the end of\
    \ the mummy's next turn. A creature that enters the cloud for the first time on\
    \ a turn or starts its turn there is [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ until the end of its next turn."
  "name": "Toxic Smoke"
- "desc": "A creature that touches the mummy or hits it with a melee attack while\
    \ within 5 feet of it takes 3 (1d6) poison damage."
  "name": "Venom-Soaked Wraps"
- "desc": "The venomous mummy doesn't require air, food, drink, or sleep."
  "name": "Undead Nature"
"actions":
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10\
    \ (2d6 + 3) bludgeoning damage plus 10 (3d6) poison damage. If the target\
    \ is a creature, it must succeed on a DC 12 Constitution saving throw or be cursed.\
    \ Every 24 hours that elapse, the cursed target must succeed on a DC 12 Constitution\
    \ saving throw or take 7 (2d6) poison damage, and its hp maximum is reduced\
    \ by that amount. This reduction lasts until the target finishes a long rest after\
    \ the curse is removed. The target dies if this effect reduces its hp maximum\
    \ to 0. The curse lasts until removed by the [remove curse](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/remove-curse.md)\
    \ spell or similar magic."
  "name": "Venomous Fist"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/venomous-mummy-tob1-2023.webp"
```
^statblock

## Environment

desert