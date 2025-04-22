```statblock
"name": "Elira, Awakened by the Amulet"
"size": "Medium"
"type": "humanoid (human)"
"alignment": "Chaotic Good"
"ac": !!int "12"
"ac_class": "mage armor (if cast), otherwise 10 + DEX"
"hp": !!int "9"
"hit_dice": "1d6 + 3"
"stats":
  - !!int "8"   # STR
  - !!int "14"  # DEX
  - !!int "13"  # CON
  - !!int "12"  # INT
  - !!int "10"  # WIS
  - !!int "17"  # CHA
"speed": "30 ft."
"skillsaves":
  "Arcana": !!int "3"
  "Deception": !!int "5"
  "Stealth": !!int "4"
"senses": "passive Perception 10"
"languages": "Common, Elvish"
"cr": "1/8"
"traits":
  - "name": "Unstable Magic"
    "desc": "Whenever Elira casts a sorcerer spell of 1st level or higher, roll a d20. On a 1, roll on the Wild Magic Surge table."
  - "name": "Awakened Amulet"
    "desc": "Elira's amulet emits soft magical radiation. While she wears it, she has advantage on Constitution saving throws to maintain concentration, and her hair and eyes glow faintly when she casts spells."
  - "name": "Sorcerous Origin: Wild Magic"
    "desc": "Elira is a Wild Magic Sorcerer, although she is only just discovering what that means."
"actions":
  - "name": "Fire Bolt (Cantrip)"
    "desc": "Ranged Spell Attack: +5 to hit, range 120 ft., one target. Hit: 1d10 fire damage."
  - "name": "Shield (1st-level Spell)"
    "desc": "As a reaction when hit, Elira casts *Shield*, raising her AC by +5 until the start of her next turn."
  - "name": "Chaos Bolt (1st-level Spell)"
    "desc": "Ranged Spell Attack: +5 to hit. Hit: 2d8 + 1d6 damage. The type of damage is determined randomly."
"bonus_actions":
  - "name": "Sorcery Points (1/day)"
    "desc": "Regains 1 sorcery point once per day, which can be used to trigger subtle or quicken spell (DM's discretion)."
"reactions":
  - "name": "Shield"
    "desc": "See above."
"source":
  - "Custom NPC"
"image": "[[Elira.png]]"
