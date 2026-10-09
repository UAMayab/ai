# Activity 15 — Reflection Questions: Digit Lab

Answer every question below using the **canonical network** and the app's default values, unless a
question specifically asks about your own Training Lab runs or drawings. Submit this file together
with your labeled screenshots — do not just describe the app, use your actual results.

---

## Part A — Representation (Session 25)

1. How many neurons does the canonical network have in its **input layer**, its **hidden layer**,
   and its **output layer**? Explain why the input layer has exactly that many neurons, and why
   the output layer has exactly 10.

2. Report the canonical network's number of **trainable parameters**, and show how that number is
   computed from the layer sizes (weights + biases between each pair of layers).

3. Report the canonical network's **train accuracy, test accuracy, train loss, and test loss**.

4. Choose **one hidden neuron** from "What did the hidden neurons learn?" (include its screenshot).
   Describe what kind of shape or stroke it seems to respond to. Nobody programmed that pattern —
   so where did it come from?

## Part B — Back-propagation (Session 26)

5. In the Back-propagation tab with the default learning rate of 0.50, report:
   (a) the network's output **o** before the update,
   (b) the error **E** before the update,
   (c) the new value of weight **w5** after the update, and
   (d) the error **after one update**.

6. In your own words, explain what the **backward pass** (steps 3 and 4) does and why the
   algorithm is called *back*-propagation. Use the deltas you saw (δo, δh1, δh2) in your
   explanation.

7. Paste your Training Lab **run-history table** (at least 4 runs: defaults, a learning rate that
   is too low, one that is too high, and "all zeros" initial weights). For the too-low and too-high
   runs, describe what the loss and accuracy curves looked like and why that learning rate caused
   it.

8. What happened when you trained with **"all zeros"** initial weights? Why can't a network learn
   well if every weight starts at exactly the same value? (Think about what each hidden neuron
   computes when all of them have identical weights.)

9. What was the **best test accuracy** you found, and with which settings? Did making the network
   bigger (more neurons or a second layer) or training longer (more epochs) *always* improve the
   test accuracy? Use the **train − test gap** from your runs to explain what you observed.

## Part C — Applications (Session 27)

10. For test images **#24, #4, and #6**, report the true label, the canonical network's
    prediction, and its confidence. Then report how many of the 1,000 test images the canonical
    network gets wrong.

11. Describe the results of your **own drawings** (at least 3): which digits did you draw, and
    what did the network answer each time? Give at least one reason why your drawings can be
    harder for this network than the MNIST test images, even though they look perfectly clear to a
    human.

12. Choose **one application area** from Session 27 (for example medical diagnosis, industrial
    quality control, autonomous driving, finance, agriculture, or education). Describe a neural
    network for it: what would its **inputs** be, what would its **outputs** be, and what is one
    real risk if it makes a wrong prediction, like the canonical network does on image #6?
