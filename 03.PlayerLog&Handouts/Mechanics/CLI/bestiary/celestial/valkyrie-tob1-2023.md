---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/11
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/celestial
statblock: inline
aliases: ["Valkyrie"]
---
# [Valkyrie](03 - Player Log & Handouts\Mechanics\CLI\bestiary\celestial/valkyrie-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 379*  

*These warrior women, armed with cruel-looking swords, sit astride massive winged wolves. Each of them is as beautiful, graceful, and fierce as a well-honed war axe.*

## Choosers of the Slain

Valkyries are sent by Odin to decide the course of battles and harvest the souls of brave fallen warriors. Riding winged wolves (use the statistics of a winter wolf with a flying speed of 80 feet and a neutral alignment), they visit battlefields to do their master's will, surrounded by crows and ravens. Valkyries remain hidden among the ravens during these missions, acting only when fate decrees.

## Love Battle

Valkyries love battle and bloodshed, and their presence on the battlefield inspires warriors to great acts of valor and heroism.

## Neutral Parties

Valkyries seldom interfere in mortal affairs, save to ensure the proper course of battles. When duty demands, as a punishment, or when they fall in love, a valkyrie may wander the mortal world.

```statblock
"name": "Valkyrie (ToB1-2023)"
"size": "Medium"
"type": "celestial"
"alignment": "Neutral"
"ac": !!int "18"
"ac_class": "[chain mail](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/chain-mail.md),\
  \ [shield](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/shield.md)"
"hp": !!int "150"
"hit_dice": "20d8 + 60"
"stats":
- !!int "18"
- !!int "18"
- !!int "16"
- !!int "12"
- !!int "19"
- !!int "18"
"speed": "30 ft., fly 60 ft."
"saves":
  "Charisma": !!int "8"
  "Wisdom": !!int "8"
  "Intelligence": !!int "5"
  "Constitution": !!int "7"
"skillsaves":
  "Perception": !!int "8"
"damage_resistances": "acid, cold, fire, lightning, thunder"
"damage_immunities": "poison; bludgeoning, piercing, slashing from nonmagical attacks"
"condition_immunities": "[frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "truesight 60 ft., passive Perception 18"
"languages": "all, telepathy 60 ft."
"cr": "11"
"traits":
- "desc": "Friendly creatures wielding weapons within 30 feet of the valkyrie have\
    \ advantage on weapon attack rolls and ability checks. At the start of each of\
    \ its turns, the valkyrie can choose to exclude any number of friendly creatures\
    \ from this aura (no action required)."
  "name": "Aura of Valor"
- "desc": "The valkyrie doesn't require food, drink, or sleep."
  "name": "Immortal Nature"
- "desc": "The valkyrie has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "The valkyrie's weapon attacks are magical. When it hits with any weapon,\
    \ the weapon deals an extra 16 (3d10) radiant damage (included in the attack)."
  "name": "Radiant Weapons"
"actions":
- "desc": "The valkyrie can use its Gaze of Doom. It then makes two Longsword attacks\
    \ and one Spear attack, or it makes three Radiant Bolt attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 8 (1d8\
    \ + 4) slashing damage, or 9 (1d10 + 4) slashing damage if used with two hands,\
    \ plus 16 (3d10) radiant damage."
  "name": "Longsword"
- "desc": "Melee or Ranged Weapon Attack: +8 to hit, reach 5 ft. or range 20/60\
    \ ft., one target. Hit: 7 (1d6 + 4) piercing damage, or 8 (1d8 + 4) piercing\
    \ damage if used with two hands to make a melee attack, plus 16 (3d10) radiant\
    \ damage."
  "name": "Spear"
- "desc": "Ranged Spell Attack: +8 to hit, range 120 ft., one target. Hit: 26\
    \ (4d10 + 4) radiant damage."
  "name": "Radiant Bolt"
- "desc": "The valkyrie's gaze foretells a doomed fate for one creature the valkyrie\
    \ can see within 60 feet of it. The target must succeed on a DC 16 Wisdom saving\
    \ throw or be [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ for 1 minute. The target can repeat the saving throw at the end of each of its\
    \ turns, ending the effect on itself on a success."
  "name": "Gaze of Doom"
- "desc": "The valkyrie touches another creature. The target magically regains 21\
    \ 6d6 hp and is freed from any curse, disease, poison, blindness, or deafness."
  "name": "Healing Touch (4/Day)"
"reactions":
- "desc": "When a friendly creature the valkyrie can see and within its Aura of Valor\
    \ is reduced to 0 hp while engaged in melee combat, the valkyrie can reincarnate\
    \ the creature as a gladiator. If the gladiator reduces at least three creatures\
    \ to 0 hp within 1 minute of its reincarnation, it transforms into an einherjar.\
    \ The valkyrie can provide ascension to up to two creatures each hour with this\
    \ reaction."
  "name": "Ascension"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/celestial/token/valkyrie-tob1-2023.webp"
```
^statblock

## Environment

any, planar