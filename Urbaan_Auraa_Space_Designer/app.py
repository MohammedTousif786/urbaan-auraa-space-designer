import streamlit as st
import math

st.set_page_config(page_title="Urbaan Auraa Space Designer", page_icon="🏡", layout="wide")

# ---------- Theme ----------
st.markdown("""
<style>
:root { --forest:#183b32; --cream:#f7f3eb; --gold:#c6a15b; }
.stApp { background: #f7f3eb; color: #24352f; }
[data-testid="stSidebar"] { background: #183b32; }
[data-testid="stSidebar"] * { color: #f8f3e8 !important; }
h1,h2,h3 { color: #183b32; }
.eyebrow { color:#a27b36; text-transform:uppercase; letter-spacing:2px; font-size:12px; font-weight:700; }
.hero { background:linear-gradient(90deg,rgba(15,42,34,.92),rgba(15,42,34,.30)),url('https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=1800&q=85'); background-size:cover;background-position:center;border-radius:18px;padding:70px 42px;color:white;margin-bottom:24px; }
.hero h1 { color:white;font-size:44px;max-width:650px;line-height:1.1; }
.hero p { color:#f4eee2;max-width:620px;font-size:17px; }
.panel { background:#fffdf8;border:1px solid #e7dfd0;border-radius:16px;padding:20px;height:100%; }
.gold { color:#a27b36;font-weight:700; }
.small-muted { color:#6d776f;font-size:13px; }
div.stButton > button { background:#183b32;color:white;border:1px solid #183b32;border-radius:10px; }
div.stButton > button:hover { background:#285647;color:white;border-color:#c6a15b; }
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("<div style='font-size:13px;letter-spacing:2px;color:#d7bb7b'>URBAAN AURAA</div><h2 style='color:#fff;margin-top:4px'>Space Designer</h2><p style='font-size:12px;color:#d8e2db'>Thoughtful spaces. Beautiful living.</p>", unsafe_allow_html=True)
pages = ["Home", "Gallery", "Design Details", "Plot Planner", "Price Estimator", "Construction Budget", "About Us"]
page = st.sidebar.radio("NAVIGATION", pages, label_visibility="visible")
st.sidebar.markdown("---")
st.sidebar.caption("Design your space with confidence.")

designs = [
    {"name":"Serene Living Room","category":"Hall / Living Room","style":"Warm contemporary","budget":"₹2.5–5 lakh","image":"photo-1600210492486-724fe5c67fb0","desc":"Soft neutral colours, layered lighting and comfortable seating."},
    {"name":"Calm Bedroom Retreat","category":"Bedroom","style":"Minimal luxury","budget":"₹1.8–3.5 lakh","image":"photo-1616486338812-3dadae4b4ace","desc":"Natural textures, warm lighting and uncluttered storage."},
    {"name":"Modern Modular Kitchen","category":"Kitchen","style":"Modern functional","budget":"₹3–6 lakh","image":"photo-1600607687920-4e2a09cf159d","desc":"Efficient work zones, durable finishes and clean cabinetry."},
    {"name":"Statement TV Unit","category":"TV Cabinet","style":"Contemporary wood","budget":"₹70,000–1.8 lakh","image":"photo-1600210492493-0946911123ea","desc":"A balanced feature wall with concealed storage."},
    {"name":"Spa-inspired Bathroom","category":"Bathroom","style":"Calm natural","budget":"₹1–2.5 lakh","image":"photo-1620626011761-996317b8d101","desc":"Easy-care surfaces, thoughtful lighting and modern fittings."},
    {"name":"Smart Wardrobe","category":"Wardrobe / Storage","style":"Space-saving","budget":"₹80,000–2 lakh","image":"photo-1616486029423-aaa4789e8c9a","desc":"Flexible shelves, drawers and a neat visual finish."},
    {"name":"Elegant Dining Space","category":"Dining","style":"Modern classic","budget":"₹1–2.5 lakh","image":"photo-1600607687939-ce8a6c25118c","desc":"A welcoming dining zone with a strong focal point."},
    {"name":"Focused Study Corner","category":"Study Room","style":"Compact modern","budget":"₹40,000–1 lakh","image":"photo-1497366754035-f200968a6e72","desc":"Ergonomic desk placement, task lighting and storage."},
    {"name":"Contemporary Facade","category":"Exterior / Facade","style":"Modern Indian","budget":"Varies by scale","image":"photo-1600585154340-be6161a56a0c","desc":"Layered materials and a clear architectural identity."},
]
def img_url(photo, width=900):
    return f"https://images.unsplash.com/{photo}?auto=format&fit=crop&w={width}&q=80"
def design_card(d):
    st.image(img_url(d["image"]), use_container_width=True)
    st.markdown(f"**{d['name']}**")
    st.caption(f"{d['category']} · {d['style']}")
    st.write(d["desc"])
    st.markdown(f"<span class='gold'>Indicative budget: {d['budget']}</span>", unsafe_allow_html=True)

if page == "Home":
    st.markdown("""<div class="hero"><div class="eyebrow" style="color:#e1c47c">URBAAN AURAA SPACE DESIGNER</div><h1>Make room for the life you imagine.</h1><p>Explore thoughtful interiors, plan your plot, and understand indicative project budgets — all in one place.</p></div>""", unsafe_allow_html=True)
    a,b,c = st.columns(3)
    with a:
        st.markdown("<div class='panel'><h3>Explore designs</h3><p>Find ideas for every room, from calm bedrooms to contemporary kitchens.</p></div>", unsafe_allow_html=True)
    with b:
        st.markdown("<div class='panel'><h3>Plan your plot</h3><p>Calculate plot area and begin thinking about space requirements.</p></div>", unsafe_allow_html=True)
    with c:
        st.markdown("<div class='panel'><h3>Estimate a budget</h3><p>Use simple inputs for an indicative construction cost breakdown.</p></div>", unsafe_allow_html=True)
    st.subheader("Featured designs")
    cols=st.columns(3)
    for i,d in enumerate(designs[:3]):
        with cols[i]: design_card(d)
    st.info("Planning estimates are indicative only. Actual design, material, labour and property costs vary by city, site and specifications.")

elif page == "Gallery":
    st.markdown("<div class='eyebrow'>CURATED INSPIRATION</div>", unsafe_allow_html=True)
    st.title("Design Gallery")
    st.write("Browse ideas by room and style. Select a category to narrow the collection.")
    cats=["All"]+list(dict.fromkeys(d["category"] for d in designs))
    selected=st.selectbox("Filter by room", cats)
    search=st.text_input("Search designs", placeholder="Try: modern, calm, kitchen...")
    filtered=[d for d in designs if (selected=="All" or d["category"]==selected) and (search.lower() in (d["name"]+" "+d["style"]+" "+d["desc"]).lower())]
    if filtered:
        for start in range(0,len(filtered),3):
            cols=st.columns(3)
            for col,d in zip(cols,filtered[start:start+3]):
                with col:
                    with st.container(border=True): design_card(d)
    else: st.warning("No designs match those filters. Try another search.")

elif page == "Design Details":
    st.markdown("<div class='eyebrow'>DESIGN PROFILE</div>", unsafe_allow_html=True)
    st.title("Design Details")
    choice=st.selectbox("Choose a design", [d["name"] for d in designs])
    d=next(x for x in designs if x["name"]==choice)
    left,right=st.columns([1.25,1])
    with left: st.image(img_url(d["image"],1200), use_container_width=True)
    with right:
        st.subheader(d["name"]); st.caption(d["category"]+" · "+d["style"])
        st.write(d["desc"])
        st.markdown("**Design highlights**")
        st.write("- Balanced lighting and practical circulation")
        st.write("- Finishes selected for durability and easy maintenance")
        st.write("- Storage planned around everyday use")
        st.markdown("**Suggested materials**")
        st.write("Engineered wood or quality plywood, low-VOC paint, warm LED lighting, and durable hardware (final selection depends on site and budget).")
        st.markdown(f"**Indicative budget:** {d['budget']}")
        if st.button("♡ Save this design"):
            st.session_state.setdefault("saved_designs",[])
            if d["name"] not in st.session_state.saved_designs: st.session_state.saved_designs.append(d["name"])
            st.success("Design saved for this session.")
    st.subheader("Saved designs")
    saved=st.session_state.get("saved_designs",[])
    st.write(", ".join(saved) if saved else "No saved designs yet. Use the button above to save an idea.")

elif page == "Plot Planner":
    st.markdown("<div class='eyebrow'>START WITH YOUR SITE</div>", unsafe_allow_html=True)
    st.title("Plot Planner")
    st.write("Enter plot dimensions to calculate the area. This is an early planning aid, not an approved architectural plan.")
    c1,c2,c3=st.columns(3)
    with c1: length=st.number_input("Plot length (feet)",min_value=1.0,value=40.0,step=1.0)
    with c2: width=st.number_input("Plot width (feet)",min_value=1.0,value=30.0,step=1.0)
    with c3: floors=st.selectbox("Preferred floors",[1,2,3,4])
    area=length*width
    st.markdown("---")
    m1,m2,m3=st.columns(3)
    m1.metric("Plot area",f"{area:,.0f} sq ft")
    m2.metric("Approx. square metres",f"{area*0.092903:,.1f} m²")
    m3.metric("Floor preference",f"{floors} floor(s)")
    st.subheader("Conceptual space checklist")
    st.caption("Illustrative only — dimensions and local building rules must be checked by a qualified architect.")
    rooms=st.multiselect("Choose spaces to consider",["Living room","Kitchen","Dining","Bedrooms","Bathrooms","Staircase","Parking","Utility / wash area","Small garden"],default=["Living room","Kitchen","Bedrooms","Bathrooms","Parking"])
    st.markdown("<div class='panel'><h3>Concept sketch</h3><p>Front / road side</p><div style='border:3px solid #183b32;padding:14px;border-radius:8px;display:grid;grid-template-columns:1fr 1fr;gap:8px'>"+''.join(f"<div style='background:#e9e1d2;padding:18px 8px;text-align:center;border-radius:4px;color:#183b32'>{r}</div>" for r in rooms)+"</div><p style='margin-top:10px;font-size:12px'>Not to scale. This visual checklist is not a construction drawing.</p></div>",unsafe_allow_html=True)

elif page == "Price Estimator":
    st.markdown("<div class='eyebrow'>INDICATIVE PROPERTY TOOL</div>", unsafe_allow_html=True)
    st.title("Price Estimator")
    st.warning("Demo estimate only — this is not a validated Indian property valuation model. Do not use it for buying, selling, lending, or legal decisions.")
    c1,c2=st.columns(2)
    with c1:
        location=st.selectbox("Location",["Bengaluru","Hyderabad","Chennai","Vijayawada","Mumbai","Delhi NCR","Other"])
        ptype=st.selectbox("Property type",["Apartment","Independent house","Villa","Plot / land"])
        area=st.number_input("Area (sq ft)",min_value=100,value=1200,step=50)
    with c2:
        age=st.selectbox("Property age",["New / under 1 year","1–5 years","6–10 years","11–20 years","Over 20 years"])
        quality=st.select_slider("Finish level",options=["Basic","Standard","Premium"])
        custom_rate=st.number_input("Assumed rate per sq ft (₹)",min_value=100,value=5000,step=250,help="Enter a local rate you have independently checked.")
    age_factor={"New / under 1 year":1.0,"1–5 years":0.96,"6–10 years":0.90,"11–20 years":0.80,"Over 20 years":0.68}[age]
    quality_factor={"Basic":0.85,"Standard":1.0,"Premium":1.25}[quality]
    estimate=area*custom_rate*age_factor*quality_factor
    st.metric("Illustrative estimate",f"₹{estimate:,.0f}")
    st.write(f"Illustrative range: **₹{estimate*0.9:,.0f} – ₹{estimate*1.1:,.0f}**")
    st.caption(f"Location selected: {location} · Type: {ptype}. The location is recorded for context only; it does not automatically verify local market rates.")
    st.info("For a meaningful estimate, use verified local comparable sales, land value, building condition, approvals, and professional valuation.")

elif page == "Construction Budget":
    st.markdown("<div class='eyebrow'>PLAN YOUR SPEND</div>", unsafe_allow_html=True)
    st.title("Construction Budget")
    st.write("Create a rough construction budget in rupees. Rates are sample assumptions and should be replaced with local contractor quotations.")
    c1,c2,c3=st.columns(3)
    with c1: built_area=st.number_input("Built-up area per floor (sq ft)",min_value=100,value=1000,step=50)
    with c2: floor_count=st.selectbox("Number of floors",[1,2,3,4])
    with c3: build_type=st.selectbox("Construction finish",["Basic","Standard","Premium"])
    rates={"Basic":1800,"Standard":2300,"Premium":3000}
    rate=rates[build_type]
    total_area=built_area*floor_count
    total=total_area*rate
    st.markdown("---")
    st.metric("Indicative total budget",f"₹{total:,.0f}")
    st.caption(f"Calculation: {total_area:,.0f} sq ft × ₹{rate:,}/sq ft. Excludes land cost and may exclude approvals, taxes, compound wall, interiors and unusual site works.")
    breakdown={"Structure & civil work":0.40,"Finishes & flooring":0.20,"Electrical & plumbing":0.12,"Doors & windows":0.10,"Painting":0.06,"Kitchen & basic fittings":0.07,"Contingency":0.05}
    st.subheader("Estimated cost breakdown")
    for label,pct in breakdown.items():
        val=total*pct
        st.write(f"**{label} — {pct*100:.0f}%** · ₹{val:,.0f}")
        st.progress(pct)
    st.info("Get a detailed bill of quantities and written quotations from local professionals before committing to a budget.")

elif page == "About Us":
    st.markdown("<div class='eyebrow'>OUR STORY · OUR APPROACH</div>", unsafe_allow_html=True)
    st.title("About Urbaan Auraa Space Designer")
    st.image(img_url("photo-1600210492486-724fe5c67fb0",1600),use_container_width=True)
    st.subheader("Spaces shaped around you.")
    st.write("Urbaan Auraa Space Designer is a design-focused concept that helps people explore ideas for homes and interiors, plan spaces thoughtfully, and begin understanding project budgets.")
    st.write("We believe a good space should reflect the people who use it — their needs, lifestyle, preferences, comfort, and budget. Our approach brings inspiration and practical planning together, so every decision starts with a clearer picture.")
    c1,c2=st.columns(2)
    with c1:
        st.markdown("<div class='panel'><h3>Our purpose</h3><p>Make design exploration simpler, more approachable, and more personal — from the first inspiration to early planning.</p><h3>Our design values</h3><ul><li>Client needs first</li><li>Comfort and functionality</li><li>Thoughtful use of space</li><li>Budget-aware choices</li><li>Timeless, considered aesthetics</li></ul></div>",unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='panel'><h3>What you can explore</h3><ul><li>Interior design inspiration</li><li>Room-wise design gallery</li><li>Plot area planning</li><li>Indicative property estimates</li><li>Construction budget planning</li></ul><h3>Contact</h3><p><b>App:</b> Urbaan Auraa Space Designer</p><p><b>Phone:</b> 8310218810</p><p><b>Email:</b> urbaan.auraa.space.designer@gmail.com</p><p class='small-muted'>Please confirm the email address is active before publishing or using it for business communication.</p></div>",unsafe_allow_html=True)
    st.caption("This application is a project/demo tool. Estimates are indicative and are not a substitute for advice from qualified architects, engineers, valuers, or contractors.")

st.markdown("---")
st.caption("© 2026 Urbaan Auraa Space Designer · Design inspiration and planning tools")
