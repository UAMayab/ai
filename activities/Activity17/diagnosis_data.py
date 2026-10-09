"""The Breast Cancer Wisconsin (Diagnostic) dataset (Session 31 practical case).

Real data: 569 breast masses, each described by 30 measurements of the cell
nuclei in a digitized image of a fine-needle aspirate, and diagnosed as
malignant or benign. Creators: W. H. Wolberg, W. N. Street, O. L. Mangasarian.
UCI Machine Learning Repository, CC BY 4.0, DOI 10.24432/C5DW2B. The copy
bundled with scikit-learn is used, so nothing is downloaded.

Labels here: 1 = malignant (the "positive" class a screening test looks for),
0 = benign. (scikit-learn's own copy uses the opposite: 0 = malignant.)

The split into training (70%) and test (30%) patients is fixed and stratified,
so both parts keep the same malignant/benign proportions.
"""

import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

_data = load_breast_cancer()
FEATURE_NAMES = [str(f) for f in _data.feature_names]
X = _data.data
Y = (_data.target == 0).astype(int)  # 1 = malignant, 0 = benign
CLASS_NAMES = ["Benign", "Malignant"]

TRAIN_IDX, TEST_IDX = train_test_split(np.arange(len(Y)), test_size=0.30, stratify=Y, random_state=31)
X_TRAIN, Y_TRAIN = X[TRAIN_IDX], Y[TRAIN_IDX]
X_TEST, Y_TEST = X[TEST_IDX], Y[TEST_IDX]

DEFAULT_FEATURES = ("worst radius", "worst concave points")
