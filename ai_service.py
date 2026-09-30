from services.gemini_utils import generate_gemini_response


def create_prompt(category, budget, preferences, occasion=""):
    prompt = f"""
You are PocketSmart AI, a smart personal budgeting
and recommendation assistant.

The user wants recommendations for:

Category: {category}
Budget: ₹{budget}
Preferences: {preferences}
Occasion: {occasion}

Create a practical budget-friendly recommendation.

Give the response in this format:

1. Budget Summary
2. Recommended Items
3. Estimated Price
4. Why It Fits
5. Money Saving Tips
6. Final Suggested Budget

Important:
- Stay within the user's budget.
- Do not recommend unnecessary expensive products.
- Give realistic Indian Rupee prices.
- Clearly mention that prices are estimated.
- Keep the answer easy to understand.
"""

    return generate_gemini_response(prompt)


def fallback_recommendation(category, budget, preferences):
    budget = float(budget)

    if category == "Home Interior":

        items = [
            ("LED Lights", budget * 0.10),
            ("Curtains", budget * 0.15),
            ("Wall Decor", budget * 0.10),
            ("Storage Furniture", budget * 0.30),
            ("Rug / Carpet", budget * 0.15),
            ("Cushions", budget * 0.10),
            ("Plants / Decor", budget * 0.10),
        ]

    elif category == "Party":

        items = [
            ("Decorations", budget * 0.20),
            ("Food", budget * 0.35),
            ("Cake", budget * 0.15),
            ("Return Gifts", budget * 0.10),
            ("Photography", budget * 0.10),
            ("Miscellaneous", budget * 0.10),
        ]

    else:

        items = [
            ("Main Jewelry", budget * 0.55),
            ("Earrings", budget * 0.15),
            ("Chain", budget * 0.15),
            ("Bracelet", budget * 0.10),
            ("Packaging", budget * 0.05),
        ]

    output = f"""
## PocketSmart AI Recommendation

### Category
{category}

### Budget
₹{budget:,.0f}

### Preferences
{preferences}

### Recommended Budget Plan

"""

    for name, price in items:
        output += f"- **{name}** — ₹{price:,.0f}\n"

    output += """

### Money Saving Tips

- Compare prices before purchasing.
- Prefer products with good customer reviews.
- Check multiple shopping platforms.
- Avoid unnecessary add-ons.
- Keep a small emergency amount aside.

*Prices shown are estimated and may vary.*
"""

    return output


def get_recommendation(
    category,
    budget,
    preferences,
    occasion=""
):

    try:

        result = create_prompt(
            category,
            budget,
            preferences,
            occasion
        )

        if result and not result.startswith("Gemini API error"):
            return result

    except Exception:
        pass

    return fallback_recommendation(
        category,
        budget,
        preferences
    )