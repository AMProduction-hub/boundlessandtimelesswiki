---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/fleemortals
- ttrpg-cli/monster/cr/
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/aberration/companion
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Otyugh Companion"
---
# [Otyugh Companion](03.PlayerLog&Handouts/Mechanics/CLI/bestiary/aberration/otyugh-companion-fleemortals.md)
*Source: Flee, Mortals! p. 217*  

```statblock
"name": "Otyugh Companion (FleeMortals)"
"size": "Large"
"type": "aberration"
"subtype": "Companion"
"alignment": "Unaligned"
"ac_class": "14 plus PB (natural armor)"
"modifier": !!int "1"
"stats":
  - !!int "16"
  - !!int "12"
  - !!int "15"
  - !!int "6"
  - !!int "13"
  - !!int "6"
"speed": "45 ft."
"saves":
  - "name": "Constitution"
    "desc": "+2 plus PB"
"skillsaves":
  - "name": "[Athletics](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Athletics)"
    "desc": "+3 plus PB"
  - "name": "[Survival](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Survival)"
    "desc": "+1 plus PB"
"damage_resistances": "acid, poison"
"condition_immunities": "[poisoned](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "[darkvision](03.PlayerLog&Handouts/Mechanics/CLI/rules/senses.md#Darkvision)\
  \ 60 ft., passive Perception 11"
"languages": ""
"traits":
  - "desc": "The otyugh ignores difficult terrain. They have advantage on Dexterity\
      \ ([Stealth](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Stealth)) checks\
      \ made to hide in piles of refuse."
    "name": "Trash Traversal"
"actions":
  - "desc": "*Melee Weapon Attack:* +3 plus PB to hit, reach 5 ft., one target.\
      \ *Hit:* 1d6 plus PB piercing damage."
    "name": "Signature Attack (Bite)"
  - "desc": "The otyugh makes a signature attack. On a hit, the target must also succeed\
      \ on a DC 10 plus PB Strength saving throw or be [grappled](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
      \ (escape DC 10 plus PB). The otyugh can only grapple one target at a time."
    "name": "1st Level: Tentacle Slam (2 Ferocity)"
  - "desc": "The otyugh moves up to their speed without provoking opportunity attacks.\
      \ During or after this move, they can make a signature attack against one target."
    "name": "3rd Level: Brutal Charge (5 Ferocity)"
  - "desc": "The otyugh regurgitates garbage in a 15-foot cone. Each creature in that\
      \ area must make a DC 10 plus PB Constitution saving throw. On a failed save,\
      \ a creature takes PBd6 poison damage and is [poisoned](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Poisoned).\
      \ On a successful save, a creature takes half as much damage and isn't [poisoned](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)."
    "name": "5th Level: Retch (8 Ferocity)"
"bonus_actions":
  - "desc": "The otyugh touches their caregiver and ends one disease or one of the\
      \ following conditions affecting the caregiver: [blinded](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
      \ [dazed](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Dazed), [deafened](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Deafened),\
      \ [paralyzed](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
      \ or [poisoned](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)."
    "name": "Slough Rot (Recharges after a Long Rest)"
"source":
  - "FleeMortals"
"image": "03.PlayerLog&Handouts/Mechanics/CLI/bestiary/aberration/token/otyugh-companion-fleemortals.png"
```
^statblock