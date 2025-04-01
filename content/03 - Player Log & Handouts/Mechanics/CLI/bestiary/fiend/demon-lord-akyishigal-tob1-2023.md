---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/12
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/fiend/demon
statblock: inline
aliases: ["Demon Lord Akyishigal"]
---
# [Demon Lord Akyishigal](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fiend/demon-lord-akyishigal-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 74*  

*This insectoid creature's filth-slicked mandibles clack ceaselessly for flesh.*

Of all the demons lurking in the Abyss, few are as vile and disgusting as Akyishigal, the Lord of Cockroaches.

## Civilization's Corruption

Although Akyishigal sired an entire race in his image, known as roachlings, he craves followers among humans, elves, and other races as a means of corrupting civilization and rotting it from within. Despite his repulsiveness, Akyishigal has followers among the urban dispossessed, the slum-dwelling poor, and those who lurk in lightless undercities. His shrines are tended in abandoned houses, tanneries, and butcher yards, as well as in sewers and similar places.

## Filth Sacrifices

In his shrines, kidnapped victims find themselves submerged in filth up to their necks. While the demon lord's cultists chant, sacramental roaches feast on the prisoner's eyes and tongue. A victim who survives the rite is dumped back onto the streets.

## Persistent Cults

Akyishigal's cults are almost as difficult to stamp out as real cockroach infestations. No matter how they are driven off or crushed, followers resurface among the teeming mobs of the downtrodden. Typical worshipers include evil humanoids, particularly kobolds and goblins, as well as roachlings, minor demons, slaves, thralls, and shadow creatures of all stripes.

```statblock
"name": "Demon Lord Akyishigal (ToB1-2023)"
"size": "Large"
"type": "fiend"
"subtype": "demon"
"alignment": "Chaotic Evil"
"ac": !!int "18"
"ac_class": "natural armor"
"hp": !!int "138"
"hit_dice": "12d10 + 72"
"stats":
- !!int "21"
- !!int "17"
- !!int "22"
- !!int "19"
- !!int "14"
- !!int "20"
"speed": "40 ft., burrow 20 ft., climb 40 ft., fly 40 ft."
"saves":
  "Charisma": !!int "9"
  "Dexterity": !!int "7"
  "Wisdom": !!int "6"
  "Strength": !!int "9"
  "Constitution": !!int "10"
"skillsaves":
  "Athletics": !!int "9"
  "Stealth": !!int "7"
  "Perception": !!int "6"
  "Acrobatics": !!int "11"
"damage_resistances": "acid; fire; bludgeoning, piercing, slashing from nonmagical\
  \ attacks"
"damage_immunities": "cold, lightning, poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 120 ft., truesight 60 ft., passive Perception 16"
"languages": "Abyssal, Common, Draconic, Elvish, Infernal, telepathy 60 ft."
"cr": "12"
"traits":
- "desc": "Akyishigal casts one of the following spells, requiring no material components\
    \ and using Charisma as the spellcasting ability (spell save DC 17):\n\nAt will:\
    \ [detect evil and good](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/detect-evil-and-good.md),\
    \ [pass without trace](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/pass-without-trace.md)\n\
    \n1/day: [contagion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/contagion.md)\
    \ (filth fever only)\n\n3/day: [dispel magic](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dispel-magic.md),\
    \ [giant insect](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/giant-insect.md),\
    \ [insect plague](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/insect-plague.md)"
  "name": "Spellcasting"
- "desc": "Akyishigal emits a cloud of flying, stinging insects from his mouth, eyes,\
    \ and tears in his skin that spreads out in a 5-foot radius from him. At the start\
    \ of each of his turns, Akyishigal chooses whether this cloak is active.\n\nWhile\
    \ this cloak is active, Akyishigal has disadvantage on Dexterity ([Stealth](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Stealth))\
    \ checks, and creatures attacking Akyishigal can't benefit from traits and features\
    \ that rely on a creature's allies distracting or surrounding the demon, such\
    \ as the Pack Tactics trait or Sneak Attack feature. In addition, each creature\
    \ that isn't a Construct or Undead that starts its turn in the cloud takes 11\
    \ (2d10) piercing damage and must succeed on a DC 17 Constitution saving throw\
    \ or take 7 (2d6) poison damage and become [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 hour. While [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ in this way, a creature emits a stench of decomposition, and uncontrolled insects\
    \ attack that creature in preference to other targets."
  "name": "Cloak of Swarms"
- "desc": "If Akyishigal fails a saving throw, he can choose to succeed instead."
  "name": "Legendary Resistance (3/Day)"
- "desc": "Akyishigal has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
"actions":
- "desc": "Akyishigal makes four Claw attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 14\
    \ (2d8 + 5) slashing damage plus 3 (1d6) poison damage."
  "name": "Claw"
- "desc": "Akyishigal magically calls one spawn of Akyishigal. The spawn arrives in\
    \ 1d4 rounds, acting as an ally of Akyishigal and obeying its telepathic commands.\
    \ The spawn remains for 1 hour, until Akyishigal dies, or until Akyishigal dismisses\
    \ it as a bonus action."
  "name": "Call Spawn (1/Day)"
"bonus_actions":
- "desc": "Akyishigal magically transforms into a Large or smaller insectoid Beast\
    \ or back into his true form, which is a Fiend. His statistics, other than his\
    \ size, are the same in each form. Any equipment he is wearing or carrying transforms\
    \ with him. He reverts to his true form if he dies."
  "name": "Change Shape"
"legendary_actions":
- "desc": "Akyishigal magically teleports, along with any equipment he is wearing\
    \ or carrying, up to 120 feet to an unoccupied space he can see."
  "name": "Teleport"
- "desc": "Akyishigal moves up to half his speed and makes one Claw attack. This movement\
    \ doesn't provoke opportunity attacks."
  "name": "Skitter (Costs 2 Actions)"
- "desc": "Akyishigal uses Spellcasting."
  "name": "Cast a Spell (Costs 2 Actions)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fiend/token/demon-lord-akyishigal-tob1-2023.webp"
```
^statblock

## Environment

planar, urban