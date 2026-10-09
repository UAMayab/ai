"""AI at Work: A Field Guide to Deep Learning and Generative AI
— Activity 18 (Sessions 34-36).

Run locally with:
    streamlit run app.py
"""

from pathlib import Path

import numpy as np
import plotly.graph_objects as go
import streamlit as st
from PIL import Image

import demos
import tools

st.set_page_config(page_title="AI at Work: Field Guide", page_icon="🧭", layout="wide")

HERE = Path(__file__).parent
BLUE, RED = "#4C8BF5", "#E94F64"


def content(name):
    """Return a content file's text split at its demo markers: {'intro': ..., marker: text after it}."""
    text = (HERE / "content" / f"{name}.md").read_text(encoding="utf-8")
    parts, current = {}, "intro"
    for line in text.splitlines(keepends=True):
        if line.strip().startswith("<!-- demo"):
            current = line.strip()[5:-4].strip()
            continue
        parts[current] = parts.get(current, "") + line
    return parts


def sources(items):
    with st.expander("Sources"):
        st.markdown("\n".join(f"- [{label}]({url})" for label, url in items))


@st.cache_data
def load_image(name, max_side=420, gray=False):
    img = Image.open(HERE / "images" / name).convert("L" if gray else "RGB")
    img.thumbnail((max_side, max_side))
    return np.asarray(img)


st.title("🧭 AI at Work: A Field Guide to Deep Learning and Generative AI")
st.markdown(
    "Sessions 34–36 in one place, **updated for 2026**: what deep learning and generative AI really are, how "
    "people build with them today, and four hands-on missions with free tools you are likely to use in your "
    "job. Where the course text is outdated or wrong, each section says so and explains what is accurate. "
    f"Tool information was last checked on **{tools.LAST_VERIFIED}**."
)

tab_dl, tab_gen, tab_build, tab_lab, tab_resp = st.tabs([
    "🧠 Deep Learning (S34)", "✨ Generative AI (S35)", "🛠️ Building with GenAI (S36)", "🧪 Tool Lab", "🛡️ Using AI Responsibly",
])

# ------------------------------------------------------------ Deep learning
with tab_dl:
    parts = content("s34_deep_learning")
    st.markdown(parts["intro"])
    st.subheader("Try it: what a convolutional filter computes")
    gray = load_image("chelsea.png", gray=True).astype(float)
    col_pick, col_kernel = st.columns([1, 1])
    name = col_pick.radio("Filter", list(demos.FILTERS), horizontal=True, key="dl_filter")
    kernel = demos.FILTERS[name]
    col_kernel.markdown("**The filter's 9 numbers**")
    col_kernel.dataframe([[f"{v:.2f}".rstrip("0").rstrip(".") for v in row] for row in kernel], hide_index=True)
    fmap = demos.apply_filter(gray, kernel)
    col_a, col_b = st.columns(2)
    col_a.image(gray.astype(np.uint8), caption="Input (grayscale). Photo: Stéfan van der Walt, CC0.", width="stretch")
    col_b.image(demos.to_image(fmap, name in demos.EDGE_FILTERS), width="stretch",
                caption=f"Feature map after {name}" + (" (brightness = edge strength)" if name in demos.EDGE_FILTERS else ""))
    st.caption("Each output pixel = the 9 pixels under the filter, multiplied by the filter's 9 numbers and added up. "
               "(Strictly this is cross-correlation, the operation every CNN library actually computes.)")
    st.markdown(parts["demo"])
    sources([
        ("McCulloch & Pitts (1943), A logical calculus of the ideas immanent in nervous activity", "https://doi.org/10.1007/BF02478259"),
        ("Fukushima (1980), Neocognitron", "https://doi.org/10.1007/BF00344251"),
        ("Rumelhart, Hinton & Williams (1986), Learning representations by back-propagating errors", "https://www.nature.com/articles/323533a0"),
        ("LeCun et al. (1989), Backpropagation applied to handwritten zip code recognition", "https://doi.org/10.1162/neco.1989.1.4.541"),
        ("Hochreiter & Schmidhuber (1997), Long short-term memory", "https://doi.org/10.1162/neco.1997.9.8.1735"),
        ("LeCun et al. (1998), Gradient-based learning applied to document recognition (LeNet-5)", "https://doi.org/10.1109/5.726791"),
        ("Krizhevsky, Sutskever & Hinton (2012), ImageNet classification with deep CNNs (AlexNet)", "https://proceedings.neurips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html"),
        ("He et al. (2015), Delving deep into rectifiers (surpassing estimated human error on ImageNet)", "https://arxiv.org/abs/1502.01852"),
        ("Vaswani et al. (2017), Attention is all you need", "https://arxiv.org/abs/1706.03762"),
        ("Dosovitskiy et al. (2020), An image is worth 16x16 words (Vision Transformer)", "https://arxiv.org/abs/2010.11929"),
    ])

# ------------------------------------------------------------ Generative AI
with tab_gen:
    parts = content("s35_generative_ai")
    st.markdown(parts["intro"])
    st.subheader("Try it: temperature")
    temperature = st.slider("Temperature", 0.1, 2.0, 1.0, 0.1, key="gen_temperature")
    probs = demos.next_word_probabilities(temperature)
    col_chart, col_samples = st.columns([3, 2])
    fig = go.Figure(go.Bar(x=demos.NEXT_WORDS, y=probs, marker_color=[BLUE if p == probs.max() else "#B0B7C3" for p in probs],
                           text=[f"{p:.1%}" for p in probs], textposition="outside"))
    fig.update_layout(title=f"\"{demos.PROMPT} ...\": probability of each next word at temperature {temperature:.1f}",
                      yaxis_tickformat=".0%", yaxis_range=[0, 1.1], height=380, margin=dict(t=50))
    col_chart.plotly_chart(fig, width="stretch", key="gen_probs")
    with col_samples:
        st.markdown("**10 sampled continuations** (fixed random seed, so you can compare temperatures):")
        st.markdown("\n".join(f"{i + 1}. {demos.PROMPT} **{w}**" for i, w in enumerate(demos.sample_words(temperature))))
        st.caption("The scores behind this table are made up for illustration; the softmax-with-temperature math is real.")
    st.markdown(parts["demo-sampling"])
    st.subheader("Try it: the forward (noising) process")
    t = st.slider("Diffusion step t (0 = original, 1000 = pure noise)", 0, demos.T_STEPS, 0, 10, key="gen_t")
    signal, noise = demos.signal_and_noise(t)
    col_img, col_info = st.columns([2, 1])
    col_img.image(demos.noisy_image(load_image("coffee.png"), t), width="stretch",
                  caption=f"Step {t}. Photo: Rachel Michetti, courtesy of Pikolo Espresso Bar, CC0.")
    with col_info:
        st.metric("Share of the original image kept (√ᾱₜ)", f"{signal:.3f}")
        st.metric("Amount of noise mixed in (√(1 − ᾱₜ))", f"{noise:.3f}")
        st.caption("x_t = √ᾱₜ · x₀ + √(1 − ᾱₜ) · noise, with the 1,000-step schedule of Ho, Jain & Abbeel (2020). "
                   "A diffusion model is trained to undo one small step of this at a time.")
    st.markdown(parts["demo-diffusion"])
    sources([
        ("Kingma & Welling (2013), Auto-encoding variational Bayes (VAE)", "https://arxiv.org/abs/1312.6114"),
        ("Goodfellow et al. (2014), Generative adversarial networks", "https://arxiv.org/abs/1406.2661"),
        ("Vaswani et al. (2017), Attention is all you need (Transformer)", "https://arxiv.org/abs/1706.03762"),
        ("Ho, Jain & Abbeel (2020), Denoising diffusion probabilistic models", "https://arxiv.org/abs/2006.11239"),
        ("Lewis et al. (2020), Retrieval-augmented generation", "https://arxiv.org/abs/2005.11401"),
        ("Rombach et al. (2022), High-resolution image synthesis with latent diffusion models", "https://arxiv.org/abs/2112.10752"),
        ("Ouyang et al. (2022), Training language models to follow instructions with human feedback (RLHF)", "https://arxiv.org/abs/2203.02155"),
    ])

# ------------------------------------------------------------ Building with GenAI
with tab_build:
    st.markdown(content("s36_building")["intro"])
    sources([
        ("Google Cloud (April 2026), Introducing Gemini Enterprise Agent Platform", "https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform"),
        ("Microsoft Learn, What is Microsoft Foundry", "https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry"),
        ("Amazon Bedrock", "https://aws.amazon.com/bedrock/"),
        ("Google AI Studio and Gemini API pricing (free tier)", "https://ai.google.dev/gemini-api/docs/pricing"),
    ])

# ------------------------------------------------------------ Tool Lab
with tab_lab:
    st.header("Four missions with real tools")
    st.markdown(
        "Complete **Missions 1–4** (the Bonus is optional) and write one **Tool Review Card** for each in "
        "`A18_ToolReviews.md`. Every mission works on a **free plan**. Use your **school accounts** where the "
        "mission says so, and read the **🛡️ Using AI Responsibly** tab before you start."
    )
    for mission in tools.MISSIONS:
        with st.expander(f"**{mission['id']}** ({mission['session']}): {mission['title']}", expanded=mission["id"] == "Mission 1"):
            st.markdown(f"*Why this matters at work:* {mission['why']}")
            st.markdown("\n".join(f"{i + 1}. {step}" for i, step in enumerate(mission["steps"])))
            if mission["id"] == "Mission 2":
                st.markdown("**The ShopSmart memo** (fictional: copy it exactly):")
                st.code(tools.SAMPLE_MEMO, language=None)
                st.markdown("**Factual questions** (pick one; check the answer at the official source):")
                st.markdown("\n".join(f"- {q} [Official source]({url})" for q, url in tools.FACT_QUESTIONS))
            if mission["id"] == "Mission 3":
                st.markdown(f"[UNESCO (2023), Guidance for generative AI in education and research]({tools.UNESCO_GUIDANCE})")
            if mission["id"] == "Bonus":
                st.markdown(f"[Content Credentials verify tool]({tools.CONTENT_CREDENTIALS_VERIFY})")
            st.markdown(f"**Evidence for your Tool Review Card:** {mission['evidence']}")
            st.markdown("**Tools**")
            for key in mission["tools"]:
                tool = tools.TOOLS[key]
                st.markdown(
                    f"- **[{tool['name']}]({tool['url']})**. Account: {tool['account']} Free plan: {tool['free']} "
                    f"Data: {tool['data']} Age: {tool['age']} ([source]({tool['source']}))"
                )
    st.caption(f"Free plans change often. Everything above was checked on the linked official pages on {tools.LAST_VERIFIED}. "
               "If a tool no longer works as described, use another tool from the same mission and say so in your review.")

# ------------------------------------------------------------ Responsible use
with tab_resp:
    st.markdown(content("responsible")["intro"])
    sources([
        ("Google Workspace for Education: Gemini and Gemini Notebook quickstart", tools.TOOLS["gemini_edu"]["source"]),
        ("Microsoft Learn: Manage Microsoft 365 Copilot Chat", tools.TOOLS["copilot_edu"]["source"]),
        ("OpenAI: Data controls in ChatGPT", tools.TOOLS["chatgpt"]["source"]),
        ("Anthropic: minimum age requirement", tools.TOOLS["claude"]["source"]),
        ("Anthropic: updates to consumer terms (model-training choice)", "https://www.anthropic.com/news/updates-to-our-consumer-terms"),
        ("C2PA (Content Credentials standard)", "https://c2pa.org/"),
        ("Content Credentials verify tool", tools.CONTENT_CREDENTIALS_VERIFY),
        ("IEA, Energy and AI: energy demand from AI", "https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai"),
        ("EU AI Act, Regulation (EU) 2024/1689", "https://eur-lex.europa.eu/eli/reg/2024/1689/oj"),
        ("Orrick (July 2026), EU AI Act update: Digital Omnibus", "https://www.orrick.com/en/Insights/2026/07/EU-AI-Act-Update-Digital-Omnibus-Finalizes-8-Compliance-Changes"),
    ])
