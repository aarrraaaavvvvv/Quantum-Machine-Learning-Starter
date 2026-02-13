from qiskit import QuantumCircuit
from qiskit.circuit.library import ZZFeatureMap, TwoLocal

def create_feature_map():
    return ZZFeatureMap(feature_dimension=2, reps=2)

def create_ansatz():
    return TwoLocal(num_qubits=2, rotation_blocks="ry", entanglement_blocks="cz", reps=2)
