---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Corrupted Ushabti"]
---
# [Corrupted Ushabti](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/corrupted-ushabti-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 375*  

*The eye sockets of the funerary figure's ornate death mask suddenly ignite with a golden radiance. With the creak of long-unused limbs, this towering figure in ancient armor raises its weapons once more.*Ushabtis are placed in tombs as servants in the afterlife for those buried there—as both a laborer in the kingdom of the dead and a guardian in the kingdom of the living. These sentinels tend to the physical work and maintenance required after death that is beyond the abilities of those of flesh and blood. Dressed in ceremonial regalia, they are sometimes mistaken for living beings by those who would intrude upon their domain, but careful examination reveals faintly glowing hieroglyphs graven into their garments and bodies.

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
"name": "Corrupted Ushabti (ToB1-2023)"
"size": "Medium"
"type": "undead"
"alignment": "Neutral Evil"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "97"
"hit_dice": "15d8 + 30"
"stats":
- !!int "17"
- !!int "14"
- !!int "15"
- !!int "6"
- !!int "10"
- !!int "5"
"speed": "30 ft."
"saves":
  "Charisma": !!int "0"
  "Wisdom": !!int "3"
"damage_vulnerabilities": "fire"
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "necrotic, poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)"
"senses": "darkvision 60 ft., passive Perception 10"
"languages": "understands Common but can't speak"
"cr": "5"
"traits":
- "desc": "The ushabti's weapon attacks are magical. When the ushabti hits with any\
    \ weapon, the weapon deals an extra (2d6) necrotic damage (included in the attack)."
  "name": "Necrotic Weapons"
- "desc": "The ushabti regains 5 hp at the start of its turn if it has at least 1\
    \ hp."
  "name": "Regeneration"
- "desc": "The corrupted ushabti is a spirit inhabiting a colony of scarabs around\
    \ a Humanoid skeleton within funerary wrappings. It can move through any opening\
    \ large enough for a Tiny scarab and Humanoid bones, and it can't regain hp or\
    \ gain temporary hp, except for its Regeneration trait. In addition, a creature\
    \ that hits the ushabti with a melee attack while within 5 feet of it takes 2\
    \ (1d4) piercing damage as a dozen Tiny scarabs skitter out and bite the attacker."
  "name": "Swarm Body"
- "desc": "The ushabti doesn't require air, food, drink, or sleep."
  "name": "Undead Nature"
"actions":
- "desc": "The corrupted ushabti makes two Ceremonial Greatsword attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one creature. Hit: 11\
    \ (2d6 + 3) slashing damage plus 7 (2d6) necrotic damage."
  "name": "Ceremonial Greatsword"
- "desc": "The corrupted ushabti exhales scarabs in a 30-foot cone. Each creature\
    \ in the area must make a DC 15 Dexterity saving throw. On a failure, a creature\
    \ takes 25 (10d4) piercing damage and is covered in scarabs. On a success, a\
    \ creature takes half the damage and isn't covered in scarabs. A creature covered\
    \ in scarabs takes 2 (1d4) piercing damage at the start of each of its turns.\
    \ A creature, including the covered creature, can take its action to brush the\
    \ scarabs off the covered creature by succeeding on a DC 15 Dexterity check."
  "name": "Vomit Swarm (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/corrupted-ushabti-tob1-2023.webp"
```
^statblock

## Environment

desert, underdark, urban