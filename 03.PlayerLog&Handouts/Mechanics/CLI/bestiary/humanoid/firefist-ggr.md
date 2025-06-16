---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/ggr
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/any-race
statblock: inline
statblock-link: "#^statblock"
aliases:
- Firefist
---
# [Firefist](03.PlayerLog&Handouts\Mechanics\CLI\bestiary\humanoid/firefist-ggr.md)
*Source: Guildmasters' Guide to Ravnica p. 231*  

Boros firefists combine potent magic with peerless fighting ability, inspiring all who serve alongside them. They often act as the point of contact between the Boros Legion and the angelic leaders.

```statblock
"name": "Firefist (GGR)"
"size": "Medium"
"type": "humanoid"
"subtype": "any race"
"alignment": "Lawful Good"
"ac": !!int "18"
"ac_class": "[plate armor](03.PlayerLog&Handouts/Mechanics/CLI/items/plate-armor.md)"
"hp": !!int "117"
"hit_dice": "18d8 + 36"
"modifier": !!int "0"
"stats":
  - !!int "16"
  - !!int "10"
  - !!int "14"
  - !!int "11"
  - !!int "17"
  - !!int "13"
"speed": "30 ft."
"saves":
  - "constitution": "+5"
  - "wisdom": "+6"
"skillsaves":
  - "name": "[Intimidation](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Intimidation)"
    "desc": "+4"
  - "name": "[Religion](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Religion)"
    "desc": "+3"
"senses": "passive Perception 13"
"languages": "any one language (usually Common)"
"cr": "7"
"traits":
  - "desc": "The firefist is a 9th-level Boros spellcaster. Its spellcasting ability\
      \ is Wisdom (spell save DC 14, +6 to hit with spell attacks). It has the following\
      \ cleric spells prepared:\n\nCantrips (at will): [fire bolt](03.PlayerLog&Handouts/Mechanics/CLI/spells/fire-bolt.md),\
      \ [light](03.PlayerLog&Handouts/Mechanics/CLI/spells/light.md), [sacred flame](03.PlayerLog&Handouts/Mechanics/CLI/spells/sacred-flame.md),\
      \ [spare the dying](03.PlayerLog&Handouts/Mechanics/CLI/spells/spare-the-dying.md)\n\
      \n1st level (4 slots): [guiding bolt](03.PlayerLog&Handouts/Mechanics/CLI/spells/guiding-bolt.md),\
      \ [healing word](03.PlayerLog&Handouts/Mechanics/CLI/spells/healing-word.md),\
      \ [heroism](03.PlayerLog&Handouts/Mechanics/CLI/spells/heroism.md), [shield\
      \ of faith](03.PlayerLog&Handouts/Mechanics/CLI/spells/shield-of-faith.md)\n\
      \n2nd level (3 slots): [lesser restoration](03.PlayerLog&Handouts/Mechanics/CLI/spells/lesser-restoration.md),\
      \ [scorching ray](03.PlayerLog&Handouts/Mechanics/CLI/spells/scorching-ray.md)\n\
      \n3rd level (3 slots): [blinding smite](03.PlayerLog&Handouts/Mechanics/CLI/spells/blinding-smite.md),\
      \ [crusader's mantle](03.PlayerLog&Handouts/Mechanics/CLI/spells/crusaders-mantle.md),\
      \ [revivify](03.PlayerLog&Handouts/Mechanics/CLI/spells/revivify.md)\n\n4th\
      \ level (3 slots): [banishment](03.PlayerLog&Handouts/Mechanics/CLI/spells/banishment.md),\
      \ [wall of fire](03.PlayerLog&Handouts/Mechanics/CLI/spells/wall-of-fire.md)\n\
      \n5th level (1 slots): [flame strike](03.PlayerLog&Handouts/Mechanics/CLI/spells/flame-strike.md)"
    "name": "Spellcasting"
"actions":
  - "desc": "The firefist makes two greatsword attacks."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 10\
      \ (2d6 + 3) slashing damage."
    "name": "Greatsword"
"reactions":
  - "desc": "When the firefist or one creature it can see within 30 feet of it makes\
      \ an attack roll, the firefist grants a +10 bonus to that roll."
    "name": "Guided Attack (Recharges after a Short or Long Rest)"
"source":
  - "GGR"
"image": "03.PlayerLog&Handouts/Mechanics/CLI/bestiary/humanoid/token/firefist-ggr.webp"
```
^statblock