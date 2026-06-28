import streamlit as st
import pandas as pd
import random

# 1. Page Configuration & Theme Overrides
st.set_page_config(
    page_title="Wealthora YouTube Studio v4 Pro",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Premium Navy & Gold CSS Styling injection
st.markdown("""
    <style>
    .stApp {
        background-color: #0d1060;
        color: #f8f7f2;
    }
    .hdr-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 32px;
        font-weight: 700;
        color: #E8C800;
        margin-bottom: 0px;
    }
    .hdr-subtitle {
        font-size: 14px;
        color: #ffffff;
        opacity: 0.8;
    }
    .custom-card {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(232, 200, 0, 0.2);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
    }
    .card-title {
        font-size: 13px;
        font-weight: 700;
        color: #E8C800;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-bottom: 15px;
    }
    .badge-gold {
        background-color: #E8C800;
        color: #0d1060;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- SESSION STATE INITIALIZATION ---
if 'current_phase' not in st.session_state:
    st.session_state.current_phase = "PHASE 1 - Search & Topics"
if 'generated_topics' not in st.session_state:
    st.session_state.generated_topics = None
if 'active_context' not in st.session_state:
    st.session_state.active_context = {}
if 'pipeline' not in st.session_state:
    st.session_state.pipeline = []

# --- HEADER BRANDING ---
st.markdown("""
<div style='display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #E8C800; padding-bottom: 10px; margin-bottom: 20px;'>
    <div>
        <h1 class='hdr-title'>Wealthora <span style='color:#fff; font-weight:300;'>YouTube Studio Pro</span></h1>
        <p class='hdr-subtitle'>High-Retention Video Engineering Engine</p>
    </div>
    <div>
        <span class='badge-gold'>AUTOMATION LIVE</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
phase_options = ["PHASE 1 - Search & Topics", "PHASE 2 - Script & Creative Assets", "PHASE 3 - Optimisation & Launch"]
selected_nav = st.sidebar.radio("Studio Engine Phases", phase_options, index=phase_options.index(st.session_state.current_phase))
st.session_state.current_phase = selected_nav

# Niche Data Engine (Simulating SEO High-Volume Search Data)
niche_keywords = {
    "Agency Performance Stack": ["workflow automation for agency", "scale digital agency operations", "agency software stack 2026", "stop manual client onboarding"],
    "Real Estate Content Matrix": ["real estate content strategy", "how to get real estate leads online", "nigerian real estate marketing", "instagram ads for property sales"],
    "Digital Fatigue Reset": ["prevent developer burnout", "productivity systems for remote workers", "digital fatigue recovery", "ergonomic workspace design"],
    "IntentIQ": ["track warm leads social media", "social media intent tracking tool", "how to find high intent buyers", "automated social listening software"]
}

# ==========================================
# PHASE 1: HIGH-SEARCH TOPIC GENERATION
# ==========================================
if st.session_state.current_phase == "PHASE 1 - Search & Topics":
    st.markdown("### 🔍 Step 1: Target High-Volume Search Intent")
    
    with st.container():
        st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
        st.markdown("<p class='card-title'>Niche Architecture Settings</p>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            product = st.selectbox("Core Product Ecosystem", list(niche_keywords.keys()))
            video_type = st.selectbox("Algorithmic Format", ["Search-Optimised How-To", "High-Retention Listicle", "Case Study Blueprint", "Deep-Dive Masterclass"])
        with col2:
            formula = st.selectbox("Script Engagement Formula", ["PPB (Problem, Promise, Bridge)", "PAS (Problem, Agitate, Solve)", "AIDA (Attention, Interest, Desire, Action)"])
            tone = st.selectbox("Narrative Persona", ["Authoritative Expert", "Conversational Strategist", "Urgent Urgency"])
        
        if st.button("⚡ Generate Search-Optimised Topics", type="primary"):
            keywords = niche_keywords[product]
            st.session_state.generated_topics = [
                {"title": f"How to Solve {keywords[0].title()} Using Systems", "search_volume": "High (8.5k/mo)", "competition": "Low", "keyword": keywords[0]},
                {"title": f"The Ultimate Blueprint for {keywords[1].title()}", "search_volume": "Medium (4.2k/mo)", "competition": "Very Low", "keyword": keywords[1]},
                {"title": f"Why Most People Fail at {keywords[2].title()}", "search_volume": "High (12.1k/mo)", "competition": "Medium", "keyword": keywords[2]},
                {"title": f"How We Automated {keywords[3].title()} in 48 Hours", "search_volume": "Medium (3.1k/mo)", "competition": "Low", "keyword": keywords[3]}
            ]
        st.markdown("</div>", unsafe_allow_html=True)

    if st.session_state.generated_topics:
        st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
        st.markdown("<p class='card-title'>🎯 Select Engineered Target Topic</p>", unsafe_allow_html=True)
        
        for idx, item in enumerate(st.session_state.generated_topics):
            col_t, col_v, col_c, col_b = st.columns([4, 1, 1, 1])
            col_t.write(f"**{item['title']}**\n*Target Keyword: {item['keyword']}*")
            col_v.success(item['search_volume'])
            col_c.warning(item['competition'])
            if col_b.button("Select & Craft", key=f"btn_{idx}"):
                st.session_state.active_context = {
                    "title": item['title'], "product": product, "keyword": item['keyword'],
                    "formula": formula, "tone": tone, "type": video_type
                }
                st.session_state.current_phase = "PHASE 2 - Script & Creative Assets"
                st.sidebar.success(f"Context locked: {item['title'][:20]}...")
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# PHASE 2: SCRIPT & CREATIVE ASSET DEPLOYMENT
# ==========================================
elif st.session_state.current_phase == "PHASE 2 - Script & Creative Assets":
    st.markdown("### ✍️ Step 2: Content Asset Generation Workspace")
    
    if not st.session_state.active_context:
        st.warning("⚠️ No topic context selected. Please return to Phase 1 and generate/select a target topic first.")
    else:
        ctx = st.session_state.active_context
        st.info(f"📐 **Active Topic Engine:** {ctx['title']} | **Target Keyword:** {ctx['keyword']}")
        
        p2_tabs = st.tabs(["📜 Dynamic Retention Script", "🎞 B-Roll & Visual Asset Prompting", "🎨 Thumbnail Blueprint"])
        
        with p2_tabs[0]:
            st.markdown("<p class='card-title'>Premium High-Retention Voiceover Script</p>", unsafe_allow_html=True)
            generated_script = f"""[HOOK - 0:00 - 0:30]
(Visual Alert Sound) If you are still trying to handle {ctx['keyword']} completely manually, you are burning cash. Most creators fail because they lack systems. In this video, we are breaking down the exact blueprint to fix this forever using the {ctx['product']} ecosystem.

[BODY SECTION - 0:30 - 6:00]
Let's analyze the core operational bottleneck. Here is exactly how to execute this strategy using the {ctx['formula']} structural approach...
* Point 1: Eliminating structural frictions.
* Point 2: Leveraging automated digital frameworks.

[CALL TO ACTION - 6:00]
Do not leave your operational scaling to guesswork. Tap the absolute first link pinned in the comments section below to clone our {ctx['product']} framework directly into your workspace right now."""
            
            st.text_area("Live Editable Script Interface", value=generated_script, height=300)
            
        with p2_tabs[1]:
            st.markdown("<p class='card-title'>🎬 Time-Coded B-Roll Stock Video Asset Prompts</p>", unsafe_allow_html=True)
            st.markdown(f"""
            * **0:00 - 0:15:** *Search Query for Pexels/Pixabay:* `frustrated business owner laptop dark room`
            * **0:15 - 0:45:** *Search Query for Pexels/Pixabay:* `futuristic glowing abstract digital network animation`
            * **0:45 - 2:00:** *Search Query for Pexels/Pixabay:* `clean professional modern office aesthetic charts overhead camera`
            * **2:00 - End:** *Search Query for Pexels/Pixabay:* `finger pressing screen tracking success matrix display dashboard`
            """)
            
        with p2_tabs[2]:
            st.markdown("<p class='card-title'>🖼 Viral Contrast Thumbnail Design Directive</p>", unsafe_allow_html=True)
            st.code(f"""
-- Background Theme: Dark Navy Gradient with subtle grid texture overlay.
-- Focal Point Left side: High contrast bright image of a dashboard mockup displaying positive growth trends.
-- Bold Text Right side: "FIX THIS NOW!" or "STOP DOING THIS!" written in large extra-bold impact typography.
-- Color Pattern: Base background #0d1060 accented strictly with hyper-vivid Gold (#E8C800) typography shadows.
            """, language="text")
            
        if st.button("Push Configuration Forward to Deployment Stack ➡️"):
            if not any(v['title'] == ctx['title'] for v in st.session_state.pipeline):
                st.session_state.pipeline.append({"title": ctx['title'], "product": ctx['product'], "status": "Ready to Export"})
            st.session_state.current_phase = "PHASE 3 - Optimisation & Launch"
            st.shape = st.rerun()

# ==========================================
# PHASE 3: OPTIMISATION & LAUNCH CHECKLISTS
# ==========================================
elif st.session_state.current_phase == "PHASE 3 - Optimisation & Launch":
    st.markdown("### 🚀 Step 3: SEO Architecture & Publishing Deployment")
    
    if not st.session_state.active_context:
        st.warning("⚠️ Select a topic context to populate localized SEO metadata tags.")
    else:
        ctx = st.session_state.active_context
        
        p3_tabs = st.tabs(["📝 YouTube Meta Packaging", "✅ Quality Launch Metrics", "📈 Live Project Stack"])
        
        with p3_tabs[0]:
            st.markdown("<p class='card-title'>Optimized Video Metadata Architecture</p>", unsafe_allow_html=True)
            st.text_input("Algorithmic Optimized Title Tag", value=f"{ctx['title']} ({datetime.date.today().year} Masterclass)")
            
            description_copy = f"""👉 Access the complete {ctx['product']} Engine Ecosystem here: [YOUR LINK HERE]

Are you trying to master {ctx['keyword']} without losing hours to repetitive administrative tasks? In this premium masterclass guide, we map out the scaling strategy built into the {ctx['product']} matrix.

TIMESTAMPS:
0:00 - The Massive {ctx['keyword']} Friction Point
1:45 - Step-by-Step Execution Framework
5:10 - How to Deploy the {ctx['product']} Solution

#automation #{ctx['product'].replace(' ', '')} #digitalgrowth #systems"""
            st.text_area("Search Optimized Description Box", value=description_copy, height=220)
            st.text_input("Semantic Search Tags & Keywords (Paste into YouTube Studio Tags box)", value=f"{ctx['keyword']}, {ctx['product'].lower()}, business automation, agency systems, viral workflows")
            
        with p3_tabs[1]:
            st.markdown("<p class='card-title'>Pre-Flight YouTube Standard Checklists</p>", unsafe_allow_html=True)
            st.checkbox("B-Roll clips accurately follow the suggested asset prompts to match the audio pacing", value=True)
            st.checkbox("Acoustic ambient levels are mixed down cleanly below -14dB relative to the primary voice layer", value=True)
            st.checkbox("The direct funnel redirection link is copied and ready to be set as the absolute first pinned comment link", value=False)
            
        with p3_tabs[2]:
            st.markdown("<p class='card-title'>Active Video Production Tracker</p>", unsafe_allow_html=True)
            if st.session_state.pipeline:
                st.dataframe(pd.DataFrame(st.session_state.pipeline), use_container_width=True)
            else:
                st.info("No active pipeline tracking metrics compiled yet.")
