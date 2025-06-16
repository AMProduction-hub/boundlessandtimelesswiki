---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/erlw
- ttrpg-cli/monster/cr/0
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/any-race
statblock: inline
statblock-link: "#^statblock"
aliases:
- Magewright
---
# [Magewright](03.PlayerLog&Handouts\Mechanics\CLI\bestiary\humanoid/magewright-erlw.md)
*Source: Eberron: Rising from the Last War p. 318*  

In Khorvaire, magic is part of everyday life. A chef might use [prestidigitation](03.PlayerLog&Handouts/Mechanics/CLI/spells/prestidigitation.md) to heat and season food, while a blacksmith uses [mending](03.PlayerLog&Handouts/Mechanics/CLI/spells/mending.md) to perform minor repairs and [guidance](03.PlayerLog&Handouts/Mechanics/CLI/spells/guidance.md) to help inspire their work. Those who work minor magic into their labors are called magewrights.

Far more limited in magical power than a typical spellcaster, a magewright is dedicated to learning a handful of spells, and magewrights cast their non-cantrip spells as rituals—even spells that can't normally be cast in this way. Most magewright rituals take 10 minutes to perform, but certain complex rituals can take up to 1 hour. However long the ritual takes, it requires extra material components, usually in the form of dragonshards.

## Creating a Magewright

The magewright stat block provides the baseline statistics for a magewright. You then add to that baseline by choosing a specialty from the Magewright Specialties table, or roll for one. The specialty determines additional spells the magewright knows, including ones that can be cast only as rituals. The specialty also gives the magewright more proficiencies.

**Magewright Specialties**

`dice: [](magewright-erlw.md#^magewright-specialties)`

| dice: d8 | Specialty | Spells | Proficiencies |
|----------|-----------|--------|---------------|
| 1 | Artisan | [Guidance](03.PlayerLog&Handouts/Mechanics/CLI/spells/guidance.md), [mending](03.PlayerLog&Handouts/Mechanics/CLI/spells/mending.md) | One type of artisan's tools |
| 2 | Entertainer | [Minor illusion](03.PlayerLog&Handouts/Mechanics/CLI/spells/minor-illusion.md), [thaumaturgy](03.PlayerLog&Handouts/Mechanics/CLI/spells/thaumaturgy.md). Ritual only: [disguise self](03.PlayerLog&Handouts/Mechanics/CLI/spells/disguise-self.md). | [Performance](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Performance) (+3) |
| 3 | Healer | [Resistance](03.PlayerLog&Handouts/Mechanics/CLI/spells/resistance.md), [spare the dying](03.PlayerLog&Handouts/Mechanics/CLI/spells/spare-the-dying.md). Ritual only: [detect poison and disease](03.PlayerLog&Handouts/Mechanics/CLI/spells/detect-poison-and-disease.md), [lesser restoration](03.PlayerLog&Handouts/Mechanics/CLI/spells/lesser-restoration.md) (1 hour). | [Medicine](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Medicine) (+4), [herbalism kit](03.PlayerLog&Handouts/Mechanics/CLI/items/herbalism-kit.md) |
| 4 | Lamplighter | [Light](03.PlayerLog&Handouts/Mechanics/CLI/spells/light.md). Ritual only: [continual flame](03.PlayerLog&Handouts/Mechanics/CLI/spells/continual-flame.md) (1 hour). | [Tinker's tools](03.PlayerLog&Handouts/Mechanics/CLI/items/tinkers-tools.md) |
| 5 | Locksmith | [Mending](03.PlayerLog&Handouts/Mechanics/CLI/spells/mending.md). Ritual only: [arcane lock](03.PlayerLog&Handouts/Mechanics/CLI/spells/arcane-lock.md) (1 hour), [knock](03.PlayerLog&Handouts/Mechanics/CLI/spells/knock.md). | [Thieves' tools](03.PlayerLog&Handouts/Mechanics/CLI/items/thieves-tools.md), [tinker's tools](03.PlayerLog&Handouts/Mechanics/CLI/items/tinkers-tools.md) |
| 6 | Mediator | [Guidance](03.PlayerLog&Handouts/Mechanics/CLI/spells/guidance.md). Ritual only: [comprehend languages](03.PlayerLog&Handouts/Mechanics/CLI/spells/comprehend-languages.md), [zone of truth](03.PlayerLog&Handouts/Mechanics/CLI/spells/zone-of-truth.md). | [Insight](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Insight) (+4), [Persuasion](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Persuasion) (+3) |
| 7 | Medium | [Minor illusion](03.PlayerLog&Handouts/Mechanics/CLI/spells/minor-illusion.md). Ritual only: [speak with dead](03.PlayerLog&Handouts/Mechanics/CLI/spells/speak-with-dead.md). | [Deception](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Deception) (+3), [Religion](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Religion) (+4) |
| 8 | Oracle | [Guidance](03.PlayerLog&Handouts/Mechanics/CLI/spells/guidance.md). Ritual only: [augury](03.PlayerLog&Handouts/Mechanics/CLI/spells/augury.md), [divination](03.PlayerLog&Handouts/Mechanics/CLI/spells/divination.md) (1 hour). | [History](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#History) (+4), [Religion](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Religion) (+4) |
^magewright-specialties

```statblock
"name": "Magewright (ERLW)"
"size": "Medium"
"type": "humanoid"
"subtype": "any race"
"alignment": "Any alignment"
"ac": !!int "11"
"hp": !!int "9"
"hit_dice": "2d8"
"modifier": !!int "1"
"stats":
  - !!int "11"
  - !!int "13"
  - !!int "10"
  - !!int "14"
  - !!int "14"
  - !!int "12"
"speed": "30 ft."
"skillsaves":
  - "name": "[Arcana](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Arcana)"
    "desc": "+4"
"senses": "passive Perception 12"
"languages": "Common plus any two languages"
"cr": "0"
"traits":
  - "desc": "The magewright's spellcasting ability is Intelligence (spell save DC\
      \ 12). To cast one of its rituals, the magewright must provide additional material\
      \ components whose value in gold pieces is 20 times the spell's level. These\
      \ components are consumed when the ritual is finished. The magewright knows\
      \ the following spells:\n\nAt will: [mage hand](03.PlayerLog&Handouts/Mechanics/CLI/spells/mage-hand.md),\
      \ [prestidigitation](03.PlayerLog&Handouts/Mechanics/CLI/spells/prestidigitation.md)\n\
      \nRituals: [knock](03.PlayerLog&Handouts/Mechanics/CLI/spells/knock.md)"
    "name": "Spellcasting"
"actions":
  - "desc": "Melee  or Ranged Weapon Attack: +3 to hit, reach 5 ft. or range 20/60\
      \ ft., one target. Hit: 3 (1d4 + 1) piercing damage."
    "name": "Dagger"
"source":
  - "ERLW"
"image": "03.PlayerLog&Handouts/Mechanics/CLI/bestiary/humanoid/token/magewright-erlw.webp"
```
^statblock