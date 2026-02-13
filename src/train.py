from qiskit.primitives import Sampler
from qiskit_machine_learning.algorithms.classifiers import VQC
from qiskit.algorithms.optimizers import COBYLA

def train_model(feature_map, ansatz, X_train, y_train):
    optimizer = COBYLA(maxiter=50)
    sampler = Sampler()

    model = VQC(
        sampler=sampler,
        optimizer=optimizer,
        feature_map=feature_map,
        ansatz=ansatz
    )

    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    return model.score(X_test, y_test)
