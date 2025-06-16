---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/mm
- ttrpg-cli/monster/cr/1-8
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/any-race
statblock: inline
statblock-link: "#^statblock"
aliases:
- Noble
---
# [Noble](03.PlayerLog&Handouts\Mechanics\CLI\bestiary\humanoid/noble.md)
*Source: Monster Manual p. 348, Curse of Strahd, Princes of the Apocalypse, Storm King's Thunder, Tales from the Yawning Portal, Tomb of Annihilation, Waterdeep: Dragon Heist, Waterdeep: Dungeon of the Mad Mage, Ghosts of Saltmarsh, Divine Contention, Dragon of Icespire Peak, Baldur's Gate: Descent Into Avernus, Eberron: Rising from the Last War, Infernal Machine Rebuild, Explorer's Guide to Wildemount, Mythic Odysseys of Theros, Icewind Dale: Rime of the Frostmaiden, Candlekeep Mysteries, Journeys through the Radiant Citadel, Dragonlance: Shadow of the Dragon Queen, Keys from the Golden Vault. Available in the <span title='Systems Reference Document (5.1)'>SRD</span>*  

Nobles wield great authority and influence as members of the upper class, possessing wealth and connections that can make them as powerful as monarchs and generals. A noble often travels in the company of guards, as well as servants who are commoners.

The noble's statistics can also be used to represent courtiers who aren't of noble birth.

```statblock
"name": "Noble"
"size": "Medium"
"type": "humanoid"
"subtype": "any race"
"alignment": "Any alignment"
"ac": !!int "15"
"ac_class": "[breastplate](03.PlayerLog&Handouts/Mechanics/CLI/items/breastplate.md)"
"hp": !!int "9"
"hit_dice": "2d8"
"modifier": !!int "1"
"stats":
  - !!int "11"
  - !!int "12"
  - !!int "11"
  - !!int "12"
  - !!int "14"
  - !!int "16"
"speed": "30 ft."
"skillsaves":
  - "name": "[Deception](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Deception)"
    "desc": "+5"
  - "name": "[Insight](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Insight)"
    "desc": "+4"
  - "name": "[Persuasion](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Persuasion)"
    "desc": "+5"
"senses": "passive Perception 12"
"languages": "any two languages"
"cr": "1/8"
"actions":
  - "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 5\
      \ (1d8 + 1) piercing damage."
    "name": "Rapier"
"reactions":
  - "desc": "The noble adds 2 to its AC against one melee attack that would hit it.\
      \ To do so, the noble must see the attacker and be wielding a melee weapon."
    "name": "Parry"
"source":
  - "MM"
  - "CoS"
  - "PotA"
  - "SKT"
  - "TftYP"
  - "ToA"
  - "WDH"
  - "WDMM"
  - "GoS"
  - "DC"
  - "DIP"
  - "BGDIA"
  - "ERLW"
  - "IMR"
  - "EGW"
  - "MOT"
  - "IDRotF"
  - "CM"
  - "JttRC"
  - "DSotDQ"
  - "KftGV"
"image": "03.PlayerLog&Handouts/Mechanics/CLI/bestiary/humanoid/token/noble.webp"
```
^statblock

## Environment

urban