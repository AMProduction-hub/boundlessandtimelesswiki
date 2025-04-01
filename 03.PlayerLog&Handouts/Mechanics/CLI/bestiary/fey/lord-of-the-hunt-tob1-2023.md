---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/18
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Lord of the Hunt"]
---
# [Lord of the Hunt](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/lord-of-the-hunt-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 174*  

*Astride a midnight horse sits a shirtless elven huntsman. His broad chest is thickly muscled and sports tattooed knot work. Great stag antlers crest the huntsman's head, curving above his rich brown hair. The pale green glow that shines from his eyes obscures the elf 's strong features, and a massive spear twined with glowing green vines drives forward in his clenched fist*.

The baying of shadow hounds, the thundering of hoof beats, and a brassy horn note; the Wild Hunt is coming, and pity its quarry. The Lord of the Hunt is an enigma among the fey nobles. His true identity beyond title and position as master of the Wild Hunt is unknown, but he has some connection to the Black Prince of the shadow fey—while also answering to elvish druids and consorting with powerful hags and dryads.

## The Wild Hunt

The Lord's court is the Wild Hunt itself, a group of huntsmen, revelers, intelligent hounds, and poor souls they sweep up in their frenzy. His home, if he has any permanent dwelling, is as mysterious as his true identity. He and his Hunt constantly move between the Plane of Shadow and the most ancient forests.

## Fey Lords and Ladies

Fey are capricious, mischievous, and often dangerous beings. However, despite their chaotic reputations, they do follow a certain set of rules. These rules—widely misunderstood by outsiders—are codified and enforced by a cadre of lofty fey nobility. Befitting any courtly structure, the fey bow to lords and ladies: eldritch creatures of immense power who rule the courts.

### Heads of State

The fey lords and ladies are beings of high station and prodigious personal power. Each rules over at least a great city if not an entire nation. No matter the scope of a fey noble's domain, in his or her eyes, a fey ruler's word is law. Outsiders might not understand the edicts and interdicts of a fey noble, but that's no protection against the harsh penalties that await any who break them, knowingly or otherwise.

### Vacant Thrones

When a lord or lady of the fey dies, the court does not remain leaderless for long. Ambitious beings among the fey always hunger for more power and covet the stations of their superiors. After a traditional month or year of mourning, vicious power struggles winnow the weak and pave the way for the most cunning or the strongest to take the court's vacant throne.

## The Lord of the Hunt's Lair

If the Lord of the Hunt has any permanent lair, it is unknown to all but his closest confidants. While the Wild Hunt is a thing of beautiful and deadly grace on the move, the Lord's encampment becomes his lair when the Hunt settles for any length of time. Tents and pavilions house the Lord and his Hunt, and great, roaring fires roast the day's kills. The hours pass with revelry, feasting, physical contests, and strong drink.

```statblock
"name": "Lord of the Hunt (ToB1-2023)"
"size": "Medium"
"type": "fey"
"alignment": "Lawful Neutral"
"ac": !!int "18"
"ac_class": "natural armor"
"hp": !!int "229"
"hit_dice": "27d8 + 108"
"stats":
- !!int "21"
- !!int "18"
- !!int "19"
- !!int "14"
- !!int "18"
- !!int "15"
"speed": "40 ft."
"saves":
  "Charisma": !!int "8"
  "Wisdom": !!int "10"
  "Strength": !!int "11"
"skillsaves":
  "Athletics": !!int "11"
  "Perception": !!int "10"
  "Survival": !!int "10"
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks not\
  \ made with cold iron weapons"
"damage_immunities": "cold, poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "blindsight 10 ft., darkvision 120 ft., passive Perception 20"
"languages": "Common, Draconic, Elvish, Sylvan"
"cr": "18"
"traits":
- "desc": "The Lord of the Hunt's weapon attacks are magical. When he hits with any\
    \ weapon, the weapon deals an extra 14 (4d6) poison damage (included in the\
    \ attack)."
  "name": "Huntsman's Weapons"
- "desc": "If the Lord of the Hunt fails a saving throw, he can choose to succeed\
    \ instead."
  "name": "Legendary Resistance (3/Day)"
- "desc": "While mounted and not [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated),\
    \ the Lord of the Hunt can't be knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
    \ dismounted, or moved against his will."
  "name": "Sure Seat"
"actions":
- "desc": "The Lord of the Hunt makes three Spear or Longbow attacks."
  "name": "Multiattack"
- "desc": "Melee or Ranged Weapon Attack: +11 to hit, reach 5 ft. or range 30/120\
    \ ft., one target. Hit: 8 (1d6 + 5) piercing damage, or 9 (1d8 + 5) piercing\
    \ damage if used in two hands, plus 14 (4d6) poison damage. If the Lord of the\
    \ Hunt throws the spear, the spear teleports up to 120 feet to the Lord of the\
    \ Hunt's hand at the start of his next turn. If he has no hand free, the spear\
    \ teleports to the ground at his feet."
  "name": "Spear"
- "desc": "Ranged Weapon Attack: +10 to hit, range 150/600 ft., one target. Hit:\
    \ 8 (1d8 + 4) piercing damage plus 14 (4d6) poison damage."
  "name": "Longbow"
- "desc": "The Lord of the Hunt magically calls 3d6 elk or boars, 1d4 giant boars\
    \ or giant elk, or 1 elephant. The called Beasts arrive in 1d4 rounds, acting\
    \ as allies of the Lord and obeying its spoken commands. The Beasts remain for\
    \ 1 hour, until the Lord dies, or until the Lord dismisses them as a bonus action.\
    \ The Lord can have any number of Beasts under its control at one time provided\
    \ the combined total CR of the Beasts is no higher than 8."
  "name": "Hunter's Quarry"
"bonus_actions":
- "desc": "The Lord of the Hunt can summon or dismiss a magical Fey mount, mounting\
    \ or dismounting it as part of this bonus action without spending movement. The\
    \ mount uses the statistics of a warhorse, except it has 40 hp, is a Fey, has\
    \ the same damage and condition resistances and immunities as the Lord of the\
    \ Hunt, and uses the Lord's saving throw bonuses in place of its own. If the mount\
    \ is slain, it disappears, leaving behind no physical form, and the Lord of the\
    \ Hunt must wait 1 hour before summoning the mount again."
  "name": "Fey Mount"
"reactions":
- "desc": "The Lord of the Hunt increases his AC by 6 against one attack that would\
    \ hit him. To do so, he must see the attacker and must be wielding a melee weapon."
  "name": "Parry"
"legendary_actions":
- "desc": "The Lord of the Hunt makes one Spear or Longbow attack."
  "name": "Attack"
- "desc": "The Lord of the Hunt moves up to his speed without provoking opportunity\
    \ attacks. If he is mounted, he can force the mount to move up to half its speed\
    \ without provoking opportunity attacks instead."
  "name": "Tenacious Stride"
- "desc": "The Lord of the Hunt blows his hunting horn and chooses one creature he\
    \ can see within 60 feet. If the creature can hear the horn, it must succeed on\
    \ a DC 16 Charisma saving throw or be [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ by the Lord of the Hunt for 8 hours. The [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ target obeys the Lord's verbal commands. If the target suffers any harm or receives\
    \ a suicidal command, it can repeat the saving throw, ending the effect on a success.\
    \ If the target successfully saves against the effect, or if the effect on it\
    \ ends, the target is immune to the Lord's Call to the Hunt for the next 24 hours.\
    \ The Lord can have only one target [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ at a time. If he charms another, the effect on the previous target ends."
  "name": "Call to the Hunt (Costs 2 Actions)"
"lair_actions":
- "desc": "On initiative count 20 (losing initiative ties), the Lord of the Hunt takes\
    \ a lair action to cause one of the following effects; the Lord of the Hunt can't\
    \ use the same effect two rounds in a row:"
  "name": ""
- "desc": "- Cry Havoc. The Wild Hunt echoes with an otherworldly war cry. One\
    \ creature the Lord of the Hunt can see within 120 feet of him must succeed on\
    \ a DC 19 Wisdom saving throw or be frightened for 1 minute. A creature can repeat\
    \ the saving throw at the end of each of its turns, ending the effect on itself\
    \ on a success.  \n- Encourage Undergrowth. Plants erupt from a point on the\
    \ ground the Lord of the Hunt can see within 120 feet of him. The area within\
    \ 20 feet of that point is difficult terrain. A creature that enters the difficult\
    \ terrain for the first time on a turn or starts its turn there must succeed on\
    \ a DC 19 Dexterity saving throw or take 9 (2d8) poison damage and be restrained\
    \ by vines. A creature, including the restrained creature, can take its action\
    \ to free the restrained creature by succeeding on a DC 19 Strength check. The\
    \ plants remain until the Lord of the Hunt uses this lair action again or until\
    \ he dies.  \n- Mark Prey. One creature the Lord of the Hunt can see within\
    \ 120 feet of him must succeed on a DC 19 Wisdom saving throw or be magically\
    \ marked until initiative count 20 on the next round. The Lord has advantage on\
    \ attack rolls against the marked target.  "
  "name": ""
"regional_effects":
- "desc": "The region containing the Lord of the Hunt's encampment is warped by his\
    \ magic, which creates one or more of the following effects:"
  "name": ""
- "desc": "- Game Preserve. Game animals become plentiful within 3 miles of the\
    \ lair. Wisdom ([Survival](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Survival))\
    \ checks to hunt for food are made with advantage, but patrols from the Wild Hunt\
    \ don't take kindly to poachers.  \n- Hunting Grounds. Areas of natural terrain\
    \ within 3 miles of the lair subtly rearrange themselves to create game trails\
    \ through even the densest wilderness.  \n- Spooked Animals. Domesticated\
    \ animals within 3 miles of the lair become skittish and fearful. They are more\
    \ difficult to handle and flee the area if left to their own devices.  "
  "name": ""
- "desc": "When the Lord of the Hunt breaks camp or dies, these effects end immediately."
  "name": ""
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/lord-of-the-hunt-tob1-2023.webp"
```
^statblock

## Environment

forest, planar