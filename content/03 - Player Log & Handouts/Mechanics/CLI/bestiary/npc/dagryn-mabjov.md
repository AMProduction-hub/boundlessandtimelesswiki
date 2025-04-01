---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/mabjov
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/dwarf
statblock: inline
aliases: ["Dagryn"]
---
# [Dagryn](03 - Player Log & Handouts\Mechanics\CLI\bestiary\npc/dagryn-mabjov.md)
*Source: Minsc and Boo's Journal of Villainy p. 110*  

> [!quote] A quote from Volo  
> 
> I've long pursued the story of the dwarf who could change into a dragon. That Minsc and his ridiculous pet could track him down first is infuriating!

Dagryn appears as an old, stooped dwarf, crippled with age and afflictions. Long ago, however, he went by another name... and another form.

Originally, Dagryn was a powerful black dragon that hunted the Underdark, feasting on everything from beholders to drow to illithid. But he was particularly fond of dwarves, whom he considered a delicacy. Supremely arrogant, Dagryn believe no denizens of the Underdark could challenge his power, until he had the misfortune of angering a coven of hags.

The hags trapped and killed the great wyrm, but instead of leaving him for dead, they reincarnated him in the form of a dwarf—a twisted joke on the once fearsome creature. In a final mockery of his former glory, they branded him with the name Dagryn—a bastardized echo of the mighty beast he once had been. Dagryn has now lived so many years as a dwarf that the memories of his life before the reincarnation have mostly faded. In addition to forgetting his true name, he no longer remembers his origin world, though he knows that Faerûn is not where he was born.

In the early years after his transformation, Dagryn discovered another cruel quirk of the hag's curse. After several years his wretched existence as a lowly dwarf became unbearable, and Dagryn was driven to suicide. But upon his death, he woke to discover his body had been restored to its original dragon form. However, his joy was short lived—after 24 hours he once again shifted back into his dwarven shape... but now he had a malformed leg, giving him a painful limp.

Over the next decades, the true scope of the horror inflicted upon him became apparent. Each time his dwarven body was killed, he would be reborn as a dragon for a single day. And each time he turned back into a dwarf he would find himself afflicted with some new infirmity: arthritic joints; rotting teeth; punishing migraines; constant ulcers.

Dagryn now dreads adding new ailments to the relentless, crippling pain of his dwarven body. Whenever he is killed—a somewhat frequent occurrence, as a frail, old dwarf is an easy target—he spends his time as a dragon unleashing mad vengeance upon the world in an orgy of death, destruction, and mayhem. As a result, he has developed two very distinct and contrasting personalities: the timid, subservient dwarf and the raging, hate-filled dragon.

```statblock
"name": "Dagryn (MaBJoV)"
"size": "Medium"
"type": "humanoid"
"subtype": "dwarf"
"alignment": "Neutral Evil"
"ac": !!int "19"
"ac_class": "[splint](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/splint-armor.md),\
  \ [shield](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/shield.md)"
"hp": !!int "84"
"hit_dice": "13d8 + 26"
"stats":
- !!int "12"
- !!int "8"
- !!int "14"
- !!int "14"
- !!int "13"
- !!int "17"
"speed": "20 ft."
"skillsaves":
  "Deception": !!int "5"
  "Performance": !!int "5"
  "Persuasion": !!int "5"
"damage_resistances": "poison"
"damage_immunities": "acid"
"senses": "darkvision 120 ft., passive Perception 11"
"languages": "Common, Draconic, Dwarvish, Undercommon"
"cr": "4"
"traits":
- "desc": "Dagryn casts one of the following spells, requiring no material components\
    \ and using Charisma as the spellcasting ability (spell save DC 13):\n\nAt will:\
    \ [alter self](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/alter-self.md),\
    \ [disguise self](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/disguise-self.md),\
    \ [levitate](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/levitate.md),\
    \ [major image](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/major-image.md),\
    \ [vicious mockery](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/vicious-mockery.md)\n\
    \n1/day each: [dimension door](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dimension-door.md),\
    \ [seeming](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/seeming.md)\n\
    \n2/day each: [bane](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/bane.md),\
    \ [fear](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/fear.md), [hold\
    \ monster](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/hold-monster.md),\
    \ [misty step](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/misty-step.md)"
  "name": "Spellcasting"
- "desc": "When Dagryn drops to 0 hit points, instead of falling [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious),\
    \ he transforms into his dragon form. He immediately gains all the statistics\
    \ of an [adult black dragon](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/dragon/adult-black-dragon.md)\
    \ with the exception that his size is Medium, and has the [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)\
    \ condition. At the start of his next turn, he grows to Large size, but remains\
    \ [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned).\
    \ At the start of his subsequent turn, Dagryn grows to Huge size and is no longer\
    \ [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned).\
    \ Dagryn remains in his dragon form for 24 hours whereupon he reverts to this\
    \ stat block."
  "name": "Draconic Transformation"
- "desc": "Dagryn has advantage on saving throws against poison, spells, and illusions,\
    \ as well as to resist being [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ or [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)."
  "name": "Dwarven Resilience"
"actions":
- "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4\
    \ + 1) bludgeoning damage."
  "name": "Club"
- "desc": "Ranged Spell Attack: +5 to hit, range 120 ft., one target. Hit: 14\
    \ (2d10 + 3) acid damage."
  "name": "Eruption"
"bonus_actions":
- "desc": "Dagryn magically turns [invisible](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Invisible)\
    \ for 1 hour or until he attacks or casts a spell. Any equipment Dagryn wears\
    \ or carries turns [invisible](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Invisible)\
    \ with him."
  "name": "Invisibility (Recharges after a Short or Long Rest)"
"source":
- "MaBJoV"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/npc/token/dagryn-mabjov.webp"
```
^statblock