import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Textile Fibers Explorer",
    page_icon="🧵",wrap
    layout="wide",
)

# -----------------------------
# Textile fiber knowledge base
# -----------------------------
FIBERS = {
    "Cotton": {
        "category": "Natural - Plant",
        "source": "Cotton plant seed hair",
        "composition": "Cellulose",
        "strength": "Good; stronger when wet",
        "moisture": "High absorbency",
        "feel": "Soft and comfortable",
        "advantages": [
            "Comfortable and breathable",
            "Good moisture absorption",
            "Easy to dye",
            "Good washability",
        ],
        "disadvantages": [
            "Wrinkles easily",
            "Can shrink",
            "Dries slowly",
            "Can mildew under damp conditions",
        ],
        "applications": "Shirts, T-shirts, bedsheets, towels, denim, underwear",
    },
    "Wool": {
        "category": "Natural - Animal",
        "source": "Sheep and other animal fleece",
        "composition": "Protein (keratin)",
        "strength": "Moderate",
        "moisture": "Good moisture absorption",
        "feel": "Warm and resilient",
        "advantages": [
            "Excellent warmth",
            "Good elasticity and resilience",
            "Absorbs moisture without feeling wet quickly",
            "Naturally flame resistant compared with many fibers",
        ],
        "disadvantages": [
            "Can shrink/felt",
            "May be damaged by insects",
            "More expensive than many common fibers",
            "Needs careful washing",
        ],
        "applications": "Suits, sweaters, coats, blankets, carpets",
    },
    "Silk": {
        "category": "Natural - Animal",
        "source": "Silkworm cocoon",
        "composition": "Protein (fibroin)",
        "strength": "High for its fineness",
        "moisture": "Moderate absorbency",
        "feel": "Smooth, soft and lustrous",
        "advantages": [
            "Excellent luster",
            "Very soft and comfortable",
            "Good drape",
            "Strong and fine fiber",
        ],
        "disadvantages": [
            "Expensive",
            "Sensitive to strong sunlight",
            "Requires careful washing",
            "Can lose strength when wet",
        ],
        "applications": "Luxury garments, scarves, ties, lingerie, furnishing fabrics",
    },
    "Linen": {
        "category": "Natural - Plant",
        "source": "Flax stem",
        "composition": "Cellulose",
        "strength": "High",
        "moisture": "High absorbency",
        "feel": "Cool and crisp",
        "advantages": [
            "Very strong",
            "Cool and breathable",
            "Good moisture absorption",
            "Dries relatively quickly",
        ],
        "disadvantages": [
            "Wrinkles easily",
            "Low elasticity",
            "Can become brittle with repeated flexing",
            "Often more expensive than cotton",
        ],
        "applications": "Summer clothing, table linen, curtains, home textiles",
    },
    "Viscose": {
        "category": "Man-made - Regenerated",
        "source": "Regenerated cellulose, commonly from wood pulp",
        "composition": "Regenerated cellulose",
        "strength": "Moderate; lower when wet",
        "moisture": "High absorbency",
        "feel": "Soft and silk-like",
        "advantages": [
            "Soft and comfortable",
            "Excellent drape",
            "Good absorbency",
            "Can be produced with a silk-like appearance",
        ],
        "disadvantages": [
            "Can weaken when wet",
            "May shrink",
            "Can wrinkle",
            "Production can require substantial chemical processing",
        ],
        "applications": "Dresses, shirts, linings, home textiles, blends",
    },
    "Polyester": {
        "category": "Synthetic",
        "source": "Petrochemical-based polymer",
        "composition": "Polyester polymer (commonly PET)",
        "strength": "High",
        "moisture": "Low absorbency",
        "feel": "Smooth; depends on construction",
        "advantages": [
            "High strength and durability",
            "Good dimensional stability",
            "Quick drying",
            "Good wrinkle resistance",
        ],
        "disadvantages": [
            "Low moisture absorbency",
            "Can retain odors",
            "Can generate static",
            "Usually derived from fossil resources",
        ],
        "applications": "Sportswear, shirts, uniforms, curtains, industrial textiles",
    },
    "Nylon": {
        "category": "Synthetic",
        "source": "Synthetic polyamide polymer",
        "composition": "Polyamide",
        "strength": "Very high",
        "moisture": "Moderate absorbency",
        "feel": "Smooth and resilient",
        "advantages": [
            "Very high strength",
            "Excellent abrasion resistance",
            "Lightweight",
            "Good elasticity and resilience",
        ],
        "disadvantages": [
            "Can yellow with prolonged sunlight exposure",
            "Can generate static",
            "Melts at high temperature",
            "Lower moisture absorption than natural cellulosic fibers",
        ],
        "applications": "Sportswear, hosiery, ropes, parachutes, carpets",
    },
    "Acrylic": {
        "category": "Synthetic",
        "source": "Synthetic polyacrylonitrile-based polymer",
        "composition": "Acrylic polymer",
        "strength": "Moderate",
        "moisture": "Low absorbency",
        "feel": "Wool-like and lightweight",
        "advantages": [
            "Lightweight",
            "Warm",
            "Wool-like appearance",
            "Good resistance to many chemicals",
        ],
        "disadvantages": [
            "Can pill",
            "Low moisture absorbency",
            "Can build static",
            "Sensitive to high heat",
        ],
        "applications": "Sweaters, blankets, carpets, knitwear",
    },
    "Spandex": {
        "category": "Synthetic",
        "source": "Polyurethane-based elastomer",
        "composition": "Segmented polyurethane",
        "strength": "Good; designed for elasticity",
        "moisture": "Low absorbency",
        "feel": "Stretchy and smooth",
        "advantages": [
            "Exceptional elasticity",
            "Excellent shape recovery",
            "Lightweight",
            "Useful in stretch fabrics",
        ],
        "disadvantages": [
            "Sensitive to heat and some chemicals",
            "Can degrade with chlorine and prolonged UV exposure",
            "Usually used as a blend rather than alone",
        ],
        "applications": "Activewear, swimwear, stretch denim, sports garments",
    },
    "Hemp": {
        "category": "Natural - Plant",
        "source": "Hemp plant stem",
        "composition": "Cellulose",
        "strength": "High",
        "moisture": "Good absorbency",
        "feel": "Firm and becomes softer with use",
        "advantages": [
            "Strong and durable",
            "Good absorbency",
            "Breathable",
            "Can be blended with other fibers",
        ],
        "disadvantages": [
            "Can feel coarse if not processed well",
            "Wrinkles",
            "Processing quality strongly affects handle",
        ],
        "applications": "Apparel, canvas, home textiles, ropes and blends",
    },
}

# -----------------------------
# Helper functions
# -----------------------------
def fiber_dataframe():
    rows = []
    for name, data in FIBERS.items():
        rows.append({
            "Fiber": name,
            "Category": data["category"],
            "Source": data["source"],
            "Composition": data["composition"],
            "Strength": data["strength"],
            "Moisture": data["moisture"],
            "Applications": data["applications"],
        })
    return pd.DataFrame(rows)


def fiber_card(name):
    data = FIBERS[name]
    st.subheader(name)
    st.caption(f"{data['category']} • Source: {data['source']}")
    c1, c2, c3 = st.columns(3)
    c1.metric("Composition", data["composition"])
    c2.metric("Strength", data["strength"])
    c3.metric("Moisture", data["moisture"])

    st.markdown("**Advantages**")
    for item in data["advantages"]:
        st.write(f"• {item}")

    st.markdown("**Disadvantages**")
    for item in data["disadvantages"]:
        st.write(f"• {item}")

    st.markdown(f"**Common applications:** {data['applications']}")


# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🧵 Textile Fibers")
st.sidebar.write("Learning and reference app for textile students.")

page = st.sidebar.radio(
    "Navigate",
    [
        "Home",
        "Fiber Explorer",
        "Compare Fibers",
        "Fiber Selection",
        "Reference Table",
    ],
)

st.sidebar.markdown("---")
st.sidebar.info(
    "Educational reference only. Properties vary with fiber grade, "
    "processing, yarn construction and fabric structure."
)

# -----------------------------
# Home
# -----------------------------
if page == "Home":
    st.title("🧵 Textile Fibers Explorer")
    st.markdown(
        "### Learn, compare and select textile fibers"
    )
    st.write(
        "This Streamlit application provides a simple study tool for "
        "understanding natural, regenerated and synthetic textile fibers."
    )

    c1, c2, c3 = st.columns(3)
    c1.metric("Fibers in database", len(FIBERS))
    c2.metric("Main categories", len(set(x["category"] for x in FIBERS.values())))
    c3.metric("Study areas", "Properties • Uses • Comparison")

    st.markdown("## Fiber categories")
    category_counts = (
        fiber_dataframe()["Category"].value_counts().rename_axis("Category").reset_index(name="Fibers")
    )
    st.dataframe(category_counts, use_container_width=True, hide_index=True)

    st.markdown("## What you can do")
    st.write("• Explore individual fibers and their properties.")
    st.write("• Compare two or three fibers side by side.")
    st.write("• Select fibers according to a desired textile application.")
    st.write("• Use the reference table for quick revision and exam preparation.")

# -----------------------------
# Fiber Explorer
# -----------------------------
elif page == "Fiber Explorer":
    st.title("🔎 Fiber Explorer")

    selected = st.selectbox("Select a textile fiber", list(FIBERS.keys()))
    search = st.text_input("Or search by fiber name").strip().lower()

    if search:
        matches = [name for name in FIBERS if search in name.lower()]
        if matches:
            selected = st.selectbox("Matching fibers", matches)

    fiber_card(selected)

# -----------------------------
# Compare
# -----------------------------
elif page == "Compare Fibers":
    st.title("⚖️ Compare Fibers")
    selected = st.multiselect(
        "Select 2 or 3 fibers",
        list(FIBERS.keys()),
        default=["Cotton", "Polyester"],
        max_selections=3,
    )

    if len(selected) < 2:
        st.warning("Select at least two fibers to compare.")
    else:
        rows = []
        for name in selected:
            d = FIBERS[name]
            rows.append({
                "Property": name,
                "Category": d["category"],
                "Composition": d["composition"],
                "Strength": d["strength"],
                "Moisture": d["moisture"],
                "Feel": d["feel"],
                "Applications": d["applications"],
            })
        comparison = pd.DataFrame(rows).set_index("Property").T
        st.dataframe(comparison, use_container_width=True)

        st.markdown("### Advantages and disadvantages")
        columns = st.columns(len(selected))
        for col, name in zip(columns, selected):
            with col:
                st.markdown(f"#### {name}")
                st.markdown("**Advantages**")
                for item in FIBERS[name]["advantages"]:
                    st.write(f"• {item}")
                st.markdown("**Disadvantages**")
                for item in FIBERS[name]["disadvantages"]:
                    st.write(f"• {item}")

# -----------------------------
# Fiber Selection Tool
# -----------------------------
elif page == "Fiber Selection":
    st.title("🎯 Fiber Selection Tool")
    st.write("Choose the properties you want in a textile material.")

    category = st.selectbox(
        "Preferred category",
        ["Any"] + sorted(set(d["category"] for d in FIBERS.values())),
    )
    moisture = st.selectbox(
        "Moisture requirement",
        ["Any", "High absorbency", "Moderate absorbency", "Low absorbency"],
    )
    application = st.selectbox(
        "Main application",
        [
            "Any",
            "Sportswear",
            "Shirts / T-shirts",
            "Home textiles",
            "Winter wear",
            "Luxury garments",
            "Industrial textiles",
        ],
    )

    def matches(name, d):
        if category != "Any" and d["category"] != category:
            return False
        if moisture != "Any" and d["moisture"] != moisture:
            return False

        app_map = {
            "Sportswear": ["Polyester", "Nylon", "Spandex"],
            "Shirts / T-shirts": ["Cotton", "Polyester", "Viscose"],
            "Home textiles": ["Cotton", "Linen", "Polyester", "Acrylic"],
            "Winter wear": ["Wool", "Acrylic", "Polyester"],
            "Luxury garments": ["Silk", "Viscose"],
            "Industrial textiles": ["Nylon", "Polyester", "Hemp"],
        }
        if application != "Any" and name not in app_map[application]:
            return False
        return True

    matches_list = [name for name, d in FIBERS.items() if matches(name, d)]

    if matches_list:
        st.success(f"{len(matches_list)} matching fiber(s) found.")
        for name in matches_list:
            st.markdown(f"### {name}")
            st.write(
                f"**Category:** {FIBERS[name]['category']} | "
                f"**Strength:** {FIBERS[name]['strength']} | "
                f"**Moisture:** {FIBERS[name]['moisture']}"
            )
            st.write(f"**Applications:** {FIBERS[name]['applications']}")
    else:
        st.warning("No fibers match all selected conditions. Try broader options.")

# -----------------------------
# Reference Table
# -----------------------------
elif page == "Reference Table":
    st.title("📚 Fiber Reference Table")
    st.write("Use the search box and filters for quick revision.")

    df = fiber_dataframe()
    search = st.text_input("Search fiber, category, composition or application")

    if search:
        mask = df.astype(str).apply(
            lambda col: col.str.contains(search, case=False, na=False)
        ).any(axis=1)
        df = df[mask]

    categories = st.multiselect(
        "Filter by category",
        sorted(fiber_dataframe()["Category"].unique()),
    )
    if categories:
        df = df[df["Category"].isin(categories)]

    st.dataframe(df, use_container_width=True, hide_index=True)

st.markdown("---")
st.caption("Textile Fibers Explorer • Built with Streamlit • Educational project")
