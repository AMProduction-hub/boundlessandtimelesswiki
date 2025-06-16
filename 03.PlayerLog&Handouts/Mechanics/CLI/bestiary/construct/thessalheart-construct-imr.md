---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/imr
- ttrpg-cli/monster/cr/0
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/construct
statblock: inline
statblock-link: "#^statblock"
aliases:
- Thessalheart Construct
---
# [Thessalheart Construct](03.PlayerLog&Handouts\Mechanics\CLI\bestiary\construct/thessalheart-construct-imr.md)
*Source: Infernal Machine Rebuild p. 86*  

A thessalheart construct is created with a connection to the life energy of another creature, allowing that creature to regenerate back from the dead as long as the construct is not destroyed. The artificer Thessalar created this crafty construct, and uses it to imbue his greater monstrous creations with even more power.

```statblock
"name": "Thessalheart Construct (IMR)"
"size": "Tiny"
"type": "construct"
"alignment": "Neutral"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "7"
"hit_dice": "2d4 + 2"
"modifier": !!int "2"
"stats":
  - !!int "4"
  - !!int "15"
  - !!int "12"
  - !!int "10"
  - !!int "10"
  - !!int "7"
"speed": "40 ft., climb 40 ft."
"damage_immunities": "poison"
"condition_immunities": "[charmed](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [poisoned](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60, passive Perception 10"
"languages": "understands the languages of its creator but can't speak"
"cr": "0"
"traits":
  - "desc": "While the construct is on the same plane of existence as its master,\
      \ it can magically convey what it senses to its master, and the two can communicate\
      \ telepathically."
    "name": "Telepathic Bond"
"actions":
  - "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 1\
      \ slashing damage, and the target must succeed on a DC 10 Constitution saving\
      \ throw or be [poisoned](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
      \ for 1 minute. If the saving throw fails by 5 or more, the target is instead\
      \ [poisoned](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
      \ for 5 (d10) minutes and [unconscious](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)\
      \ while [poisoned](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
      \ in this way."
    "name": "Claws"
"source":
  - "IMR"
"image": "03.PlayerLog&Handouts/Mechanics/CLI/bestiary/construct/token/thessalheart-construct-imr.webp"
```
^statblock