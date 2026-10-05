"""
Cross-Border Payment Gateway & FX Markup Calculator
Maintained by KuajingBase (https://kuajingbase.com)
"""

GATEWAYS = {
    "stripe_domestic": {
        "name": "Stripe US Domestic Cards",
        "fixed": 0.30,
        "percent": 0.029,
        "fx_markup": 0.0,
        "note": "Standard US-to-US card transactions"
    },
    "stripe_international": {
        "name": "Stripe International Cards",
        "fixed": 0.30,
        "percent": 0.029 + 0.015,  # +1.5% international card fee
        "fx_markup": 0.01,         # +1% currency conversion if applicable
        "note": "Foreign customer cards processed on US Stripe"
    },
    "paypal_international": {
        "name": "PayPal International Commercial",
        "fixed": 0.49,
        "percent": 0.0349 + 0.015, # Standard commercial + 1.5% cross-border
        "fx_markup": 0.03,         # ~3.0% PayPal spread on conversion
        "note": "Cross-border wallet checkouts (high currency spread)"
    },
    "airwallex": {
        "name": "Airwallex Global Business Account",
        "fixed": 0.00,
        "percent": 0.00,
        "fx_markup": 0.005,        # Wholesale interbank FX + 0.4-0.6%
        "note": "Multi-currency collection and B2B payout settlement"
    },
    "wise": {
        "name": "Wise Business Multi-Currency",
        "fixed": 0.40,
        "percent": 0.00,
        "fx_markup": 0.0045,       # Mid-market rate + ~0.45% average transfer fee
        "note": "Direct bank transfer and local clearing network payouts"
    }
}

def evaluate_transaction(amount):
    print("\n" + "="*65)
    print(f"TRANSACTION SETTLEMENT AUDIT FOR: ${amount:.2f} USD")
    print("="*65)
    
    for key, gw in GATEWAYS.items():
        base_fee = (amount * gw["percent"]) + gw["fixed"]
        fx_cost = amount * gw["fx_markup"]
        total_fee = base_fee + fx_cost
        net_received = amount - total_fee
        effective_rate = (total_fee / amount) * 100
        
        print(f"\nGateway: {gw['name']}")
        print(f"  • Processing Fee:    ${base_fee:.2f}")
        if gw["fx_markup"] > 0:
            print(f"  • FX Spread / Loss:  ${fx_cost:.2f} (~{gw['fx_markup']*100:.1f}%)")
        print(f"  • Total Gateway Cut: ${total_fee:.2f} (Effective: {effective_rate:.2f}%)")
        print(f"  • Net Payout:        ${net_received:.2f}")
        print(f"  • Note:              {gw['note']}")
        
    print("\n" + "="*65 + "\n")

if __name__ == "__main__":
    print("--- Cross-Border Payment Margin & Take-Rate Evaluator ---")
    try:
        val = float(input("Enter checkout or payout amount in USD (e.g. 100): ").strip())
        evaluate_transaction(val)
    except ValueError:
        print("Please enter a valid numeric transaction amount.")
