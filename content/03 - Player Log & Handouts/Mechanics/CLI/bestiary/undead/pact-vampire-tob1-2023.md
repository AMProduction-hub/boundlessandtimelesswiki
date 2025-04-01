---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/15
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Pact Vampire"]
---
# [Pact Vampire](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/pact-vampire-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 380*  

*Blood flows up the slain man's body, defying gravity as it makes its way into the skin and fanged maw of this wild-haired vampire.*

Pact warlocks seek transformation into a vampire while blessed by a patron of blood, destruction, or undead. The pact vampire's thirst for blood is so all-consuming that it can draw the blood of others through the air to its open maw.

## Blood Line

The patron's blessing frees the warlock from some of a vampire's weaknesses, but it also secures a magical line of blood and life energy between the warlock and the patron. This drives the warlock to wantonly shed and drink blood, fueling the patron with each drop. A pact vampire must feed blood to its patron weekly by shedding the blood of other creatures and absorbing that blood into its body. A pact vampire that forgets or refuses to shed blood for its patron begins to lose vitality, steadily becoming more gaunt until it withers into a mindless, skincovered skeleton under the patron's control.

## Transformed Vampires

Not all pact vampires start as living warlocks. Some vampires choose to make a pact with a foul power to diminish some of its weaknesses and to gain more control over its own blood and the blood of others. Such vampires transform into pact vampires, giving up some of their autonomy for greater power and safety from running water and sunlight. Regardless of how it initially transformed, a pact vampire can't change its form like a standard vampire, relying on its followers and its patron's power to ensure its safe exit from dangerous situations.

## Poisonous Blood

A pact vampire's blood is tainted by its enhanced magical connection to its patron, and when introduced to living creatures, the vampire's blood causes the creature's blood to flow more freely. Pact vampires coat their claws in this blood to better subdue and sup from bleeding victims. Particularly brave alchemists have attempted to harvest pact vampire blood for use in treating diseases related to thick or sluggish blood, but few survive the attempt.

> [!note] A Pact of a Different Color
> 
> The pact vampire represented here is based on the Fiend patron. Not all patrons, especially those of good alignment, would condone their warlocks seeking transformation into an especially bloodthirsty vampire. Those patrons who are associated with blood, destruction, or undeath, however, take special glee in aiding such a transformation, reveling in the blood shed by the warlock and sending their minions to assist in the mayhem.
> 
> If you want to bring a pact vampire into play from a different patron, consider some changes. Damage resistances, immunities, and actions like Children of the Lower Planes can be changed to reflect a different pact, such as resistance to damage from weapons not made with cold iron for a pact vampire whose patron is one of the fey lords or ladies (see Tome of Beasts) or magically calling mephits and other minor elementals for a pact vampire whose patron is a genie lord.
^a-pact-of-a-different-color

## A Pact Vampire's Lair

Needing to be near civilization for ready access to the blood its patron craves, a pact vampire dwells in a city's catacombs, sewers, or other underground complex with easy access to the city's streets at night. Pact vampires often lead secret cults within the city, building its patron's followers while drinking in the blood of the victims the cult brings to it. Due to the pact vampire's more direct link to the patron than many warlocks, the lair takes on aspects of the patron and is subtly shaped by the patron's will, filling the lair with hellish heat, eldritch lights, sourceless screams, and similar effects pleasing to that particular patron.

```statblock
"name": "Pact Vampire (ToB1-2023)"
"size": "Medium"
"type": "undead"
"alignment": "Any Evil alignment"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "178"
"hit_dice": "17d8 + 102"
"stats":
- !!int "22"
- !!int "16"
- !!int "22"
- !!int "17"
- !!int "15"
- !!int "20"
"speed": "30 ft."
"saves":
  "Charisma": !!int "10"
  "Dexterity": !!int "8"
  "Wisdom": !!int "7"
  "Constitution": !!int "11"
"skillsaves":
  "Stealth": !!int "8"
  "Perception": !!int "7"
  "Persuasion": !!int "10"
"damage_resistances": "necrotic; bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 120 ft., passive Perception 17"
"languages": "the languages it knew in life"
"cr": "15"
"traits":
- "desc": "The pact vampire can pinpoint the location of creatures that aren't Constructs\
    \ or Undead within 60 feet of it and can sense the general direction of such creatures\
    \ within 1 mile of it."
  "name": "Blood Sense"
- "desc": "If the pact vampire fails a saving throw, it can choose to succeed instead."
  "name": "Legendary Resistance (3/Day)"
- "desc": "A creature that hits the pact vampire with a melee attack while within\
    \ 5 feet of it takes 7 (2d6) poison damage."
  "name": "Poisonous Blood"
- "desc": "The pact vampire regains 25 hp at the start of its turn if it has at least\
    \ 1 hp and isn't in sunlight. If the vampire takes radiant damage or damage from\
    \ holy water, this trait doesn't function at the start of the vampire's next turn."
  "name": "Regeneration"
- "desc": "The pact vampire doesn't require air."
  "name": "Undead Nature"
- "desc": "The pact vampire has the following flaws:"
  "name": "Vampire Weaknesses"
- "desc": "If a piercing weapon made of wood is driven into the vampire's heart while\
    \ the vampire is [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ in its resting place, the vampire is [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ until the stake is removed."
  "name": "Stake to the Heart"
- "desc": "The vampire takes 10 radiant damage when it starts its turn in sunlight.\
    \ While in sunlight, it has disadvantage on attack rolls and ability checks."
  "name": "Sunlight Hypersensitivity"
"actions":
- "desc": "The pact vampire makes three Claw attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 13\
    \ (2d6 + 6) slashing damage plus 13 (3d8) poison damage."
  "name": "Claw"
- "desc": "The pact vampire draws the blood out of a bleeding creature's body, where\
    \ it flows through the air into the vampire's mouth. One creature the vampire\
    \ can see within 60 feet of it that doesn't have all its hp and isn't a Construct\
    \ or Undead must succeed on a DC 18 Constitution saving throw or take 22 (4d10)\
    \ necrotic damage, and its hp maximum is reduced by that amount. The vampire regains\
    \ hp equal to half the damage dealt. This reduction lasts until the target finishes\
    \ a long rest. The target dies if this effect reduces its hp maximum to 0."
  "name": "Call Blood"
- "desc": "One Humanoid the vampire can see within 30 feet of it must succeed on a\
    \ DC 18 Wisdom saving throw or be magically [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ for 1 day. The [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ target obeys the vampire's verbal commands. If the target suffers any harm or\
    \ receives a suicidal command, it can repeat the saving throw, ending the effect\
    \ on itself on a success. If the target's saving throw is successful or the effect\
    \ ends for it, the target is immune to this vampire's Charm for the next 24 hours.\n\
    \nThe vampire can have only one target [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ at a time. If it charms another, the effect on the previous target ends."
  "name": "Charm"
- "desc": "The pact vampire magically calls 2d4 dretches, 1d4 imps, or 1 bearded\
    \ devil. The called Fiends arrive in 1d4 rounds, acting as allies of the vampire\
    \ and obeying its spoken commands. The Fiends remain for 1 hour, until the vampire\
    \ dies, or until the vampire dismisses them as a bonus action."
  "name": "Children of the Lower Planes (1/Day)"
"legendary_actions":
- "desc": "The pact vampire moves up to its speed without provoking opportunity attacks."
  "name": "Move"
- "desc": "The pact vampire uses Call Blood."
  "name": "Call Blood (Costs 2 Actions)"
- "desc": "The pact vampire's blood briefly turns into a mist around it. Each creature\
    \ within 15 feet of the vampire must succeed on a DC 18 Constitution saving throw\
    \ or take 14 (4d6) poison damage and be [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ until the end of its next turn."
  "name": "Spread Poison (Costs 2 Actions)"
"regional_effects":
- "desc": "The region containing a pact vampire's lair is warped by its presence,\
    \ which creates one or more of the following effects."
  "name": ""
- "desc": "- Hemophilia. Creatures bleed more easily within 3 miles of the lair,\
    \ causing even the slightest scratch to bleed a little longer than usual.  \n\
    - Overcast Skies. The area within 6 miles of the lair is perpetually overcast\
    \ with bits of moonlight peeking through the thick clouds on nights important\
    \ to the vampire or its patron.  \n- Thinned Veil. The veil between the Material\
    \ Plane within 1 mile of the lair and the vampire's patron's home plane is thinned.\
    \ Conjuration spells that pull from the patron's home plane are more potent and\
    \ last longer, and planar travel between the Material Plane and the patron's home\
    \ plane is easier.  "
  "name": ""
- "desc": "If the pact vampire dies, these effects fade over the course of 1d10\
    \ days."
  "name": ""
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/pact-vampire-tob1-2023.webp"
```
^statblock

## Environment

urban