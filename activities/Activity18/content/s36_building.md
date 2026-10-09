## How apps are built with generative AI in 2026

The lecture describes building generative models from scratch with TensorFlow, PyTorch, or Keras. Those are **deep-learning frameworks for training models**, which is what research labs and model companies do. Most people who build *apps* with generative AI use models that already exist:

| Layer | What it is | Examples |
|---|---|---|
| **Chat assistants** | Use a model directly to write, analyze, plan, and code | Gemini, Microsoft Copilot, ChatGPT, Claude |
| **Coding assistants** | Suggest and write code inside the developer's editor, review it, explain it | GitHub Copilot, Gemini Code Assist, Claude Code, Cursor |
| **App builders** ("describe it and it builds it") | An agent writes, runs, and fixes a whole small app from a description | Google AI Studio (Build), Bolt.new, Lovable, v0, Replit |
| **Model APIs and SDKs** | A program sends text or images to a model over the internet and gets the answer back | Gemini API, OpenAI API, Anthropic API |
| **Cloud AI platforms** | Companies host, govern, and scale AI apps and agents | Gemini Enterprise Agent Platform (formerly Vertex AI), Microsoft Foundry, Amazon Bedrock |
| **Open-weight models** | Models whose weights you can download and run yourself | Llama, Gemma, Mistral, Qwen, DeepSeek (often run with tools such as Ollama or Hugging Face) |
| **Orchestration frameworks** | Code libraries that connect models, documents, and tools (RAG, agents) | LangChain, LlamaIndex |

TensorFlow and PyTorch still matter, mainly if you train or fine-tune your own models.

## Habits of a professional

- **Review and test everything** an AI writes, exactly as you would a new colleague's work. Run it, try strange inputs, read the code you ship.
- **Keep secrets and personal data out** of prompts and code: passwords, API keys, customer data, grades.
- **Watch for prompt injection.** Text inside a document or web page can contain hidden instructions that try to hijack an AI tool that reads it.
- **Check licenses and terms** before using generated code, images, or text commercially.
- **Disclose AI use** when your school, client, or employer requires it.

## What the lecture says vs. what is accurate (2026)

| The lecture says | What is accurate |
|---|---|
| To build a GenAI app "you will need a framework" such as TensorFlow, PyTorch, or Keras | Those train models. Apps usually call existing models through **APIs/SDKs**, coding assistants, or **app builders**; orchestration libraries like LangChain connect the pieces. |
| Platforms: "Google Cloud AI Platform, Microsoft Azure AI, and Amazon SageMaker" | Google Cloud AI Platform became **Vertex AI** (2021) and then the **Gemini Enterprise Agent Platform** (April 2026); Microsoft's became **Azure AI Studio** → **Azure AI Foundry** → **Microsoft Foundry** (November 2025); Amazon's generative-AI service is **Amazon Bedrock** (2023). Product names change fast: always check the current one. |
| "Don't expect to describe a complex program and have a GenAI system output a complete, ready-to-use application. We're not there yet." (an Oracle quote, about 2023) | App builders now produce **working small apps** from a description in minutes. Complex, secure, production software still needs skilled people to design, review, and test it. **You will judge this yourself in Mission 4.** |
