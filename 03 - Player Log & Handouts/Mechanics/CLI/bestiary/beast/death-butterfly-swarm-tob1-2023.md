---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/farmland
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Death Butterfly Swarm"]
---
# [Death Butterfly Swarm](03 - Player Log & Handouts\Mechanics\CLI\bestiary\beast/death-butterfly-swarm-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 70*  

*Enormous clouds of orange and green butterflies add a reek of putrefaction to the air, stirred by the flapping of delicate wings.*

## Demon-Haunted

A death butterfly swarm results when a rare breed of carrion-eating butterfly, drawn en masse to the stench of decay, feeds on the corpse of a fiend, demon, or similar creature.

## Dizzying and Poisonous

The colorful, chaotic flapping of the insects' wings blinds and staggers those in its path, allowing the swarm to necrotize flesh from those it overruns. Attracted to rotting material, the swarm spreads a fast-acting, poison on its victims, creating carrion it can feed on immediately.

## Devour the Undead

Undead creatures are not immune to a death butterfly swarm's poison. A swarm can rot an undead creature's animating energies as easily as those of the living. Given the choice between an undead and living creature, a death butterfly swarm always attacks the undead, finding ghouls and vampires particularly appealing. Some good-aligned forces regard summoning these swarms as a necessary evil.

```statblock
"name": "Death Butterfly Swarm (ToB1-2023)"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "60"
"hit_dice": "11d10"
"stats":
- !!int "1"
- !!int "14"
- !!int "10"
- !!int "1"
- !!int "12"
- !!int "12"
"speed": "5 ft., fly 40 ft. (hover)"
"damage_vulnerabilities": "cold, fire"
"damage_resistances": "bludgeoning, piercing, slashing"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
  \ [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
  \ [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)"
"senses": "darkvision 60 ft., passive Perception 11"
"languages": ""
"cr": "4"
"traits":
- "desc": "Undead with resistance or immunity to poison damage or the [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ condition can be affected by the swarm's poison."
  "name": "Potent Poison"
- "desc": "The swarm can occupy another creature's space and vice versa, and the swarm\
    \ can move through any opening large enough for a Tiny insect. The swarm can't\
    \ regain hp or gain temporary hp."
  "name": "Swarm"
- "desc": "A creature that starts its turn in the swarm's space has its speed halved\
    \ and must succeed on a DC 12 Dexterity saving throw or become [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded).\
    \ Both effects end when the creature ends its turn outside the swarm's space.\
    \ On a successful saving throw, the creature is immune to the blinding effect\
    \ of Weight of Wings for the next 24 hours."
  "name": "Weight of Wings"
"actions":
- "desc": "Melee Weapon Attack: +4 to hit, reach 0 ft., one creature in the swarm's\
    \ space. Hit: 21 (6d6) piercing damage, or 10 (3d6) piercing damage if the\
    \ swarm has half of its hp or fewer. The target must make a DC 12 Constitution\
    \ saving throw. On a failure, it takes 10 (3d6) poison damage and is [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ until the end of its next turn. On a success, it takes half the damage and isn't\
    \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)."
  "name": "Bites"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/beast/token/death-butterfly-swarm-tob1-2023.webp"
```
^statblock

## Environment

farmland, forest, urban