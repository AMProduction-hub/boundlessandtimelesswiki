---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/vgm
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/any-race
statblock: inline
aliases: ["Booyahg Slave of the Fiend"]
---
# [Booyahg Slave of the Fiend](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/booyahg-slave-of-the-fiend-vgm.md)
*Source: Volo's Guide to Monsters p. 42*  

This goblin warlock serves a patron who can extract payment in flesh if the goblin doesn't do as promised. Often this patron is a coven of hags serving as the tribe's boss, a fiend that has made its way into the world, or an undying lord such as a lich or a vampire. (For more information on undying lord patrons, see the "Sword Coast Adventurer's Guide").

## Booyahgs

Spellcasters of any sort among the goblins are rare. Goblins typically lack the intelligence and patience needed to learn and practice wizardry, and they fare poorly even when given access to the necessary training and knowledge. Sorcerers are less prevalent among them than in many other races, and Khurgorbaeyag seems to dislike sharing his divine power with his followers. And although many goblins would readily offer anything to have the abilities of a warlock, the patrons that grant such power know a goblin is unlikely to be able to uphold its end of any bargain.

Even when a goblin is born with the ability to become a spellcaster, the knowledge and talent necessary to carry on the tradition rarely persists for more than a couple of generations. Because they have so little experience with magic, goblins make no distinction between its forms. To them all magic is "booyahg," and the word is part of the name they give to any of its practitioners.

A goblin with access to booyahg becomes a member of the lashers and can often rise to the role of boss.

```statblock
"name": "Booyahg Slave of the Fiend (VGM)"
"size": "Medium"
"type": "humanoid"
"subtype": "any race"
"alignment": "Any alignment"
"ac": !!int "12"
"ac_class": "15 with [mage armor](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/mage-armor.md)"
"hp": !!int "78"
"hit_dice": "12d8 + 24"
"stats":
- !!int "10"
- !!int "14"
- !!int "15"
- !!int "12"
- !!int "12"
- !!int "18"
"speed": "30 ft."
"saves":
  "Charisma": !!int "7"
  "Wisdom": !!int "4"
"skillsaves":
  "Deception": !!int "7"
  "Religion": !!int "4"
  "Arcana": !!int "4"
  "Persuasion": !!int "7"
"damage_resistances": "slashing from nonmagical attacks not made with silvered weapons"
"senses": "darkvision 60 ft., darkvision 60 ft., passive Perception 11"
"languages": "any two languages (usually Abyssal or Infernal), Goblin"
"cr": "7"
"traits":
- "desc": "The goblin's innate spellcasting ability is Charisma. It can innately cast\
    \ the following spells (spell save DC 15), requiring no material components:\n\
    \nAt will: [alter self](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/alter-self.md),\
    \ [false life](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/false-life.md),\
    \ [levitate](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/levitate.md)\
    \ (self only), [mage armor](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/mage-armor.md)\
    \ (self only), [silent image](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/silent-image.md)\n\
    \n1/day each: [feeblemind](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/feeblemind.md),\
    \ [finger of death](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/finger-of-death.md),\
    \ [plane shift](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/plane-shift.md)"
  "name": "Innate Spellcasting"
- "desc": "The goblin is a 17th-level spellcaster. Its spellcasting ability is Charisma\
    \ (spell save DC 15, +7 to hit with spell attacks). It regains its expended\
    \ spell slots when it finishes a short or long rest. It knows the following warlock\
    \ spells:\n\nCantrips (at will): [eldritch blast](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/eldritch-blast.md),\
    \ [fire bolt](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/fire-bolt.md),\
    \ [friends](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/friends.md),\
    \ [mage hand](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/mage-hand.md),\
    \ [minor illusion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/minor-illusion.md),\
    \ [prestidigitation](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/prestidigitation.md),\
    \ [shocking grasp](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/shocking-grasp.md)\n\
    \n1st-5th level (4 slots): [banishment](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/banishment.md),\
    \ [burning hands](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/burning-hands.md),\
    \ [flame strike](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/flame-strike.md),\
    \ [hellish rebuke](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/hellish-rebuke.md),\
    \ [magic circle](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/magic-circle.md),\
    \ [scorching ray](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/scorching-ray.md),\
    \ [scrying](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/scrying.md),\
    \ [stinking cloud](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/stinking-cloud.md),\
    \ [suggestion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/suggestion.md),\
    \ [wall of fire](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/wall-of-fire.md)"
  "name": "Spellcasting"
- "desc": "When the goblin makes an ability check or saving throw, it can add a d10\
    \ to the roll. It can do this after the roll is made but before any of the roll's\
    \ effects occur."
  "name": "Dark One's Own Luck (Recharges after a Short or Long Rest)"
- "desc": "The goblin"
  "name": "Nimble Escape"
"actions":
- "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d6)\
    \ bludgeoning damage plus 10 (3d6) fire damage."
  "name": "Mace"
"source":
- "VGM"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/booyahg-slave-of-the-fiend-vgm.webp"
```
^statblock