---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1-4
- ttrpg-cli/monster/environment/farmland
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Clurichaun"]
---
# [Clurichaun](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/clurichaun-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 66*  

*Around a corner in the wine cellar stumbles a tiny, surly man carrying an open bottle of wine. He has a bushy beard and wears a rumpled, red overcoat over a dirty white shirt and knee-length red trousers with blue stockings and silver-buckled shoes. A cap made from leaves stitched together with gold thread slouches atop his head, and he reeks of stale beer and wine*.

## Drunks in the Cellar

Clurichauns are mean-spirited, alcohol-loving fey that plague butteries and wine cellars. These drunken fey were once leprechauns, but they long ago forsook a life of toil for one of solitary debauchery. Now they spend every night drinking, warbling off-key, and tormenting their hapless hosts with cruel pranks. However, if the clurichaun's host keeps him or her well supplied with a favorite libation and otherwise leaves him or her alone, the clurichaun protects their wine cellars from thieves, drunkards, or worse—becoming quite vigorous when they feel the security of the cellars is threatened in any way. They have a particular hatred for rum gremlins and for other clurichauns.

## Contest Evictions

Most people can't tolerate or afford a clurichaun's presence for long. Unfortunately, attempts to drive them off usually result in the spiteful clurichaun going on a destructive rampage and spoiling any remaining wine. The best way to evict a clurichaun is to challenge him or her to a drinking contest. A clurichaun can't abide losing to a mortal and if defeated by one, slinks away in shame, never to be seen again. This is a risky option, because clurichauns can drink prodigiously with little ill effect.

## Small Brawlers

While clurichauns aren't averse to an old-fashioned tavern brawl, they rely mainly on their magic to protect themselves. Creatures under a clurichaun's spell feel and act as if they were intoxicated, complete with hangovers the next morning!

```statblock
"name": "Clurichaun (ToB1-2023)"
"size": "Tiny"
"type": "fey"
"alignment": "Chaotic Neutral"
"ac": !!int "14"
"ac_class": "clurichaun's luck"
"hp": !!int "22"
"hit_dice": "4d4 + 12"
"stats":
- !!int "13"
- !!int "12"
- !!int "16"
- !!int "10"
- !!int "8"
- !!int "16"
"speed": "30 ft."
"saves":
  "Constitution": !!int "5"
"skillsaves":
  "Stealth": !!int "3"
  "Perception": !!int "1"
"condition_immunities": "[frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 11"
"languages": "Common, Elvish, Sylvan"
"cr": "1/4"
"traits":
- "desc": "The clurichaun casts one of the following spells, requiring alcohol as\
    \ the only material component and using Charisma as the spellcasting ability (spell\
    \ save DC 13):\n\nAt will: [mending](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/mending.md),\
    \ [purify food and drink](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/purify-food-and-drink.md)\n\
    \n1/day each: [blur](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/blur.md),\
    \ [heroism](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/heroism.md),\
    \ [suggestion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/suggestion.md)"
  "name": "Spellcasting"
- "desc": "While the clurichaun is conscious and wearing no armor and wielding no\
    \ shield, it adds its Charisma modifier to its AC (included above)."
  "name": "Clurichaun's Luck"
- "desc": "The clurichaun has advantage on saving throws against spells and other\
    \ magical effects."
  "name": "Magic Resistance"
"actions":
- "desc": "Melee or Ranged Weapon Attack: +3 to hit, reach 5 ft. or range 20/60\
    \ ft., one target. Hit: 3 (1d4 + 1)bludgeoning, 3 (1d4 + 1)piercing, or\
    \ 3 (1d4 + 1)slashing damage, depending on the weapon."
  "name": "Improvised Weapon"
- "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4\
    \ + 1) bludgeoning damage."
  "name": "Slam"
- "desc": "Ranged Spell Attack: +5 to hit, range 30 ft., one creature. Hit:\
    \ 5 (1d4 + 3) psychic damage, and the target must succeed on a DC 13 Wisdom\
    \ saving throw or be [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ until the end of its next turn as it doubles over in laughter or freezes up\
    \ in embarrassment (the target's choice)."
  "name": "Bawdy Remark"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/clurichaun-tob1-2023.webp"
```
^statblock

## Environment

farmland, urban