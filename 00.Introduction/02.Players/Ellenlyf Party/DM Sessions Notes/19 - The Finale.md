# 🛤️ FINALE SESSION — THE MIDNIGHT TRAIN (DM PLAYBOOK)

> **Recommended Session Length:** 3.5–4 hours  
> **Tone:** Inevitable, lethal, Spaghetti Western  
> **Music:** Ambient Western → *The Trio* (Stage 4)

---

## PARTY STATUS AT SESSION START

- 6 PCs, Level 7
- 4 PCs heavily wounded
- No magical healing
- Hit Dice healing requires **full day**
- Ammo is finite and tracked
- No firearm proficiency (DEX / STR only)

This session assumes:
- Players **cannot fully reset**
- Attrition is intentional

---

## STAGE 1 — THE STOP  
### Oil Tank Ambush

**Time Budget:** ~45 minutes  
**Location:** Rail line near Stormwood, outskirts of Le Grant Kanyun  
**Goal:** Stop the train without triggering full alarm

---

### SCENE NOTES (READ THIS TO YOURSELF)

- This is **tense and quiet**
- Let players plan for 5–10 minutes
- Do NOT rush first contact
- Red Jack gives minimal instructions, no speeches

---

### ENEMY DEPLOYMENT (6 PCs)

- **6 Baron Rail Guards**
  - 2 on top of train cars
  - 2 patrolling near engine
  - 2 walking the rail line
- **1 Rail Sergeant**
  - Rifle, stays 40–60 ft back
  - Does NOT rush unless alarmed

---

### ENVIRONMENT NOTES

- Dim moonlight
- Half cover everywhere (crates, wheels, rail cars)
- Oil tank pulled by horses:
  - AC irrelevant
  - HP 40
  - On explosion: 3d10 fire, prone, loud

---

### ALARM TRACKER (DM TOOL)

- Silent takedown: +0 alarm
- Missed shot / loud hit: +1 alarm
- Explosion / scream: +2 alarm

At **3 alarm**:
- Train guards mobilize fully
- Stage 2 escalates

---

### WIN CONDITION

- Train halted
- Oil tank placed on rails
- Alarm ≤ 2

---

### FAIL FORWARD

If alarm ≥ 3:
- Train still stops
- Add:
  - **+2 Guards in Stage 2**
  - **Sniper deployed early**

---

## STAGE 2 — THE HOLD  
### Running Gunfight

**Time Budget:** ~60–75 minutes  
**Location:** Along the train  
**Goal:** Hold position while Red Jack’s gang extracts components

---

### SCENE NOTES

- This is the **main attrition fight**
- Let PCs feel:
  - Ammo pressure
  - Reload pain
  - Cover math stress
- Do NOT overdescribe — keep momentum

---

### BASE ENEMY WAVES (6 PCs)

#### Wave A — Initial Push
- **6 Baron Guards**
- Arrive from opposite side of train
- Aggressive, short range

#### Wave B — Suppression
- **1 Baron Sniper**
- **4 Baron Guards**
- Sniper targets:
  - Anyone exposed
  - Anyone not in cover

#### Wave C — Pressure Spike (Optional)
Use ONLY if party is holding too well.

- **3 Marshal Scouts**
- Revolvers + rifles
- They shoot once, then retreat

---

### ESCALATION RULE

If Stage 1 failed:
- Add **+2 Guards total across waves**
- Sniper arrives at start of Wave B automatically

---

### EXIT CONDITION

- Red Jack’s gang secures:
  - Generator
  - Dinamo
  - Copper Cables

Red Jack yells:
> *“Barang di tangan. Mundur.”*

---

## STAGE 3 — THE COLLAPSE  
### Trap Revealed

**Time Budget:** ~30–40 minutes  
**Location:** Rail yard / canyon mouth  
**Goal:** Escape with components

---

### SCENE NOTES

- This is NOT a fair fight
- You are showing inevitability
- Stop tracking ammo precisely here

---

### ENEMY PRESENCE

- **Marshal Eliza Kane**
- **8–10 Marshals**
- **Remaining Baron Guards fall back intentionally**

This should feel:
> “We were allowed to get this far.”

---

### KEY STORY BEATS

- Red Jack is shot (non-lethal, serious)
- Marshals form a wide semicircle
- Angel Eye is NOT visible

End structured combat.

---

### TRANSITION LINE (USE THIS)

> “Peluru berhenti beterbangan.  
> Yang tersisa hanyalah siapa berdiri di mana.”

---

## STAGE 4 — THE MEXICAN STANDOFF  
### Final Draw

**Time Budget:** ~30–40 minutes  
**Music:** *The Trio*

---

### PARTICIPANTS

- Marshal Eliza Kane
- Red Jack
- 1–2 PCs who can still stand
- Angel Eye (conditional)

---

### STANDOFF RULES

- No initiative
- No reactions
- No movement
- No cover
- No persuasion checks

This is **mechanical fate**.

---

### STANDOFF MECHANIC

#### Step 1 — Declare Intent
Each declares:
- Kill
- Disable
- Hold

NPC intent is hidden.

---

#### Step 2 — The Draw

Roll:
DEX modifier only
Highest acts first.

---

#### Step 3 — Resolution

- Shot resolves immediately
- Damage is not reduced
- Survivors continue in order

No interruptions.

---

### ANGEL EYE TRIGGER

Angel Eye appears if:
- Red Jack dies first
- OR both PCs drop

Angel Eye:
- Shoots once
- Ends the standoff
- Leaves without comment

---

## EPILOGUE

- Who lives
- Who dies
- Who the Bureau extracts

The Frontier remembers:
- Not heroes
- Not villains
- Only who drew first

---

## DM REMINDER

This finale works because:
- It is **not fair**
- It is **not safe**
- It is **not negotiable**

Let it be sharp.
Let it end clean.

# Statblock
```statblock
"name": "Baron Rail Guard"
"size": "Medium"
"type": "humanoid"
"alignment": "Lawful Neutral"
"ac": !!int "11"
"ac_class": "leather coat"
"hp": !!int "42"
"hit_dice": "7d8 + 7"
"modifier": !!int "1"
"stats":
  - !!int "11"
  - !!int "14"
  - !!int "13"
  - !!int "10"
  - !!int "11"
  - !!int "10"
"speed": "30 ft."
"skillsaves":
  - "name": "Perception"
    "desc": "+3"
"senses": "passive Perception 13"
"languages": "Common"
"cr": "2"
"traits":
  - "name": "Rail Discipline"
    "desc": "If the Rail Guard is within 10 ft. of an ally, it gains advantage on its first attack roll each round."
"actions":
  - "name": "Revolver"
    "desc": "Ranged Weapon Attack: +2 to hit (DEX), range 30/60 ft., one target. Hit: 9 (2d6 + 2) piercing damage."
  - "name": "Bayonet"
    "desc": "Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) piercing damage."
```
**Use**: Cannon fodder with teeth
**Role**: Pressure + flanking

```statblock
"name": "Baron Rail Sergeant"
"size": "Medium"
"type": "humanoid"
"alignment": "Lawful Neutral"
"ac": !!int "12"
"ac_class": "reinforced coat"
"hp": !!int "68"
"hit_dice": "8d8 + 24"
"modifier": !!int "2"
"stats":
  - !!int "13"
  - !!int "14"
  - !!int "16"
  - !!int "11"
  - !!int "12"
  - !!int "14"
"speed": "30 ft."
"skillsaves":
  - "name": "Intimidation"
    "desc": "+4"
  - "name": "Perception"
    "desc": "+4"
"senses": "passive Perception 14"
"languages": "Common"
"cr": "4"
"traits":
  - "name": "Commanding Presence"
    "desc": "As a bonus action, one ally within 30 ft. may immediately reload or move up to half speed without provoking attacks."
"actions":
  - "name": "Rifle"
    "desc": "Ranged Weapon Attack: +2 to hit (DEX), range 60/100 ft., one target. Hit: 13 (2d10 + 2) piercing damage."
  - "name": "Sidearm"
    "desc": "Ranged Weapon Attack: +2 to hit, range 30/60 ft., one target. Hit: 9 (2d6 + 2) piercing damage."

```
**Use:** Fire support & morale anchor  
**Role:** Keeps guards dangerous longer

```statblock
"name": "Baron Sniper"
"size": "Medium"
"type": "humanoid"
"alignment": "Lawful Neutral"
"ac": !!int "12"
"ac_class": "long coat"
"hp": !!int "54"
"hit_dice": "8d8 + 16"
"modifier": !!int "3"
"stats":
  - !!int "10"
  - !!int "16"
  - !!int "14"
  - !!int "12"
  - !!int "14"
  - !!int "11"
"speed": "30 ft."
"skillsaves":
  - "name": "Perception"
    "desc": "+5"
  - "name": "Stealth"
    "desc": "+5"
"senses": "passive Perception 15"
"languages": "Common"
"cr": "4"
"traits":
  - "name": "Scoped Shot"
    "desc": "If the Sniper spends a bonus action to aim, its next rifle attack deals an additional 1d12 damage."
"actions":
  - "name": "Sniper Rifle"
    "desc": "Ranged Weapon Attack: +3 to hit (DEX), range 200/300 ft., one target. Hit: 18 (2d12 + 3) piercing damage."
```
**Use:** Fear piece  
**Role:** Punishes exposure
```statblock
"name": "Marshal Scout"
"size": "Medium"
"type": "humanoid"
"alignment": "Lawful Neutral"
"ac": !!int "12"
"ac_class": "dust coat"
"hp": !!int "48"
"hit_dice": "7d8 + 14"
"modifier": !!int "2"
"stats":
  - !!int "12"
  - !!int "15"
  - !!int "14"
  - !!int "10"
  - !!int "13"
  - !!int "12"
"speed": "35 ft."
"skillsaves":
  - "name": "Perception"
    "desc": "+4"
  - "name": "Survival"
    "desc": "+4"
"senses": "passive Perception 14"
"languages": "Common"
"cr": "3"
"traits":
  - "name": "Advance and Withdraw"
    "desc": "After making a ranged attack, the Scout may move up to 15 ft. without provoking opportunity attacks."
"actions":
  - "name": "Revolver"
    "desc": "Ranged Weapon Attack: +2 to hit (DEX), range 30/60 ft., one target. Hit: 9 (2d6 + 2) piercing damage."
  - "name": "Carbine"
    "desc": "Ranged Weapon Attack: +2 to hit (DEX), range 60/100 ft., one target. Hit: 13 (2d10 + 2) piercing damage."

```
**Use:** Foreshadow Kane  
**Role:** Harass, then retreat
```statblock
"name": "Angel Eye"
"size": "Medium"
"type": "humanoid"
"alignment": "Neutral"
"ac": !!int "13"
"ac_class": "stillness"
"hp": !!int "88"
"hit_dice": "11d8 + 33"
"modifier": !!int "4"
"stats":
  - !!int "12"
  - !!int "18"
  - !!int "16"
  - !!int "13"
  - !!int "14"
  - !!int "15"
"speed": "30 ft."
"skillsaves":
  - "name": "Perception"
    "desc": "+6"
  - "name": "Intimidation"
    "desc": "+6"
"senses": "passive Perception 16"
"languages": "Common"
"cr": "6"
"traits":
  - "name": "Dead Man's Draw"
    "desc": "Angel Eye cannot be surprised. On the first round of any standoff or combat, he automatically acts first."
  - "name": "Ivory Revolver"
    "desc": "Angel Eye's revolver ignores cover percentages."
"actions":
  - "name": "Ivory Revolver"
    "desc": "Ranged Weapon Attack: +4 to hit (DEX), range 30/60 ft., one target. Hit: 13 (2d6 + 4) piercing damage. On a critical hit, deal an additional 2d6 damage."

```
