---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/humanoid/lemurfolk
statblock: inline
aliases: ["Greyfur"]
---
# [Greyfur](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/greyfur-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 250*  

*This furred humanoid glides silently through the canopy of trees, gripping a blowgun. It observes visitors cautiously with two intelligent, bulbous eyes.*

## Jungle Rulers

These small, squirrel-like humanoids live in reclusive societies deep in the jungle. They are omnivorous gliders, subsisting on fruits and roots, insects and larvae, bird and snake eggs, and birds and small mammals. They sometimes barter with other humanoids for metal and forged items, but they prefer to rely on the forest for most of their needs.

## Greyfur Elders

Greyfurs are the eldest and most revered lemurfolk, as much as 80 years old. Their age can be estimated by the graying of their fur, but they don't track the years. Greyfurs are cunning individuals and command the arcane arts, though they rarely pursue the art of necromancy—a strong taboo prohibits them from interacting with the dead. A typical lemurfolk stands 2 feet tall and weighs 30 pounds.

```statblock
"name": "Greyfur (ToB1-2023)"
"size": "Small"
"type": "humanoid"
"subtype": "lemurfolk"
"alignment": "Neutral"
"ac": !!int "13"
"hp": !!int "67"
"hit_dice": "15d6 + 15"
"stats":
- !!int "9"
- !!int "16"
- !!int "12"
- !!int "16"
- !!int "12"
- !!int "10"
"speed": "30 ft., climb 20 ft."
"skillsaves":
  "Stealth": !!int "5"
  "Acrobatics": !!int "5"
"senses": "darkvision 60 ft., passive Perception 11"
"languages": "Common, Lemurfolk"
"cr": "3"
"traits":
- "desc": "The greyfur casts one of the following spells, requiring no material components\
    \ and using Intelligence as the spellcasting ability (spell save DC 13):\n\nAt\
    \ will: [light](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/light.md),\
    \ [mage hand](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/mage-hand.md),\
    \ [prestidigitation](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/prestidigitation.md)\n\
    \n3/day each: [color spray](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/color-spray.md),\
    \ [sleep](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/sleep.md)"
  "name": "Spellcasting"
- "desc": "The greyfur has membranes between its fore and hind limbs that expand when\
    \ falling to slow its rate of descent to 60 feet per round, landing on its feet\
    \ and taking no falling damage. It can move up to 5 feet horizontally for every\
    \ 1 foot it falls. The greyfur can't gain height with its gliding membranes alone.\
    \ If subjected to a strong wind or lift of any kind, it can use the updraft to\
    \ glide farther."
  "name": "Glide"
"actions":
- "desc": "The greyfur lemurfolk makes two Greyfur's Staff or Arcane Bolt attacks.\
    \ It can replace one attack with a use of Spellcasting."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6\
    \ + 3) bludgeoning damage plus 5 (2d4) force damage."
  "name": "Greyfur's Staff"
- "desc": "Ranged Spell Attack: +5 to hit, range 60 ft., one target. Hit: 10\
    \ (2d6 + 3) force damage."
  "name": "Arcane Bolt"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/greyfur-tob1-2023.webp"
```
^statblock

## Environment

forest