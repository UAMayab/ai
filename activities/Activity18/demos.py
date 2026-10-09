"""Three small demos for Activity 18 (Sessions 34-35), in plain NumPy.

1. Filters: what one convolutional layer computes. A 3x3 filter slides over the
   image and, at every position, multiplies the 9 pixels under it by the 9
   filter numbers and adds them up. (Strictly, CNN libraries compute
   *cross-correlation*: the filter is not flipped. For learned filters the
   difference doesn't matter, and every major library does it this way.)
2. Next-word sampling: how an LLM turns scores into a choice, and what
   "temperature" does. The word list and scores are made up for illustration.
3. Diffusion, forward process: the noise schedule of Ho, Jain & Abbeel (2020,
   "Denoising Diffusion Probabilistic Models"): 1,000 steps, beta rising
   linearly from 0.0001 to 0.02, and x_t = sqrt(abar_t) * x_0 + sqrt(1 - abar_t) * noise.
"""

import numpy as np

# ------------------------------------------------------------------ 1. filters
FILTERS = {
    "Edge filter A": np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=float),
    "Edge filter B": np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=float),
    "Blur": np.full((3, 3), 1 / 9),
    "Sharpen": np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=float),
    "Emboss": np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]], dtype=float),
}
EDGE_FILTERS = ("Edge filter A", "Edge filter B")


def apply_filter(gray, kernel):
    """Valid-mode 2D cross-correlation of a grayscale image (H x W floats) with a 3x3 kernel."""
    h, w = gray.shape
    out = np.zeros((h - 2, w - 2))
    for di in range(3):
        for dj in range(3):
            out += kernel[di, dj] * gray[di:di + h - 2, dj:dj + w - 2]
    return out


def to_image(feature_map, is_edge):
    """Feature map -> displayable 0-255 image. Edge maps show the strength |response|."""
    if is_edge:
        m = np.abs(feature_map)
        return (255 * m / (m.max() or 1)).astype(np.uint8)
    return np.clip(feature_map, 0, 255).astype(np.uint8)


# ------------------------------------------------------------------ 2. next-word sampling
PROMPT = "Mérida is famous for its"
NEXT_WORDS = ["food", "cenotes", "heat", "architecture", "hammocks", "traffic", "snow"]
SCORES = np.array([2.0, 1.6, 1.2, 0.9, 0.5, -0.5, -3.0])  # made-up "logits"


def next_word_probabilities(temperature):
    """Softmax of score / temperature (temperature > 0)."""
    z = SCORES / temperature
    e = np.exp(z - z.max())
    return e / e.sum()


def sample_words(temperature, n=10, seed=0):
    rng = np.random.default_rng(seed)
    return [NEXT_WORDS[i] for i in rng.choice(len(NEXT_WORDS), size=n, p=next_word_probabilities(temperature))]


# ------------------------------------------------------------------ 3. diffusion forward process
T_STEPS = 1000
BETAS = np.linspace(1e-4, 0.02, T_STEPS)
ALPHA_BAR = np.cumprod(1 - BETAS)  # ALPHA_BAR[t - 1] is abar_t for t = 1..1000


def signal_and_noise(t):
    """(sqrt(abar_t), sqrt(1 - abar_t)) for step t in 0..1000 (t = 0 is the clean image)."""
    if t == 0:
        return 1.0, 0.0
    a = ALPHA_BAR[t - 1]
    return float(np.sqrt(a)), float(np.sqrt(1 - a))


def noisy_image(rgb_uint8, t, seed=0):
    """x_t for an RGB image, with pixels scaled to [-1, 1] as in DDPM; returned as uint8 for display."""
    x0 = rgb_uint8.astype(float) / 127.5 - 1.0
    noise = np.random.default_rng(seed).standard_normal(x0.shape)
    s, n = signal_and_noise(t)
    xt = s * x0 + n * noise
    return np.clip((xt + 1.0) * 127.5, 0, 255).astype(np.uint8)
