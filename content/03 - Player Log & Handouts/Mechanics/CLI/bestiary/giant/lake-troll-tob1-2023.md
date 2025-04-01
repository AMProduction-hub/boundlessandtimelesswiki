---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/environment/coastal
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/giant
statblock: inline
aliases: ["Lake Troll"]
---
# [Lake Troll](03 - Player Log & Handouts\Mechanics\CLI\bestiary\giant/lake-troll-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 370*  

*This large, lanky creature has arms too long for its body. Its hands are webbed and equipped with wicked claws. Its skin is covered in dull green scales and embedded with stones, and limp hair like scraggly seaweed hangs across its long-nosed face*.

Water-dwelling cousins of the more common trolls, lake trolls are both stronger and slightly more intelligent, but thankfully less common. Accompanied by a reek of old, rotting fish, these slimy creatures live beneath the surface of lakes, ponds, rivers, and sometimes even ocean coves.

## Violently Territorial

A lake troll is savage in the defense of its claimed expanse of territory; any encroachment into the creature's water is met with sudden violence from the depths. Fishermen are the most vulnerable to these attacks, especially when they explore new bodies of water.

## Cruel Cunning

Even seasoned soldiers are wise enough to fear the claws of a lake troll; a person with no weapon facing the creature is doomed. Lake trolls delight in splintering wood and twisting metal with their talons and in shrugging off the deadliest of blows with their tough hide. They often prioritize wielders of grand weapons because they delight in the horror brought on by dulling their prey's weapons with a few strokes of their powerful claws. Lake trolls are cunning ambushers. They make use of the water to cover their attack and to protect themselves from the flames of would-be troll hunters.

## Hard to Kill

A lake troll's regeneration is shut down only by cold and fire damage at nearly the same time, making them tricky to fight and exceedingly difficult to kill. Many adventurers have been shocked or slain when a lake troll they presumed was burned to death suddenly leapt back into the fray. Because they're reclusive and so very lethal, these creatures are poorly understood by most scholars.

```statblock
"name": "Lake Troll (ToB1-2023)"
"size": "Large"
"type": "giant"
"alignment": "Chaotic Evil"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "126"
"hit_dice": "12d10 + 60"
"stats":
- !!int "22"
- !!int "13"
- !!int "20"
- !!int "8"
- !!int "10"
- !!int "6"
"speed": "20 ft., swim 40 ft."
"skillsaves":
  "Stealth": !!int "4"
  "Perception": !!int "3"
"senses": "darkvision 60 ft., passive Perception 13"
"languages": "Common, Giant"
"cr": "7"
"traits":
- "desc": "The lake troll can breathe air and water."
  "name": "Amphibious"
- "desc": "The lake troll has advantage on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on smell."
  "name": "Keen Smell"
- "desc": "The lake troll regains 10 hp at the start of its turn. If the lake troll\
    \ takes cold or fire damage, it regains only 5 hp at the start of its next turn.\
    \ If the lake troll takes both cold and fire damage, this trait doesn't function\
    \ at the start of the lake troll's next turn. The lake troll dies only if it starts\
    \ its turn with 0 hp and doesn't regenerate."
  "name": "Regeneration"
"actions":
- "desc": "The lake troll makes one Bite attack and two Claw attacks. If both Claw\
    \ attacks hit one creature that is wielding a weapon, the target must succeed\
    \ on a DC 16 Dexterity saving throw or the target's weapon takes a permanent and\
    \ cumulative -1 penalty to damage rolls. If the weapon's penalty drops to -5,\
    \ the weapon is destroyed. If the target is wielding more than one weapon, the\
    \ troll chooses which weapon to affect."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 10\
    \ (1d8 + 6) slashing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +9 to to hit, reach 5 ft., one target. Hit: 15\
    \ (2d8 + 6) piercing damage."
  "name": "Claw"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/giant/token/lake-troll-tob1-2023.webp"
```
^statblock

## Environment

coastal, forest, underwater