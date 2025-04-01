---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/plant
statblock: inline
aliases: ["Citrullus"]
---
# [Citrullus](03 - Player Log & Handouts\Mechanics\CLI\bestiary\plant/citrullus-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 58*  

*The humble melon plant slowly rises up, its striped melon splitting to reveal a maw of teeth and a gullet full of seed-filled, oozing fruit flesh.*

The citrullus is a carnivorous plant that has adapted to mimic the guise of ordinary melons. When attacking, the creature's toothy mouth reveals its horrible, juicy gullet. During the first stage of its life, the citrullus grows from sunlight, water, and the nutrients from decaying animals and plants. Once it reaches a few feet in size, these elements are no longer enough to sustain its hunger for growth, and it turns to living prey.

## Pest Control

The first citrullus was created by a wizard with a keen interest in magical gardening. This wizard discovered that as her garden grew lush with enchanted fruits and vegetables, local wildlife began eating the magical plants before she could harvest them. Over time, she created a fruit that would defend itself and the other plants against these pets. Her creation was such a success, that she eventually fell prey to its ravenous hunger. As the citrullus's flowers bloomed and withered, it spread its seeds far and wide. Some daring farmers still use this tactic today—but with far more caution.

## Juicy Demise

Unlike many sentient plants, which use vines to trap prey, the citrullus has a sticker solution. It can spew an adhesive, seed-filled fluid at creatures it considers to be an easy meal. Once a creature is trapped, the seeds sprout small creepers that drag the creature back to the maw of the citrullus. Many people believe that eating the seeds of the citrullus causes the plant to grow in the stomach of the consumer, but this rumor has been debunked by alchemists who use the seeds to craft antacid cocktails for upset stomachs and potions of acid resistance.

```statblock
"name": "Citrullus (ToB1-2023)"
"size": "Medium"
"type": "plant"
"alignment": "Unaligned"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "85"
"hit_dice": "10d10 + 30"
"stats":
- !!int "18"
- !!int "8"
- !!int "16"
- !!int "3"
- !!int "10"
- !!int "1"
"speed": "15 ft."
"damage_vulnerabilities": "bludgeoning"
"damage_immunities": "acid"
"senses": "blindsight 30 ft., passive Perception 10"
"languages": ""
"cr": "3"
"traits":
- "desc": "While the citrullus remains motionless, it is indistinguishable from a\
    \ normal melon plant."
  "name": "False Appearance"
- "desc": "When the citrullus takes bludgeoning damage, sticky juice splashes out\
    \ of it. If the attacker is within 30 feet of the citrullus, the attacker must\
    \ succeed on a DC 13 Dexterity saving throw or be [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ by the sticky juice as if it had failed a saving throw against the plant's Bile\
    \ Spray action."
  "name": "Gush"
"actions":
- "desc": "Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 18\
    \ (4d6 + 4) piercing damage plus 7 (2d6) acid damage."
  "name": "Bite"
- "desc": "The citrullus exhales pink bile in a 30-foot cone. Each creature in that\
    \ area must make a DC 13 Dexterity saving throw. On a failure, the creature takes\
    \ 14 (4d6) acid damage and is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ by the sticky seed-filled juice for 1 minute. On a success, the creature takes\
    \ half the damage and isn't [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained).\
    \ A creature, including the [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ creature, can take its action to free the [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ creature by succeeding on a DC 13 Strength check."
  "name": "Bile Spray (Recharge 5-6)"
"bonus_actions":
- "desc": "The seeds in the sticky juice grow viny tendrils and drag each creature\
    \ [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ by Bile Spray and Gush up to 25 feet straight toward the citrullus."
  "name": "Creeping Seedlings"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/plant/token/citrullus-tob1-2023.webp"
```
^statblock

## Environment

desert, forest, hill