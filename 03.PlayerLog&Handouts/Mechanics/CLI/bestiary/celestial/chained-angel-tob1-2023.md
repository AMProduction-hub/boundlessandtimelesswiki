---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/8
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/celestial
statblock: inline
aliases: ["Chained Angel"]
---
# [Chained Angel](03 - Player Log & Handouts\Mechanics\CLI\bestiary\celestial/chained-angel-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 18*  

*The angel's dark halo, flayed skin, and soulless, rage-filled eyes hint at the horrors it endured to end up shackled at the feet of the demon.*

## Broken and Chained

These angels have been captured by fiends, tortured, and turned to serve darkness. They invariably wear chains, shackles, barbed flesh hooks, or manacles to show their captive state. A pack of chained angels is considered a status symbol among the servants of evil. A chained angel fights for the forces of evil as long as it remains chained, which amuses demons and devils greatly.

## Chance at Redemption

While their souls are tainted with the blood of innocents, in their hearts chained angels still hope to be redeemed, or at least to gain the solace of extinction. Any creature that kills a chained angel receives a gift of gratitude for the release of death. If it cannot be redeemed, a chained angel is a storm of destruction.

```statblock
"name": "Chained Angel (ToB1-2023)"
"size": "Medium"
"type": "celestial"
"alignment": "Neutral Evil"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "121"
"hit_dice": "22d8 + 22"
"stats":
- !!int "18"
- !!int "16"
- !!int "12"
- !!int "12"
- !!int "18"
- !!int "20"
"speed": "30 ft., fly 60 ft."
"saves":
  "Charisma": !!int "8"
  "Dexterity": !!int "6"
  "Wisdom": !!int "7"
"skillsaves":
  "Perception": !!int "7"
"damage_resistances": "piercing"
"damage_immunities": "fire, radiant"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion)"
"senses": "darkvision 200 ft., passive Perception 17"
"languages": "Celestial, Common, Infernal, telepathy 120 ft."
"cr": "8"
"traits":
- "desc": "The chained angel doesn't require food, drink, or sleep."
  "name": "Immortal Nature"
- "desc": "The chained angel has advantage on saving throws against spells and other\
    \ magical effects."
  "name": "Magic Resistance"
- "desc": "When a creature casts the [knock](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/knock.md)\
    \ spell on the chained angel's chains, the chains release a blast of unholy flame.\
    \ The spellcaster must make a DC 16 Dexterity saving throw, taking 16 (3d10)\
    \ fire damage and 16 (3d10) radiant damage on a failed save, or half as much\
    \ damage on a successful one. If the spellcaster survives, the chained angel must\
    \ immediately make a DC 17 Wisdom saving throw. On a success, the angel's chains\
    \ fall away. It is restored to its senses and the form it had before it was chained,\
    \ typically a deva. On a failure, the chained angel remains chained for 7 days,\
    \ and during that time, any further attempts to cast [knock](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/knock.md)\
    \ on the angel's chains fail."
  "name": "Redemption"
"actions":
- "desc": "The chained angel makes two Fiery Greatsword attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11\
    \ (2d6 + 4) slashing damage plus 16 (3d10) fire damage."
  "name": "Fiery Greatsword"
- "desc": "Each creature the chained angel can see within 50 feet of it must make\
    \ a DC 15 Strength saving throw. On a failure, a creature takes 19 (3d12) radiant\
    \ damage and is knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone).\
    \ On a success, a creature takes half the damage and isn't knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Fallen Glory (Recharge 5-6)"
"reactions":
- "desc": "When a creature the chained angel can see within 60 feet of it casts a\
    \ spell that appears on the cleric or paladin spell list, the chained angel can\
    \ counter the spell with a successful ability check. This works like the [counterspell](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/counterspell.md)\
    \ spell with a +5 spellcasting ability check, except the chained angel must make\
    \ the ability check no matter the level of the spell."
  "name": "Fiendish Cunning"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/celestial/token/chained-angel-tob1-2023.webp"
```
^statblock

## Environment

planar