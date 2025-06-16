---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/vgm
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/any-race
statblock: inline
statblock-link: "#^statblock"
aliases:
- Booyahg Slave of the Archfey
---
# [Booyahg Slave of the Archfey](03.PlayerLog&Handouts\Mechanics\CLI\bestiary\humanoid/booyahg-slave-of-the-archfey-vgm.md)
*Source: Volo's Guide to Monsters p. 42*  

This goblin warlock serves a patron who can extract payment in flesh if the goblin doesn't do as promised. Often this patron is a coven of hags serving as the tribe's boss, a fiend that has made its way into the world, or an undying lord such as a lich or a vampire. (For more information on undying lord patrons, see the "Sword Coast Adventurer's Guide").

## Booyahgs

Spellcasters of any sort among the goblins are rare. Goblins typically lack the intelligence and patience needed to learn and practice wizardry, and they fare poorly even when given access to the necessary training and knowledge. Sorcerers are less prevalent among them than in many other races, and Khurgorbaeyag seems to dislike sharing his divine power with his followers. And although many goblins would readily offer anything to have the abilities of a warlock, the patrons that grant such power know a goblin is unlikely to be able to uphold its end of any bargain.

Even when a goblin is born with the ability to become a spellcaster, the knowledge and talent necessary to carry on the tradition rarely persists for more than a couple of generations. Because they have so little experience with magic, goblins make no distinction between its forms. To them all magic is "booyahg," and the word is part of the name they give to any of its practitioners.

A goblin with access to booyahg becomes a member of the lashers and can often rise to the role of boss.

```statblock
"name": "Booyahg Slave of the Archfey (VGM)"
"size": "Medium"
"type": "humanoid"
"subtype": "any race"
"alignment": "Any alignment"
"ac": !!int "11"
"ac_class": "14 with [mage armor](03.PlayerLog&Handouts/Mechanics/CLI/spells/mage-armor.md)"
"hp": !!int "49"
"hit_dice": "11d8"
"modifier": !!int "1"
"stats":
  - !!int "9"
  - !!int "13"
  - !!int "11"
  - !!int "11"
  - !!int "12"
  - !!int "18"
"speed": "30 ft."
"saves":
  - "wisdom": "+3"
  - "charisma": "+6"
"skillsaves":
  - "name": "[Arcana](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Arcana)"
    "desc": "+2"
  - "name": "[Deception](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Deception)"
    "desc": "+6"
  - "name": "[Nature](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Nature)"
    "desc": "+2"
  - "name": "[Persuasion](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Persuasion)"
    "desc": "+6"
"condition_immunities": "[charmed](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Charmed)"
"senses": "darkvision 60 ft., passive Perception 11"
"languages": "any two languages (usually Sylvan), Goblin"
"cr": "4"
"traits":
  - "desc": "The goblin is an 11th-level spellcaster. Its spellcasting ability is\
      \ Charisma (spell save DC 14, +6 to hit with spell attacks). It regains its\
      \ expended spell slots when it finishes a short or long rest. It knows the following\
      \ warlock spells:\n\nCantrips (at will): [dancing lights](03.PlayerLog&Handouts/Mechanics/CLI/spells/dancing-lights.md),\
      \ [eldritch blast](03.PlayerLog&Handouts/Mechanics/CLI/spells/eldritch-blast.md),\
      \ [friends](03.PlayerLog&Handouts/Mechanics/CLI/spells/friends.md), [mage hand](03.PlayerLog&Handouts/Mechanics/CLI/spells/mage-hand.md),\
      \ [minor illusion](03.PlayerLog&Handouts/Mechanics/CLI/spells/minor-illusion.md),\
      \ [prestidigitation](03.PlayerLog&Handouts/Mechanics/CLI/spells/prestidigitation.md),\
      \ [vicious mockery](03.PlayerLog&Handouts/Mechanics/CLI/spells/vicious-mockery.md)\n\
      \n1st-5th level (3 slots): [blink](03.PlayerLog&Handouts/Mechanics/CLI/spells/blink.md),\
      \ [charm person](03.PlayerLog&Handouts/Mechanics/CLI/spells/charm-person.md),\
      \ [dimension door](03.PlayerLog&Handouts/Mechanics/CLI/spells/dimension-door.md),\
      \ [dominate beast](03.PlayerLog&Handouts/Mechanics/CLI/spells/dominate-beast.md),\
      \ [faerie fire](03.PlayerLog&Handouts/Mechanics/CLI/spells/faerie-fire.md),\
      \ [fear](03.PlayerLog&Handouts/Mechanics/CLI/spells/fear.md), [hold monster](03.PlayerLog&Handouts/Mechanics/CLI/spells/hold-monster.md),\
      \ [misty step](03.PlayerLog&Handouts/Mechanics/CLI/spells/misty-step.md), [phantasmal\
      \ force](03.PlayerLog&Handouts/Mechanics/CLI/spells/phantasmal-force.md), [seeming](03.PlayerLog&Handouts/Mechanics/CLI/spells/seeming.md),\
      \ [sleep](03.PlayerLog&Handouts/Mechanics/CLI/spells/sleep.md)"
    "name": "Spellcasting"
  - "desc": "The goblin's innate spellcasting ability is Charisma. It can innately\
      \ cast the following spells (spell save DC 15), requiring no material components:\n\
      \nAt will: [disguise self](03.PlayerLog&Handouts/Mechanics/CLI/spells/disguise-self.md),\
      \ [mage armor](03.PlayerLog&Handouts/Mechanics/CLI/spells/mage-armor.md) (self\
      \ only), [silent image](03.PlayerLog&Handouts/Mechanics/CLI/spells/silent-image.md),\
      \ [speak with animals](03.PlayerLog&Handouts/Mechanics/CLI/spells/speak-with-animals.md)\n\
      \n1/day: [conjure fey](03.PlayerLog&Handouts/Mechanics/CLI/spells/conjure-fey.md)"
    "name": "Innate Spellcasting"
  - "desc": "The goblin"
    "name": "Nimble Escape"
"actions":
  - "desc": "Melee  or Ranged Weapon Attack: +3 to hit, reach 5 ft. or range 20/60\
      \ ft., one target. Hit: 4 (1d4 + 2) piercing damage."
    "name": "Dagger"
"reactions":
  - "desc": "In response to taking damage, the goblin turns [invisible](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Invisible)\
      \ and teleports up to 60 feet to an unoccupied space it can see. It remains\
      \ [invisible](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Invisible)\
      \ until the start of its next turn or until it attacks, makes a damage roll,\
      \ or casts a spell."
    "name": "Misty Escape (Recharges after a Short or Long Rest)"
"source":
  - "VGM"
"image": "03.PlayerLog&Handouts/Mechanics/CLI/bestiary/humanoid/token/booyahg-slave-of-the-archfey-vgm.webp"
```
^statblock