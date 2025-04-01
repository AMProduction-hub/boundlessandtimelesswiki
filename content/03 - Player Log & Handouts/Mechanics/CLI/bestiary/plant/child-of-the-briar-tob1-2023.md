---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/plant
statblock: inline
aliases: ["Child of the Briar"]
---
# [Child of the Briar](03 - Player Log & Handouts\Mechanics\CLI\bestiary\plant/child-of-the-briar-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 55*  

*Its eyes gleam like polished walnuts, and its sly smile seems oddly placed on the tiny body, covered in spikes and thorns. The creature's waist is no thicker than a clenched fist, and its sinuous arms are no wider than a finger but twice the length of its body.*

## Born of Magic

Children of the briar are a frequent nuisance to fey and mortal alike. They grow in deep briar patches in forest clearings or along sunny hillsides and riverbanks. More rarely, they spawn when a sorcerer or magical creature's blood is spilled on the forest floor, or when summoned into being by obscure druidic items of power.

## Thorn Fortresses

Despite their size, children of the briar gather in great numbers, cultivating ancient forest thickets into veritable fortresses. Wise men flee when they hear the clicking language in the underbrush, for children of the briar have the capricious wickedness of spiteful children and a taste for blood.

## Spies and Scouts

From their lairs, children of the briar creep far and wide to spy on the forest's inhabitants, sometimes using spiders, monstrous centipedes, and giant dragonflies as mounts. They converse with travelers bearing interesting news, but their words are thorned with gleeful malice, jealous bile, and lies. They are not above murder. They trade news and gossip for trinkets, favors, and drops of spilled blood.

## Fey Blessed

The fey have long used children of the briar as spies and informants. The power of the fey courses through their veins, allowing them to work simple magical tricks and slip between the mortal and fey realms with relative ease.

```statblock
"name": "Child of the Briar (ToB1-2023)"
"size": "Tiny"
"type": "plant"
"alignment": "Neutral Evil"
"ac": !!int "13"
"hp": !!int "50"
"hit_dice": "20d4"
"stats":
- !!int "6"
- !!int "17"
- !!int "11"
- !!int "13"
- !!int "10"
- !!int "14"
"speed": "20 ft., climb 10 ft."
"skillsaves":
  "Stealth": !!int "7"
  "Perception": !!int "4"
"damage_vulnerabilities": "fire"
"senses": "darkvision 60 ft., passive Perception 14"
"languages": "Briarclick, Common, Sylvan"
"cr": "1"
"traits":
- "desc": "The child of the briar has advantage on saving throws against being [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
    \ and magic can't put it to sleep."
  "name": "Fey Ancestry"
"actions":
- "desc": "The child of the briar makes two Claw attacks. If both attacks hit a Medium\
    \ or smaller creature, the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 13). At the start of each of the [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ creature's turns, it takes 2 (1d4) piercing damage. The child of the briar\
    \ can have only one target [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ at a time."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6\
    \ + 3) piercing damage."
  "name": "Claw"
- "desc": "Ranged Weapon Attack: +5 to hit, range 20/60 ft., one target. Hit:\
    \ 6 (1d6 + 3) piercing damage."
  "name": "Spitdart Tongue (Recharge 4-6)"
- "desc": "While within 10 feet of at least one other child of the briar, this child\
    \ can cast the [entangle](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/entangle.md)\
    \ spell (spell save DC 13). Each friendly child of the briar within 30 feet of\
    \ this child can use its reaction to join the casting. For each child beyond the\
    \ first participating in the casting, the save DC increases by 1, to a maximum\
    \ of DC 17, and the size increases by 5 feet, to a maximum of a 40-foot square.\
    \ The entangled area must include at least one of the children involved in the\
    \ casting. All participating children of the briar are immune to the spell's effects."
  "name": "Entangle"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/plant/token/child-of-the-briar-tob1-2023.webp"
```
^statblock

## Environment

forest