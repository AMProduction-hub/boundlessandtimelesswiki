---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/16
- ttrpg-cli/monster/environment/mountain
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/dragon
statblock: inline
aliases: ["Adult Flame Dragon"]
---
# [Adult Flame Dragon](03 - Player Log & Handouts\Mechanics\CLI\bestiary\dragon/adult-flame-dragon-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 118*  

*The dragon bears black scales, more charred than naturally colored. Cracks between the scales glow a dull red, until the dragon rears its head and roars. Red embers become bright orange flames as the creature lights up from tail to maw*.

Flame dragons are capricious creatures, fascinated by dark emotions and destructive passions. The dragons of eternal fire are proud and jealous, quick to anger, and utterly unforgiving. They bring total ruin to entire civilizations for trivial reasons, but their true motivation is the fun to be had. These burning serpents treat rage, deceit, and despair as toys for their amusement. "May you be the fire's plaything" is a curse often used by the foolish.

## Taunting Others

The hot-blooded creatures tease their victims like cats, seeing the world and all within it as their rightful prey. Young flame dragons are less subtle than their elders. Wyrmlings may force a woman to watch her family die or ruin a beautiful face for pleasure—direct and evil. As the dragon matures, this natural sadism develops into a desire for more complicated sport. Aging dragons of fire use politics, murder, and magic in elaborate schemes only their ilk can appreciate. Many create plots so intricate and layered that they lack a true resolution, creating only endless manipulation. A hero might foil an assassination only to see the king thus saved become a despot. She might defeat the vizier whispering lies in the ruler's ear only to discover he was a pawn in a vast conspiracy. Dark ambitions, poisoned daggers, and old vendettas build such momentum that one scheme begins each time another ends. Often, even killing the draconic mastermind cannot extinguish the fires it started.

## Malevolent Purpose

The results of a flame dragon's schemes are secondary to the enjoyment it derives from pursuing a nebulous and ever-changing goal. Some flame dragons spend centuries torturing a family line for nothing more than trespassing on the dragon's land. Others plot eternal curses after twisting poorly chosen words into dire insults. The vengeance itself is secondary to an excuse for hate, plot, and ruin. Flame dragons relish such opportunities for revenge. Each is a delightful hobby. Any disruption in their game kindles a terrible rage, and in these rare moments of defeat, their anger can be catastrophic. Entire cities burn.

## Fond of Souvenirs

Flame dragons are as materialistic and territorial as other true dragons. Each pursues an individual obsession it fixates upon with mad devotion to fill its hoard. Some corrupt innocence, others push nations to war, but they always collect a memento for each victory, petty or grand. One might collect scorched skulls, while another saves the melted treasures of toppled empires. When not out sowing discord, the ancient flame dragons enjoy contemplating their hoards. Every piece reminds them of their own majesty and genius.

## Vengeful Brethren

Nothing is safe from a flame dragon's scheming and narcissism. They crave absolute attention and constant reassurance. Anyone who humiliates a flame dragon would be wiser to kill it. Its survival ensures the dragon's undivided attention for generations. Wiser still, is to remove all trace of involvement in a flame dragon's death. All burning serpents see the murder of one of their kin as the gravest insult.

## A Flame Dragon's Lair

Flame dragons dwell near ever-burning fires: volcanoes, sulfur mines, caves full of geysers, and places where the Elemental Plane of Fire touches the Material Plane. Whatever the place, it must serve as a showcase for all the dragon's trophies. Carefully arranged and organized prizes decorate the area, sometimes protected behind crystal walls. This display feeds the dragon's vanity and pride, and it serves as a lure for adventurers. Many of these lairs also feature a huge, reflective surface, as a flame dragon likes nothing more than itself.

```statblock
"name": "Adult Flame Dragon (ToB1-2023)"
"size": "Huge"
"type": "dragon"
"alignment": "Chaotic Evil"
"ac": !!int "19"
"ac_class": "natural armor"
"hp": !!int "275"
"hit_dice": "22d12 + 132"
"stats":
- !!int "19"
- !!int "14"
- !!int "23"
- !!int "17"
- !!int "14"
- !!int "20"
"speed": "40 ft., climb 40 ft., fly 80 ft."
"saves":
  "Charisma": !!int "10"
  "Dexterity": !!int "7"
  "Wisdom": !!int "7"
  "Constitution": !!int "11"
"skillsaves":
  "Deception": !!int "10"
  "Stealth": !!int "7"
  "Perception": !!int "12"
  "Persuasion": !!int "10"
"damage_immunities": "fire"
"senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 22"
"languages": "Common, Draconic, Ignan"
"cr": "16"
"traits":
- "desc": "Creatures with resistance to fire damage don't have resistance to the fire\
    \ damage dealt by the flame dragon. A creature with immunity to fire damage is\
    \ still immune to the dragon's fire damage."
  "name": "Fire Incarnate"
- "desc": "A creature that touches the flame dragon or hits it with a melee attack\
    \ while within 5 feet of it takes 10 (3d6) fire damage."
  "name": "Heated Body"
- "desc": "If the dragon fails a saving throw, it can choose to succeed instead."
  "name": "Legendary Resistance (3/Day)"
"actions":
- "desc": "The dragon uses its Frightful Presence. It then makes one Bite attack and\
    \ two Claw attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 15\
    \ (2d10 + 4) piercing damage plus 10 (3d6) fire damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 11\
    \ (2d6 + 4) slashing damage."
  "name": "Claw"
- "desc": "Melee Weapon Attack: +9 to hit, reach 15 ft., one target. Hit: 13\
    \ (2d8 + 4) bludgeoning damage."
  "name": "Tail"
- "desc": "Each creature of the dragon's choice that is within 120 feet of the dragon\
    \ and aware of it must succeed on a DC 18 Wisdom saving throw or become [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ for 1 minute. A creature can repeat the saving throw at the end of each of its\
    \ turns, ending the effect on itself on a success. If a creature's saving throw\
    \ is successful or the effect ends for it, the creature is immune to the dragon's\
    \ Frightful Presence for the next 24 hours."
  "name": "Frightful Presence"
- "desc": "The dragon exhales fire in a 60-foot cone. Each creature in that area must\
    \ make a DC 19 Dexterity saving throw, taking 56 (16d6) fire damage on a failed\
    \ save, or half as much damage on a successful one. Each creature in that area\
    \ must also succeed on a DC 18 Wisdom saving throw or go on a rampage for 1 minute.\
    \ A rampaging creature must attack the nearest creature other than the dragon\
    \ on its turn. If no other creature is near enough to move to and attack, the\
    \ rampaging creature stalks off in a random direction, seeking a target for its\
    \ rage. The rampaging creature can repeat the Wisdom saving throw at the end of\
    \ each of its turns, ending the effect on itself on a success."
  "name": "Fire Breath (Recharge 5-6)"
"bonus_actions":
- "desc": "The dragon magically transforms into a Huge or smaller fire-based Elemental\
    \ (such as a salamander, magma mephit, or fire elemental) or back into its true\
    \ form, which is a Dragon. Without wings or other way of flying, it loses its\
    \ flying speed. Its statistics, other than its size and speed, are the same in\
    \ each form. Any equipment it is wearing or carrying transforms with it. It reverts\
    \ to its true form if it dies."
  "name": "Shifting Flames"
"legendary_actions":
- "desc": "The dragon makes a Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ check."
  "name": "Detect"
- "desc": "The dragon makes a Tail attack."
  "name": "Tail Attack"
- "desc": "The dragon beats its wings. Each creature within 10 feet of the dragon\
    \ must succeed on a DC 17 Dexterity saving throw or take 11 (2d6 + 4) bludgeoning\
    \ damage and be knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone).\
    \ The dragon can then fly up to half its flying speed."
  "name": "Wing Attack (Costs 2 Actions)"
"lair_actions":
- "desc": "On initiative count 20 (losing initiative ties), the dragon takes a lair\
    \ action to cause one of the following effects; the dragon can't use the same\
    \ effect two rounds in a row:"
  "name": ""
- "desc": "- Blinding Smoke. A cloud of smoke swirls in a 20-foot-radius sphere\
    \ centered on a point the dragon can see within 120 feet of it. The cloud spreads\
    \ around corners, and the area is lightly obscured. Each creature in the cloud\
    \ must succeed on a DC 15 Constitution saving throw or be blinded for 1 minute.\
    \ A blinded creature can repeat the saving throw at the end of each of its turns,\
    \ ending the effect on itself on a success.  \n- Curtain of Fire. A wall of\
    \ fire rises up from the ground within 120 feet of the dragon. The wall is up\
    \ to 60 feet long, 10 feet high, and 5 feet thick, can take any shape the dragon\
    \ wants, and is opaque. When the wall appears, each creature in its area must\
    \ succeed on a DC 15 Dexterity saving throw or take 21 (6d6) fire damage. Each\
    \ creature that enters the wall for the first time on a turn or ends its turn\
    \ there takes 21 (6d6) fire damage. The wall is extinguished when the dragon\
    \ uses this lair action again or when the dragon dies.  \n- Volcanic Debris.\
    \ The ground erupts with volcanic force at a point the dragon can see within 120\
    \ feet of it. Any creature within 20 feet of the point must make succeed on a\
    \ DC 15 Dexterity saving throw or be knocked prone and buried under rock and debris.\
    \ The buried creature is restrained and can't breathe or stand up. A creature,\
    \ including the buried creature, can take an action to free the buried creature\
    \ by succeeding on a DC 15 Strength check.  "
  "name": ""
"regional_effects":
- "desc": "The region containing a legendary flame dragon's lair is warped by the\
    \ dragon's magic, which creates one or more of the following effects:"
  "name": ""
- "desc": "- Extreme Heat. Temperatures rise within 6 miles of the lair, causing\
    \ most water sources to dry up and all but the hardiest plants to wither.  \n\
    - Fiery Tempers. Arguments and misunderstandings erupt easily within 6 miles\
    \ of the lair. Friendships are easily broken and criminal acts are common.  \n\
    - Superheated Fumaroles. Sulfur geysers dot the landscape within 1 mile of\
    \ the dragon's lair, making the area inhospitable for most plants and creatures.\
    \  "
  "name": ""
- "desc": "If the dragon dies, Fiery Tempers disappears immediately, and temperatures\
    \ return to normal within 1d10 days. Any geysers remain where they are."
  "name": ""
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/dragon/token/adult-flame-dragon-tob1-2023.webp"
```
^statblock

## Environment

mountain, underdark