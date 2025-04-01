---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1-4
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/humanoid/lemurfolk
statblock: inline
aliases: ["Lemurfolk"]
---
# [Lemurfolk](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/lemurfolk-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 250*  

*This furred humanoid glides silently through the canopy of trees, gripping a blowgun. It observes visitors cautiously with two intelligent, bulbous eyes.*

## Jungle Rulers

These small, squirrel-like humanoids live in reclusive societies deep in the jungle. They are omnivorous gliders, subsisting on fruits and roots, insects and larvae, bird and snake eggs, and birds and small mammals. They sometimes barter with other humanoids for metal and forged items, but they prefer to rely on the forest for most of their needs.

## Greyfur Elders

Greyfurs are the eldest and most revered lemurfolk, as much as 80 years old. Their age can be estimated by the graying of their fur, but they don't track the years. Greyfurs are cunning individuals and command the arcane arts, though they rarely pursue the art of necromancy—a strong taboo prohibits them from interacting with the dead. A typical lemurfolk stands 2 feet tall and weighs 30 pounds.

```statblock
"name": "Lemurfolk (ToB1-2023)"
"size": "Small"
"type": "humanoid"
"subtype": "lemurfolk"
"alignment": "Neutral"
"ac": !!int "12"
"hp": !!int "21"
"hit_dice": "6d6"
"stats":
- !!int "10"
- !!int "15"
- !!int "11"
- !!int "12"
- !!int "10"
- !!int "8"
"speed": "30 ft., climb 20 ft."
"skillsaves":
  "Stealth": !!int "4"
  "Acrobatics": !!int "4"
"senses": "darkvision 60 ft., passive Perception 10"
"languages": "Common, Lemurfolk"
"cr": "1/4"
"traits":
- "desc": "The lemurfolk has membranes between its fore and hind limbs that expand\
    \ when falling to slow its rate of descent to 60 feet per round, landing on its\
    \ feet and taking no falling damage. It can move up to 5 feet horizontally for\
    \ every 1 foot it falls. The lemurfolk can't gain height with its gliding membranes\
    \ alone. If subjected to a strong wind or lift of any kind, it can use the updraft\
    \ to glide farther."
  "name": "Glide"
"actions":
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6\
    \ + 2) bludgeoning damage."
  "name": "Slam"
- "desc": "Ranged Weapon Attack: +4 to hit, range 25/100 ft., one creature. Hit:\
    \ 4 (1d4 + 2) piercing damage, and the target must succeed on a DC 12 Constitution\
    \ saving throw or be [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 hour. If the saving throw fails by 5 or more, the target is also [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)\
    \ while [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ in this way. The target wakes up if it takes damage or if another creature takes\
    \ an action to shake it awake."
  "name": "Blowgun"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/lemurfolk-tob1-2023.webp"
```
^statblock

## Environment

forest