---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/19
- ttrpg-cli/monster/environment/mountain
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/giant/shapechanger
- ttrpg-cli/monster/type/giant/titan
statblock: inline
aliases: ["Hraesvelgr"]
---
# [Hraesvelgr](03 - Player Log & Handouts\Mechanics\CLI\bestiary\npc/hraesvelgr-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 207*  

*The giant stands braced in the midst of powerful wind. With a baleful stare, he shakes his fist and bellows a war cry. The cry becomes an avian shriek, and the giant's form melts into that of a massive bird whose wings blot out the sky*.

A giant with divine blood in his veins, Hraesvelgr the Corpse Swallower is powerfully muscled. His skin is a pale bronze, his eyes are violet, and his hair is the color of storm clouds.

## Roc Form

When he takes his alternate form, Hraesvelgr becomes a tremendous roc, with massive wings that stir the wind across the sky. His eyes remain the same violet and these roc-form feathers match the color of his hair, sparkling with specks of color here and there, like jewels set in steel.

## Birth of the Wind

Hraesvelgr dwells on the fringe of the world itself. From atop the peak of his home, he creates the wind and sends it across the globe. As befits a creature of such primal power, Hraesvelgr doesn't take kindly to intruders. He gluts himself on the bodies of fools who test his might in search of the fabled riches in his home.

## Hraesvelgr's Lair

Hraesvelgr's lair is a windswept crag of gray stone at the edge of the world. At the highest pinnacle rests a massive cottage hewn from the mountainside. A great nest made from the splintered trunks of immense trees rests on the flat roof of the cottage, and the wind constantly howls.

```statblock
"name": "Hraesvelgr (ToB1-2023)"
"size": "Huge"
"type": "giant"
"subtype": "shapechanger, titan"
"alignment": "Neutral"
"ac": !!int "19"
"ac_class": "natural armor"
"hp": !!int "241"
"hit_dice": "21d12 + 105"
"stats":
- !!int "25"
- !!int "10"
- !!int "20"
- !!int "16"
- !!int "17"
- !!int "20"
"speed": "50 ft. (20 ft. fly 120 ft. in roc form)"
"saves":
  "Charisma": !!int "11"
  "Dexterity": !!int "6"
  "Wisdom": !!int "9"
  "Intelligence": !!int "9"
"skillsaves":
  "Athletics": !!int "13"
  "Perception": !!int "9"
  "Survival": !!int "9"
"damage_resistances": "lightning, thunder"
"damage_immunities": "cold; bludgeoning, piercing, slashing from nonmagical attacks"
"condition_immunities": "[exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion)"
"senses": "passive Perception 19"
"languages": "Auran, Common, Giant (can't speak in roc form)"
"cr": "19"
"traits":
- "desc": "Hraesvelgr has advantage on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on sight."
  "name": "Keen Sight (Roc Form Only)"
- "desc": "Nearby weather responds to Hraesvelgr's desires. At the start of each minute,\
    \ Hraesvelgr can choose to change the precipitation and wind within 3 miles of\
    \ him by one stage, up or down (no action required). This effect works like the\
    \ changing weather conditions aspect of the [control weather](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/control-weather.md)\
    \ spell, except Hraesvelgr can't change the temperature and the conditions change\
    \ immediately."
  "name": "Influence Weather"
- "desc": "If Hraesvelgr fails a saving throw, he can choose to succeed instead."
  "name": "Legendary Resistance (3/Day)"
"actions":
- "desc": "Hraesvelgr makes one Beak attack and two Talon attacks, or he makes three\
    \ Fist attacks. Alternatively, he can make three Gale Blast attacks. If two Fist\
    \ attacks hit one creature, the target must succeed on a DC 19 Constitution saving\
    \ throw or be [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)\
    \ until the end of its next turn."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +13 to hit, reach 10 ft., one target. Hit: 25\
    \ (4d8 + 7) piercing damage."
  "name": "Beak (Roc Form Only)"
- "desc": "Melee Weapon Attack: +13 to hit, reach 10 ft., one target. Hit: 20\
    \ (3d8 + 7) bludgeoning damage."
  "name": "Fist (Giant Form Only)"
- "desc": "Melee Weapon Attack: +13 to hit, reach 5 ft., one target. Hit: 17\
    \ (3d6 + 7) slashing damage, and the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 17). Until this grapple ends, the target is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained).\
    \ Hraesvelgr has two talons, each of which can grapple only one target."
  "name": "Talons (Roc Form Only)"
- "desc": "Ranged Spell Attack: +11 to hit, range 120 ft., one target. Hit:\
    \ 14 (2d8 + 5) bludgeoning damage plus 7 (2d6) cold damage."
  "name": "Gale Blast"
- "desc": "Hraesvelgr makes one Beak attack against a Large or smaller creature he\
    \ is grappling. If the attack hits, the target is also swallowed, and the grapple\
    \ ends. While swallowed, the creature is [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ and [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ it has total cover against attacks and other effects outside Hraesvelgr, and\
    \ it takes 17 (5d6) acid damage at the start of each of Hraesvelgr's turns.\
    \ Hraesvelgr can have only one creature swallowed at a time.\n\nIf Hraesvelgr\
    \ takes 40 damage or more on a single turn from the swallowed creature, Hraesvelgr\
    \ must succeed on a DC 15 Constitution saving throw at the end of that turn or\
    \ regurgitate the creature, which falls [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)\
    \ in a space within 10 feet of Hraesvelgr. Hraesvelgr has disadvantage on this\
    \ saving throw if he isn't in his roc form. If Hraesvelgr dies, a swallowed creature\
    \ is no longer [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ by him and can escape from the corpse by using 15 feet of movement, exiting\
    \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Swallow (Roc Form Only)"
- "desc": "Hraesvelgr unleashes a powerful gust of wind in a 60-foot line that is\
    \ 10 feet wide. Each creature in the line must make a DC 19 Strength saving throw.\
    \ On a failure, a creature takes 63 (18d6) bludgeoning damage and is pushed\
    \ up to 15 feet away from Hraesvelgr. On a success, a creature takes half the\
    \ damage and isn't pushed."
  "name": "Sudden Gust (Recharge 5-6)"
"bonus_actions":
- "desc": "Hraesvelgr transforms into a roc or back into his true form, which is a\
    \ Giant. His statistics, other than his speed, are the same in each form. Any\
    \ equipment he is wearing or carrying isn't transformed. He reverts to his true\
    \ form if he dies."
  "name": "Change Shape"
"legendary_actions":
- "desc": "Hraesvelgr makes a Fist or Talons attack."
  "name": "Attack"
- "desc": "Hraesvelgr moves up to his speed, or flies up to half his flying speed\
    \ if in roc form, without provoking opportunity attacks."
  "name": "Move"
- "desc": "Hraesvelgr lets out an ear-splitting screech. Each creature within 30 feet\
    \ of Hraesvelgr must succeed on a DC 19 Constitution saving throw or take 14 (4d6)\
    \ thunder damage and be [deafened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Deafened)\
    \ until the end of its next turn."
  "name": "Ear-Splitting Screech (Costs 2 Actions; Roc Form Only)"
"lair_actions":
- "desc": "On initiative count 20 (losing initiative ties), Hraesvelgr takes a lair\
    \ action to cause one of the following effects; Hraesvelgr can't use the same\
    \ effect two rounds in a row:"
  "name": ""
- "desc": "- Pillar of Wind. One creature within 60 feet that Hraesvelgr can see\
    \ must succeed on a DC 19 Strength saving throw or be swept up in a pillar of\
    \ wind. The creature is restrained and suspended 15 feet off the ground. A creature\
    \ can take an action to free the restrained creature by succeeding on a DC 19\
    \ Strength check. If the restrained creature has a way to pull itself out of the\
    \ air, it can free itself in the same way. If the restrained creature has a flying\
    \ speed, it can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success. Otherwise, this effect lasts until Hraesvelgr\
    \ uses this lair action again or until he dies.  \n- Powerful Exhale. Hraesvelgr\
    \ unleashes a blast of wind in a 60-foot cone. Each creature in the area must\
    \ succeed on a DC 19 Dexterity saving throw or be knocked prone.  \n- Terrifying\
    \ Utterance. Hraesvelgr lets out a thunderous bellow. Each creature within 30\
    \ feet of him and that can hear him must succeed on a DC 19 Constitution saving\
    \ throw or be frightened for 1 minute. A frightened creature can repeat the saving\
    \ throw at the end of each of its turns, ending the effect on itself on a success.\
    \  "
  "name": ""
"regional_effects":
- "desc": "The region containing Hraesvelgr's lair is warped by his magic, which creates\
    \ one or more of the following effects:"
  "name": ""
- "desc": "- Active Weather. Strong windstorms are common within 6 miles of the\
    \ lair.  \n- Roosting Rocs. Within 3 miles of the lair, giant avian Beasts\
    \ are more populous and fiercely defend the area against intruders.  \n- Stench\
    \ of Decay. The wind within 10 miles of the lair bears a pungent carrion stench.\
    \  "
  "name": ""
- "desc": "If Hraesvelgr dies, these effects fade over the course of 1d10 days."
  "name": ""
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/npc/token/hraesvelgr-tob1-2023.webp"
```
^statblock

## Environment

mountain