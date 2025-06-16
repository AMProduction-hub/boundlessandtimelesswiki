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
- Blood Witch
---
# [Blood Witch](03.PlayerLog&Handouts\Mechanics\CLI\bestiary\humanoid/blood-witch-ggr.md)
*Source: Guildmasters' Guide to Ravnica p. 248*  

Blood witches imagine themselves to be the intermediaries between Rakdos and his cult-the pinnacle of his priesthood, his trusted advisors, and the messengers who communicate his will to the scattered troupes and ringmasters. The Cult of Rakdos recognizes no authority but Rakdos, and the demon lord requires no advisors. Nonetheless, the blood witches are smart, charismatic, and powerful, so their voices do carry some weight.

Blood witches strive both to protect the cult from external interference and to punish those who bring harm to the guild. They claim grandiose titles, such as Tormentor of the Wojek, as a way of mocking their intended victims.

```statblock
"name": "Blood Witch (GGR)"
"size": "Medium"
"type": "humanoid"
"subtype": "any race"
"alignment": "Chaotic Evil"
"ac": !!int "12"
"ac_class": "15 with [mage armor](03.PlayerLog&Handouts/Mechanics/CLI/spells/mage-armor.md)"
"hp": !!int "78"
"hit_dice": "12d8 + 24"
"modifier": !!int "2"
"stats":
  - !!int "16"
  - !!int "14"
  - !!int "15"
  - !!int "13"
  - !!int "9"
  - !!int "19"
"speed": "30 ft."
"saves":
  - "wisdom": "+2"
  - "charisma": "+7"
"skillsaves":
  - "name": "[Arcana](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Arcana)"
    "desc": "+4"
  - "name": "[Intimidation](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Intimidation)"
    "desc": "+7"
  - "name": "[Perception](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Perception)"
    "desc": "+2"
  - "name": "[Stealth](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Stealth)"
    "desc": "+5"
"damage_resistances": "psychic"
"senses": "darkvision 120 ft., passive Perception 12"
"languages": "Abyssal plus any one language (usually Common)"
"cr": "7"
"traits":
  - "desc": "The witch's innate spellcasting ability is Charisma (spell save DC 15,\
      \ +7 to hit with spell attacks). The witch can innately cast the following\
      \ spells, requiring no material components:\n\nAt will: [alter self](03.PlayerLog&Handouts/Mechanics/CLI/spells/alter-self.md),\
      \ [detect magic](03.PlayerLog&Handouts/Mechanics/CLI/spells/detect-magic.md),\
      \ [eldritch blast](03.PlayerLog&Handouts/Mechanics/CLI/spells/eldritch-blast.md)\
      \ (at 11th level), [false life](03.PlayerLog&Handouts/Mechanics/CLI/spells/false-life.md),\
      \ [levitate](03.PlayerLog&Handouts/Mechanics/CLI/spells/levitate.md) (self only),\
      \ [mage armor](03.PlayerLog&Handouts/Mechanics/CLI/spells/mage-armor.md) (self\
      \ only)\n\n3/day each: [hellish rebuke](03.PlayerLog&Handouts/Mechanics/CLI/spells/hellish-rebuke.md),\
      \ [hex](03.PlayerLog&Handouts/Mechanics/CLI/spells/hex.md), [scorching ray](03.PlayerLog&Handouts/Mechanics/CLI/spells/scorching-ray.md)\
      \ (at 3rd level)\n\n1/day each: [circle of death](03.PlayerLog&Handouts/Mechanics/CLI/spells/circle-of-death.md),\
      \ [enthrall](03.PlayerLog&Handouts/Mechanics/CLI/spells/enthrall.md), [suggestion](03.PlayerLog&Handouts/Mechanics/CLI/spells/suggestion.md)"
    "name": "Innate Spellcasting"
  - "desc": "The witch can use a bonus action to control the movement of one creature\
      \ cursed by its [hex](03.PlayerLog&Handouts/Mechanics/CLI/spells/hex.md) spell\
      \ that it can see within 30 feet of it. The creature must succeed on a DC 15\
      \ Charisma saving throw or use its reaction to move up to 30 feet in a direction\
      \ of the witch's choice."
    "name": "Blood Witch Dance"
  - "desc": "Magical darkness doesn't impede the witch's darkvision."
    "name": "Devil's Sight"
"actions":
  - "desc": "The witch makes two attacks: one with its longsword and one with its\
      \ shortsword."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7\
      \ (1d8 + 3) slashing damage."
    "name": "Longsword"
  - "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 6\
      \ (1d6 + 3) piercing damage."
    "name": "Shortsword"
"source":
  - "GGR"
"image": "03.PlayerLog&Handouts/Mechanics/CLI/bestiary/humanoid/token/blood-witch-ggr.webp"
```
^statblock