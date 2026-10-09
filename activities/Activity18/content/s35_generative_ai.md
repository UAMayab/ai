## The model families behind today's tools

**Generative AI** produces new content (text, images, audio, video, code) that resembles its training data. Four families matter; the first two power almost every tool you will use:

| Family | Idea | Powers |
|---|---|---|
| **Large language models (LLMs)**, built on **transformers** | Predict the **next token** (a word or piece of a word), over and over, using the *whole* text so far. | ChatGPT, Gemini, Claude, Copilot, coding assistants |
| **Diffusion models** | Learn to **remove noise** from an image step by step; to create, start from pure noise and denoise. | Most image and video generators (e.g. Stable Diffusion, DALL·E 3, Google's Imagen and Veo, OpenAI's Sora). Some newer image generators build images piece by piece like an LLM instead. |
| **GANs** (2014) | A *generator* turns random noise into fake samples while a *discriminator* tries to tell fake from real; both improve by competing. | Realistic faces and image editing (2014–2021); still used in niches; largely replaced by diffusion |
| **VAEs** (2013) | Compress data into a small code and learn to rebuild it; sample new codes to create. | Rarely used alone today; a VAE is a component inside many diffusion systems |

## How an LLM picks its next word

An LLM gives a **score** to every possible next token, turns the scores into **probabilities**, and then **samples** one. **Temperature** controls how adventurous that sampling is: low temperature almost always picks the most likely word; high temperature spreads the chances out, so unusual (and sometimes wrong) words appear. The table below is made up for illustration (a real model has a vocabulary of tens of thousands of tokens), but the math is exactly the one LLMs use.

<!-- demo-sampling -->

This is also why **hallucinations** happen (Activity 2): the model produces *plausible* text, not *checked* text. Nothing in next-token prediction looks facts up.

## How diffusion creates an image

Training starts with real images and adds noise in many small steps until nothing but static remains (the **forward process**, below). The network learns to undo one small step at a time. To generate, it starts from pure noise and removes noise step by step, guided by your prompt, until an image appears. (Most image tools do this in a compressed "latent" space for speed.)

<!-- demo-diffusion -->

## Key ideas you will meet at work

- **Tokens and context window.** Models read and write tokens; the context window is how much text (or images) the model can consider at once.
- **Training stages.** *Pre-training* on huge amounts of text (predict the next token), then *fine-tuning* and **RLHF** (reinforcement learning from human feedback; Activity 2) to make the model helpful and follow instructions.
- **Grounding and RAG** (retrieval-augmented generation). The tool first retrieves relevant passages from trusted documents, then answers from them, with citations. This is what Gemini Notebook does (Mission 3), and it reduces, but does not eliminate, hallucinations.
- **Multimodal models** read and produce text, images, and audio together.
- **Agents** are models that can use tools (search, run code, click buttons) and work through multi-step tasks; app builders (Mission 4) are agents.

## What the lecture says vs. what is accurate (2026)

| The lecture says | What is accurate |
|---|---|
| The main types of generative AI are **GANs and RNNs** | Today's tools run on **transformer LLMs** (text, code) and **diffusion models** (images, video, audio). GANs are mostly historical; RNNs are rarely used for generation. |
| ChatGPT works "in much the same way as a Markov model" | Both predict the next word, but a Markov model only looks at the last one or two words, while a transformer weighs the **entire** context with attention; ChatGPT is also fine-tuned with human feedback (RLHF). |
| A GAN's generator works by "taking an input data sample and modifying it" | The generator turns **random noise** into new samples; it never sees real data directly; only the discriminator does. |
| GANs generate "images or texts" | GANs work well for images but poorly for text (text is made of discrete tokens). |
