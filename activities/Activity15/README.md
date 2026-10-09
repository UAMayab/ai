# Activity 15: Digit Lab — Teaching a Neural Network to Read Handwriting
## Sessions 25–27
## Due date (mm/dd/yyyy): __/__/2026
## Delivery Format: [] Video URL | [X] Markdown file | [] Jupyter Notebook file

---

# Activity Description

## The Story

Before you deposit a check from your phone, a computer reads the handwritten amount. Before a
letter reaches your door, a machine reads the handwritten postal code. Both jobs are done by
**neural networks** — programs loosely inspired by the neurons in your brain, which *learn* to
recognize patterns from thousands of examples instead of being given rules.

In this activity you get your own neural network that reads handwritten digits (0–9). You will
look inside it (**Session 25**: how a network represents an image), watch it learn one step at a
time (**Session 26**: back-propagation), train your own versions by changing the settings, and
finally test it on your own handwriting (**Session 27**: neural networks applied to a real problem).

**No programming background is required.** Everything happens by clicking, moving sliders, and
drawing in the app.

**App link:** https://uam-aiclass-a15.streamlit.app/

If you'd rather run it on your own machine instead of using the shared link, see
**Running It Yourself** below.

### The App

Four tabs:

1. **🧠 Meet the Network** — how a 28 × 28 pixel image becomes 784 numbers, the **canonical
   network** (a fixed network that everyone gets exactly the same, used for the graded answers),
   its training curves, its confusion matrix, and pictures of what each hidden neuron learned.
2. **🔁 Back-propagation Step by Step** — a tiny 2-2-1 network where you click through one full
   training step: forward pass, error, deltas, gradients, and the weight update, with every number
   shown.
3. **🎛️ Training Lab** — choose your own hyperparameters (hidden layers, neurons, activation
   function, learning rate, epochs, batch size, initial weights), press **Train**, and compare your
   network with the canonical one.
4. **✏️ Draw & Classify** — classify any of the 1,000 test images, draw your own digit for the
   network to read, and browse the test images the canonical network gets wrong.

### Your Tasks

1. **In the Meet the Network tab**, study the canonical network: its layers, its number of
   trainable parameters, its train/test accuracy and loss, and its training curves. Take a
   screenshot of the diagram and the five numbers below it.

   > 💡 **Hint:** The diagram tells you how many neurons each layer has. Ask yourself *why* the input
   > layer has exactly that many neurons. The "What the network sees" grid above it is the clue.

2. **Scroll down to "What did the hidden neurons learn?"** Pick one neuron whose picture looks
   like it has a clear shape and take a screenshot of it.

   > 💡 **Hint:** Red areas are where ink makes the neuron fire; blue areas are where ink makes it
   > stay quiet. Squint: does a neuron look like part of a stroke, a loop, or an edge?

3. **In the Back-propagation tab, leave the learning rate at 0.50** and click **Next step ▶**
   through all 5 steps. Take a screenshot of step 2 (the error) and of step 5 (the weight table and
   the "Error after one update" number).

   > 💡 **Hint:** Read each step's sentence before clicking on. Step 3 starts the *backward* pass:
   > notice which direction the information is now flowing, compared with step 1.

4. **In the Training Lab tab, train at least 4 networks** and keep the run-history table:
   - one with **all settings at their defaults** (you should get exactly the canonical network),
   - one with a learning rate that is **too low**,
   - one with a learning rate that is **too high**,
   - one with **"all zeros"** initial weights.

   Then experiment freely to find the best test accuracy you can. Take a screenshot of your run
   history table.

   > 💡 **Hint:** Change **one** setting at a time, so you know what caused the difference. A
   > learning rate is "too low" when the network is still improving slowly at the last epoch, and
   > "too high" when the loss jumps around or the accuracy collapses. Training takes a few seconds,
   > and the same settings always give the same result.

5. **In the Draw & Classify tab**, look up **test images #24, #4, and #6** with the
   "Test image number" box. For each one, write down the true label, the canonical network's
   prediction, and its confidence. Take a screenshot of image #6.

   > 💡 **Hint:** Below the canvas, the "Where the canonical network gets it wrong" gallery shows
   > every misclassified test image. Its first sentence tells you how many there are.

6. **Draw at least 3 digits of your own** on the canvas and note what the network answers each
   time. Take a screenshot of at least one attempt, including the small "What the network sees"
   image.

   > 💡 **Hint:** Draw large and centered, then try a deliberately messy, tiny, or off-center digit.
   > Compare the 28 × 28 version of your drawing with the MNIST images in the first tab.

7. **Fill out `A15_ReflectionQuestions.md`**, using the exact numbers from your screenshots, and
   submit it along with your labeled screenshots (a `.zip` with the `.md` file and the images is
   fine).

### Running It Yourself (optional)

```bash
conda activate ai_uam
cd Activity15
pip install -r requirements.txt
streamlit run app.py
```

### About the Data

The handwriting comes from **MNIST** (Yann LeCun, Corinna Cortes, and Christopher J.C. Burges), the
classic benchmark of 70,000 handwritten digits originally collected from U.S. Census Bureau employees
and high-school students. The app uses a fixed subset of 6,000 training images and 1,000 test
images (exactly 600 and 100 of each digit) so that training takes seconds.

# References:
- [Streamlit documentation](https://docs.streamlit.io/)
- [3Blue1Brown — But what is a neural network?](https://www.youtube.com/watch?v=aircAruvnKk)
- [Markdown Guide](https://www.markdownguide.org/basic-syntax/)
