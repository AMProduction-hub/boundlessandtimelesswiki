---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1-2
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["War Ostrich"]
---
# [War Ostrich](03 - Player Log & Handouts\Mechanics\CLI\bestiary\beast/war-ostrich-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 393*  

*The large, flightless bird dove in and out of battle, screeching defiantly as its rider drove a spear into its foes.*

In the wild, war ostriches are dangerous and skittish, prone to lashing out with punishing kicks while sprinting around the battlefield. Humanoids in grasslands use them to create chaos by driving a flock of fast-moving war ostriches into a caravan or enemy troop formations.

## Faster than Horses

War ostriches have been domesticated for centuries. They are a fearsome sight on the field of combat when bearing warriors into battle. War ostriches are heavily employed in regions where horses are rare or impractical or where their leaping ability enables cavalry to charge over broken ground. Stubborn and willful, these creatures are difficult to train. Once trained though, they are loyal and fierce mounts, fighting to the death in battle alongside their riders.

> [!note] War Ostriches in Midgard
> 
> War ostriches are commonly found throughout the Southlands both as wild and domestic animals. The people of Nuria Natal, in particular, use war ostriches as beasts of burden and mounts along the River Nuria, switching to camels for long treks across the Crescent or Sarklan Deserts. Further south, gnolls and nkosi both hunt and domesticate war ostriches, and many warriors decorate their armor, clothing, or hair with the feathers of favored mounts who helped the warrior achieve greatness in battle.
^war-ostriches-in-midgard

```statblock
"name": "War Ostrich (ToB1-2023)"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "11"
"hp": !!int "42"
"hit_dice": "5d10 + 15"
"stats":
- !!int "15"
- !!int "12"
- !!int "16"
- !!int "2"
- !!int "10"
- !!int "5"
"speed": "60 ft."
"senses": "passive Perception 10"
"languages": ""
"cr": "1/2"
"traits":
- "desc": "If the war ostrich jumps at least 15 feet straight toward a creature and\
    \ then hits it with a Claw attack on the same turn, that target must succeed on\
    \ a DC 13 Strength saving throw or be knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone).\
    \ If the target is [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
    \ the ostrich can make one Beak attack against it as a bonus action."
  "name": "Leaping Pounce"
- "desc": "The war ostrich's long jump is up to 30 feet and its high jump is up to\
    \ 15 feet, with or without a running start."
  "name": "Standing Leap"
"actions":
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8\
    \ + 2) piercing damage."
  "name": "Beak"
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (2d4\
    \ + 2) bludgeoning damage."
  "name": "Claw"
- "desc": "The war ostrich screeches at a creature it can see within 30 feet of it.\
    \ The target must succeed on a DC 13 Wisdom saving throw or have disadvantage\
    \ on attack rolls until the end of its next turn, as the screech rattles it."
  "name": "Intimidating Screech"
"bonus_actions":
- "desc": "The war ostrich takes the Dash or Disengage action."
  "name": "Skittish"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/beast/token/war-ostrich-tob1-2023.webp"
```
^statblock

## Environment

grassland