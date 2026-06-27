# 🏪 Downtown Pawnshop POS
### Precious Metals & Coin Point-of-Sale System

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-gold?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Platform](https://img.shields.io/badge/platform-iOS%20%7C%20Android%20%7C%20Web-blue?style=for-the-badge)
![Dependencies](https://img.shields.io/badge/dependencies-zero-brightgreen?style=for-the-badge)

**A full-featured pawn shop management system built for precious metals and coin dealers.**  
Single HTML file. No server. No framework. No monthly fees. Runs anywhere.

[Features](#features) · [Screenshots](#screenshots) · [Setup](#setup) · [Compliance](#compliance) · [Security](#security)

</div>

---

## ✨ Overview

Downtown Pawnshop POS is a complete point-of-sale and inventory management system purpose-built for precious metals and coin dealers. It combines real-time market intelligence, AI-powered coin appraisal, full transaction tracking, customer management, and law enforcement compliance reporting into a single, self-contained file that runs on any device with a browser.

Designed to work exactly like industry software (Bravo, PawnMaster) — without the subscription fees, vendor lock-in, or IT requirements.

---

## 🚀 Features

### 🔐 Multi-User Authentication
- **Master admin PIN** with full system access
- **Individual employee PINs** — each employee gets their own 4-digit code
- **Role-based access control** — staff see what they need, admins see everything
- **Auto-lock** after 5 minutes of inactivity
- **Lockout protection** — 3 failed attempts triggers a 30-second cooldown
- **PIN management** — admin can reset any employee PIN, change master PIN anytime

---

### 📋 Transaction Management

Four ticket types, each with unique numbering and workflows:

| Type | Format | Use Case |
|------|--------|----------|
| **BUY** | `DPS-BUY-YYMMDD-001` | Shop purchases item from customer |
| **SELL** | `DPS-SLL-YYMMDD-001` | Shop sells item to customer |
| **LOAN** | `DPS-LN-YYMMDD-001` | Pawn loan with collateral hold |
| **LAYAWAY** | `DPS-LAY-YYMMDD-001` | Customer paying over time |

Every ticket captures:
- Customer (linked to full profile with ID)
- Item description, coin type, grade, year, mint mark
- Live melt value calculation at time of transaction
- Offer tiers (70% / 80% / 90% of melt) shown automatically
- Employee who processed the transaction
- Police reporting status

---

### 👤 Customer Management

Full Bravo-style customer profiles:

- Legal name, date of birth, full address
- Government ID type, number, issuing state, expiry date
- **ID photo capture** — camera or upload, stored per profile
- Transaction history — every ticket linked to customer
- **Do Not Buy flag** — visible everywhere the customer appears
- Suspicious activity notes
- Search by name, phone number, or ID number

---

### 📦 Inventory & Hold Compliance

- Every bought item enters inventory automatically tagged to customer and employee
- **Configurable hold period** (default 10 days for Michigan — set to your state's requirement)
- Real-time hold countdown per item
- Status pipeline: **HOLD → CLEAR TO SELL → SOLD**
- Full chain of custody: who bought it, from whom, when, for how much
- Margin tracking: buy price vs sell price vs melt value
- Filter by hold status, clear to sell, or sold history

---

### 🔬 AI Coin Evaluation

Powered by Claude Sonnet AI vision:

- **Dual-image capture** — submit obverse and reverse together for maximum accuracy
- Identifies coin type, series, date, mint mark automatically
- Grades to ANA standard (AG through MS70) with confidence rating
- Estimates numismatic value range (low/high)
- Calculates melt value at live spot
- **Patina analysis** — maps toning colors against thin-film interference physics
- Detects cleaning, artificial toning, and counterfeit indicators
- Returns **BUY / CONSIDER / PASS** recommendation with reasoning
- **Weight verification** — enter scale reading, instant PASS/MARGINAL/SUSPECT verdict vs mint specs
- One tap to pre-fill a Buy Ticket with all evaluation data

---

### 🚔 Law Enforcement Compliance

Built for US pawn shops operating under state secondhand dealer regulations:

- **Configurable hold period** — set to match your state and city requirements
- **Agency management** — add local PD, county sheriff, state police, federal agencies
- Per-agency contact information (detective name, phone, email)
- **Automated police report generation** — all unreported buy/loan transactions compiled into a formatted report
- Report includes: ticket number, date, item description, seller name, ID type/number, address, amount paid
- **Report history log** — track what was submitted, when, and to whom
- Mark individual tickets as reported
- Print-ready report format

> ⚠️ **Note:** Hold period and reporting requirements vary by state and municipality. Consult your local ordinances. Michigan default is 10 days under the Pawnbrokers Act (PA 273 of 1917).

---

### 📈 Live Market Intelligence

- **Real-time spot prices** — Silver, Gold, Platinum, Palladium
- Automatic refresh on app open
- Price per gram displayed alongside per-troy-oz
- **Metal ratios** — Gold/Silver, Gold/Platinum, Platinum/Silver with buy signals
- **Gold/Silver ratio signal** — flags when silver is historically undervalued
- **Live metals news** — AI-curated headlines with bullish/bearish/neutral signals
- Refreshes on demand with web search integration

---

### ⚖️ Weight & Unit Converter

Baked into the Market tab — no switching screens:

- Enter any amount in **grams**, **troy ounces**, or **pennyweights (dwt)**
- Instant conversion across all three units
- Shows spot value, shop bid (80%), and online value (95%) for any metal
- Uses correct troy oz (31.1035g) not avoirdupois

---

### 👥 Employee KPI Dashboard *(Admin Only)*

Real performance metrics, not just activity logs:

| Metric | Description |
|--------|-------------|
| **Coins Bought** | Total transactions processed |
| **Coins Sold** | Items moved out of inventory |
| **Margin Generated** | Total profit on completed sales |
| **$ Bought** | Total capital deployed |
| **$ Sold** | Total revenue generated |
| **Avg Bid %** | How efficiently they're buying (vs melt) |
| **Best Find** | Highest paper-gain item they sourced |

Period filters: Today / This Week / This Month / All Time

---

### 👤 Customer-Facing Mode

One tap switches to a clean public view customers can hold:

- Displays shop name prominently
- Live precious metals prices (AG, AU, PT, PD)
- Customer builds their own coin list — type and quantity
- Instant melt value calculation
- Shows **shop offer (~80%)** vs **online value (~95%)**
- Per-coin breakdown with full weight display
- Smart advice based on lot size
- Staff view returns instantly

---

### 🏠 Dashboard

At-a-glance shop status every shift:

- Today's buy count, sell count, hold count, clearing today
- Today's revenue and total inventory value (at melt)
- **Hold alerts** — items releasing within 48 hours highlighted
- Recent activity feed — last 6 transactions across all employees
- Quick-access ticket buttons for all 4 transaction types

---

### ⚙️ Settings *(Admin Only)*

- Shop name, address, city, state, ZIP, phone (live updates lock screen and header)
- Pawn license number
- Hold period in days
- API key management (show/hide, update anytime)
- Admin PIN change (requires current PIN verification)
- Export all data as JSON (customers, tickets, inventory, reports)
- Factory reset with double confirmation

---

## 🛠️ Setup

### Deploy to GitHub Pages (recommended)

```
1. Create a new GitHub repository
2. Upload index.html (rename pawnshop.html → index.html)
3. Settings → Pages → Deploy from branch → main → / (root)
4. Live at: https://yourusername.github.io/your-repo-name
```

### Add to iPhone Home Screen

```
Safari → your GitHub Pages URL → Share → Add to Home Screen
```

Launches fullscreen like a native app. No App Store. No updates to manage.

### First Launch

The setup wizard walks through three steps:

1. **Shop Information** — name, address, state, hold period, API key
2. **Admin PIN** — set your master PIN (enter twice to confirm)
3. **First Employee** — add your first staff member, or skip

Total setup time: under 3 minutes.

---

## 🔑 API Key

An Anthropic API key is required for:
- AI coin evaluation (EVALUATE tab)
- Live metals news (MARKET tab)
- Live dealer price fetching

Get a free key at **[console.anthropic.com](https://console.anthropic.com)**

**Estimated monthly cost at typical pawn shop usage:**

| Usage | Est. Monthly Cost |
|-------|------------------|
| 20 coin scans/day | ~$3–5 |
| 5 coin scans/day | ~$0.75–1.50 |
| News fetches only | ~$0.10–0.30 |

Set a spend cap at console.anthropic.com → Billing to prevent surprises.

All other features (tickets, customers, inventory, hold tracking, compliance) work without an API key.

---

## 🔐 Security

| Feature | Implementation |
|---------|---------------|
| PIN storage | SHA-256 hashed with salt — never stored plaintext |
| API key storage | Device localStorage only — never transmitted except to Anthropic |
| Customer data | localStorage on device — never leaves the browser |
| ID photos | Base64 encoded, stored locally |
| Admin PIN | Separate from employee PINs, required for settings changes |
| Idle lock | 5-minute timeout, configurable |
| Brute force | 3-attempt lockout with 30-second cooldown |

> ⚠️ **Data note:** All data is stored in browser localStorage on the device. It does not sync across devices. Use the Export function regularly to back up your data.

---

## 💾 Data & Backup

Export all data at any time:  
**Settings → Export All Data (JSON)**

This exports:
- All customer profiles (excluding ID photos for file size)
- Complete ticket history
- Full inventory with hold records
- All police reports and agency contacts
- Shop configuration

Store the export in a secure location. Recommended: weekly exports to a private cloud folder.

---

## 🏛️ Compliance Notes

This software is designed to assist with compliance record-keeping. It does **not** replace legal counsel or guarantee compliance with any specific state or local ordinance. Always verify requirements with:

- Your state's department of licensing
- Your local police department
- Your pawn industry association (NPA, NPRRA)

**Known state-specific requirements included by default:**

| State | Default Hold | Notes |
|-------|-------------|-------|
| Michigan | 10 days | PA 273 of 1917 |
| *All others* | Configurable | Set in Settings |

---

## 🛠️ Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Vanilla HTML5 / CSS3 / ES2022 |
| AI Vision | Claude Sonnet (Anthropic API) |
| Web Search | Claude Web Search tool |
| Spot Prices | metals.live API |
| Storage | Browser localStorage |
| Hosting | GitHub Pages |
| Dependencies | **Zero** |

No build process. No npm. No webpack. One file, open in browser, done.

---

## 🗺️ Roadmap

- [ ] Multi-device sync via encrypted cloud backend
- [ ] Receipt/ticket PDF generation and printing
- [ ] Barcode/QR scanning for item lookup
- [ ] Automated daily email compliance reports
- [ ] Layaway payment tracking and reminders
- [ ] Loan renewal and redemption workflow
- [ ] Photo attachment per inventory item
- [ ] Multi-location support
- [ ] Stripe integration for card payments
- [ ] Custom report builder

---

## 📄 License

MIT — see [LICENSE](LICENSE)

Free to use, modify, and deploy. Attribution appreciated but not required.

---

## 👨‍💻 Built By

**Scott Van Leeuwen**  
Systems Engineer & Silver Stacker  
[VonDuke Designs](https://github.com/vonduke)

> *"Built from the floor of a pawn shop, for the floor of a pawn shop."*

---

<div align="center">

**[⭐ Star this repo](https://github.com/vonduke/PreciousMetal_Coin_Calc)** if it saves you money on software subscriptions.

*Made with obsessive attention to detail and an unhealthy interest in silver coins.*

</div>
