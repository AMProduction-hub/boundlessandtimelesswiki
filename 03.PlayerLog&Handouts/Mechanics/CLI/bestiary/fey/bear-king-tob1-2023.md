---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/12
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fey/shapechanger
statblock: inline
aliases: ["Bear King"]
---
# [Bear King](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/bear-king-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 172*  

*Dressed in hunting leathers with a thick bearskin cloak around his shoulders, the bearded king sits upon a throne carved from a whole tree trunk. A crown of holly leaves wreathes his head, and a blackened maul rests near his hand. An ornate clay pot filled with honey hangs at his hip*.

Mesikammen the Bear King, called "Old Honey Paws," rules the northern Kingdom of the Bear. Its forests are thick with bears, and bearfolk and werebears are common among its people.

## Abuzz with Bees

The country's chief product and export, thanks to the Bear King's insatiable appetite for sweets, is honey. The Bear King's hive-keepers harvest rich, blossom-sweet honey from the hives of giant bees they tend. The land's brewers use the honey to create the finest mead, and the most potent brews are infused with fey glamour.

## Boisterous Revels

The Bear King and his court of bear jarls, witches, and oracles spend most of their time hunting in the hills, feasting, brawling, and drinking mead. Old Honey Paws maintains his rulership over this court by besting all rivals in a yearly series of challenges. The challenges are open to anyone, but the Bear King has defeated all comers since he rose to the throne.

## Fey Lords and Ladies

Fey are capricious, mischievous, and often dangerous beings. However, despite their chaotic reputations, they do follow a certain set of rules. These rules—widely misunderstood by outsiders—are codified and enforced by a cadre of lofty fey nobility. Befitting any courtly structure, the fey bow to lords and ladies: eldritch creatures of immense power who rule the courts.

### Heads of State

The fey lords and ladies are beings of high station and prodigious personal power. Each rules over at least a great city if not an entire nation. No matter the scope of a fey noble's domain, in his or her eyes, a fey ruler's word is law. Outsiders might not understand the edicts and interdicts of a fey noble, but that's no protection against the harsh penalties that await any who break them, knowingly or otherwise.

### Vacant Thrones

When a lord or lady of the fey dies, the court does not remain leaderless for long. Ambitious beings among the fey always hunger for more power and covet the stations of their superiors. After a traditional month or year of mourning, vicious power struggles winnow the weak and pave the way for the most cunning or the strongest to take the court's vacant throne.

## Bear King's Lair

The Bear King's fortress thrusts up from the foothills of a mountain range like a petrified wave. The lair is riddled with caves and tunnels and contains the court of the Bear King.

```statblock
"name": "Bear King (ToB1-2023)"
"size": "Medium"
"type": "fey"
"subtype": "shapechanger"
"alignment": "Lawful Neutral"
"ac": !!int "18"
"ac_class": "natural armor"
"hp": !!int "133"
"hit_dice": "14d8 + 70"
"stats":
- !!int "21"
- !!int "10"
- !!int "20"
- !!int "12"
- !!int "18"
- !!int "16"
"speed": "40 ft."
"saves":
  "Dexterity": !!int "4"
  "Wisdom": !!int "8"
  "Strength": !!int "9"
"skillsaves":
  "Intimidation": !!int "7"
  "Athletics": !!int "9"
  "Perception": !!int "8"
"damage_resistances": "cold"
"damage_immunities": "bludgeoning, slashing, piercing, poison from nonmagical attacks\
  \ not made with cold iron weapons"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 120 ft., truesight 10 ft., passive Perception 18"
"languages": "Common, Elvish, Giant, Sylvan"
"cr": "12"
"traits":
- "desc": "Radiant, magical honey drips from the Bear King's paws and coats his weapons,\
    \ making his weapon attacks magical. When the Bear King hits with any weapon,\
    \ the weapon deals an extra 3d8 radiant damage (included in the attack)."
  "name": "Honeyed Weapons"
- "desc": "The Bear King has advantage on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on smell."
  "name": "Keen Smell"
- "desc": "If the Bear King fails a saving throw, he can choose to succeed instead."
  "name": "Legendary Resistance (3/Day)"
- "desc": "The Bear King regains 10 hp at the start of his turn if he has at least\
    \ 1 hp."
  "name": "Regeneration (Bear or Hybrid Form only)"
"actions":
- "desc": "The Bear King makes one Bite attack and two Claw attacks, or he makes three\
    \ Maul or Honey Bolt attacks. If two Maul attacks hit one Large or smaller creature,\
    \ the target must succeed on a DC 17 Strength saving throw or be knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 10\
    \ (1d10 + 5) piercing damage plus 13 (3d8) radiant damage. The target must\
    \ succeed on a DC 17 Dexterity saving throw or take 9 (2d8) radiant damage at\
    \ the start of each of its turns, as radiant honey sticks to the wound. Any creature\
    \ can take an action to remove the honey from the wound with a successful DC 14\
    \ Wisdom ([Medicine](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Medicine))\
    \ check. The honey dissolves if the target receives magical healing."
  "name": "Bite (Bear or Hybrid Form Only)"
- "desc": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 12\
    \ (2d6 + 5) slashing damage plus 13 (3d8) radiant damage."
  "name": "Claw (Bear or Hybrid Form Only)"
- "desc": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 12\
    \ (2d6 + 5) bludgeoning damage plus 13 (3d8) radiant damage."
  "name": "Maul (Fey or Hybrid Form Only)"
- "desc": "Ranged Spell Attack: +8 to hit, range 120 ft., one target. Hit: 22\
    \ (4d8 + 4) radiant damage."
  "name": "Honey Bolt"
"bonus_actions":
- "desc": "The Bear King transforms into a Large brown bear, or a Large bear-Humanoid\
    \ hybrid, or back into his true form, which is Fey. His statistics other than\
    \ his size, are the same in each form. Any equipment he is wearing or carrying\
    \ isn't transformed. The Bear King reverts to his true form if he dies."
  "name": "Change Shape"
"legendary_actions":
- "desc": "The Bear King moves up to his speed without provoking opportunity attacks."
  "name": "Move"
- "desc": "The Bear King throws a jar of magical honey at a creature he can see within\
    \ 120 feet of him. The target must succeed on a DC 17 Dexterity saving throw or\
    \ be [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ by sticky honey until the end of its next turn."
  "name": "Honey Toss"
- "desc": "The Bear King lets out a bloodcurdling roar. Each hostile creature within\
    \ 60 feet of the Bear King and that can hear the roar must succeed on a DC 17\
    \ Wisdom saving throw or be [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ until the end of its next turn."
  "name": "Frightful Roar (Costs 2 Actions)"
"lair_actions":
- "desc": "On initiative count 20 (losing initiative ties), the Bear King takes a\
    \ lair action to cause one of the following effects; the Bear King can't use the\
    \ same effect two rounds in a row:"
  "name": ""
- "desc": "- Quake. A minor quake starts on a point the Bear King can see within\
    \ 120 feet of him. Each creature within 20 feet of that point must succeed on\
    \ a DC 17 Strength saving throw or take 7 (2d6) bludgeoning damage and fall\
    \ prone.  \n- Summon Bees. The lair's denizens rise up to defend their king,\
    \ causing 2d4 giant bees (use the statistics of a giant wasp) to appear in unoccupied\
    \ spaces of the Bear King's choice within 60 feet of him. The bees act on initiative\
    \ count 20, are allies of the Bear King, and obey his spoken commands. The bees\
    \ remain until the Bear King dies or until he dismisses them as a bonus action.\
    \ The Bear King can have no more than eight giant bees under his control at one\
    \ time.  \n- Ursine Transformation. One creature the Bear King can see within\
    \ 30 feet of him must succeed on a DC 17 Constitution saving throw or transform\
    \ into a brown bear as if the creature had failed a saving throw against the polymorph\
    \ spell. While transformed, the creature must move to and attack a target chosen\
    \ by the Bear King on each of its turns. The transformation lasts until the Bear\
    \ King dies or until he uses this lair action again. The transformed creature\
    \ can repeat the saving throw at the end of each of its turns, ending the transformation\
    \ on itself on a success.  "
  "name": ""
"regional_effects":
- "desc": "The region surrounding the Bear King's lair is warped by his magic, which\
    \ creates one or more of the following effects:"
  "name": ""
- "desc": "- Angry Bees. Bees within 10 miles of the Bear King's lair are easily\
    \ agitated and quick to attack Humanoids that aren't bearfolk or werebears.  \n\
    - Call of the Bear King. Within 5 miles of the Bear King's lair, creatures\
    \ have disadvantage on saving throws made to avoid contracting lycanthropy from\
    \ a werebear.  \n- Heightened Passions. Emotions within 10 miles of the Bear\
    \ King's lair run high. Arguments quickly descend into physical scuffles and enjoyable\
    \ get-togethers are likely to become raucous carousing.  "
  "name": ""
- "desc": "If the Bear King dies, these effects fade over the course of 1d10 days."
  "name": ""
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/bear-king-tob1-2023.webp"
```
^statblock

## Environment

forest, planar