# Activity 2 — Setup Guide
## Installing Anaconda, Creating `ai_uam`, and Verifying JupyterLab

Follow these steps in order on your own computer. Every Python activity for the rest of the semester depends on this environment, so it's worth getting right now.

---

## Step 1 — Install Anaconda

Anaconda is a free distribution that bundles Python, conda (the environment/package manager), and JupyterLab together.

### Windows

1. Go to https://www.anaconda.com/download and download the **Windows installer (64-bit)**.
2. Run the `.exe` file. During setup:
   - Choose **"Just Me"** (not "All Users") unless your instructor tells you otherwise.
   - You do **not** need to check "Add Anaconda to my PATH environment variable" — the installer will create an **Anaconda Prompt** you'll use instead.
3. When installation finishes, open **Anaconda Prompt** from the Start Menu (search "Anaconda Prompt").

### Mac

1. Go to https://www.anaconda.com/download and download the **macOS installer**.
   - **Check your chip first:** click the Apple menu → "About This Mac." If it says **Apple M1/M2/M3/M4**, download the **Apple Silicon (arm64)** installer. If it says **Intel**, download the **Intel (x86_64)** installer. Installing the wrong one will cause problems later.
2. Run the `.pkg` file and follow the installer wizard.
3. **Close and reopen Terminal** after installation (this refreshes your shell so it can find `conda`).

### Linux

1. Download the Linux installer script from https://www.anaconda.com/download.
2. In a terminal:
   ```bash
   bash Anaconda3-*-Linux-x86_64.sh
   ```
3. Follow the prompts, and say **yes** when asked whether to run `conda init`.
4. Close and reopen your terminal.

### Verify Anaconda is installed (all operating systems)

In Anaconda Prompt (Windows) or Terminal (Mac/Linux), run:

```bash
conda --version
conda info
```

**Expected output (version numbers may differ slightly):**
```
conda 24.x.x
```
followed by a block of information about your installation (active environment, platform, etc.).

**📸 Screenshot 1:** Capture this terminal window showing `conda --version` and its output.

---

## Step 2 — Create the `ai_uam` Conda Environment

This creates an isolated environment named `ai_uam` with Python 3.11, so this course's packages never conflict with anything else on your computer. These commands are identical on Windows, Mac, and Linux.

```bash
conda create -n ai_uam python=3.11
```

Conda will list the packages it plans to install and ask for confirmation:
```
Proceed ([y]/n)?
```
Type `y` and press Enter.

Once it finishes, activate the environment:

```bash
conda activate ai_uam
```

Your prompt should now show `(ai_uam)` at the beginning of the line, e.g.:
```
(ai_uam) C:\Users\yourname>
```
or
```
(ai_uam) yourname@laptop ~ %
```

Confirm the environment exists:

```bash
conda env list
```

**Expected output:**
```
# conda environments:
#
base                     C:\Users\yourname\anaconda3
ai_uam               *   C:\Users\yourname\anaconda3\envs\ai_uam
```
The `*` marks whichever environment is currently active.

**📸 Screenshot 2:** Capture the terminal showing `conda env list` with `ai_uam` in the list, and your prompt showing `(ai_uam)` active.

---

## Step 3 — Verify Python

With `ai_uam` still activated, run:

```bash
python --version
```

**Expected output:**
```
Python 3.11.x
```

**📸 Screenshot 3:** Capture this command and its output, with `(ai_uam)` visible in the prompt.

---

## Step 4 — Install & Verify JupyterLab

With `ai_uam` still activated, install JupyterLab:

```bash
conda install -c conda-forge jupyterlab
```

Confirm with `y` when prompted. This may take a few minutes.

Once it finishes, verify:

```bash
jupyter lab --version
```

**Expected output:** a version number, e.g. `4.x.x`.

**📸 Screenshot 4:** Capture this command and its output, with `(ai_uam)` visible in the prompt.

---

## Step 5 — Launch JupyterLab & Create Your Proof Notebook

With `ai_uam` still activated, launch JupyterLab:

```bash
jupyter lab
```

This opens a new browser tab at an address like `http://localhost:8888/lab`. Leave the terminal window open in the background — closing it will shut down JupyterLab.

1. In the JupyterLab launcher, click **Python 3 (ipykernel)** (it may also be labeled **Python (ai_uam)**) to create a new notebook.
2. In the first cell, type the following, replacing the placeholder with your own full name:

   ```python
   from datetime import datetime

   print("Full Name: Your Full Name Here")
   print("Environment: ai_uam")
   print("Timestamp:", datetime.now())
   ```
3. Run the cell (Shift + Enter) and confirm the output appears below it with your real name and the current date/time.

**📸 Screenshot 5:** Capture the full browser window, showing:
- The URL bar (should show `localhost:8888`)
- The notebook cell and its output (your name and the timestamp must be clearly readable)

This screenshot is what makes your submission uniquely yours — a generic "JupyterLab is open" screenshot without this cell will not count as proof.

---

## Screenshot Checklist

Before submitting, confirm you have all five, each clearly labeled:

- [ ] **Screenshot 1** — `conda --version` / `conda info` output (Anaconda installed)
- [ ] **Screenshot 2** — `conda env list` showing `ai_uam`, with `(ai_uam)` active in the prompt
- [ ] **Screenshot 3** — `python --version` inside `ai_uam` showing Python 3.11.x
- [ ] **Screenshot 4** — `jupyter lab --version` inside `ai_uam`
- [ ] **Screenshot 5** — JupyterLab open in the browser with your personalized proof cell executed

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `'conda' is not recognized` / `conda: command not found` | Windows: use **Anaconda Prompt**, not regular Command Prompt/PowerShell. Mac/Linux: close and reopen your terminal so it picks up the changes the installer made to your shell profile. |
| `CondaValueError: prefix already exists` when creating `ai_uam` | You already created it once. Skip to `conda activate ai_uam` directly, or remove it first with `conda env remove -n ai_uam` and recreate it. |
| `jupyter: command not found` after installing JupyterLab | Make sure `ai_uam` is activated (`conda activate ai_uam`) before running `jupyter lab` — it was installed inside that environment, not system-wide. |
| Mac: installer fails or Anaconda Navigator won't open | You likely downloaded the wrong chip version. Recheck Apple menu → "About This Mac" and reinstall with the matching Apple Silicon or Intel installer. |
| JupyterLab opens but shows the wrong Python version | In the notebook, check the kernel name in the top-right corner. If it doesn't say `ai_uam`, switch kernels via **Kernel → Change Kernel**, or reinstall JupyterLab with `ai_uam` activated. |
| Browser doesn't open automatically after `jupyter lab` | Copy the `http://localhost:8888/lab?token=...` URL printed in the terminal and paste it into your browser manually. |

---

*Activity 2 | Introduction to Artificial Intelligence*
