---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fiend/devil
statblock: inline
aliases: ["Gilded Devil"]
---
# [Gilded Devil](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fiend/gilded-devil-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 95*  

*This tall, bronze-complexioned man is abnormally long-limbed and clad in armor of stained and battered coins. His wiry frame is festooned with mismatched bracelets, rings, and necklaces, each gaudier than the last.*

## Servants of Mammon

Rarely seen in their natural form outside of Hell, gilded devils are the servitors of the devil‑god Mammon, Lord of Greed. They tempt and corrupt with promises of wealth and power, twisting mortal greed into sure damnation.

## Impression of Wisdom

When pursuing a mortal of high standing, gilded devils prefer unassuming appearances, molding their flesh and gaudy trappings to make themselves look the parts of wise advisers, canny merchants, or sly confidants. Even in their humblest form, gilded devils always wear a piece of golden jewelry or a jeweled button or ornament.

```statblock
"name": "Gilded Devil (ToB1-2023)"
"size": "Medium"
"type": "fiend"
"subtype": "devil"
"alignment": "Lawful Evil"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "112"
"hit_dice": "15d8 + 45"
"stats":
- !!int "20"
- !!int "15"
- !!int "17"
- !!int "15"
- !!int "18"
- !!int "17"
"speed": "30 ft."
"saves":
  "Charisma": !!int "6"
  "Wisdom": !!int "7"
  "Constitution": !!int "6"
"skillsaves":
  "Sleight of Hand": !!int "5"
  "Deception": !!int "9"
  "Insight": !!int "7"
  "History": !!int "5"
  "Persuasion": !!int "9"
"damage_resistances": "cold; bludgeoning, piercing, slashing from nonmagical attacks\
  \ that aren't silvered"
"damage_immunities": "fire, poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 14"
"languages": "Celestial, Common, Draconic, Infernal, telepathy 120 ft."
"cr": "7"
"traits":
- "desc": "The gilded devil casts one of the following spells, requiring no material\
    \ components and using Wisdom as the spellcasting ability (spell save DC 15):\n\
    \nAt will: [alter self](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/alter-self.md),\
    \ [detect thoughts](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/detect-thoughts.md),\
    \ [suggestion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/suggestion.md)\n\
    \n3/day each: [charm person](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/charm-person.md),\
    \ [scrying](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/scrying.md)"
  "name": "Spellcasting"
- "desc": "Magical darkness doesn't impede the gilded devil's darkvision."
  "name": "Devil's Sight"
- "desc": "The gilded devil's Golden Flail attacks are magical. When the devil hits\
    \ with the Golden Flail, the flail deals an extra 4d6 fire damage (included\
    \ in the attack). In addition, the devil can transform the flail into gold jewelry\
    \ or back into a weapon as a bonus action."
  "name": "Golden Flail"
- "desc": "If a creature accepts a gift of jewelry from the gilded devil, the creature\
    \ becomes cursed until cured by a [remove curse](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/remove-curse.md)\
    \ spell or similar magic. While cursed, the creature has disadvantage on saving\
    \ throws against the devil's spells and abilities."
  "name": "Liar's Largesse"
- "desc": "The gilded devil has advantage on saving throws against spells and other\
    \ magical effects."
  "name": "Magic Resistance"
"actions":
- "desc": "The gilded devil makes two Golden Flail attacks or three Hurl Flame attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 10\
    \ (1d10 + 5) bludgeoning damage plus 14 (4d6) fire damage."
  "name": "Golden Flail"
- "desc": "Ranged Spell Attack: +7 to hit, range 120 ft., one target. Hit: 14\
    \ (3d6 + 4) fire damage."
  "name": "Hurl Flame"
- "desc": "The gilded devil magically teleports, along with any equipment it is wearing\
    \ or carrying, up to 120 feet to an unoccupied space it can see."
  "name": "Teleport (Recharge 4-6)"
- "desc": "The gilded devil magically consumes up to 1 cubic foot of nonmagical jewelry\
    \ or coins made of precious material within 5 feet of it. It regains 5 hp for\
    \ every 200 gp of the consumed objects' value. If the jewelry or coins are being\
    \ worn or carried by a creature, that creature must succeed on a DC 15 Dexterity\
    \ saving throw to prevent the consumption."
  "name": "Voracious Greed"
"bonus_actions":
- "desc": "One creature wearing jewelry (an object made of precious material and worth\
    \ at least 100 gp) the gilded devil can see within 60 feet of it must make a DC\
    \ 15 Wisdom saving throw. On a failure, the target takes 13 (3d8) bludgeoning\
    \ damage and suffers an effect until it finishes a short rest. The effect is based\
    \ on the location of the worn jewelry (devil's choice if worn in multiple locations):\
    \ on upper limbs, its melee damage is halved; on lower limbs, its speed is halved;\
    \ on head, it is [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ or [deafened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Deafened)\
    \ (devil's choice); on body, it has vulnerability to bludgeoning damage. On a\
    \ success, the target takes half the damage and doesn't suffer an additional effect."
  "name": "Betrayal of Riches (Recharge 4-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fiend/token/gilded-devil-tob1-2023.webp"
```
^statblock

## Environment

planar, urban