## What "deep" means

**Deep learning** is machine learning with neural networks that have **many layers** (Activity 15's network had one hidden layer; modern networks have dozens or hundreds). Each layer turns its input into a slightly more useful description: in an image network, early layers react to edges and colors, middle layers to textures and parts (an eye, a wheel), and late layers to whole objects. Nobody programs those features: training (back-propagation, Session 26) finds them.

Neural networks are **loosely inspired** by the brain (neurons, connections), but they do not "mimic" how the brain works; they are mathematical functions tuned with calculus.

### A short, accurate timeline

| Year | Milestone |
|---|---|
| 1943 | McCulloch & Pitts describe a mathematical model of a neuron. |
| 1980 | Fukushima's *neocognitron*: layers of feature detectors, inspired by the visual cortex. |
| 1986 | Rumelhart, Hinton & Williams popularize **back-propagation** for training multi-layer networks. |
| 1989 | LeCun and colleagues at Bell Labs train a **convolutional network** to read handwritten ZIP codes; **LeNet-5** follows in 1998. |
| 1997 | Hochreiter & Schmidhuber introduce the **LSTM**, a recurrent network that remembers longer. |
| 2012 | **AlexNet** wins the ImageNet competition by a wide margin, trained on GPUs. This is the moment deep learning took over computer vision. |
| 2015 | On the ImageNet benchmark, the best models beat the *estimated* human error rate. (On that benchmark, not on vision in general.) |
| 2017 | **The Transformer** ("Attention Is All You Need"): the architecture behind today's language models. |
| 2020 | Vision Transformers show transformers also work for images. |

## Convolutional neural networks (CNNs)

A CNN's first layers are **filters**: small grids of numbers (often 3 × 3) that slide across the image. At every position the filter multiplies the pixels under it by its numbers and adds them up, producing a **feature map** that is bright wherever the image matches the filter's pattern. Try it below with a few classic hand-made filters. A real CNN starts with random filters and **learns** hundreds of them during training.

<!-- demo -->

Two things the lecture overstates:

- **"Invariant to location, size, and orientation."** Convolution plus pooling makes CNNs fairly tolerant of an object's *position*, but not of its *size* or *rotation*. Networks learn those only from varied training data (or data augmentation: flipped, zoomed, rotated copies of the images).
- **"Superhuman."** Only on specific benchmarks. The same models can fail on images that a child would get right, such as unusual angles or backgrounds (you will see this yourself in Mission 1).

## From recurrent networks to transformers

**Recurrent neural networks (RNNs)** read a sequence one step at a time, carrying a memory forward; LSTMs and GRUs improved how long that memory lasts. But RNNs are slow to train (each step waits for the previous one) and still struggle with long texts.

**Transformers** (2017) replaced recurrence with **attention**: every word looks at every other word in the passage at once and decides which ones matter for its meaning. This processes the whole sequence in parallel on GPUs and connects distant parts of a text. Today, transformers are the dominant architecture for language, and are widely used for images, audio, and video too. CNNs are still everywhere in vision (phones, cameras, medical imaging) because they are efficient.

## What the lecture says vs. what is accurate (2026)

| The lecture says | What is accurate |
|---|---|
| "Warren McCullough" | Warren **McCulloch** (McCulloch & Pitts, 1943). |
| LeCun built the first CNN, LeNet, in 1988, as "director of Facebook's AI Research Group" | The ZIP-code CNN was published in **1989**, from **Bell Labs**; LeNet-5 in 1998; earlier, Fukushima's neocognitron (1980) introduced the layered feature-detector idea. LeCun joined Facebook much later (2013). |
| Deep learning "mimics the operation of the human brain" | Neural networks are *loosely inspired* by neurons; they don't work like a brain. |
| CNNs and RNNs "are the most important" architectures | Since about 2018, **transformers** are the dominant architecture (language, and much of vision and audio). CNNs remain important; RNNs are now niche. |
| CNNs recognize objects "regardless of their location, size, or orientation" | Roughly tolerant to **position** only; size and rotation must be learned from varied data. |
| An RNN has "four layers: input, output, hidden and loss" | The **loss** is a score computed during training, not a layer of the network. |
