---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/17
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/mountain
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Queen of Witches"]
---
# [Queen of Witches](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/queen-of-witches-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 180*  

*This statuesque woman towers over any tall man and most ogres. Her hair falls in a cascade of curls and looks as if it is spun from copper. Her eyes are the color of moss beds, with no iris or pupil. A billowy robe of forest green enshrouds her body, and she grasps a great ring of etched silver in one massive fist*.

Nicnevin, the Queen of Witches, is the Mountain Ogress, Lady of Copper and Crystal, and the Moon Weaver. She is not what one usually imagines in a fey lady, but she has an imposing figure of mass and power. Her stature speaks to great physical strength and the stalwart defiance of the mountain itself, but her true power is in her command of magic.

## Pact Patron

The Queen of Witches is one of the foremost patrons of those who seek power through a pact. Many hag covens offer her loyalty and tribute. She rules from beneath her mountain, attended by a court of fey witches, hags, and mortal supplicants. Her favor is highly sought after, and it is said that a single hair from her coppery head contains all the power a mortal might ever desire.

## Fey Lords and Ladies

Fey are capricious, mischievous, and often dangerous beings. However, despite their chaotic reputations, they do follow a certain set of rules. These rules—widely misunderstood by outsiders—are codified and enforced by a cadre of lofty fey nobility. Befitting any courtly structure, the fey bow to lords and ladies: eldritch creatures of immense power who rule the courts.

### Heads of State

The fey lords and ladies are beings of high station and prodigious personal power. Each rules over at least a great city if not an entire nation. No matter the scope of a fey noble's domain, in his or her eyes, a fey ruler's word is law. Outsiders might not understand the edicts and interdicts of a fey noble, but that's no protection against the harsh penalties that await any who break them, knowingly or otherwise.

### Vacant Thrones

When a lord or lady of the fey dies, the court does not remain leaderless for long. Ambitious beings among the fey always hunger for more power and covet the stations of their superiors. After a traditional month or year of mourning, vicious power struggles winnow the weak and pave the way for the most cunning or the strongest to take the court's vacant throne.

## The Queen of Witches's Lair

The Queen of Witches makes her lair in a cavern deep beneath a windswept, rocky mountain. Near the mountain's peak is an enormous quartz crystal that grows down to the lair. This crystal channels the light of the moon into the Queen's home when she doesn't emerge into the night sky. Her hags and attendant witches perform powerful rites in this magic-saturated sanctum.

```statblock
"name": "Queen of Witches (ToB1-2023)"
"size": "Large"
"type": "fey"
"alignment": "Neutral"
"ac": !!int "18"
"ac_class": "natural armor"
"hp": !!int "218"
"hit_dice": "23d10 + 92"
"stats":
- !!int "22"
- !!int "10"
- !!int "19"
- !!int "16"
- !!int "18"
- !!int "22"
"speed": "40 ft., fly 50 ft. (hover)"
"saves":
  "Charisma": !!int "12"
  "Dexterity": !!int "6"
  "Wisdom": !!int "10"
"skillsaves":
  "Deception": !!int "12"
  "Insight": !!int "10"
  "Perception": !!int "10"
  "History": !!int "9"
  "Arcana": !!int "15"
"damage_resistances": "bludgeoning, piercing, slashing, cold, fire from nonmagical\
  \ attacks not made with cold iron weapons"
"damage_immunities": "radiant"
"condition_immunities": "[blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
  \ [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)"
"senses": "darkvision 120 ft., truesight 60 ft., passive Perception 20"
"languages": "Celestial, Common, Draconic, Elvish, Sylvan, Umbral"
"cr": "17"
"traits":
- "desc": "The Queen of Witches casts one of the following spells, requiring no material\
    \ components and using Charisma as the spellcasting ability (save DC 20):\n\n\
    At will: [faerie fire](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/faerie-fire.md),\
    \ [silent image](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/silent-image.md),\
    \ [tongues](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/tongues.md)\n\
    \n1/day each: [power word kill](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/power-word-kill.md),\
    \ [sleep](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/sleep.md)\
    \ (as a 9th level spell), [true polymorph](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/true-polymorph.md)\n\
    \n2/day each: [bestow curse](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/bestow-curse.md),\
    \ [mass suggestion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/mass-suggestion.md),\
    \ [flesh to stone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/flesh-to-stone.md)\n\
    \n3/day each: [dispel magic](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dispel-magic.md),\
    \ [hypnotic pattern](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/hypnotic-pattern.md),\
    \ [teleportation circle](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/teleportation-circle.md)\
    \ (as an action)"
  "name": "Spellcasting"
- "desc": "The Queen of Witches has advantage on saving throws against spells and\
    \ other magical effects."
  "name": "Magic Resistance"
- "desc": "The Queen of Witches's weapon attacks are magical. When she hits with any\
    \ weapon, the weapon deals an extra 7 (2d6) radiant damage (included in the\
    \ attack)."
  "name": "Moonlit Weapons"
- "desc": "If the Queen of Witches fails a saving throw, she can choose to succeed\
    \ instead."
  "name": "Legendary Resistance (3/Day)"
- "desc": "The Queen of Witches can spend 1 minute cutting and tying a lock of her\
    \ hair into a small token of her favor. A creature that is wearing or carrying\
    \ the favor gains the benefits of the Magic Resistance trait. The Queen can revoke\
    \ this magic at any time (no action required). If she does so, the creature has\
    \ disadvantage on saving throws against spells and other magical effects for 24\
    \ hours."
  "name": "Token of Favor"
"actions":
- "desc": "The Queen of Witches makes three Moonsilver Ring attacks or four Mystical\
    \ Blast attacks. She can replace one attack with a use of spellcasting. If she\
    \ hits one creature with two Mystical Blast attacks, the target must succeed on\
    \ a DC 20 Strength saving throw or be pushed up to 10 feet away from her."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 15\
    \ (2d8 + 6) slashing damage plus 7 (2d6) radiant damage."
  "name": "Moonsilver Ring"
- "desc": "Melee or Ranged Spell Attack: +12 to hit, reach 5 ft. or range 120\
    \ ft., one target. Hit: 16 (3d6 + 6) force damage."
  "name": "Mystical Blast"
- "desc": "The Queen of Witches sends moonlight flooding out from her. Each creature\
    \ within 15 feet of her must make a DC 20 Dexterity saving throw, taking 42 (12d6)\
    \ radiant damage on a failed save, or half as much damage on a successful one.\
    \ If the Queen is standing in an area of moonlight when she uses this action,\
    \ each creature in the area has disadvantage on the saving throw. A creature that\
    \ fails the saving throw by 5 or more is [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ until the end of its next turn."
  "name": "Spray of Moonlight (Recharge 5-6)"
"reactions":
- "desc": "When a creature the Queen of Witches can see within 30 feet of her casts\
    \ a spell, the Queen can absorb the spell's energy, countering it. This works\
    \ like the [counterspell](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/counterspell.md)\
    \ spell, except the Queen must always make a spellcasting ability check, no matter\
    \ the spell's level. Her ability check for this is +10. If she successfully counters\
    \ the spell, she regains 5 hp for each level of the spell."
  "name": "Absorb Spell"
"legendary_actions":
- "desc": "The Queen makes one Mystical Blast attack."
  "name": "Mystical Blast"
- "desc": "The Queen magically teleports, along with any equipment she is wearing\
    \ or carrying, to an unoccupied space she can see within 60 feet."
  "name": "Teleport"
- "desc": "The Queen of Witches uses Spellcasting."
  "name": "Cast a Spell (Costs 2 Actions)"
"lair_actions":
- "desc": "On initiative count 20 (losing initiative ties), the Queen of Witches takes\
    \ a lair action to cause one of the following effects; she can't use the same\
    \ effect two rounds in a row:"
  "name": ""
- "desc": "- Conjure Crystal Wall. A wall of softly glowing crystal springs up\
    \ from a solid surface the Queen can see within 120 feet of her. The wall is 60\
    \ feet long, 10 feet high, 5 feet thick, blocks line of sight, and sheds dim light\
    \ in a 10-foot radius. When the wall appears, each creature within its area is\
    \ pushed out of the wall's space, appearing on whichever side of the wall it wants,\
    \ and must succeed on a DC 20 Dexterity saving throw or take 14 (4d6) radiant\
    \ damage. Each 10-foot section of the wall has AC 15, 10 hp, vulnerability to\
    \ thunder damage, resistance to fire, slashing, and piercing damage, and immunity\
    \ to poison and psychic damage. The wall remains until the Queen uses this lair\
    \ action again, until she dismisses it as a bonus action, or until she dies. \
    \ \n- Disrupt Spellcasting. Until initiative count 20 on the next round, each\
    \ creature, other than fey, that casts a spell while within 60 feet of the Queen\
    \ must succeed on a DC 20 Constitution saving throw or the spell fails, expending\
    \ the spell slot.  \n- Moonlight Blast. A searing flare of moonlight bursts\
    \ from a point the Queen can see within 120 feet of her. Each creature within\
    \ 15 feet of that point must succeed on a DC 20 Dexterity saving throw, taking\
    \ 13 (3d8) radiant damage on a failed save, or half as much damage on a successful\
    \ one. A creature not in its true form has disadvantage on the saving throw, and\
    \ if it fails, it reverts to its true form.  "
  "name": ""
"regional_effects":
- "desc": "The region containing the Queen of Witches's lair is warped by the queen's\
    \ magic, which creates one or more of the following effects:"
  "name": ""
- "desc": "- Lunar Constancy. Despite the weather, the moon is always visible\
    \ for most of the night within 10 miles of the lair. Cloud cover has many breaks,\
    \ or the moon's light sharply penetrates the clouds.  \n- Moonlit Audience.\
    \ Calling the Queen of Witches's name under the light of the moon within 3 miles\
    \ of her lair draws her attention. She can choose to teleport to the supplicant\
    \ and hear their request. For 24 hours after the invocation, even if the Queen\
    \ never teleported to the supplicant, she has a connection to the area where the\
    \ supplicant called for her and can teleport to an unoccupied space within 30\
    \ feet of it or back to her lair as an action.  \n- Susurrating Fog. Silvery\
    \ fog is common within 10 miles of the lair, and strange whispers are heard within\
    \ the mist.  "
  "name": ""
- "desc": "If the Queen of Witches dies, these effects fade over the course of 1d10\
    \ days."
  "name": ""
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/queen-of-witches-tob1-2023.webp"
```
^statblock

## Environment

forest, mountain, planar