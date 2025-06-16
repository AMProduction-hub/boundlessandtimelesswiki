---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/idrotf
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/human
statblock: inline
statblock-link: "#^statblock"
aliases:
- Frost Druid
---
# [Frost Druid](03.PlayerLog&Handouts\Mechanics\CLI\bestiary\humanoid/frost-druid-idrotf.md)
*Source: Icewind Dale: Rime of the Frostmaiden p. 288*  

Frost druids are solitary defenders of nature and the natural enemies of civilization in the North. They seek to preserve the arctic wilderness by destroying outsiders who cross their path. Each patrols its territory in the guise of an arctic fox, a mountain goat, a snowy owl, or a wolf, reverting to human form only when it attacks. Clever ambushers, they use [hallucinatory terrain](03.PlayerLog&Handouts/Mechanics/CLI/spells/hallucinatory-terrain.md) spells to create illusory snowdrifts under which they can hide, or to obscure pools covered by thin ice through which others might fall.

## Awakened Companions

A frost druid is often accompanied by one or more beasts, shrubs, or evergreen trees that it has made sentient using the [awaken](03.PlayerLog&Handouts/Mechanics/CLI/spells/awaken.md) spell. These druids favor polar bears and reindeer (use the [elk](03.PlayerLog&Handouts/Mechanics/CLI/bestiary/beast/elk.md) stat block in the "Monster Manual") as companions, and such creatures typically share the druid's disposition.

## Ice Sickle

A frost druid can carve a sickle out of ice, requiring a total of 24 hours for the work. Bitter cold courses through this weapon while it's in the druid's hands. If the druid dies, the ice sickle melts away. The weapon is otherwise identical to a normal sickle.

```statblock
"name": "Frost Druid (IDRotF)"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Any alignment"
"ac": !!int "13"
"ac_class": "[hide armor](03.PlayerLog&Handouts/Mechanics/CLI/items/hide-armor.md)"
"hp": !!int "67"
"hit_dice": "9d8 + 27"
"modifier": !!int "1"
"stats":
  - !!int "12"
  - !!int "13"
  - !!int "16"
  - !!int "10"
  - !!int "16"
  - !!int "9"
"speed": "40 ft. (wolf form only), burrow 5 ft. (fox form only), climb 30 ft. (goat\
  \ form only), fly 60 ft. (owl form only)"
"saves":
  - "intelligence": "+3"
  - "wisdom": "+6"
"skillsaves":
  - "name": "[Nature](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Nature)"
    "desc": "+3"
  - "name": "[Perception](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Perception)"
    "desc": "+6"
  - "name": "[Survival](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Survival)"
    "desc": "+6"
"damage_resistances": "cold"
"senses": "darkvision 60 ft. (beast form only), passive Perception 16"
"languages": "Common, Druidic"
"cr": "5"
"traits":
  - "desc": "The druid is a 9th-level spellcaster. Its spellcasting ability is Wisdom\
      \ (spell save DC 14; +6 to hit with spell attacks). It has the following druid\
      \ spells prepared:\n\nCantrips (at will): [druidcraft](03.PlayerLog&Handouts/Mechanics/CLI/spells/druidcraft.md),\
      \ [guidance](03.PlayerLog&Handouts/Mechanics/CLI/spells/guidance.md), [resistance](03.PlayerLog&Handouts/Mechanics/CLI/spells/resistance.md)\n\
      \n1st level (4 slots): [animal friendship](03.PlayerLog&Handouts/Mechanics/CLI/spells/animal-friendship.md),\
      \ [fog cloud](03.PlayerLog&Handouts/Mechanics/CLI/spells/fog-cloud.md), [speak\
      \ with animals](03.PlayerLog&Handouts/Mechanics/CLI/spells/speak-with-animals.md)\n\
      \n2nd level (3 slots): [animal messenger](03.PlayerLog&Handouts/Mechanics/CLI/spells/animal-messenger.md),\
      \ [moonbeam](03.PlayerLog&Handouts/Mechanics/CLI/spells/moonbeam.md), [pass\
      \ without trace](03.PlayerLog&Handouts/Mechanics/CLI/spells/pass-without-trace.md)\n\
      \n3rd level (3 slots): [conjure animals](03.PlayerLog&Handouts/Mechanics/CLI/spells/conjure-animals.md),\
      \ [sleet storm](03.PlayerLog&Handouts/Mechanics/CLI/spells/sleet-storm.md),\
      \ [wind wall](03.PlayerLog&Handouts/Mechanics/CLI/spells/wind-wall.md)\n\n4th\
      \ level (3 slots): [hallucinatory terrain](03.PlayerLog&Handouts/Mechanics/CLI/spells/hallucinatory-terrain.md),\
      \ [ice storm](03.PlayerLog&Handouts/Mechanics/CLI/spells/ice-storm.md)\n\n5th\
      \ level (1 slots): [awaken](03.PlayerLog&Handouts/Mechanics/CLI/spells/awaken.md)"
    "name": "Spellcasting (Humanoid Form Only)"
"actions":
  - "desc": "The druid makes two melee attacks."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 3\
      \ (1d4 + 1) slashing damage plus 5 (2d4) cold damage."
    "name": "Ice Sickle (Humanoid Form Only)"
  - "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 3\
      \ (1d4 + 1) piercing damage."
    "name": "Maul (Beast Form Only)"
  - "desc": "The druid magically polymorphs into a beast form—fox, mountain goat,\
      \ owl, or wolf—or back into its humanoid form. Any equipment it is wearing or\
      \ carrying is absorbed or borne by the beast form (the druid's choice). It reverts\
      \ to its humanoid form when it dies. The druid's statistics are the same in\
      \ each form, except where noted in this stat block."
    "name": "Change Shape"
"source":
  - "IDRotF"
"image": "03.PlayerLog&Handouts/Mechanics/CLI/bestiary/humanoid/token/frost-druid-idrotf.webp"
```
^statblock