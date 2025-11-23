import streamlit as st
from datetime import datetime

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------
st.set_page_config(
    page_title="GoalSignalAI – Madison Match Intelligence",
    page_icon="⚽",
    layout="wide"
)

# ------------------------------------------------
# HEADER / HERO
# ------------------------------------------------
st.markdown(
    """
    <style>
    .gs-hero-title {
        font-size: 2.4rem;
        font-weight: 800;
        letter-spacing: 0.03em;
    }
    .gs-tagline {
        font-size: 1.0rem;
        opacity: 0.85;
    }
    .gs-pill {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 999px;
        font-size: 0.8rem;
        border: 1px solid rgba(0,255,180,0.3);
        margin-bottom: 0.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="gs-pill">GoalSignalAI • Madison Framework</div>', unsafe_allow_html=True)
st.markdown('<div class="gs-hero-title">Madison Match Intelligence Assistant</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="gs-tagline">Where emotion meets football data — turning match scenarios into structured Madison insights for coaches, analysts, and storytellers.</div>',
    unsafe_allow_html=True
)

st.caption("Describe any football scenario, pick your goal, and get a Madison-style breakdown of **opportunities, risks, and next steps**.")

st.divider()

# ------------------------------------------------
# CORE ANALYSIS LOGIC (placeholder – no external API)
# ------------------------------------------------

def run_madison_analysis(
    scenario: str,
    context: str,
    goal: str,
    include_emotion: bool,
    detail_level: str
):
    """
    Placeholder Madison-style analysis for GoalSignalAI.

    This DOES NOT call any external AI API.
    It simply structures the input into a Madison-flavored response.

    Later you can plug in your real Madison agent here.
    """

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Summary
    summary = (
        f"In this scenario, you are focusing on **{context.lower()}** with a primary goal of "
        f"**{goal}**. The assistant reads your description as a football decision moment and "
        "frames it using Madison-style reasoning: defining the situation, diagnosing the drivers, "
        "and directing next steps."
    )

    # Opportunities (very light pseudo-logic based on goal)
    opps = []

    if "Performance" in goal:
        opps.append("You can use data to tune tactics, player roles, and in-game adjustments more systematically.")
        opps.append("There is room to run small experiments (pressing triggers, shape changes, substitutions) and track impact over time.")
    if "Engagement" in goal:
        opps.append("The scenario creates strong hooks for fan stories, graphics, and real-time content.")
        opps.append("You can segment fans by behavior or channel and test different narrative angles.")
    if "Scouting" in goal:
        opps.append("You can benchmark this player or unit against similar profiles using consistent metrics.")
        opps.append("You can spot undervalued traits (off-ball movement, pressing intensity, decision timing) that don’t show up in basic stats.")
    if "Commercial" in goal:
        opps.append("There is a clear opportunity to tie performance moments to sponsor messaging or premium content.")
        opps.append("You can use match data plus fan behavior to design targeted campaigns and offers.")
    if not opps:
        opps.append("There is clear space to use structured data and Madison-style thinking to clarify what ‘good’ looks like.")
        opps.append("You can turn this scenario into a repeatable framework for future decisions.")

    # Emotion layer (optional)
    emotion_text = ""
    if include_emotion:
        emotion_text = (
            " This scenario also carries an emotional layer: fan reactions, momentum swings, and narrative arcs. "
            "Capturing those signals can explain *why* certain decisions feel right or wrong, beyond pure xG or passing maps."
        )

    # Risks
    risks = [
        "If you rely only on surface-level stats, you might miss deeper patterns in positioning, pressure, or decision timing.",
        "Bias from recent matches or highlight moments can distort how you judge players, tactics, or campaigns.",
        "Operational constraints (staff time, data quality, tech stack) can limit how much of this analysis gets used week-to-week.",
    ]

    if include_emotion:
        risks.append("Over-weighting emotional spikes (big wins/losses, viral clips) can lead to reactive decisions that don’t scale.")

    # Recommendations (Madison-style Direct)
    recs = [
        "Write down a clear, single success metric for this scenario (e.g., xG difference, chance quality, engagement rate, or revenue per fan).",
        "Use a small pilot approach: test one or two changes rather than redesigning everything at once.",
        "Review results within 24–48 hours with key stakeholders and decide whether to scale, tweak, or stop.",
    ]

    if include_emotion:
        recs.append("Pair event-level data (shots, passes, phases) with emotional markers (crowd reaction, social spikes) to see where emotion and performance align.")
        recs.append("Capture learnings as short ‘Madison snapshots’ so that coaches, analysts, and media teams can reuse the logic later.")

    # Adjust detail level slightly
    if detail_level == "Concise":
        opps = opps[:2]
        risks = risks[:2]
        recs = recs[:3]
    elif detail_level == "More detailed":
        opps.append("Layer Madison thinking over time: define the situation pre-match, diagnose live, and direct adjustments after the game.")
        risks.append("Without clear ownership, insights may stay in tools instead of shaping matchday decisions.")
        recs.append("Assign a clear owner for Madison-style reviews so that insights consistently reach coaches and decision-makers.")

    return {
        "timestamp": timestamp,
        "summary": summary + emotion_text,
        "opportunities": opps,
        "risks": risks,
        "recommendations": recs,
    }

# ------------------------------------------------
# LAYOUT – INPUTS
# ------------------------------------------------

left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader("1. Describe the match situation")

    scenario = st.text_area(
        "In plain language, describe the football scenario you’re thinking about.",
        placeholder=(
            "Example: We’re preparing for a derby match where we struggle to defend transitions. "
            "Our front three press high but the midfield gets stretched, and we’re unsure how to "
            "balance risk vs control..."
        ),
        height=200,
    )

    context = st.selectbox(
        "Context",
        [
            "Pre-match game plan",
            "In-game decision / adjustment",
            "Post-match review",
            "Player scouting / recruitment",
            "Fan engagement / storytelling",
            "Commercial / sponsorship decision",
        ],
    )

    goal = st.selectbox(
        "Primary goal",
        [
            "On-pitch Performance",
            "Fan Engagement",
            "Scouting & Recruitment",
            "Commercial & Sponsorship",
            "General Decision Clarity",
        ],
    )

    include_emotion = st.checkbox(
        "Include emotion / fan-sentiment layer",
        value=True,
        help="Adds an extra focus on crowd energy, narrative swings, and fan reaction."
    )

    detail_level = st.radio(
        "How detailed should the analysis be?",
        ["Concise", "Standard", "More detailed"],
        horizontal=True,
    )

    run_button = st.button("⚽ Run Madison Match Intelligence", type="primary")

with right_col:
    st.subheader("What this assistant does (for non-technical users)")
    st.markdown(
        """
        **Madison Match Intelligence** is a GoalSignalAI prototype that helps you think
        through football decisions using a structured lens.

        **You provide:**
        - A short description of a match, player, or campaign scenario  
        - The context (pre-match, in-game, post-match, scouting, fan engagement, etc.)  
        - Your primary goal (performance, engagement, scouting, commercial, or clarity)  

        **You get back:**
        - A clear summary of the situation  
        - Madison-style **opportunities**  
        - Key **risks & constraints**  
        - Practical **recommendations** you can act on  

        There’s no code, no dashboards to configure — just football questions turned into
        structured thinking.
        """
    )

    st.divider()
    st.markdown(
        """
        **How this fits GoalSignalAI:**  
        This assistant acts as the “thinking layer” on top of match data and emotion signals,
        helping coaches, analysts, and content teams align on what to try next.
        """
    )

st.divider()

# ------------------------------------------------
# OUTPUT SECTION
# ------------------------------------------------

if run_button:
    if not scenario.strip():
        st.error("Please describe your football scenario before running the analysis.")
    else:
        with st.spinner("Reading the game in Madison mode..."):
            result = run_madison_analysis(
                scenario=scenario,
                context=context,
                goal=goal,
                include_emotion=include_emotion,
                detail_level=detail_level,
            )

        st.success("Analysis complete.")

        st.subheader("2. Madison-structured view")

        st.markdown(f"_Generated on: **{result['timestamp']}**_")

        # Summary
        st.markdown("### 📝 Summary")
        st.write(result["summary"])

        # Opportunities
        st.markdown("### ✅ Opportunities")
        for i, item in enumerate(result["opportunities"], start=1):
            st.markdown(f"- **Opportunity {i}:** {item}")

        # Risks
        st.markdown("### ⚠️ Risks & Constraints")
        for i, item in enumerate(result["risks"], start=1):
            st.markdown(f"- **Risk {i}:** {item}")

        # Recommendations
        st.markdown("### 🎯 Recommendations")
        for i, item in enumerate(result["recommendations"], start=1):
            st.markdown(f"- **Next Step {i}:** {item}")

        # Echo back situation
        with st.expander("📌 View the scenario you entered"):
            st.write(scenario)

# ------------------------------------------------
# FOOTER – PORTFOLIO INTEGRATION
# ------------------------------------------------

st.divider()
st.markdown(
    """
    _Prototype built for INFO7375 – Branding & AI (Madison Framework)._  

    **GoalSignalAI landing page:** https://v0-goal-signal-ai-landing-page.vercel.app/  

    """
)
