---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/13
- ttrpg-cli/monster/environment/coastal
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Nihileth Aboleth"]
---
# [Nihileth Aboleth](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/nihileth-aboleth-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 9*  

*Eons ago, a group of aboleth left the Material Plane to wander through distant planes—seeing them through magical scrying was not enough, so these aboleth used astral magic and bodily travel to see far beyond normal realms*.

## A Forgotten Tribe

As ages passed, memories of those who departed slowly faded from the minds of those aboleth who remained behind. Those few aboleth who did remember that long ago some of their kin had gone plane-wandering assumed that the wanderers died in distant hells or paradises.

## Changed by Planar Wandering

The plane-wanderers hadn't died. Instead, their eons-long exposure to alien realms and the space between changed them, restructuring their life force, making them into something even more nightmarish—but better able to withstand both strange hells and golden realms of eldritch delight. They returned even more corrupt and powerful than when left, and these wandering nihileths returned to the mortal world intent on spreading the influence of the Void and the utter evil they found in the vast darkness between worlds.

## Undead Servitors

Humanoids, giants, and monstrosities that succumb to the nihileth's disease transform into servitors for the twisted aboleths. Most humanoids transform into nihilethic zombies, while the larger giants and monstrosities transform into nihilethic dominators. While the creatures retain much of the general shape they had in life, these servitors have translucent and slimy skin, and are adept swimmers, able to function in water or on land in service to their nihileth masters.

## A Nihileth's Lair

While aboleths create their lairs underwater, spending most of their time submerged, a nihileth can create a lair outside the water, often in a cave or a ruined, abandoned city. Nihileth lairs on land typically contain several pools of water and are often within at least 1 mile of a large body of water, as the nihileth's ability to fully function outside of water is limited.

```statblock
"name": "Nihileth Aboleth (ToB1-2023)"
"size": "Large"
"type": "undead"
"alignment": "Chaotic Evil"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "157"
"hit_dice": "21d10 + 42"
"stats":
- !!int "21"
- !!int "9"
- !!int "15"
- !!int "18"
- !!int "15"
- !!int "18"
"speed": "10 ft., fly 40 ft. (hover) in void ghost form, swim 40 ft."
"saves":
  "Wisdom": !!int "7"
  "Intelligence": !!int "9"
  "Constitution": !!int "7"
"skillsaves":
  "Perception": !!int "10"
  "History": !!int "12"
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "cold, necrotic, poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)"
"senses": "darkvision 120 ft., passive Perception 20"
"languages": "telepathy 120 ft., Void Speech"
"cr": "13"
"traits":
- "desc": "The nihileth has resistance to acid, fire, lightning, and thunder damage,\
    \ it has immunity to the [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)\
    \ condition, and it has immunity to bludgeoning, piercing, and slashing damage\
    \ from nonmagical attacks. In addition, the nihileth can move through other creatures\
    \ and objects as if they were difficult terrain. It takes 5 (1d10) force damage\
    \ if it ends its turn inside an object."
  "name": "Ghostly Body (Void Ghost Form Only)"
- "desc": "If a creature communicates telepathically with the nihileth, or deals psychic\
    \ damage to it, the creature must succeed on a DC 15 Wisdom saving throw or become\
    \ infected with the nihilethic rot disease."
  "name": "Infecting Telepathy"
- "desc": "This disease takes 1 minute to manifest in an infected creature, during\
    \ which time the disease can be removed with the [lesser restoration](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/lesser-restoration.md)\
    \ spell. After 1 minute, the creature's flesh becomes slimy and translucent, and\
    \ the disease can be cured only by the [heal](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/heal.md)\
    \ spell or similar magic. Until this disease is cured, the creature can't regain\
    \ hp unless it is submerged in water, and it can breathe air and water. The creature\
    \ must be submerged in water at least once every 2 hours to avoid suffocating,\
    \ and if it is outside a body of water, it takes 7 (2d6) acid damage every 10\
    \ minutes, unless moisture is applied to its skin before 10 minutes have passed.\
    \ If a Humanoid dies while infected with this disease, it rises 1 minute later\
    \ as a nihilethic zombie under the nihileth's control. If a Large giant or monstrosity\
    \ dies while infected with this disease, it rises 1 minute later as a nihilethic\
    \ dominator under the nihileth's control."
  "name": "Nihilethic Rot"
- "desc": "If damage reduces the nihileth to 0 hp, it must make a Constitution saving\
    \ throw with a DC of 5 + the damage taken, unless the damage is radiant or from\
    \ a critical hit. On a success, the nihileth drops to 1 hp instead."
  "name": "Undead Fortitude"
- "desc": "The nihileth doesn't require air, food, drink, or sleep."
  "name": "Undead Nature"
- "desc": "The nihileth is surrounded by a chilling cloud. A creature that isn't a\
    \ construct or undead and that starts its turn within 5 feet of the nihileth must\
    \ succeed on a DC 15 Constitution saving throw or its speed is halved until the\
    \ start of its next turn. In addition, a creature infected with nihilethic rot\
    \ takes 7 (2d6) cold damage when it starts its turn within this aura."
  "name": "Void Aura"
"actions":
- "desc": "The nihileth makes two Tentacle attacks and one Tail attack, or it makes\
    \ three Withering Touch attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +10 to hit, reach 10 ft. one target. Hit: 15\
    \ (3d6 + 5) bludgeoning damage."
  "name": "Tail (Undead Form Only)"
- "desc": "Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 12\
    \ (2d6 + 5) bludgeoning damage, and the target must succeed on a DC 15 Constitution\
    \ saving throw or contract the nihilethic rot disease (see the Nihilethic Rot\
    \ trait)."
  "name": "Tentacle (Undead Form Only)"
- "desc": "Melee Spell Attack: +9 to hit, reach 10 ft., one creature. Hit: 14\
    \ (3d6 + 4) necrotic damage."
  "name": "Withering Touch (Void Ghost Form Only)"
"bonus_actions":
- "desc": "The nihileth magically transforms into a dark purple, Void ghost form or\
    \ back into its Undead form. Its statistics, other than its speed, resistances,\
    \ and immunities, are the same in each form. Any equipment it is wearing or carrying\
    \ changes with it. It reverts to its Undead form if it dies."
  "name": "Void Shape"
"reactions":
- "desc": "When the nihileth takes damage, it can reduce the damage to 0. Radiant\
    \ damage can be reduced by only half."
  "name": "Void Body"
"legendary_actions":
- "desc": "The nihileth makes a Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ check."
  "name": "Detect"
- "desc": "The nihileth makes one Tail attack."
  "name": "Tail Swipe"
- "desc": "One creature infected with the nihilethic rot disease within 30 feet of\
    \ the nihileth takes 10 (3d6) psychic damage, and the nihileth regains hp equal\
    \ to that amount."
  "name": "Rotten Drain (Costs 2 Actions)"
"lair_actions":
- "desc": "On initiative count 20 (losing initiative ties), the nihileth can take\
    \ a lair action to cause one of the following effects; the nihileth can't use\
    \ the same effect two rounds in a row:"
  "name": ""
- "desc": "- Open the Void. Up to three points in water the nihileth can see within\
    \ 90 feet of it become conduits to the Void. Each creature within 10 feet of a\
    \ point must succeed on a DC 15 Wisdom saving throw or take 7 (2d6) necrotic\
    \ damage.  \n- Void Absorbance. The nihileth can pull the life force from\
    \ nearby nihilethic zombies and dominators to replenish its own life. Nihilethic\
    \ dominators and zombies within 30 feet of the nihileth take a total of 21 (6d6)\
    \ psychic damage, divided evenly between them, and the nihileth regains hp equal\
    \ to that amount. If a zombie or dominator is reduced to 0 hp from this damage,\
    \ it is destroyed.  \n- Void Shuffle. The nihileth calls on the power of the\
    \ Void within its lair to rearrange its servitors. The nihileth can teleport each\
    \ nihilethic dominator and zombie it can see within 60 feet of it to an unoccupied\
    \ space within 15 feet of the target's starting location.  "
  "name": ""
"regional_effects":
- "desc": "The region containing a nihileth's lair is corrupted by its presence, which\
    \ creates one or more of the following effects:"
  "name": ""
- "desc": "- Befouled Water. Water sources within 1 mile of a nihileth's lair\
    \ are not only supernaturally fouled but can spread the nihileth's disease. A\
    \ creature that drinks such water must succeed on a DC 11 Constitution saving\
    \ throw or become infected with thenihilethic rotdisease (see the Nihilethic\
    \ Rot trait).  \n- Thinned Veil. The veil between the Material Plane and the\
    \ Void is thinner within 1 mile of the nihileth's lair. Beasts born or hatched\
    \ in the area often have additional vestigial limbs, protoeyes, black or sludge-like\
    \ blood, or similar signs of the corrupting influence of the Void.  "
  "name": ""
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/nihileth-aboleth-tob1-2023.webp"
```
^statblock

## Environment

coastal, underdark, underwater