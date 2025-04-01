---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/celestial/shapechanger
statblock: inline
aliases: ["Fidele Angel"]
---
# [Fidele Angel](03 - Player Log & Handouts\Mechanics\CLI\bestiary\npc/fidele-angel-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 19*  

*What appears to be a mated pair of birds changes into two bestial celestials that move in perfect harmony.*

Fidele angels form from souls so devoted to each other that their love transcends death.

## Friends to Lovers

Fideles are charged with exhorting mortals to respect the bonds of partnership. They assist lovers facing obstacles and punish the enemies of love. Where there is a conflict between two cultures' laws in love, they prefer the result that keeps lovers together.

## Quiet Diplomats

They prefer diplomacy to force and, despite the urgency of love, they've been known to live secretly among mortals for years or decades while waging quiet campaigns against social mores and cultural norms that keep love from achieving its full potential.

```statblock
"name": "Fidele Angel (ToB1-2023)"
"size": "Medium"
"type": "celestial"
"subtype": "shapechanger"
"alignment": "Lawful Good"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "104"
"hit_dice": "16d8 + 32"
"stats":
- !!int "20"
- !!int "18"
- !!int "14"
- !!int "14"
- !!int "16"
- !!int "18"
"speed": "40 ft., fly 40 ft. (10 ft. fly 80 ft. in eagle form)"
"saves":
  "Charisma": !!int "7"
  "Dexterity": !!int "7"
  "Wisdom": !!int "6"
  "Intelligence": !!int "5"
  "Constitution": !!int "5"
"skillsaves":
  "Insight": !!int "6"
  "Perception": !!int "6"
"damage_resistances": "fire; lightning; poison; bludgeoning, piercing, slashing from\
  \ nonmagical attacks"
"damage_immunities": "acid, cold"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 16"
"languages": "Celestial, Common, Infernal, telepathy 60 ft."
"cr": "5"
"traits":
- "desc": "The angel casts one of the following spells, requiring no material components\
    \ and using Charisma as its spellcasting ability (spell save DC 15):\n\nAt will:\
    \ [detect evil and good](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/detect-evil-and-good.md),\
    \ [purify food and drink](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/purify-food-and-drink.md),\
    \ [spare the dying](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/spare-the-dying.md)\n\
    \n3/day each: [bless](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/bless.md),\
    \ [cure wounds](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/cure-wounds.md),\
    \ [daylight](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/daylight.md)"
  "name": "Spellcasting"
- "desc": "Fidele angels are magically connected. Damage taken by the fidele angel\
    \ is split evenly between the fidele angel and its paired fidele angel. The angel\
    \ that was the original target of the attack takes any damage that won't divide\
    \ evenly. All other effects, such as reducing ability scores or being the target\
    \ of a [bless](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/bless.md)\
    \ spell, affect only the target."
  "name": "Ever Connected"
- "desc": "The fidele angel doesn't require food, drink, or sleep."
  "name": "Immortal Nature"
- "desc": "The angel has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "The angel's weapon attacks are magical."
  "name": "Magic Weapons"
- "desc": "No spell, feature, trait, magic, or other effect can cause a fidele angel\
    \ to act against or harm its mate or change its love or loyalty toward its mate."
  "name": "Unshakeable Fidelity"
"actions":
- "desc": "The fidele angel makes three Longsword or Radiant Bolt attacks. Alternatively,\
    \ it makes one Beak attack and two Talons attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 9 (1d8\
    \ + 5) slashing damage, or 10 (1d10 + 5) slashing damage if used with two hands."
  "name": "Longsword (Humanoid or True Form Only)"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 8 (1d6\
    \ + 5) piercing damage."
  "name": "Beak (Bird Form Only)"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 12\
    \ (2d6 + 5) slashing damage."
  "name": "Talons (Bird Form Only)"
- "desc": "Ranged Spell Attack: +7 to hit, range 120 ft., one target. Hit: 11\
    \ (2d6 + 4) radiant damage."
  "name": "Radiant Bolt"
- "desc": "If its mate is more than 1 mile away from it, the fidele angel can magically\
    \ teleport, along with any equipment it is wearing or carrying, to an unoccupied\
    \ space within 10 feet of its mate. The angel can use this action even if its\
    \ mate is on another plane of existence."
  "name": "To My Lover's Side"
"bonus_actions":
- "desc": "The fidele angel transforms into a Medium or smaller Humanoid, a Large\
    \ or smaller birdlike Beast, or back into its true form, which is a winged Celestial.\
    \ Without wings, it loses its flying speed. Its statistics, other than its size\
    \ and speed, are the same in each form. Any equipment it is wearing or carrying\
    \ isn't transformed. It reverts to its true form if it dies."
  "name": "Change Shape"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/npc/token/fidele-angel-tob1-2023.webp"
```
^statblock

## Environment

planar