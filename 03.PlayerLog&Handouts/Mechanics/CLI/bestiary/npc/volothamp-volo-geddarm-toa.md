---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/toa
- ttrpg-cli/monster/cr/1-4
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/human
statblock: inline
statblock-link: "#^statblock"
aliases:
- Volothamp "Volo" Geddarm
---
# [Volothamp "Volo" Geddarm](03.PlayerLog&Handouts\Mechanics\CLI\bestiary\npc/volothamp-volo-geddarm-toa.md)
*Source: Tomb of Annihilation p. 235, Waterdeep: Dragon Heist*  

The bombastic world traveler Volothamp Geddarm has come to Chult to deliver signed copies of his latest book, Volo's Guide to Monsters. In addition to setting up audiences with the seven merchant princes of Port Nyanzaru (whom he knows well), Volo is visiting local taverns to promote his work, and the characters might meet him at some point in the city. Volo is a font of information (not all of it accurate), but he won't join the party under any circumstances. He might, however, allow the characters to tag along while he visits each merchant prince in turn.

The personable Volo is more than willing to share `1d4 + 1` rumors from the Jungle Rumors table at the end of chapter 1, which he's overheard since arriving in Port Nyanzaru.

## Volo's Traits

### Ideal

"I have no wish to explore jungles, lost cities, and dungeons. Friendly taverns and bawdy festhalls are more my style."

### Bond

"Planning an expedition? You really should buy a copy of my latest book, Volo's Guide to Monsters!"

### Flaw

"My penchant for indulgence and my propensity for mockery have earned me a few enemies. I tend to wear out my welcome."

```statblock
"name": "Volothamp \"Volo\" Geddarm (ToA)"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Chaotic Good"
"ac": !!int "11"
"hp": !!int "31"
"hit_dice": "7d8"
"modifier": !!int "1"
"stats":
  - !!int "9"
  - !!int "12"
  - !!int "10"
  - !!int "15"
  - !!int "11"
  - !!int "16"
"speed": "30 ft."
"saves":
  - "constitution": "+2"
  - "wisdom": "+2"
"skillsaves":
  - "name": "[Animal Handling](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Animal%20Handling)"
    "desc": "+4"
  - "name": "[Arcana](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Arcana)"
    "desc": "+4"
  - "name": "[Deception](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Deception)"
    "desc": "+5"
  - "name": "[History](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#History)"
    "desc": "+4"
  - "name": "[Insight](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Insight)"
    "desc": "+2"
  - "name": "[Investigation](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Investigation)"
    "desc": "+4"
  - "name": "[Perception](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Perception)"
    "desc": "+2"
  - "name": "[Performance](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Performance)"
    "desc": "+7"
  - "name": "[Persuasion](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Persuasion)"
    "desc": "+7"
  - "name": "[Sleight of Hand](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Sleight%20of%20Hand)"
    "desc": "+3"
  - "name": "[Survival](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Survival)"
    "desc": "+2"
"senses": "passive Perception 12"
"languages": "Common, Dwarvish, Elvish"
"cr": "1/4"
"traits":
  - "desc": "Volo is a 1st-level spellcaster. His spellcasting ability is Intelligence\
      \ (spell save DC 12, +4 to hit with spell attacks). He has the following wizard\
      \ spells prepared:\n\nCantrips (at will): [friends](03.PlayerLog&Handouts/Mechanics/CLI/spells/friends.md),\
      \ [mending](03.PlayerLog&Handouts/Mechanics/CLI/spells/mending.md), [prestidigitation](03.PlayerLog&Handouts/Mechanics/CLI/spells/prestidigitation.md)\n\
      \n1st level (2 slots): [comprehend languages](03.PlayerLog&Handouts/Mechanics/CLI/spells/comprehend-languages.md),\
      \ [detect magic](03.PlayerLog&Handouts/Mechanics/CLI/spells/detect-magic.md),\
      \ [disguise self](03.PlayerLog&Handouts/Mechanics/CLI/spells/disguise-self.md)"
    "name": "Spellcasting"
"actions":
  - "desc": "Melee  or Ranged Weapon Attack: +3 to hit, reach 5 ft. or range 20/60\
      \ ft., one target. Hit: 3 (1d4 + 1) piercing damage."
    "name": "Dagger"
"source":
  - "ToA"
  - "WDH"
"image": "03.PlayerLog&Handouts/Mechanics/CLI/bestiary/npc/token/volothamp-volo-geddarm-toa.webp"
```
^statblock