---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Far Darrig"]
---
# [Far Darrig](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/far-darrig-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 167*  

*This small man wears hunting leathers and a cowl decorated with antlers, and he holds a glaive made of antlers.*

These shy fairies dress as small fey herdsmen wearing hide armor, hide boots, cloaks, and cowls, all trimmed in fox fur and with a red sash or tunic. They often ride woodland creatures, such as elk, giant weasels, or snowy giant owls.

## Hunters and Herders

The far darrig were the hunters, herders, and equerry of the elven nobility. Some still serve in this capacity in planes where the elves rule. Far darrig carry glaives made from fey antlers; each remains enchanted only as long as a far darrig holds it. Their leaders ride on fey elk the color of foxes, with gleaming green eyes. When these elk shed their antlers, the far darrigs' smiths craft the antlers into the glaives wielded by their people.

## Hate Arcanists

While not inherently evil, far darrig are hostile to most humanoids and often attack humanoid spellcasters on sight. If they can be persuaded of a spellcaster's or humanoid's good intentions, they make good guides, scouts, and hunters in dangerous forests.

## Serve Hags and Worse

They are sometimes found as thralls or scouts serving hags or other evil fey, but they rarely do so willingly.

> [!note] Far Darrig in Midgard
> 
> The far darrig thrive in forests such as the Arbonesse and Margreve, and they are close allies to the druids in those woodlands. Some believe they also serve in a hidden fey court, somewhere in or near the Green Duchy of Verrayne.
^far-darrig-in-midgard

```statblock
"name": "Far Darrig (ToB1-2023)"
"size": "Small"
"type": "fey"
"alignment": "Neutral"
"ac": !!int "14"
"ac_class": "[hide armor](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/hide-armor.md)"
"hp": !!int "84"
"hit_dice": "13d6 + 39"
"stats":
- !!int "17"
- !!int "16"
- !!int "17"
- !!int "11"
- !!int "15"
- !!int "17"
"speed": "30 ft."
"saves":
  "Charisma": !!int "5"
"skillsaves":
  "Nature": !!int "4"
  "Animal Handling": !!int "4"
  "Perception": !!int "4"
  "Survival": !!int "4"
"senses": "darkvision 60 ft., passive Perception 14"
"languages": "Common, Elvish, Sylvan"
"cr": "3"
"traits":
- "desc": "The far darrig's attacks with its Antler Glaive are magical. When the far\
    \ darrig hits with an Antler Glaive attack, the weapon deals an extra 1d6 force\
    \ damage (included in the attack)."
  "name": "Enchanted Antlers"
- "desc": "The far darrig can communicate with Beasts as if they shared a language."
  "name": "Speak with Beasts"
"actions":
- "desc": "The far darrig makes two Antler Glaive attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +5 to hit, reach 10 ft., one target. Hit: 8\
    \ (1d10 + 3) piercing damage or slashing damage (the far darrig's choice) plus\
    \ 3 (1d6) force damage. The target must succeed on a DC 13 Strength saving throw\
    \ or be knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Antler Glaive"
- "desc": "The far darrig magically calls 1d4 elk or giant weasels. The called Beasts\
    \ arrive in 1d4 rounds, acting as allies of the far darrig and obeying its spoken\
    \ commands. The Beasts remain for 1 hour, until the far darrig dies, or until\
    \ the far darrig dismisses them as a bonus action."
  "name": "Woodland Friends (1/Day)"
"bonus_actions":
- "desc": "The far darrig takes the Dash or Disengage action. The far darrig can use\
    \ this bonus action only if it is in a forest."
  "name": "Nimble Woodsman"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/far-darrig-tob1-2023.webp"
```
^statblock

## Environment

forest