---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/11
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/fiend/demon
statblock: inline
aliases: ["Berstuc Demon"]
---
# [Berstuc Demon](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fiend/berstuc-demon-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 83*  

*Although slightly stooped, this male figure is muscular and broad‑shouldered. The creature's head is lost in a riot of moss, while a thick mustache and beard reach almost to its waist.*

The hulking, moss-haired berstuc looks sculpted out of a primordial forest—it stands over 12 feet tall and weighs 800 pounds. Despite its great stature, it seems strangely gentle, with a serene, almost soothing presence. Nothing could be further from the truth; the berstuc is a murderous demon that stalks woodlands and jungles of the Material Plane.

## Poisoned Fruit

Berstuc prowl forests in search of travelers to torment. A berstuc demon poses as a benevolent, or at least indifferent, wood spirit to gain the trust of mortals. It allows itself to be persuaded to help lost travelers (reluctantly) or to lead them to their destinations. Once it draws its unwitting prey deep into the woods, it strikes.

```statblock
"name": "Berstuc Demon (ToB1-2023)"
"size": "Large"
"type": "fiend"
"subtype": "demon"
"alignment": "Chaotic Evil"
"ac": !!int "18"
"ac_class": "natural armor"
"hp": !!int "157"
"hit_dice": "15d10 + 75"
"stats":
- !!int "22"
- !!int "10"
- !!int "20"
- !!int "12"
- !!int "14"
- !!int "19"
"speed": "40 ft., burrow 20 ft."
"saves":
  "Charisma": !!int "8"
  "Wisdom": !!int "6"
  "Strength": !!int "10"
"skillsaves":
  "Nature": !!int "9"
  "Deception": !!int "8"
  "Stealth": !!int "4"
  "Survival": !!int "6"
"damage_resistances": "acid; cold; fire; bludgeoning, piercing, slashing from nonmagical\
  \ attacks"
"damage_immunities": "lightning, poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 120 ft., passive Perception 12"
"languages": "Abyssal, Common, Sylvan, telepathy 120 ft."
"cr": "11"
"traits":
- "desc": "The berstuc detects as a Fey when sensed by spells and features, such as\
    \ the [detect evil and good](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/detect-evil-and-good.md)\
    \ spell or a paladin's Divine Sense. However, it is still a Fiend and can be subjected\
    \ to spells and features that affect Fiends, such as Divine Smite. Beasts and\
    \ Plants find the berstuc's presence soothing and don't attack the berstuc unless\
    \ ordered to or provoked."
  "name": "False Presence"
- "desc": "The berstuc has advantage on Dexterity ([Stealth](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Stealth))\
    \ checks made to hide in forest terrain."
  "name": "Forest Camouflage"
- "desc": "The berstuc has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "While in a nonmagical forest, the berstuc leaves no trail and can't be\
    \ tracked, except by magical means. Creatures of the berstuc's choice within 30\
    \ feet of it that travel with it can't retrace their own trails, and become hopelessly\
    \ lost after 1 hour of travel with the berstuc. Creatures led astray by the berstuc\
    \ have disadvantage on ability checks to discern their location or to navigate\
    \ for 24 hours."
  "name": "Twisted Path"
- "desc": "The berstuc doesn't require food or sleep."
  "name": "Verdant Nature"
"actions":
- "desc": "The berstuc makes three Slam attacks. If two Slam attacks hit a Medium\
    \ or smaller creature, the berstuc can use Enclose on it."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 19\
    \ (3d8 + 6) bludgeoning damage, and the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 17) if it is a Large or smaller creature and the berstuc doesn't\
    \ have two other creatures [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)."
  "name": "Slam"
- "desc": "The berstuc encloses a Medium or smaller creature [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ by it in a mossy growth on the berstuc's body, and the grapple ends. While enclosed\
    \ in the berstuc's growth, the target is [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ and [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ it has total cover from attacks and other effects outside the berstuc, and it\
    \ takes 21 (6d6) poison damage at the start of each of the berstuc's turns.\
    \ The berstuc can have only one creature enclosed at a time.\n\nIf the berstuc\
    \ takes 30 damage or more on a single turn from a creature inside its growth,\
    \ the berstuc must succeed on a DC 15 Constitution saving throw at the end of\
    \ that turn or expel the enclosed creature as the growth bursts. The expelled\
    \ creature falls [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)\
    \ in a space within 5 feet of the berstuc. If the berstuc dies, an enclosed creature\
    \ is no longer [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ by it and can escape from the growth by using 5 feet of movement, exiting [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Enclose"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fiend/token/berstuc-demon-tob1-2023.webp"
```
^statblock

## Environment

forest, planar