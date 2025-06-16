---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/gos
- ttrpg-cli/monster/cr/10
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/aberration
statblock: inline
statblock-link: "#^statblock"
aliases:
- Mr. Dory
---
# [Mr. Dory](03.PlayerLog&Handouts\Mechanics\CLI\bestiary\npc/mr-dory-gos.md)
*Source: Ghosts of Saltmarsh p. 246*  

One of the four councillors who rule the Styes, Mr. Dory hides his cursed nature in plain sight. His rare, liquid-sensitive "skin condition" is actually a form of the same aboleth affliction that creates skum, though Dory's condition is not as severe, and he has managed to retain his free will.

```statblock
"name": "Mr. Dory (GoS)"
"size": "Medium"
"type": "aberration"
"alignment": "Chaotic Evil"
"ac": !!int "18"
"ac_class": "[studded leather](03.PlayerLog&Handouts/Mechanics/CLI/items/studded-leather-armor.md),\
  \ [shield](03.PlayerLog&Handouts/Mechanics/CLI/items/shield.md)"
"hp": !!int "170"
"hit_dice": "20d8 + 80"
"modifier": !!int "5"
"stats":
  - !!int "13"
  - !!int "20"
  - !!int "19"
  - !!int "14"
  - !!int "14"
  - !!int "16"
"speed": "30 ft."
"saves":
  - "constitution": "+8"
  - "wisdom": "+6"
"skillsaves":
  - "name": "[Athletics](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Athletics)"
    "desc": "+5"
  - "name": "[Perception](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Perception)"
    "desc": "+6"
  - "name": "[Stealth](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Stealth)"
    "desc": "+9"
"damage_immunities": "necrotic"
"senses": "darkvision 60 ft., passive Perception 16"
"languages": "Abyssal, Common, Deep Speech, telepathy 60 ft."
"cr": "10"
"traits":
  - "desc": "Mr. Dory's innate spellcasting ability is Charisma (save DC 15, +7\
      \ to hit with spell attacks). Mr. Dory can innately cast the following spells,\
      \ requiring no material components:\n\nAt will: [detect magic](03.PlayerLog&Handouts/Mechanics/CLI/spells/detect-magic.md),\
      \ [detect thoughts](03.PlayerLog&Handouts/Mechanics/CLI/spells/detect-thoughts.md),\
      \ [invisibility](03.PlayerLog&Handouts/Mechanics/CLI/spells/invisibility.md)\
      \ (self only)\n\n2/day each: [fear](03.PlayerLog&Handouts/Mechanics/CLI/spells/fear.md),\
      \ [fireball](03.PlayerLog&Handouts/Mechanics/CLI/spells/fireball.md), [fly](03.PlayerLog&Handouts/Mechanics/CLI/spells/fly.md)\n\
      \n1/day each: [cloudkill](03.PlayerLog&Handouts/Mechanics/CLI/spells/cloudkill.md),\
      \ [etherealness](03.PlayerLog&Handouts/Mechanics/CLI/spells/etherealness.md)"
    "name": "Innate Spellcasting"
  - "desc": "Mr. Dory has advantage on saving throws against spells and other magical\
      \ effects."
    "name": "Magic Resistance"
  - "desc": "Mr. Dory takes 6 (d12) acid damage at the end of every hour he goes\
      \ without exposure to water."
    "name": "Water Dependency"
"actions":
  - "desc": "Mr. Dory makes three attacks with his rapier."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 9\
      \ (1d8 + 5) piercing damage and 7 (2d6) necrotic damage."
    "name": "Rapier"
  - "desc": "Mr. Dory glares at a creature he can see within 30 feet of him. The target\
      \ must make a DC 15 Constitution saving throw. On a failed save, it takes 27\
      \ (5d10) necrotic damage and 27 (5d10) poison damage and then gains vulnerability\
      \ to both necrotic and poison damage for 1 minute. On a successful save, it\
      \ takes half damage and does not gain the vulnerabilities."
    "name": "Eye of Corruption (Recharge 5-6)"
"source":
  - "GoS"
"image": "03.PlayerLog&Handouts/Mechanics/CLI/bestiary/npc/token/mr-dory-gos.webp"
```
^statblock