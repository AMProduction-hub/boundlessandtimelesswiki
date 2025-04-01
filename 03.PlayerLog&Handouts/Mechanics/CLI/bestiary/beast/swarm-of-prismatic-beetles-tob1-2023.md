---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Swarm of Prismatic Beetles"]
---
# [Swarm of Prismatic Beetles](03 - Player Log & Handouts\Mechanics\CLI\bestiary\beast/swarm-of-prismatic-beetles-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 356*  

*A dazzling explosion of multicolored lights erupts from this cloud of flying beetles, flashing every color of the rainbow.*

## Flesh-Eating Beauties

The depths of the jungle are filled with beautiful-but-lethal wildlife, and prismatic beetles are superlative examples of this. These flesh-eating, venomous insects distract and subdue their prey with sparkling beauty even as they devour it alive. Individual prismatic beetles sparkle like precious gems in the light. Tosculi traders, gnolls, and humans often incorporate their carapaces into decorative jewelry or use them as special components in enchantment and illusion spells and items.

## Hypno-Paralytic

When swarming in the thousands, these beautiful bugs create a hypnotic cascade of glimmering hues capable of enthralling creatures. As they descend on their dazed prey, the beetles' bites slowly paralyze their victims while their toxins distract the mind with feelings of euphoria and delight.

## Predator Partners

Although carnivorous, prismatic beetles are not overly aggressive; they attack other creatures only when hungry or threatened. Even when they're not attacking, however, they can be a threat. More than one unwary traveler has stopped to admire what they thought was a docile swarm of prismatic beetles and became captivated. The unfortunates are often killed and eaten by a lurking jungle predator, as such animals know the beetles can attract prey.

```statblock
"name": "Swarm of Prismatic Beetles (ToB1-2023)"
"size": "Medium"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "13"
"hp": !!int "60"
"hit_dice": "11d8 + 11"
"stats":
- !!int "3"
- !!int "16"
- !!int "12"
- !!int "1"
- !!int "13"
- !!int "2"
"speed": "20 ft., burrow 5 ft., fly 30 ft."
"skillsaves":
  "Stealth": !!int "5"
  "Perception": !!int "3"
"damage_resistances": "bludgeoning, piercing, slashing"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
  \ [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
  \ [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)"
"senses": "blindsight 10 ft., darkvision 30 ft., passive Perception 13"
"languages": ""
"cr": "3"
"traits":
- "desc": "When a creature that can see the swarm starts its turn within 30 feet of\
    \ the swarm and the swarm is in bright or dim light, the swarm can force the creature\
    \ to make a DC 13 Wisdom saving throw if the swarm isn't [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ and can see the creature. If the saving throw fails by 5 or more, the creature\
    \ falls [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious).\
    \ Otherwise, a creature that fails the save is [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ and its speed is reduced to 0 until the start of its next turn, as it remains\
    \ transfixed in place by the glitter of the swarm. A creature has advantage on\
    \ the saving throw if the swarm is in dim light. Unless surprised, a creature\
    \ can avert its eyes to avoid the saving throw at the start of its turn. If the\
    \ creature does so, it can't see the swarm until the start of its next turn, when\
    \ it can avert its eyes again. If the creature looks at the swarm in the meantime,\
    \ it must immediately make the save."
  "name": "Glittering Carapace"
- "desc": "The swarm can occupy another creature's space and vice versa, and the swarm\
    \ can move through any opening large enough for a Tiny insect. The swarm can't\
    \ regain hp or gain temporary hp."
  "name": "Swarm"
"actions":
- "desc": "Melee Weapon Attack: +5 to hit, reach 0 ft., one creature in the swarm's\
    \ space. Hit: 14 (4d6) piercing damage, or 7 (2d6) piercing damage if the\
    \ swarm has half of its hp or fewer. The target must make a DC 13 Constitution\
    \ saving throw. On a failure, a creature takes 10 (4d4) poison damage and is\
    \ euphoric for 1 minute. On a success, a creature takes half the damage and isn't\
    \ euphoric. A euphoric creature has disadvantage on saving throws. The creature\
    \ can repeat the saving throw at the end of each of its turns, ending the effect\
    \ on itself on a success."
  "name": "Bites"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/beast/token/swarm-of-prismatic-beetles-tob1-2023.webp"
```
^statblock

## Environment

forest