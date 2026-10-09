"""Tool Lab data for Activity 18: missions, tools, and the sample texts.

Free plans, names, and limits change often. Every fact below was checked on
the official page listed in `source` on LAST_VERIFIED; re-check them before
each semester. Numbers are only given where the official page states them.
"""

LAST_VERIFIED = "October 9, 2026"

TOOLS = {
    "teachable": {
        "name": "Google Teachable Machine",
        "url": "https://teachablemachine.withgoogle.com/train/image",
        "account": "No account needed (a Google account is only used if you choose to save your project to Drive).",
        "free": "Free.",
        "data": "Training runs in your web browser; if you close the tab without saving or uploading, nothing is kept on any server. \"Upload my model\" publishes it at a shareable link, so don't upload models trained on people, and don't film anyone without their permission.",
        "age": "No account, no age gate; follow your school's rules for webcam use.",
        "source": "https://teachablemachine.withgoogle.com/faq",
    },
    "gemini_edu": {
        "name": "Gemini (school Google account)",
        "url": "https://gemini.google.com",
        "account": "Your school Google account.",
        "free": "Included free of charge in all Google Workspace for Education editions.",
        "data": "Google states that with a Workspace for Education account, data is not human reviewed or used to train AI models.",
        "age": "Available to users of all ages through school accounts (stricter content rules under 18).",
        "source": "https://knowledge.workspace.google.com/admin/getting-started/editions/quickstart-guide-to-gemini-and-notebooklm-for-education",
    },
    "copilot_edu": {
        "name": "Microsoft 365 Copilot Chat (school Microsoft account)",
        "url": "https://m365.cloud.microsoft/chat",
        "account": "Your school Microsoft account (the school must have turned it on).",
        "free": "No extra cost for students 13 and older with the school's Microsoft 365 student licenses.",
        "data": "Enterprise data protection applies only when you are signed in with your school account; check for the protection shield before typing.",
        "age": "Students 13 and older.",
        "source": "https://learn.microsoft.com/copilot/manage",
    },
    "chatgpt": {
        "name": "ChatGPT (personal account, fallback)",
        "url": "https://chatgpt.com",
        "account": "A personal account (free plan).",
        "free": "Free plan with usage limits.",
        "data": "Conversations can be used to train models unless you turn off Settings → Data controls → \"Improve the model for everyone\".",
        "age": "13 or older; under 18 needs a parent's or guardian's permission.",
        "source": "https://help.openai.com/en/articles/7730893-data-controls-in-chatgpt",
    },
    "claude": {
        "name": "Claude (personal account, fallback)",
        "url": "https://claude.ai",
        "account": "A personal account (free plan).",
        "free": "Free plan with usage limits.",
        "data": "You choose whether your chats may be used to improve the models; change it any time in Privacy Settings.",
        "age": "18 or older.",
        "source": "https://support.claude.com/en/articles/13117299-minimum-age-requirement-access-restriction",
    },
    "notebook_edu": {
        "name": "Gemini Notebook, formerly NotebookLM (school Google account)",
        "url": "https://notebook.google.com",
        "account": "Your school Google account.",
        "free": "Included free of charge in all Google Workspace for Education editions.",
        "data": "Same Workspace for Education protection as Gemini: not human reviewed or used to train AI models.",
        "age": "Available to users of all ages through school accounts.",
        "source": "https://knowledge.workspace.google.com/admin/getting-started/editions/quickstart-guide-to-gemini-and-notebooklm-for-education",
    },
    "ai_studio": {
        "name": "Google AI Studio, Build mode",
        "url": "https://aistudio.google.com",
        "account": "A Google account (if your school account can't open it, use a personal one).",
        "free": "Google states that AI Studio usage is free of charge in all available regions.",
        "data": "Google states that free-tier content is used to improve its products: type nothing private.",
        "age": "Follow Google's terms for your account type.",
        "source": "https://ai.google.dev/gemini-api/docs/pricing",
    },
    "bolt": {
        "name": "Bolt.new (fallback)",
        "url": "https://bolt.new",
        "account": "A free account.",
        "free": "Free plan: 300,000 tokens per day and 1 million per month; free sites show Bolt branding.",
        "data": "Read the privacy policy on the site; type nothing private.",
        "age": "Follow the site's terms.",
        "source": "https://bolt.new/pricing",
    },
    "lovable": {
        "name": "Lovable (fallback)",
        "url": "https://lovable.dev",
        "account": "A free account.",
        "free": "Free plan: 5 build credits per day, up to 30 per month (they don't roll over).",
        "data": "Read the privacy policy on the site; type nothing private.",
        "age": "Follow the site's terms.",
        "source": "https://lovable.dev/pricing",
    },
    "firefly": {
        "name": "Adobe Firefly",
        "url": "https://firefly.adobe.com",
        "account": "A free Adobe account.",
        "free": "Free daily generations; the limits refresh every day.",
        "data": "Adobe states that it automatically attaches Content Credentials and that Firefly model outputs are safe for commercial use; read the terms before using them.",
        "age": "Follow Adobe's terms.",
        "source": "https://www.adobe.com/products/firefly/plans.html",
    },
    "canva": {
        "name": "Canva (fallback)",
        "url": "https://www.canva.com",
        "account": "A free Canva account.",
        "free": "The free plan includes a small monthly allowance of AI uses.",
        "data": "Read Canva's AI terms before using generated images commercially.",
        "age": "Follow Canva's terms.",
        "source": "https://www.canva.com/help/ai-access/",
    },
}

MISSIONS = [
    {
        "id": "Mission 1", "session": "Session 34", "title": "Train a deep-learning model in your browser",
        "tools": ["teachable"],
        "why": "Every company that uses image recognition depends on good training data. Here you see, in 15 minutes, how a model's data decides what it can and cannot do.",
        "steps": [
            "Open Teachable Machine → **Image Project** → **Standard image model**.",
            "Create **3 classes** of objects you have at hand (for example: pen, phone, mug). Record **at least 50 webcam images** of each, in the same place and light.",
            "Click **Train Model** and wait for it to finish.",
            "In **Preview**, test each class **10 times in the same conditions**. Count how many it gets right.",
            "Now test each class **10 times in new conditions**: a different background, different light, another angle, or another person holding the object. Count again.",
            "Explain any drop in accuracy as a **data** problem: what was missing from your training images?",
            "Under the hood (from the Teachable Machine FAQ): your classes are trained on top of a **pretrained MobileNet** network, a technique called **transfer learning**.",
        ],
        "evidence": "Screenshots of your classes and of the Preview panel, and your two counts (same conditions vs. new conditions) for each class.",
    },
    {
        "id": "Mission 2", "session": "Session 35", "title": "Two assistants, one work task",
        "tools": ["gemini_edu", "copilot_edu", "chatgpt", "claude"],
        "why": "Writing, summarizing, and organizing information with an assistant is now an everyday office skill, and so is catching its mistakes.",
        "steps": [
            "Use **two different assistants**: Gemini (school Google account) and Copilot Chat (school Microsoft account). If one isn't available to you, use ChatGPT or Claude with a personal account instead.",
            "Paste the **ShopSmart memo** below into each assistant, with the **same three requests**: (1) summarize it in 3 bullet points for a busy manager; (2) write a polite reply to the customer complaint in it; (3) make a table of the action items with an owner and a deadline.",
            "Compare the answers: which one is more accurate to the memo? Did either one **invent** something that isn't in the memo?",
            "Ask each assistant **one factual question** from the list below and check its answer against the official source given.",
        ],
        "evidence": "Screenshots of both conversations (your prompts must be visible), plus what you checked and where.",
    },
    {
        "id": "Mission 3", "session": "Session 35", "title": "Research with sources: Gemini Notebook",
        "tools": ["notebook_edu"],
        "why": "Grounded tools answer from documents you give them and show where each answer came from, the safest way to use AI for research and analysis at work.",
        "steps": [
            "Download UNESCO's *Guidance for generative AI in education and research* (2023, free, CC BY-SA 3.0 IGO) and add it to a new notebook. (Or use another public report from your own field.)",
            "Ask **3 questions** about the document. Click one **citation** and check that the passage really says what the answer claims.",
            "Ask **1 question the document cannot answer** (for example, about a law passed after 2023) and record exactly what the tool does.",
            "Optional: generate an **Audio Overview** and listen to the first two minutes.",
        ],
        "evidence": "Screenshots of your questions, one answer with its citation open, and the answer to the question outside the document.",
    },
    {
        "id": "Mission 4", "session": "Session 36", "title": "Build an app by describing it",
        "tools": ["ai_studio", "bolt", "lovable"],
        "why": "Describing what you need, testing what an AI builds, and spotting what's wrong is how many teams now prototype, whatever their job title.",
        "steps": [
            "Open **Google AI Studio → Build** (or Bolt.new, or Lovable). Describe a **small app that is useful in your field**: flashcards for this course, a tip-and-split calculator, a product catalog with search, a portfolio page...",
            "Run it and **test it with 3 different inputs**, including one strange one (an empty field, a negative number, a very long text).",
            "Ask the tool for **at least 2 improvements or fixes**, one at a time.",
            "Record **one bug or problem** you found, and whether the tool fixed it.",
            "Decide: does the lecture's 2023 quote (\"we're not there yet\") still hold for **your** app?",
        ],
        "evidence": "Your first prompt, screenshots of the app before and after your changes, your 3 tests, and the bug you found. Add the app's link if the tool lets you share it.",
    },
    {
        "id": "Bonus", "session": "Session 35", "title": "Create a marketing image and check its credentials",
        "tools": ["firefly", "canva"],
        "why": "Designers, marketers, and animators already use image generators daily, and need to know what they may legally publish.",
        "steps": [
            "Create a marketing image for a ShopSmart product (fictional), using Adobe Firefly (or Canva).",
            "Download the original file and upload it to **contentcredentials.org/verify**. Record what it shows.",
            "Find, in the tool's terms or help pages, whether you may use the image commercially.",
        ],
        "evidence": "Your prompt, the image, a screenshot of the Content Credentials result, and the sentence from the terms about commercial use (with its link).",
    },
]

SAMPLE_MEMO = """INTERNAL MEMO (fictional): ShopSmart Customer Care, weekly summary

From: Customer Care team. To: Operations manager.

1. Late deliveries: 37 orders arrived late this week (up from 22 last week), all from the Mérida warehouse. The new courier, RápidoSur, started on Monday.
2. Complaint: customer Ana López wrote on Thursday that her blender (order 48217) arrived with a cracked jar, 4 days late. She asks for a replacement jar and a refund of the delivery fee (89 MXN).
3. Returns: 12 returns this week, mostly headphones (7). Two customers said the size chart for shoes is confusing.
4. Action items discussed: call RápidoSur about the delays (Operations, by Tuesday); send Ana a replacement jar and refund the fee (Customer Care, by Monday); fix the shoe size chart (Web team, no deadline agreed)."""

FACT_QUESTIONS = [
    ("When did the EU AI Act enter into force?", "https://eur-lex.europa.eu/eli/reg/2024/1689/oj"),
    ("In what year was the Transformer architecture introduced, and in which paper?", "https://arxiv.org/abs/1706.03762"),
    ("Who wrote the first paper on generative adversarial networks (GANs), and when?", "https://arxiv.org/abs/1406.2661"),
]

UNESCO_GUIDANCE = "https://unesdoc.unesco.org/ark:/48223/pf0000386693"
CONTENT_CREDENTIALS_VERIFY = "https://contentcredentials.org/verify"
