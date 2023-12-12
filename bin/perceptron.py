"""
perceptron.py

This is a sample Python module that demonstrates the use of a Perceptron model.

This module contains a class for performing Perceptron model training and prediction.

Functions:
    None

Classes:
    - Perceptron: A simple class representing a Perceptron.

Usage:
    You can import this module and use its functions and classes as follows:

    >>> HERE

Note:
    None
"""

class Perceptron:
    """
    This is a simple class representing a Perceptron.
    """
    def __init__(self):
        """
        Initialize a Perceptron object.
        """
        self._weights = None

    def train(self, inputs, labels):
        """
        Train a Perceptron model.

        Args:
            inputs (HERE): HERE.
            labels (HERE): HERE.
    
        Returns:
            None
        """
        dummied_inputs = [x + [-1] for x in inputs]
        self._weights = [0.2] * len(dummied_inputs[0])
        for _ in range(5000):
            for sample, label in zip(dummied_inputs, labels):
                label_delta = label - self.predict(sample)
                for index, x_value in enumerate(sample):
                    self._weights[index] += .1 * x_value * label_delta

    def predict(self, new_data):
        """
        Predict function for Perceptron model.

        Args:
            new_data (HERE): HERE.

        Returns:
            Highest probability output.
        """
        if len(new_data) == 0:
            return None
        new_data = new_data + [-1]
        # pylint: disable=consider-using-generator
        return int(0 < sum([x[0]*x[1] for x in zip(self._weights, new_data)]))
