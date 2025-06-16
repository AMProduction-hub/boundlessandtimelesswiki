---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/mm
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/arctic
- ttrpg-cli/monster/environment/coastal
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/environment/mountain
- ttrpg-cli/monster/environment/swamp
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/any-race
statblock: inline
statblock-link: "#^statblock"
aliases:
- Druid
---
# [Druid](03.PlayerLog&Handouts\Mechanics\CLI\bestiary\humanoid/druid.md)
*Source: Monster Manual p. 346, Curse of Strahd, Princes of the Apocalypse, Storm King's Thunder, Tomb of Annihilation, Ghosts of Saltmarsh, Dragon of Icespire Peak, Sleeping Dragon's Wake, Baldur's Gate: Descent Into Avernus, Explorer's Guide to Wildemount, Mythic Odysseys of Theros, Icewind Dale: Rime of the Frostmaiden, Candlekeep Mysteries, Journeys through the Radiant Citadel. Available in the <span title='Systems Reference Document (5.1)'>SRD</span>*  

Druids dwell in forests and other secluded wilderness locations, where they protect the natural world from monsters and the encroachment of civilization. Some are tribal shamans who heal the sick, pray to animal spirits, and provide spiritual guidance.

```statblock
"name": "Druid"
"size": "Medium"
"type": "humanoid"
"subtype": "any race"
"alignment": "Any alignment"
"ac": !!int "11"
"ac_class": "16 with [barkskin](03.PlayerLog&Handouts/Mechanics/CLI/spells/barkskin.md)"
"hp": !!int "27"
"hit_dice": "5d8 + 5"
"modifier": !!int "1"
"stats":
  - !!int "10"
  - !!int "12"
  - !!int "13"
  - !!int "12"
  - !!int "15"
  - !!int "11"
"speed": "30 ft."
"skillsaves":
  - "name": "[Medicine](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Medicine)"
    "desc": "+4"
  - "name": "[Nature](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Nature)"
    "desc": "+3"
  - "name": "[Perception](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Perception)"
    "desc": "+4"
"senses": "passive Perception 14"
"languages": "Druidic plus any two languages"
"cr": "2"
"traits":
  - "desc": "The druid is a 4th-level spellcaster. Its spellcasting ability is Wisdom\
      \ (spell save DC 12, +4 to hit with spell attacks). It has the following druid\
      \ spells prepared:\n\nCantrips (at will): [druidcraft](03.PlayerLog&Handouts/Mechanics/CLI/spells/druidcraft.md),\
      \ [produce flame](03.PlayerLog&Handouts/Mechanics/CLI/spells/produce-flame.md),\
      \ [shillelagh](03.PlayerLog&Handouts/Mechanics/CLI/spells/shillelagh.md)\n\n\
      1st level (4 slots): [entangle](03.PlayerLog&Handouts/Mechanics/CLI/spells/entangle.md),\
      \ [longstrider](03.PlayerLog&Handouts/Mechanics/CLI/spells/longstrider.md),\
      \ [speak with animals](03.PlayerLog&Handouts/Mechanics/CLI/spells/speak-with-animals.md),\
      \ [thunderwave](03.PlayerLog&Handouts/Mechanics/CLI/spells/thunderwave.md)\n\
      \n2nd level (3 slots): [animal messenger](03.PlayerLog&Handouts/Mechanics/CLI/spells/animal-messenger.md),\
      \ [barkskin](03.PlayerLog&Handouts/Mechanics/CLI/spells/barkskin.md)"
    "name": "Spellcasting"
"actions":
  - "desc": "Melee Weapon Attack: +2 to hit (+4 to hit with shillelagh), reach\
      \ 5 ft., one target. Hit: 3 (d6) bludgeoning damage, 4 (d8) bludgeoning\
      \ damage if wielded with two hands, or 6 (1d8 + 2) bludgeoning damage with\
      \ [shillelagh](03.PlayerLog&Handouts/Mechanics/CLI/spells/shillelagh.md)."
    "name": "Quarterstaff"
"source":
  - "MM"
  - "CoS"
  - "PotA"
  - "SKT"
  - "ToA"
  - "GoS"
  - "DIP"
  - "SDW"
  - "BGDIA"
  - "EGW"
  - "MOT"
  - "IDRotF"
  - "CM"
  - "JttRC"
"image": "03.PlayerLog&Handouts/Mechanics/CLI/bestiary/humanoid/token/druid.webp"
```
^statblock

## Environment

coastal, mountain, grassland, hill, arctic, forest, swamp, underdark, desert