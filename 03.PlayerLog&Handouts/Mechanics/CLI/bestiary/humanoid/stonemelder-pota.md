---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/pota
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/human
statblock: inline
statblock-link: "#^statblock"
aliases:
- Stonemelder
---
# [Stonemelder](03.PlayerLog&Handouts\Mechanics\CLI\bestiary\humanoid/stonemelder-pota.md)
*Source: Princes of the Apocalypse p. 197*  

Stonemelders are spellcasters who gain their power from Ogrémoch, using elemental earth magic to sheathe their bodies in carapaces of rock. They are elite champions of the cult and answer only to the cult leaders. Not even the Black Earth priests tell stonemelders what to do.

Each stonemelder carries a weapon known as a Black Earth rod. Such a rod is like an ordinary mace, but in the hands of a stonemelder, it serves as a conduit for Ogrémoch's wrath.

```statblock
"name": "Stonemelder (PotA)"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Neutral Evil"
"ac": !!int "17"
"ac_class": "[splint armor](03.PlayerLog&Handouts/Mechanics/CLI/items/splint-armor.md)"
"hp": !!int "75"
"hit_dice": "10d8 + 30"
"modifier": !!int "0"
"stats":
  - !!int "15"
  - !!int "10"
  - !!int "16"
  - !!int "12"
  - !!int "11"
  - !!int "17"
"speed": "30 ft."
"skillsaves":
  - "name": "[Intimidation](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Intimidation)"
    "desc": "+5"
  - "name": "[Perception](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Perception)"
    "desc": "+2"
"senses": "tremorsense 30 ft., passive Perception 12"
"languages": "Common, Terran"
"cr": "4"
"traits":
  - "desc": "The Stonemelder is a 7th-level spellcaster. Its spellcasting ability\
      \ is Charisma (spell save DC 13, +5 to hit with spell attacks). It knows the\
      \ following sorcerer spells:\n\nCantrips (at will): [acid splash](03.PlayerLog&Handouts/Mechanics/CLI/spells/acid-splash.md),\
      \ [blade ward](03.PlayerLog&Handouts/Mechanics/CLI/spells/blade-ward.md), [light](03.PlayerLog&Handouts/Mechanics/CLI/spells/light.md),\
      \ [mending](03.PlayerLog&Handouts/Mechanics/CLI/spells/mending.md), [mold earth](03.PlayerLog&Handouts/Mechanics/CLI/spells/mold-earth-xge.md)\n\
      \n1st level (4 slots): [expeditious retreat](03.PlayerLog&Handouts/Mechanics/CLI/spells/expeditious-retreat.md),\
      \ [false life](03.PlayerLog&Handouts/Mechanics/CLI/spells/false-life.md), [shield](03.PlayerLog&Handouts/Mechanics/CLI/spells/shield.md)\n\
      \n2nd level (3 slots): [Maximilian's earthen grasp](03.PlayerLog&Handouts/Mechanics/CLI/spells/maximilians-earthen-grasp-xge.md),\
      \ [shatter](03.PlayerLog&Handouts/Mechanics/CLI/spells/shatter.md)\n\n3rd\
      \ level (3 slots): [erupting earth](03.PlayerLog&Handouts/Mechanics/CLI/spells/erupting-earth-xge.md),\
      \ [meld into stone](03.PlayerLog&Handouts/Mechanics/CLI/spells/meld-into-stone.md)\n\
      \n4th level (1 slots): [stoneskin](03.PlayerLog&Handouts/Mechanics/CLI/spells/stoneskin.md)"
    "name": "Spellcasting"
  - "desc": "When the Stonemelder dies, it turns to stone and explodes in a burst\
      \ of rock shards, becoming a smoking pile of rubble. Each creature within 10\
      \ feet of the exploding Stonemelder must make a DC 14 Dexterity saving throw,\
      \ taking 11 (2d10) bludgeoning damage on a failed save, or half as much damage\
      \ on a successful one."
    "name": "Death Burst"
"actions":
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5\
      \ (1d6 + 2) bludgeoning damage. The Stonemelder can also expend a spell slot\
      \ to deal extra damage, dealing 2d8 bludgeoning damage for a 1st level slot,\
      \ plus an additional d8 for each level of the slot above 1st."
    "name": "Black Earth Rod"
"source":
  - "PotA"
"image": "03.PlayerLog&Handouts/Mechanics/CLI/bestiary/humanoid/token/stonemelder-pota.webp"
```
^statblock