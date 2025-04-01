---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/16
- ttrpg-cli/monster/environment/mountain
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Snow Queen"]
---
# [Snow Queen](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/snow-queen-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 184*  

*This severe elf has pale, almost white skin and tightly braided blond hair. Her gown is exquisite, fashioned of luminous blue fabric that catches light and shines from within. Lacy ice crystals accent the gown, and a snow-white mantle cascades from her shoulders. Icicles radiate in a crownlike halo behind her head, drifting gracefully through the air*.

Her Crystalline Majesty, Morrinn, is the cold-hearted Snow Queen, Daughter of Boreas. The Snow Queen rules a northern kingdom in the remote, frozen reaches of the world. Perpetually shrouded in snow and ice, her domain is inhospitable to outsiders. She rules from a castle of delicate spires carved entirely out of ice. The dwelling catches and reflects even the faintest glimmer of light, shining like a beacon and enticing travelers to risk the dangerous winter realm.

## Queen of Giants

The Snow Queen is proud and cruel to any who cross her. Her daughters, the ice maidens, roam her kingdom with ease. Travelers who can't give a good reason to be moving through the Queen's territory meet a quick end in the maidens' chilly embrace. The Snow Queen commands the loyalty of winter-born tribes of fraughashar, ogres, frost giants, thursir giants, and trollkin. She is said to have mocked both Thor and Loki and often leads their priests astray into winter storms.

## Fey Lords and Ladies

Fey are capricious, mischievous, and often dangerous beings. However, despite their chaotic reputations, they do follow a certain set of rules. These rules—widely misunderstood by outsiders—are codified and enforced by a cadre of lofty fey nobility. Befitting any courtly structure, the fey bow to lords and ladies: eldritch creatures of immense power who rule the courts.

### Heads of State

The fey lords and ladies are beings of high station and prodigious personal power. Each rules over at least a great city if not an entire nation. No matter the scope of a fey noble's domain, in his or her eyes, a fey ruler's word is law. Outsiders might not understand the edicts and interdicts of a fey noble, but that's no protection against the harsh penalties that await any who break them, knowingly or otherwise.

### Vacant Thrones

When a lord or lady of the fey dies, the court does not remain leaderless for long. Ambitious beings among the fey always hunger for more power and covet the stations of their superiors. After a traditional month or year of mourning, vicious power struggles winnow the weak and pave the way for the most cunning or the strongest to take the court's vacant throne.

## The Snow Queen's Lair

The Snow Queen's lair is a castle made of ice. Sunlight and moonlight flash through the delicate spires and translucent walls, setting the palace agleam even in the deepest night. The castle reflects its mistress: beautiful, cold, and unforgivingly deadly.

```statblock
"name": "Snow Queen (ToB1-2023)"
"size": "Medium"
"type": "fey"
"alignment": "Neutral Evil"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "182"
"hit_dice": "28d8 + 56"
"stats":
- !!int "16"
- !!int "18"
- !!int "14"
- !!int "18"
- !!int "20"
- !!int "18"
"speed": "40 ft."
"saves":
  "Charisma": !!int "9"
  "Dexterity": !!int "9"
  "Constitution": !!int "7"
"skillsaves":
  "Stealth": !!int "9"
  "Perception": !!int "10"
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks not\
  \ made with cold iron weapons"
"damage_immunities": "cold"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)"
"senses": "blindsight 10 ft., darkvision 120 ft., passive Perception 20"
"languages": "Common, Elvish, Giant, Sylvan"
"cr": "16"
"traits":
- "desc": "When climbing on ice, the Snow Queen has a climbing speed of 20 feet, and\
    \ she can climb difficult surfaces made of ice and snow, including upside down\
    \ on ceilings, without needing to make an ability check."
  "name": "Ice Climb"
- "desc": "The Snow Queen's weapon attacks are magical. When she hits with any weapon,\
    \ the weapon deals an extra 2d6 cold damage (included in the attack)."
  "name": "Icy Weapons"
- "desc": "If the Snow Queen fails a saving throw, she can choose to succeed instead."
  "name": "Legendary Resistance (3/Day)"
- "desc": "The Snow Queen can see through areas obscured by snowfall, sleet, rain,\
    \ and other wintry precipitation without penalty."
  "name": "Snowsight"
- "desc": "The Snow Queen can move across icy surfaces without needing to make an\
    \ ability check. Additionally, difficult terrain composed of ice or snow doesn't\
    \ cost her extra movement."
  "name": "Snow Walk"
"actions":
- "desc": "The Snow Queen makes two Claw or Ice Bolt attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 11\
    \ (2d6 + 4) slashing damage plus 7 (2d6) cold damage."
  "name": "Claw"
- "desc": "Ranged Spell Attack: +10 to hit, range 120 ft., one target. Hit:\
    \ 13 (2d8 + 4) piercing damage plus 7 (2d6) cold damage. The target's speed\
    \ is reduced by 10 feet until the end of its next turn."
  "name": "Ice Bolt"
- "desc": "The Snow Queen causes the temperature around her to drop dramatically.\
    \ Each creature without 30 feet of the Snow Queen must make a DC 18 Constitution\
    \ saving throw. On a failure, a creature takes 42 (12d6) cold damage and suffers\
    \ one level of [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion).\
    \ On a success, a creature takes half the damage and doesn't suffer [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion).\
    \ A creature that is immune to cold damage doesn't suffer [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
    \ even if it fails the saving throw. A creature that fails the saving throw by\
    \ 5 or more is [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified)\
    \ in ice for 1 minute. A [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success. A [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified)\
    \ creature that takes fire damage has advantage on the saving throw to end the\
    \ effect."
  "name": "Cold Snap (Recharge 5-6)"
"legendary_actions":
- "desc": "The Snow Queen makes a Claw or Ice Bolt attack."
  "name": "Attack"
- "desc": "The Snow Queen moves up to her speed without provoking opportunity attacks."
  "name": "Move"
- "desc": "One creature the Snow Queen can see within 120 feet of her must succeed\
    \ on a DC 18 Dexterity saving throw or be [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ by swirling snow until the end of its next turn."
  "name": "Snowblind"
- "desc": "Each creature within 15 feet of the Snow Queen must succeed on a DC 18\
    \ Constitution saving throw or have vulnerability to cold damage until the end\
    \ of its next turn. A creature with immunity to cold damage that fails this saving\
    \ throw instead loses its immunity to cold damage but isn't vulnerable to it."
  "name": "Wintry Swirl (Costs 2 Actions)"
"lair_actions":
- "desc": "On initiative count 20 (losing initiative ties), the Snow Queen takes a\
    \ lair action to cause one of the following effects; the Snow Queen can't use\
    \ the same effect two rounds in a row:"
  "name": ""
- "desc": "- Induce Snow Blindness. The snow and ice of the lair shimmer and gleam,\
    \ catching the light and flashing it into the eyes of the Snow Queen's foes. Each\
    \ hostile creature within 30 feet of the Snow Queen has disadvantage on attack\
    \ rolls against her until initiative count 20 on the next round.  \n- Isolated\
    \ Blizzard. A blast of wintry weather and heavy snow falls in a 30-foot radius\
    \ centered on a point on the ground that the Snow Queen can see within 120 feet\
    \ of her. The area becomes difficult terrain, and each creature that enters the\
    \ area for the first time on a turn must succeed on a DC 18 Strength saving throw\
    \ or be restrained by the snow. A creature, including the restrained creature,\
    \ can take an action to free the restrained creature by succeeding on a DC 18\
    \ Strength check. The snow melts away when the Queen uses this lair action again\
    \ or when the Queen dies.  \n- Snow Wall. A wall of dense snow erupts on a\
    \ solid surface within 120 feet of the Snow Queen. The wall is up to 60 feet long,\
    \ 10 feet high, and 5 feet thick, and it blocks line of sight. When the wall appears,\
    \ each creature in its area must succeed on a DC 18 Dexterity saving throw or\
    \ take 14 (4d6) cold damage and be pushed 5 feet out of the wall's space, appearing\
    \ on whichever side of the wall it wants. A creature can move through the wall,\
    \ though the wall is filled with freezing snow. For every 1 foot a creature moves\
    \ through the wall, it must spend 4 feet of movement. A creature that starts its\
    \ turn in the wall or enters the wall's space for the first time on a turn must\
    \ make a DC 18 Constitution saving throw, taking 14 (4d6) cold damage on a failed\
    \ save, or half as much damage on a successful one. Each 10-foot section of the\
    \ wall has AC 5, 15 hp, vulnerability to fire damage, resistance to bludgeoning\
    \ damage, and immunity to cold, poison, and psychic damage. The wall melts when\
    \ the Queen uses this lair action again or when she dies.  "
  "name": ""
"regional_effects":
- "desc": "The region containing the Snow Queen's lair is warped by her magic, which\
    \ creates one or more of the following effects:"
  "name": ""
- "desc": "- Concealing Flurries. Light snowfall or swirling powder blown by the\
    \ wind lightly obscures the area within 5 miles of the lair.  \n- Permafrost.\
    \ Within 10 miles of the lair, snow and ice resist melting, doing so only after\
    \ prolonged contact with fire or other major source of heat.  \n- Snow-Covered\
    \ Land. Deep snow and frequent snowfall make the area within 3 miles of the\
    \ lair difficult terrain for Medium and smaller creatures.  "
  "name": ""
- "desc": "If the Snow Queen dies, these effects fade over the course of 1d10 days."
  "name": ""
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/snow-queen-tob1-2023.webp"
```
^statblock

## Environment

mountain, planar