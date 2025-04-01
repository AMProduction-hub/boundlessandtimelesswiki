---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/mabjov
- ttrpg-cli/monster/cr/13
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/half-elf
statblock: inline
aliases: ["Jaheira"]
---
# [Jaheira](03 - Player Log & Handouts\Mechanics\CLI\bestiary\npc/jaheira-mabjov.md)
*Source: Minsc and Boo's Journal of Villainy p. 60*  

Jaheira is a half-elf druid and an experienced leader within the organization known as the Harpers. She originally traveled to the Sword Coast with Khalid, her husband and fellow Harper, to investigate the Iron Crisis of 1368 DR on behalf of the secretive organization. Khalid was killed during the mission and Jaheira has never remarried. Although harsh and somewhat abrasive, Jaheira is fiercely loyal to the Harpers.

Born to a noble Tethyrian family loyal to King Alemander, Jaheira lost her parents at a young age at the hands of a mob during the country's violent civil war. She would have met the same fate, had a servant not saved her by smuggling her out of the castle. Chance led the pair to find a group of druids in the nearby forest, which took Jaheira in and raised her.

Jaheira believes that true balance and protection of nature can only come through action. When given no other choice, however, Jaheira strongly prefers to facilitate good over evil.

Jaheira has been a member of the Harpers for more than a century, though her elven blood gives her an appearance that is still relatively youthful. However, her age means that she is no longer an active Harper agent. Instead she seeks out those that she feels might help with the Harper cause and tries to recruit them. Jaheira is always on the lookout for an excuse to go back out on to the field and use her magic to destroy those who would harm the natural world or oppose the goals of the Harpers.

## Jaheira as a Contact

Jaheira becomes available as a contact for the Harpers at 9th level. Jaheira can put you in contact with a powerful Harper ally. These allies can come to your aid in a time of need. The cost is a magic item that Jaheira enchants. When you require assistance, you may read the magical rune and your item will vanish to be replaced by a powerful ally who will fight by your side for one hour.

**Allies via Jaheira**

| Ally | Required Level | Magic Item Sacrifice |
|------|----------------|----------------------|
| Mage, unicorn or Vellin (see entry in on next page) | 9 | Uncommon Boots, Cloak, Ring, Rod, Staff, Wand or Weapon |
| Assassin (named Arylin Moonblade), young silver dragon or deva | 12 | Uncommon Boots, Cloak, Ring, Rod, Staff, Wand or Weapon |
| Archmage (named either alustriel silverhand, Elminster Aumar or laeral silverhand), adult brass dragon or Jaheira | 14 | Rare Boots, Cloak, Ring, Rod, Staff, Wand or Weapon |
| Planetar | 16 | Rare Boots, Cloak, Ring, Rod, Staff, Wand or Weapon |
^allies-via-jaheira

```statblock
"name": "Jaheira (MaBJoV)"
"size": "Medium"
"type": "humanoid"
"subtype": "half-elf"
"alignment": "Neutral"
"ac": !!int "11"
"ac_class": "16 with [barkskin](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/barkskin.md)"
"hp": !!int "150"
"hit_dice": "20d8 + 60"
"stats":
- !!int "14"
- !!int "12"
- !!int "16"
- !!int "12"
- !!int "20"
- !!int "15"
"speed": "30 ft."
"saves":
  "Wisdom": !!int "10"
  "Constitution": !!int "8"
"skillsaves":
  "Medicine": !!int "10"
  "Nature": !!int "6"
  "Perception": !!int "10"
"senses": "darkvision 60 ft., passive Perception 20"
"languages": "Common, Druidic, Elvish, Sylvan"
"cr": "13"
"traits":
- "desc": "Jaheira casts ones of the following spells, using Wisdom as the spellcasting\
    \ ability (spell save DC 18):\n\nAt will: [barkskin](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/barkskin.md),\
    \ [druidcraft](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/druidcraft.md),\
    \ [poison spray](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/poison-spray.md),\
    \ [produce flame](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/produce-flame.md),\
    \ [shillelagh](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/shillelagh.md)\n\
    \n1/day each: [heal](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/heal.md),\
    \ [heroes' feast](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/heroes-feast.md),\
    \ [stoneskin](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/stoneskin.md)\n\
    \n2/day each: [animal messenger](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/animal-messenger.md),\
    \ [commune with nature](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/commune-with-nature.md)\
    \ (as an action), [entangle](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/entangle.md),\
    \ [speak with animals](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/speak-with-animals.md)"
  "name": "Spellcasting"
- "desc": "Jaheira has advantage on saving throws against being [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
    \ and magic can't put Jaheira to sleep."
  "name": "Fey Ancestry"
"actions":
- "desc": "Jaheira makes three Quarterstaff attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 5\
    \ (1d8 + 5) bludgeoning damage plus 21 (6d6) thunder damage."
  "name": "Quarterstaff"
- "desc": "Jaheira targets a creature she can see within 60 feet and causes a swarm\
    \ of flying insects to cover the creature. The creature must make a DC 18 Constitution\
    \ saving throw, taking 44 (8d10) piercing damage on a failed save, or half as\
    \ much damage on a successful one. If the target fails their saving throw they\
    \ are also [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ until the end of their next turn."
  "name": "Cleansing Plague (Recharge 6)"
"bonus_actions":
- "desc": "Jaheira summons three CR 2 Beasts or six CR 1 Beasts. These summoned creatures\
    \ have maximum hit points and the damage they inflict is considered magical for\
    \ the purpose of overcoming immunity and resistance to nonmagical attacks and\
    \ damage."
  "name": "Mighty Summons (1/Day)"
"source":
- "MaBJoV"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/npc/token/jaheira-mabjov.webp"
```
^statblock