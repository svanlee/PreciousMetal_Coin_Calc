# ASSAY — Silver Coin Intelligence

> A mobile-first precious metals and coin evaluation tool built for pawn shop use. PIN-protected, works from any browser, no app store required.

**Live app:** [https://vonduke.github.io/PreciousMetal_Coin_Calc](https://vonduke.github.io/PreciousMetal_Coin_Calc)

---

## Features

### 📈 Live Market Data
- Real-time gold, silver, platinum, and palladium spot prices
- Gold/Silver, Gold/Platinum, and Silver/Platinum ratios with buy signals
- Silver Pressure Index and Gold Pressure Index
- Live dealer buy/sell prices (APMEX, JM Bullion, SD Bullion, Provident, MCM)
- Best place to sell rankings with estimated return percentages
- Live precious metals news feed with bullish/bearish/neutral signals

### 🔬 AI Coin Scanner
- Dual-image capture — obverse and reverse submitted together
- Powered by Claude vision AI
- Identifies coin type, series, date, mint mark, and grade
- Estimates numismatic value range (low/high)
- Detects cleaning, artificial toning, and counterfeiting indicators
- Patina analysis using thin-film interference physics (Jhon E. Cash model)
- Toning color sequence mapped against standard Ag₂S progression
- Buy / Consider / Pass recommendation with reasoning
- One tap to pre-fill the full coin log entry from scan results

### ⚖ Weight Verification
- Expected weight and diameter for every coin type
- Enter actual scale reading — instant Pass / Marginal / Suspect verdict
- Flags underweight (possible clad core or shaved) and overweight (possible plating)
- Tolerance-based verdict: ±0.15g tight pass, ±0.30g marginal, outside = suspect
- Weight carries through from scan to log entry automatically

### 💰 Offer Calculator
- Customer walks in to sell — instantly calculate what to offer
- Bid percentage slider (50–95% of melt)
- Grade and condition adjustments (cleaned, damaged, original skin, rainbow toned)
- Three-tier offer display: Low / Fair / Strong
- Counter-offer verdict: Take It / Consider / Negotiate / Pass
- Smart advice line for cleaned coins, toned coins, key dates

### 📦 Bulk Entry
- Log a full lot of the same coin type at once
- Individual year / mint mark / grade per coin row
- Live batch summary: total cost, total melt, paper gain, average premium

### 📒 Coin Ledger
- Full flip tracker with cost basis, melt value, and P&L per coin
- Status workflow: Holding → Sold / Keep / Passed
- Filter by status
- LOUPE detail per coin — full patina and authenticity record
- Photo attachment (obverse and reverse)
- One-tap Mark Sold

### 📊 Trends
- Average flip profit, hold time, and win rate
- Profit per flip bar chart
- Spot price at purchase history chart
- Profit by coin type comparison chart
- Manual spot price history log

### 👤 Customer Mode
- Full-screen clean overlay — tap CUSTOMER in header
- Live metal prices displayed prominently
- Customer builds their own coin list and sees melt value instantly
- Shows shop offer (~80%) vs online value (~95%)
- Per-coin breakdown in g / troy oz / dwt
- Smart advice: small lot vs large lot sell strategy
- Exit returns to shop view

### ⚖ Weight & Unit Converter
- Baked into Market, Offer, and Customer tabs
- Enter any amount in g, troy oz, or dwt
- Converts across all three units instantly
- Shows spot value, shop bid (80%), and online value (95%) for any metal

---

## Supported Coin Types

| Coin | Silver | Weight |
|------|--------|--------|
| Peace Dollar | 0.7735 ozt | 26.73g |
| Morgan Dollar | 0.7735 ozt | 26.73g |
| Walking Liberty Half | 0.3617 ozt | 12.50g |
| Franklin Half | 0.3617 ozt | 12.50g |
| Kennedy Half (1964) | 0.3617 ozt | 12.50g |
| Kennedy Half (1965-70) | 0.1479 ozt | 11.50g |
| Barber Half | 0.3617 ozt | 12.50g |
| Seated Liberty Half | 0.3617 ozt | 12.44g |
| Washington Quarter | 0.1808 ozt | 6.25g |
| Standing Liberty Quarter | 0.1808 ozt | 6.25g |
| Barber Quarter | 0.1808 ozt | 6.25g |
| Mercury Dime | 0.0723 ozt | 2.50g |
| Roosevelt Dime | 0.0723 ozt | 2.50g |
| Barber Dime | 0.0723 ozt | 2.50g |
| War Nickel (35%) | 0.0563 ozt | 5.00g |
| American Silver Eagle | 1.0 ozt | 31.10g |
| 1oz Silver Round | 1.0 ozt | 31.10g |
| 1oz Silver Bar | 1.0 ozt | 31.10g |

---

## Security

- PIN required on every app open
- Auto-locks after 5 minutes idle
- 3 incorrect attempts triggers 30-second lockout
- PIN stored as SHA-256 hash — never plaintext
- PIN changeable from lock screen without touching code
- API key obfuscated via XOR encoding split across 3 parts

---

## Setup

No build process. Single HTML file.

1. Fork or download this repository
2. Enable GitHub Pages: Settings → Pages → Deploy from branch → main → / (root)
3. Access at `https://yourusername.github.io/PreciousMetal_Coin_Calc`
4. In Safari: Share → Add to Home Screen for native app experience

---

## Stack

- Vanilla HTML / CSS / JavaScript — zero dependencies
- Claude Sonnet API (vision + web search) for coin scanning, dealer prices, and news
- metals.live API for live spot prices
- localStorage for all coin data (stays on your device)
- GitHub Pages for hosting

---

## Built By

Scott Van Leeuwen — [VonDuke Designs](https://github.com/vonduke)  
Systems engineer, silver stacker, pawn shop consultant.

---

## License

MIT — see [LICENSE](LICENSE)
