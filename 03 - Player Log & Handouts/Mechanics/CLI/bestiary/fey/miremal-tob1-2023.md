---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1-2
- ttrpg-cli/monster/environment/swamp
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Miremal"]
---
# [Miremal](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/miremal-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 272*  

*A short, lean, biped emerges from the shadows. Fungi and mosses cover its pale-skinned body, growing into its flesh. Its green eyes weep bloody tears*.

Miremals are savage, degenerate fey who delight in crafting paths through treacherous swamps. These seemingly safe paths are riddled with traps and ambush points.

## Unreliable Guides

Miremals hunt in packs of three to six and often serve a more powerful creature, especially one that commands potent magic. As a result, many of their paths lead travelers into the grove of a green hag coven or into the lair of a black dragon.

## Swamp Dwellers

Miremals have adapted from sylvan forests to the swamps: patches of red and green fungus sprout from their skin, mushrooms and branches grow haphazardly out of their bodies, and moss hangs from beneath their arms. They can even take on a puddle-like form when close to death, escaping from whatever seeks to harm them. Their eyes are forest green and perpetually wet with bloody tears. Their legends say their tears come from rage over the banishment from their forest homes and agony from knowing they can never return.

## Hate Moss Lurkers

Miremals are occasionally confused with moss lurkers, but the two despise one another and both consider the comparison odious.

> [!note] Miremals in Midgard
> 
> Miremals once served the Faerie Queen Titania as honorable scouts and spies. The habits of mind they cultivated though, made them susceptible to the blandishments of Titania's dark sister, Sarastra, Queen of Night and Magic. She planted within the miremals a hunger for flesh, and many succumbed to Sarastra's enchantment. They turned against those who resisted and devoured their former companions.
> 
> When the miremals regained their senses, they saw the slaughter they had wrought. Titania cursed and banished the miremals, changing their form and admonishing them to repent and atone. Thus far, they have shown no remorse.
^miremals-in-midgard

```statblock
"name": "Miremal (ToB1-2023)"
"size": "Small"
"type": "fey"
"alignment": "Chaotic Evil"
"ac": !!int "12"
"hp": !!int "22"
"hit_dice": "5d6 + 5"
"stats":
- !!int "10"
- !!int "15"
- !!int "12"
- !!int "10"
- !!int "12"
- !!int "8"
"speed": "30 ft., swim 30 ft."
"skillsaves":
  "Stealth": !!int "6"
  "Perception": !!int "3"
  "Survival": !!int "3"
"senses": "darkvision 60 ft., passive Perception 13"
"languages": "Sylvan, Umbral"
"cr": "1/2"
"traits":
- "desc": "The miremal can breathe air and water."
  "name": "Amphibious"
- "desc": "If the miremal takes 7 damage or less that would reduce it to 0 hp, it\
    \ is reduced to 1 hp instead and becomes a puddle of filthy swamp water. At the\
    \ start of the miremal's next turn, it can move up to 15 feet as a puddle. Then\
    \ it returns to its normal form."
  "name": "Muddled Escape (Recharges after a Short or Long Rest)"
- "desc": "The miremal has advantage on Dexterity ([Stealth](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Stealth))\
    \ checks made to hide in swampy terrain."
  "name": "Swamp Camouflage"
"actions":
- "desc": "The miremal makes one Bite attack and one Claw attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6\
    \ + 2) piercing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4\
    \ + 2) slashing damage."
  "name": "Claw"
- "desc": "The miremal spews a noxious stream of bog filth mixed with stomach acid\
    \ at one creature it can see within 20 feet of it. The target must make a DC 11\
    \ Constitution saving throw. On a failure, the target takes 7 (2d6) acid damage\
    \ and is [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ until the end of its next turn. On a success, the target takes half the damage\
    \ and isn't [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)."
  "name": "Bog Spew (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/miremal-tob1-2023.webp"
```
^statblock

## Environment

swamp