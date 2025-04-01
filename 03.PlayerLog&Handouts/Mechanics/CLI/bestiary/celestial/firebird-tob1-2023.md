---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/celestial
statblock: inline
aliases: ["Firebird"]
---
# [Firebird](03 - Player Log & Handouts\Mechanics\CLI\bestiary\celestial/firebird-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 187*  

*This proud bird struts like a peacock, made all the more majestic by its flaming fan of feathers, which shift through the color spectrum.*

## Guides and Helpers

Firebirds are welcome sights to those in need of warmth and safety. They primarily work at night or in underground areas, where their talents are most needed. Friendly to all creatures, they become aggressive only upon witnessing obviously evil acts. Firebirds enjoy working with good adventuring parties, providing light and healing, though their wanderlust prevents them from staying for long.

## Redeemers

Firebirds enjoy acting as reformers. They search for creatures they perceive as potential "light bringers," and they grant boons to such creatures, magically coaxing the creatures into performing good deeds in the hope such acts redeem the creatures.

## Magical Feathers

Firebird feathers are prized throughout the mortal world, and occasionally, the creatures bestow feathers upon those they favor. Firebirds also seed hidden locations with specialized feathers, which burst into full-grown firebirds after a year. Firebirds live over 100 years.

```statblock
"name": "Firebird (ToB1-2023)"
"size": "Small"
"type": "celestial"
"alignment": "Neutral Good"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "88"
"hit_dice": "16d6 + 32"
"stats":
- !!int "12"
- !!int "19"
- !!int "14"
- !!int "16"
- !!int "15"
- !!int "21"
"speed": "20 ft., fly 60 ft."
"saves":
  "Charisma": !!int "7"
  "Wisdom": !!int "4"
"skillsaves":
  "Medicine": !!int "4"
  "Insight": !!int "4"
  "Perception": !!int "6"
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "fire, poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "truesight 60 ft., passive Perception 16"
"languages": "Celestial, Common, Primordial, telepathy 60 ft."
"cr": "4"
"traits":
- "desc": "A creature that has received assistance, such as healing or a glowing feather,\
    \ from the firebird must succeed on a DC 15 Wisdom saving throw or be affected\
    \ by the [geas](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/geas.md)\
    \ spell for 30 days. While under the geas, the affected creature must assist nonhostile\
    \ creatures suffering from starvation or thirst by alleviating the starvation\
    \ or thirst."
  "name": "Enforce Good Deeds"
- "desc": "The firebird's weapon attacks are magical. When the firebird hits with\
    \ any weapon, the weapon deals an extra 2d6 fire damage (included in the attack)."
  "name": "Fiery Weapons"
- "desc": "The firebird sheds bright light in a 5- to 20-foot radius and dim light\
    \ for an additional number of feet equal to the chosen radius. The firebird can\
    \ alter the radius as a bonus action. If the firebird willingly gifts a feather\
    \ to a creature, the feather sheds bright light in a 10-foot radius and dim light\
    \ for an additional 10 feet indefinitely."
  "name": "Glowing Feathers"
- "desc": "The firebird has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "The firebird and each creature within 5 feet of it are immune to the effects\
    \ of cold environments, provided the cold is caused by naturally occurring weather\
    \ and climate. When the firebird is inside a structure, it can choose for this\
    \ trait to affect all creatures within the structure (no action required), regardless\
    \ of how close they are to it."
  "name": "Warming Presence"
"actions":
- "desc": "The firebird makes one Beak attack and one Talon attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7 (1d6\
    \ + 4) piercing damage plus 7 (2d6) fire damage."
  "name": "Beak"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (2d4\
    \ + 4) slashing damage plus 7 (2d6) fire damage."
  "name": "Talon"
- "desc": "The firebird fires a burning ray of light from its tail feathers in a 30-foot\
    \ line that is 5 feet wide. Each creature in that line must make a DC 15 Dexterity\
    \ saving throw. On a failure, a creature takes 17 (5d6) fire damage and is [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ until the end of its next turn. On a success, a creature takes half the damage\
    \ and isn't [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)."
  "name": "Blinding Ray (Recharge 5-6)"
- "desc": "The firebird touches another creature, brushing its wings against the creature.\
    \ The target magically regains 10 3d6 hp and is freed from any disease, poison,\
    \ blindness, or deafness."
  "name": "Healing Feathers (3/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/celestial/token/firebird-tob1-2023.webp"
```
^statblock

## Environment

forest, underdark