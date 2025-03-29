---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/14
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/construct
statblock: inline
aliases: ["Ushabti Royal Guard"]
---
# [Ushabti Royal Guard](03 - Player Log & Handouts\Mechanics\CLI\bestiary\construct/ushabti-royal-guard-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 377*  

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
"name": "Ushabti Royal Guard (ToB1-2023)"
"size": "Large"
"type": "construct"
"alignment": "Unaligned"
"ac": !!int "19"
"ac_class": "natural armor"
"hp": !!int "168"
"hit_dice": "16d10 + 80"
"stats":
- !!int "22"
- !!int "16"
- !!int "20"
- !!int "11"
- !!int "19"
- !!int "9"
"speed": "30 ft."
"saves":
  "Charisma": !!int "4"
  "Wisdom": !!int "9"
"skillsaves":
  "Perception": !!int "9"
  "History": !!int "5"
  "Arcana": !!int "5"
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "poison, psychic"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 19"
"languages": "understands the languages of its creator but can't speak"
"cr": "14"
"traits":
- "desc": "The ushabti doesn't require air, food, drink, or sleep."
  "name": "Construct Nature"
- "desc": "While the ushabti is motionless, it is indistinguishable from a normal\
    \ funerary statue."
  "name": "False Appearance"
- "desc": "If a creature within 30 feet of the ushabti regains hp from a spell or\
    \ magical effect, the creature regains only half the amount and the ushabti regains\
    \ the other half."
  "name": "Healing Leech"
- "desc": "The ushabti is immune to any spell or effect that would alter its form."
  "name": "Immutable Form"
- "desc": "If the ushabti fails a saving throw, it can choose to succeed instead."
  "name": "Legendary Resistance (3/Day)"
- "desc": "The ushabti has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "The ushabti's weapon attacks are magical. When the ushabti hits with any\
    \ weapon, the weapon deals an extra (2d8) necrotic damage (included in the attack)."
  "name": "Necrotic Weapons"
"actions":
- "desc": "The ushabti can use its Breath-Stealing Presence. It then makes two Khopesh\
    \ attacks and one Medjai's Scepter attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 13\
    \ (2d6 + 6) slashing damage plus 9 (2d8) necrotic damage."
  "name": "Khopesh"
- "desc": "Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 15\
    \ (2d8 + 6) bludgeoning damage plus 9 (2d8) necrotic damage."
  "name": "Medjai's Scepter"
- "desc": "Each creature of the ushabti's choice within 30 feet of the ushabti and\
    \ aware of it must succeed on a DC 18 Constitution saving throw or take 9 (2d8)\
    \ necrotic damage and be unable to speak or breathe for 1 minute. A creature can\
    \ repeat the saving throw at the end of each of its turns, ending the effect on\
    \ itself on a success. If a creature's saving throw is successful or the effect\
    \ ends for it, the creature is immune to the ushabti's Breath‑Stealing Presence\
    \ for the next 24 hours."
  "name": "Breath-Stealing Presence"
- "desc": "The ushabti emits waves of necrotic energy. Each creature within 30 feet\
    \ of the ushabti must make a DC 18 Constitution saving throw, taking 49 (11d8)\
    \ necrotic damage on a failed save, or half as much damage on a successful one.\
    \ A creature that can't breathe because of the ushabti's Breath‑Stealing Presence\
    \ has disadvantage on the saving throw. If the saving throw fails by 5 or more,\
    \ the creature also suffers one level of [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion).\
    \ A Humanoid slain by this effect rises 1d4 hours later as a mummy under the\
    \ ushabti's control, unless the Humanoid is restored to life or its body is destroyed.\
    \ The ushabti can have no more than five mummies under its control at one time."
  "name": "Enervating Surge (Recharge 5-6)"
"reactions":
- "desc": "When a creature more than 5 feet away from the ushabti moves to a space\
    \ within 5 feet of the ushabti, the ushabti can make one Khopesh attack against\
    \ it."
  "name": "Sudden Strike"
"legendary_actions":
- "desc": "The ushabti moves up to its speed without provoking opportunity attacks."
  "name": "Move"
- "desc": "The ushabti makes one Medjai's Scepter attack."
  "name": "Medjai's Scepter (Costs 2 Actions)"
- "desc": "Up to two creatures the ushabti can see within 60 feet of it must succeed\
    \ on a DC 18 Strength saving throw or the ushabti moves the creature up to 30\
    \ feet in any direction (including upward). A moved target is then [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ until the start of the ushabti's next turn."
  "name": "Telekinesis (Costs 2 Actions)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/construct/token/ushabti-royal-guard-tob1-2023.webp"
```
^statblock

## Environment

desert, underdark, urban