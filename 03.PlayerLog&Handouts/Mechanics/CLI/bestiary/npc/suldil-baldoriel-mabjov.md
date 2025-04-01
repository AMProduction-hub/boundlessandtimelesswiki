---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/mabjov
- ttrpg-cli/monster/cr/10
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/half-elf
statblock: inline
aliases: ["Suldil Baldoriel"]
---
# [Suldil Baldoriel](03 - Player Log & Handouts\Mechanics\CLI\bestiary\npc/suldil-baldoriel-mabjov.md)
*Source: Minsc and Boo's Journal of Villainy p. 66*  

More than a thousand years ago, Suldil was born to a human boatswain and his sea-elf bride. Her innate magical prowess brought her to the attention of the fledgling order of the Knights of Bahamut. The Knights of Bahamut were an order of dragon riders that worshipped Bahamut and bonded to young metallic dragons.

The rise of the Knights of Bahamut was meteoric in its speed, but so was their fall. They vanished from the history books in 250 DR, victims of their own success. Fearful of the rising power of the Knights of Bahamut, their enemies formed an alliance that struck quickly and brutally. When the final days came, Suldil was a veteran dragon rider bonded to a beautiful bronze dragon. She was happily married and the proud mother to a son. In a single night Suldil lost everything. She survived only through the intervention of a nymph of the Feywild. The nymph took Suldil into her sylvan realm at night when the enemies of the Knights of Bahamut were killing the other riders, dragons and their families.

Suldil would stay in the Feywild for a decade. Not out of her own choice, but because of the obsession of the nymph. The fey creature was enamored with Suldil and had no desire to let her go. It was only through years of Suldil's pleas that the nymph finally allowed the former knight to return to her world. When Suldil was finally released from the Feywild, a decade had passed for her, but a millennium had passed in the mortal world. It was the harshest way to learn that time flows differently in the Feywild.

Suldil is disheartened that the Knights of Bahamut have vanished from history. She prayed to Bahamut and was surprised when she was given a vision. The vision led her to the lair of a bronze dragon killed by fortune hunters. One of the dragon's eggs was hidden beneath a pile of copper that the hunters had left behind. Suldil bonded with the bronze wyrmling that hatched from the egg a few months later.

Suldil wants to bring the Order of Bahamut back and searches for candidates that she thinks are worthy of joining her resurrected order.

## Suldil as a Contact

Suldil becomes a contact for members of the Knights of Bahamut at 9th level. Suldil has access to the scrolls and texts of the ancient Knights of Bahamut. This includes the formula for transforming certain magic items into more powerful items. A successful [History](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#History) check is required to hunt down all of the appropriate scrolls and texts.

**Enhancing Magic Items via Suldil**

| Magic Item | Magic Item Needed As A Component | History Check DC | Material Cost |
|------------|----------------------------------|------------------|---------------|
| Bead of force | Uncommon wondrous item | 20 | 100 gp |
| Horn of blasting | Uncommon wondrous item | 15 | 100 gp |
| Javelin of lightning | Uncommon magical weapon | 10 | 50 gp |
| Ring of feather falling | Uncommon ring | 10 | 100 gp |
| Ring of resistance—lightning | Uncommon ring | 15 | 150 gp |
| Ring of the ram | Uncommon ring | 15 | 150 gp |
| Staff of thunder and lightning | Rare rod, staff or wand | 20 | 500 gp |
| Wand of lightning bolts | Uncommon rod, staff or wand | 15 | 300 gp |
^enhancing-magic-items-via-suldil

```statblock
"name": "Suldil Baldoriel (MaBJoV)"
"size": "Medium"
"type": "humanoid"
"subtype": "half-elf"
"alignment": "Chaotic Good"
"ac": !!int "12"
"ac_class": "15 with [mage armor](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/mage-armor.md)"
"hp": !!int "137"
"hit_dice": "25d8 + 25"
"stats":
- !!int "10"
- !!int "14"
- !!int "12"
- !!int "12"
- !!int "14"
- !!int "20"
"speed": "30 ft."
"saves":
  "Charisma": !!int "9"
  "Constitution": !!int "5"
"skillsaves":
  "Deception": !!int "9"
  "Arcana": !!int "9"
  "Persuasion": !!int "9"
"damage_resistances": "lightning"
"senses": "passive Perception 12"
"languages": "Celestial, Common, Draconic, Elvish"
"cr": "10"
"traits":
- "desc": "Suldil casts one of the following spells, using Charisma as the spellcasting\
    \ ability (spell save DC 17):\n\nAt will: [detect magic](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/detect-magic.md),\
    \ [light](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/light.md),\
    \ [mage hand](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/mage-hand.md)\n\
    \n1/day: [disintegrate](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/disintegrate.md)\n\
    \n2/day each: [counterspell](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/counterspell.md),\
    \ [shield](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/shield.md)"
  "name": "Spellcasting"
- "desc": "Suldil is accompanied by a [young bronze dragon](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/dragon/young-bronze-dragon.md).\
    \ The dragon allows Suldil to use him as a mount."
  "name": "Young Bronze Dragon"
"actions":
- "desc": "Melee or Ranged Spell Attack: +9 to hit, reach 5 ft. or range 120 ft.,\
    \ one target. Hit: 21 (3d10 + 5) lightning damage."
  "name": "Bronze Bolt"
- "desc": "Suldil discharges a burst of energy in a 60-foot-radius. Each creature\
    \ in that area must make a DC 17 Dexterity saving throw, taking 44 (8d10) lightning\
    \ damage on failed save, half as much damage on a successful save."
  "name": "Explosion (1/Day)"
"bonus_actions":
- "desc": "If Suldil isn't mounted, she can use a bonus action to magically teleport\
    \ onto her young bronze dragon mount, provided Suldil and the young bronze dragon\
    \ are on the same plane of existence. When she teleports, Suldil appears astride\
    \ the young bronze dragon along with any equipment she is wearing or carrying.\
    \ While mounted and not [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated),\
    \ Suldil can't be surprised, and both her and her mount gain advantage on Dexterity\
    \ saving throws."
  "name": "Mounted"
"source":
- "MaBJoV"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/npc/token/suldil-baldoriel-mabjov.webp"
```
^statblock