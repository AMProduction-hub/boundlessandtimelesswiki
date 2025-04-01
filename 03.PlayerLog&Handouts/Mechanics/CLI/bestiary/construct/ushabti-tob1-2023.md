---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/8
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/construct
statblock: inline
aliases: ["Ushabti"]
---
# [Ushabti](03 - Player Log & Handouts\Mechanics\CLI\bestiary\construct/ushabti-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 376*  

*The eye sockets of the funerary figure's ornate death mask suddenly ignite with a golden radiance. With the creak of long-unused limbs, this towering figure in ancient armor raises its weapons once more.*

Ushabtis are placed in tombs as servants in the afterlife for those buried there—as both a laborer in the kingdom of the dead and a guardian in the kingdom of the living. These sentinels tend to the physical work and maintenance required after death that is beyond the abilities of those of flesh and blood. Dressed in ceremonial regalia, they are sometimes mistaken for living beings by those who would intrude upon their domain, but careful examination reveals faintly glowing hieroglyphs graven into their garments and bodies.

## Tomb Guardians

Ushabtis are most commonly encountered as guardians—a function they fulfill effectively, fiercely attacking anything that threatens their sworn charge. An ushabti is sometimes obvious from the blood of its victims staining its form. Some ceaselessly babble ancient scriptures or invocations to the gods of death. Tombs are often littered with bones of tomb robbers an ushabti has dispatched.

## Serene Repose

Most ushabtis have human faces and proportions, with features resembling a death mask. When at rest, they stand or lie with arms folded across their chests, clutching their ceremonial weapons. Many variations have been found, however, including some that are animal-headed, completely monstrous, or have abstract or fanciful designs, such as a sun-sphere head or a body made of papyrus scrolls.

## Sacrificial Corruptions

Some dark practitioners use sacrifices—willing or not—as undying servants of their godkings and god-queens. Generals, trusted advisors, and close allies have willingly accompanied their dying lords into the afterlife through this horrifying transformation. The sacrifices are tightly bound in linens and sealed within a sarcophagus among a swarm of flesh-eating scarabs that, over a period of days to weeks, fully consume their bodies. The servant's devotion to their task and the anguish of their passing transforms the scarab colony and animates the funerary wrappings to carry on with the sacred duty. Most view this as a corruption of the process for creating ushabtis, reducing the time and cost of construction with blood and resulting in a weaker, uncontrollable guardian. Though a corrupted ushabti fulfills its duties to protect its dead charges, it views living creatures as meals for the scarab colony within its wrappings, regardless of that creature's identity.

> [!note] Ushabti in Midgard
> 
> In Midgard, ushabtis are common in the Southlands as funerary figures. Originally gifted to his faithful by the wise god Eshu—whether this was truly as a gift or as trickery depends on the scholar telling the tale—these constructs gained near universal usage among the priests of other faiths. In Nuria Natal, they take on many more utilitarian roles for the living, not being confined to merely serving the dead, such as by protecting travelers and offerings at roadside shrines and as bodyguards and servants for the living god‑kings and other important figures.
> 
> Of note, a corrupted ushabti is viewed with some esteem in Nuria Natal, assuming the sacrifice was willing. These ushabti are sometimes called imy-ut ushabtis.
^ushabti-in-midgard

```statblock
"name": "Ushabti (ToB1-2023)"
"size": "Medium"
"type": "construct"
"alignment": "Unaligned"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "119"
"hit_dice": "14d8 + 56"
"stats":
- !!int "14"
- !!int "20"
- !!int "18"
- !!int "6"
- !!int "11"
- !!int "6"
"speed": "40 ft."
"saves":
  "Charisma": !!int "1"
  "Wisdom": !!int "3"
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "poison, psychic"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 10"
"languages": "understands the languages of its creator but can't speak"
"cr": "8"
"traits":
- "desc": "The ushabti doesn't require air, food, drink, or sleep."
  "name": "Construct Nature"
- "desc": "While the ushabti is motionless, it is indistinguishable from a normal\
    \ funerary statue."
  "name": "False Appearance"
- "desc": "The ushabti is immune to spells and effects that would alter its form."
  "name": "Immutable Form"
- "desc": "The ushabti has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "The ushabti's weapon attacks are magical. When the ushabti hits with any\
    \ weapon, the weapon deals an extra (3d8) necrotic damage (included in the attack)."
  "name": "Necrotic Weapons"
"actions":
- "desc": "The ushabti makes two Nabboot attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 12\
    \ (2d6 + 5) bludgeoning damage plus 13 (3d8) necrotic damage. If the target\
    \ is a creature, it must succeed on a DC 16 Constitution saving throw or be cursed\
    \ with tomb taint. The cursed target's speed is halved, and its hp maximum decreases\
    \ by 3 (1d6) for every 24 hours that elapse. If the curse reduces the target's\
    \ hp maximum to 0, the target dies, and its body turns to dust. The curse lasts\
    \ until removed by the [remove curse](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/remove-curse.md)\
    \ spell or comparable magic."
  "name": "Nabboot"
- "desc": "The ushabti commands its armlets to drop to the floor and transform into\
    \ two giant, poisonous snakes. The snakes act as allies of the ushabti and obey\
    \ its spoken commands. The snakes remain for 1 hour, until the ushabti dies, or\
    \ until the ushabti dismisses one or both of them as a bonus action. When the\
    \ snakes disappear, they become wisps of smoke and reform as armlets around the\
    \ ushabti's arms."
  "name": "Serpentine Armlets (1/Day)"
"reactions":
- "desc": "One creature the ushabti can see within 60 feet of it must succeed on a\
    \ DC 16 Strength saving throw or the ushabti moves the creature up to 30 feet\
    \ in any direction (including upward). The target is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ until the start of the ushabti's next turn."
  "name": "Telekinesis"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/construct/token/ushabti-tob1-2023.webp"
```
^statblock

## Environment

desert, underdark, urban