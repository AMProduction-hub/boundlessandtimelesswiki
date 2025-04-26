---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
statblock: inline
aliases: ["The Paladin"]
---

``` statblock
"name": "Sir Aldric, The Relentless (Merchant Mode)"
"size": "Medium"
"type": "humanoid (human)"
"alignment": "Lawful Good"
"ac": !!int "16"
"ac_class": "chain shirt"
"hp": !!int "175"
"hit_dice": "20d10 + 60"
"stats":
  - !!int "20"  # STR
  - !!int "12"  # DEX
  - !!int "16"  # CON
  - !!int "10"  # INT
  - !!int "14"  # WIS
  - !!int "18"  # CHA
"speed": "30 ft."
"skillsaves":
  "Insight": !!int "7"
  "Persuasion": !!int "9"
  "Perception": !!int "6"
  "Deception": !!int "6"
"senses": "passive Perception 16"
"languages": "Common, Celestial, Infernal"
"cr": "15"
"traits":
  - "name": "Calm but Ready"
    "desc": "Sir Aldric appears as a humble merchant, but retains sharp instincts. Gains +5 to initiative and draws his sword if combat begins."
  - "name": "Aura of Protection"
    "desc": "Allies within 10 ft. gain a bonus to saving throws equal to his Charisma modifier (+4)."
  - "name": "Lay Low"
    "desc": "While unarmored or in casual clothes, has advantage on Deception checks to appear non-threatening."
  - "name": "Divine Smite"
    "desc": "When hitting with a melee weapon attack, Aldric can expend a spell slot to deal an extra 2d8 radiant damage (plus 1d8 per spell level above 1st, max 5d8). Deals +1d8 more vs undead or fiends."
  - "name": "Second Wind (1/Short Rest)"
    "desc": "Regain 1d10 + 20 HP as a bonus action."
  - "name": "Action Surge (1/Short Rest)"
    "desc": "Take one additional action on his turn."
  - "name": "Riposte (Battlemaster Maneuver)"
    "desc": "When a creature misses him with a melee attack, can use a reaction to make a melee attack and add 1d12 damage if he hits."
"actions":
  - "name": "Concealed Greatsword (Carsomyr)"
    "desc": "Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 2d6 + 5 slashing + 3 radiant. On hit, may expend spell slot to use Divine Smite for bonus radiant damage."
  - "name": "Lay on Hands (100 HP/day)"
    "desc": "As an action, can restore up to 100 HP per day to self or others, or cure disease/poison (5 HP per condition)."
"bonus_actions":
  - "name": "Bonus Attack (Great Weapon Master)"
    "desc": "If he scores a critical hit or reduces a target to 0 HP, may make one additional weapon attack as a bonus action."
"reactions":
  - "name": "Riposte"
    "desc": "When missed by a melee attack, makes a melee weapon attack and adds 1d12 damage on hit."
"source":
  - "Custom NPC"
"image": "[[SirAldric_BakerMode.png]]"

```

```statblock
"name": "Sir Aldric, The Relentless (Paladin Mode)"
"size": "Medium"
"type": "humanoid (human)"
"alignment": "Lawful Good"
"ac": !!int "20"
"ac_class": "plate armor"
"hp": !!int "235"
"hit_dice": "20d10 + 100"
"stats":
  - !!int "20"  # STR
  - !!int "12"  # DEX
  - !!int "20"  # CON
  - !!int "10"  # INT
  - !!int "14"  # WIS
  - !!int "18"  # CHA
"speed": "30 ft."
"skillsaves":
  "Insight": !!int "7"
  "Persuasion": !!int "9"
  "Athletics": !!int "10"
  "Perception": !!int "6"
"senses": "passive Perception 16"
"languages": "Common, Celestial, Infernal"
"cr": "18"
"traits":
  - "name": "Aura of Protection"
    "desc": "Allies within 10 ft. gain a bonus to all saving throws equal to his Charisma modifier (+4)."
  - "name": "Aura of Courage"
    "desc": "Allies within 10 ft. cannot be frightened while Aldric is conscious."
  - "name": "Divine Smite"
    "desc": "When Aldric hits with a melee weapon attack, he may expend a spell slot to deal radiant damage: +2d8 (1st-level slot), +1d8 per level above 1st. +1d8 more vs undead or fiends."
  - "name": "Unyielding Will"
    "desc": "Advantage on saving throws against being charmed, frightened, or possessed."
  - "name": "Second Wind (1/Short Rest)"
    "desc": "Regain 1d10 + 20 HP as a bonus action."
  - "name": "Action Surge (1/Short Rest)"
    "desc": "Take one additional action on his turn."
  - "name": "Riposte (Battlemaster Maneuver)"
    "desc": "When a creature misses him with a melee attack, can use a reaction to make a melee attack and add 1d12 extra damage."
  - "name": "Legendary Resistance (3/Day)"
    "desc": "If Aldric fails a saving throw, he can choose to succeed instead."
"actions":
  - "name": "Greatsword of Judgement (Carsomyr)"
    "desc": "Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 2d6 + 5 slashing + 3 radiant. May expend spell slot to smite. Target loses magical benefits (Dispel Magic effect) on hit once per turn (DC 17)."
  - "name": "Lay on Hands (100 HP/day)"
    "desc": "As an action, Aldric can restore up to 100 HP per day, or cure disease/poison (5 HP per condition)."
  - "name": "Smite the Unholy (Recharge 5–6)"
    "desc": "Aldric channels divine energy. Each creature of fiend or undead type within 15 ft. must succeed on a DC 17 Con save or take 6d10 radiant damage and be blinded until end of Aldric’s next turn. Half on save."
"bonus_actions":
  - "name": "Great Weapon Master Strike"
    "desc": "Before making an attack, Aldric may choose to take a –5 penalty to hit. If he hits, he adds +10 to the damage."
  - "name": "Bonus Attack (GWM)"
    "desc": "If he scores a critical hit or reduces a target to 0 HP, he may make one weapon attack as a bonus action."
"reactions":
  - "name": "Riposte"
    "desc": "When a creature misses with a melee attack, Aldric makes a melee weapon attack and adds 1d12 extra damage."
"legendary_actions":
  - "name": "Move"
    "desc": "Aldric moves up to his speed without provoking opportunity attacks."
  - "name": "Smite Attack"
    "desc": "Aldric makes a melee attack with his Greatsword of Judgement. If it hits, he smites with a 2nd-level spell slot."
  - "name": "Dispel Wave (Costs 2 Actions)"
    "desc": "Aldric casts *Dispel Magic* at 3rd level, targeting a creature he can see within 30 ft."
"source":
  - "Custom NPC"
"image": "[[SirAldric_PaladinMode.png]]"

```
