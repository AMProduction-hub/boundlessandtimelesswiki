---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["White Ape"]
---
# [White Ape](03 - Player Log & Handouts\Mechanics\CLI\bestiary\monstrosity/white-ape-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 396*  

*This hulking primate looms over others of its kind. Its filthy white fur is matted and yellowed, and a deranged look haunts its blood-red eyes.*

## Awakened by Sorcery

White apes were once docile, gentle giants that roamed forested hills and savannah lands. Two thousand years ago, a kingdom of mages awakened the apes and employed them as soldiers and servants, protecting and replacing the mages who were slowly dying of an unknown disease. When the mages died out, the apes remained.

## Arcane Wasting

The enchantment that imbued the apes with intelligence also bleached their fur white and made them carriers of the arcane wasting disease that hastened their creators' demise. The apes are immune to the wasting's effects, but they can pass it to humanoids. Among spellcasters, the wasting spreads like a plague.

## Driven Away

Their long relationship with the ancient mages built in the white apes a culture of communal knowledge and protection. This drives many white ape tribes to seek partnerships and companionship with nearby humanoid settlements. Unfortunately, their carrying of the arcane wasting disease leaves many humanoids terrified of them, viciously driving away the apes. They are acutely aware of the injustice that was done to them, and generations of exile have turned their desire for companionship to animosity, especially toward the spellcasters that are so susceptible to the disease they carry.

```statblock
"name": "White Ape (ToB1-2023)"
"size": "Large"
"type": "monstrosity"
"alignment": "Neutral"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "114"
"hit_dice": "12d10 + 48"
"stats":
- !!int "18"
- !!int "16"
- !!int "18"
- !!int "8"
- !!int "14"
- !!int "8"
"speed": "40 ft., climb 40 ft."
"skillsaves":
  "Intimidation": !!int "5"
  "Athletics": !!int "7"
  "Perception": !!int "5"
"senses": "darkvision 60 ft., passive Perception 15"
"languages": "Common"
"cr": "6"
"traits":
- "desc": "If the white ape sees a creature cast a spell, the ape has advantage on\
    \ attack rolls against that creature on the ape's next turn."
  "name": "Spellcasting Animosity"
- "desc": "Characterized by the slow mental deterioration it causes, arcane wasting\
    \ is a disease that infects Humanoids and spreads through spellcasting. A creature\
    \ infected with this disease manifests symptoms 1d4 days after infection, which\
    \ include brain fog and difficulty recalling memories. Until the disease is cured,\
    \ at the end of each long rest, the infected creature must succeed on a DC 15\
    \ Constitution saving throw or its Intelligence and Wisdom scores are each reduced\
    \ by 1d2. This reduction lasts until the creature finishes a long rest after\
    \ the disease is cured. If the disease reduces a creature's Intelligence or Wisdom\
    \ to 0, the creature dies. If the infected creature casts a spell on a Humanoid\
    \ before the disease is cured, and the Humanoid is hit by the spell or fails the\
    \ saving throw, that Humanoid must succeed on a DC 15 Constitution saving throw\
    \ or also become infected with the arcane wasting disease."
  "name": "Arcane Wasting"
- "desc": "The white ape has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
"actions":
- "desc": "The white ape makes one Bite attack and two Fist attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 13\
    \ (2d8 + 4) piercing damage, and the target must succeed on a DC 15 Constitution\
    \ saving throw or contract the arcane wasting disease (see the Arcane Wasting\
    \ trait)."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 15\
    \ (2d10 + 4) bludgeoning damage."
  "name": "Fist"
- "desc": "The white ape lashes out wildly at nearby creatures, flailing and biting.\
    \ Each creature within 10 feet of the white ape must make a DC 15 Dexterity saving\
    \ throw. On a failure, a creature takes 35 (10d6) bludgeoning damage and is\
    \ pushed up to 10 feet away from the ape. On a success, a creature takes half\
    \ the damage and isn't pushed. A creature that succeeds on this saving throw also\
    \ has advantage on attack rolls against the white ape until the end of its next\
    \ turn."
  "name": "Frenzy (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/monstrosity/token/white-ape-tob1-2023.webp"
```
^statblock

## Environment

forest, grassland, hill