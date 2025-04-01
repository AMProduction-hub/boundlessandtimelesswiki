---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/aberration
statblock: inline
aliases: ["Spider of Leng"]
---
# [Spider of Leng](03 - Player Log & Handouts\Mechanics\CLI\bestiary\aberration/spider-of-leng-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 341*  

*These bloated purple spiders have small claws on their front legs that serve as handlike manipulators. Their abdomens are a sickly purple-white.*

## Hate Humanoids

The nefarious spiders of Leng are highly intelligent. They are a very ancient people, steeped in evil lore and hideous malice, with an abiding hatred for all humanoid races. They sometimes keep ghostwalk spiders as guardians or soldiers.

## Dangerous Blood

Their blood is poisonous and corrosive to most creatures native to the Material Plane. The folk of Leng prize it in the making of etheric harpoons and enchanted nets.

```statblock
"name": "Spider of Leng (ToB1-2023)"
"size": "Large"
"type": "aberration"
"alignment": "Chaotic Evil"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "144"
"hit_dice": "17d10 + 51"
"stats":
- !!int "14"
- !!int "16"
- !!int "16"
- !!int "18"
- !!int "10"
- !!int "10"
"speed": "30 ft., climb 20 ft."
"saves":
  "Dexterity": !!int "6"
  "Intelligence": !!int "7"
  "Constitution": !!int "6"
"skillsaves":
  "Athletics": !!int "5"
  "Stealth": !!int "6"
  "Perception": !!int "3"
"damage_immunities": "poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)"
"senses": "darkvision 240 ft., passive Perception 13"
"languages": "Common, Void Speech"
"cr": "7"
"traits":
- "desc": "The spider of Leng casts one of the following spells, requiring no material\
    \ components and using Intelligence as the spellcasting ability (spell save DC\
    \ 15):\n\nAt will: [comprehend languages](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/comprehend-languages.md),\
    \ [detect magic](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/detect-magic.md)\n\
    \n1/day each: [arcane eye](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/arcane-eye.md),\
    \ [hypnotic pattern](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/hypnotic-pattern.md)\n\
    \n3/day each: [confusion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/confusion.md),\
    \ [silence](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/silence.md)"
  "name": "Spellcasting"
- "desc": "The spider of Leng can read and use any spell scroll or magic item, ignoring\
    \ all class, race, and level requirements."
  "name": "Eldritch Understanding"
- "desc": "A creature that hits the spider of Leng with a melee attack while within\
    \ 5 feet of it takes 4 (1d8) poison damage."
  "name": "Poisonous Blood"
- "desc": "When the spider of Leng dies, the poisonous blood in its body vaporizes,\
    \ forming a cloud in the spider's space until initiative count 20 on the next\
    \ round. Each creature within 5 feet of the spider and each creature that enters\
    \ the cloud for the first time on a turn must make a DC 15 Constitution saving\
    \ throw, taking 9 (2d8) poison damage on a failed save, or half as much damage\
    \ on a successful one."
  "name": "Poisonous Death"
"actions":
- "desc": "The spider of Leng makes two Claw attacks and one Staff of Leng attack,\
    \ or it makes three Spit Venom attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 12\
    \ (2d8 + 3) slashing damage plus 4 (1d8) poison damage."
  "name": "Claw"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7 (1d6\
    \ + 3) bludgeoning damage plus 7 (2d6) psychic damage, and the target must\
    \ succeed on a DC 15 Wisdom saving throw or be [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)\
    \ until the end of is next turn."
  "name": "Staff of Leng"
- "desc": "Ranged Weapon Attack: +6 to hit, range 20/60 ft., one target. Hit:\
    \ 16 (3d8 + 3) poison damage, and the target must succeed on a DC 15 Constitution\
    \ saving throw or be [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ and [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ until the end of its next turn."
  "name": "Spit Venom"
"reactions":
- "desc": "The spider of Leng adds 3 to its AC against one melee attack that would\
    \ hit it. To do so, the spider must see the attacker. If this effect causes the\
    \ attack to miss, the attacker takes 4 (1d8) poison damage."
  "name": "Poisonous Riposte"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/aberration/token/spider-of-leng-tob1-2023.webp"
```
^statblock

## Environment

planar