
# 💳 Cross-Border Payment Gateway & FX Margin Calculator

A lightweight Python tool for international digital entrepreneurs, SaaS founders, and DTC merchants to audit payment processing fees and currency conversion (FX) spreads across **Stripe, PayPal, Wise, and Airwallex**.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://python.org)
[![Maintained by KuajingBase](https://img.shields.io/badge/Maintained%20by-KuajingBase-orange.svg)](https://kuajingbase.com)

---

## 📌 Problem

When selling globally, headline fees (like Stripe’s `2.9% + $0.30`) only tell half the story. International payment rails introduce hidden margins:

* **Cross-border card surcharges** (typically +1.5% for foreign-issued cards).
* **Currency conversion markups** (from Stripe’s 1.0% to PayPal’s 3.0%+ spread over mid-market rates).
* **Multi-currency payout losses** during bank settlement.

For a cross-border merchant, unmonitored payment leakages can easily erode 3% to 5% of gross transaction volume.

---

## 📊 Gateway Fee Comparison Matrix (2026 Baseline)

| Gateway / Channel | Standard Base Fee | International Surcharge | Typical FX Spread | Best Use Case |
|---|---|---|---|---|
| **Stripe (Domestic)** | 2.9% + $0.30 | None | 0% | Domestic US customer checkouts |
| **Stripe (International)** | 2.9% + $0.30 | +1.5% | ~1.0% | Global DTC ecommerce & subscription SaaS |
| **PayPal Commercial** | 3.49% + $0.49 | +1.5% | 3.0% – 4.0% | Wallet checkouts (high trust, high fee) |
| **Airwallex** | Interchange+ | Zero incoming fees | 0.4% – 0.6% | Global multi-currency accounts & vendor payouts |
| **Wise Business** | Flat transfer fee | None | 0.35% – 0.5% | Direct contractor & intercompany wire clearing |

---

## ⚡ Quick Start

```bash
git clone https://github.com/reituman602/cross-border-payment-calculator.git
cd cross-border-payment-calculator
python calc.py
```

### Sample Output:
```text
TRANSACTION SETTLEMENT AUDIT FOR: $100.00 USD
=================================================================

Gateway: Stripe International Cards
  • Processing Fee:    $4.70
  • FX Spread / Loss:  $1.00 (~1.0%)
  • Total Gateway Cut: $5.70 (Effective: 5.70%)
  • Net Payout:        $94.30

Gateway: PayPal International Commercial
  • Processing Fee:    $5.48
  • FX Spread / Loss:  $3.00 (~3.0%)
  • Total Gateway Cut: $8.48 (Effective: 8.48%)
  • Net Payout:        $91.52
```

---

## 🔗 Master Reference & Integration Guides

For complete tutorials on setting up foreign entity accounts, configuring checkout webhooks, and optimizing checkout conversion:

* 💳 **[Stripe International Setup & Risk Management Guide](https://kuajingbase.com/en/payment/stripe)** (Official Step-by-Step)
* 🏦 **[Cross-Border Payment Gateways & Banking Directory](https://kuajingbase.com/payment)** (Fee Benchmarks & Comparison)
* 🏛️ **[US LLC Formation Guide for Non-Residents](https://kuajingbase.com/en/legal/us-llc)** (Required for US Stripe Onboarding)
* 🌐 **[KuajingBase Official Portal](https://kuajingbase.com/en)**

---

## ⚖️ License
MIT License. Maintained by [KuajingBase](https://kuajingbase.com).
