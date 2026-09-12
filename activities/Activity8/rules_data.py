"""The ShopSmart knowledge base (Session 15: Expert Systems).

A small, fixed rule base and a fixed set of customer/system profiles for a
fictional online store, ShopSmart. There is no randomness anywhere in this
file — every student who runs the app sees the exact same rules and the
exact same profiles, so the inference engine's output is fully reproducible.

Each rule follows the classic production-rule (IF-THEN) format used by
expert systems, and is tagged with which department would "own" it:
IT (security/systems), Business (sales/marketing), or both.
"""

# --------------------------------------------------------------------------
# Fixed customer / system profiles (the "facts" fed into the engine)
# --------------------------------------------------------------------------

PROFILES = {
    "A — Camila R. (Loyal Shopper)": {
        "returning_customer": True,
        "loyalty_points": 650,
        "on_checkout_page": True,
        "cart_total": 45,
        "failed_logins": 1,
        "ip_flagged": False,
        "cpu_load_pct": 40,
        "server_temp_c": 22,
    },
    "B — New Visitor": {
        "returning_customer": False,
        "loyalty_points": 0,
        "on_checkout_page": True,
        "cart_total": 150,
        "failed_logins": 0,
        "ip_flagged": False,
        "cpu_load_pct": 55,
        "server_temp_c": 24,
    },
    "C — Suspicious Login (Flagged IP)": {
        "returning_customer": True,
        "loyalty_points": 800,
        "on_checkout_page": False,
        "cart_total": 0,
        "failed_logins": 5,
        "ip_flagged": True,
        "cpu_load_pct": 30,
        "server_temp_c": 21,
    },
    "D — Big Spender, System Under Load": {
        "returning_customer": True,
        "loyalty_points": 1200,
        "on_checkout_page": True,
        "cart_total": 250,
        "failed_logins": 4,
        "ip_flagged": False,
        "cpu_load_pct": 95,
        "server_temp_c": 38,
    },
    "E — Quiet Night": {
        "returning_customer": False,
        "loyalty_points": 0,
        "on_checkout_page": False,
        "cart_total": 0,
        "failed_logins": 0,
        "ip_flagged": False,
        "cpu_load_pct": 15,
        "server_temp_c": 19,
    },
}

FACT_LABELS = {
    "returning_customer": "Returning customer?",
    "loyalty_points": "Loyalty points",
    "on_checkout_page": "On checkout page?",
    "cart_total": "Cart total ($)",
    "failed_logins": "Failed login attempts",
    "ip_flagged": "IP address flagged?",
    "cpu_load_pct": "Server CPU load (%)",
    "server_temp_c": "Server temperature (°C)",
}

# --------------------------------------------------------------------------
# Fixed rule base (the "knowledge base" the inference engine reasons over)
# --------------------------------------------------------------------------
# Each rule: id, department, plain-English IF-THEN text, the list of
# (fact, comparison-as-text, check-function) conditions (ALL must hold for
# the rule to fire), and its conclusion if it fires.


def _gt(threshold):
    return lambda value: value > threshold


def _is(expected):
    return lambda value: value == expected


RULES = [
    {
        "id": "R1",
        "name": "Loyalty Discount",
        "department": "Business",
        "text": "IF returning_customer = True AND loyalty_points > 500 THEN offer a 10% discount on the next purchase.",
        "conditions": [
            ("returning_customer", "= True", _is(True)),
            ("loyalty_points", "> 500", _gt(500)),
        ],
        "conclusion": "Offer a 10% discount on the next purchase.",
    },
    {
        "id": "R2",
        "name": "Free Shipping",
        "department": "Business",
        "text": "IF on_checkout_page = True AND cart_total > 100 THEN unlock free shipping.",
        "conditions": [
            ("on_checkout_page", "= True", _is(True)),
            ("cart_total", "> 100", _gt(100)),
        ],
        "conclusion": "Unlock free shipping.",
    },
    {
        "id": "R3",
        "name": "Account Lockout",
        "department": "IT",
        "text": "IF failed_logins > 3 AND ip_flagged = False THEN temporarily lock the account for security review.",
        "conditions": [
            ("failed_logins", "> 3", _gt(3)),
            ("ip_flagged", "= False", _is(False)),
        ],
        "conclusion": "Temporarily lock the account for security review.",
    },
    {
        "id": "R4",
        "name": "Server Alert",
        "department": "IT",
        "text": "IF cpu_load_pct > 90 AND server_temp_c > 35 THEN trigger emergency cooling and alert IT.",
        "conditions": [
            ("cpu_load_pct", "> 90", _gt(90)),
            ("server_temp_c", "> 35", _gt(35)),
        ],
        "conclusion": "Trigger emergency cooling and alert IT.",
    },
]
