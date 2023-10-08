import os
import sys
import pytest
import platform
sys.path.append(".")

from bin.perceptron import Perceptron

@pytest.fixture(scope="module")
def trained_perceptron():
    the_perceptron = Perceptron()
    the_perceptron.train([
        [1, 1],
        [1, 0],
        [0, 1],
        [0, 0],
    ], [1, 1, 1, 0])
    return the_perceptron

def test_perceptron(trained_perceptron):
    # GIVEN a Preceptron object with known trainingset values
    # the_perceptron = Perceptron()
    # the_perceptron.train([
    #     [1,1],
    #     [1,0],
    #     [0,1],
    #     [0,0],
    # ], [1,1,1,0])

    # WHEN we call predict() on the object with known values
    # THEN the result will be an integer of known value
    assert trained_perceptron.predict([1, 1]) == 1, "Failed: [1, 1] should predict 1"
    assert trained_perceptron.predict([1, 0]) == 1, "Failed: [1, 0] should predict 1"
    assert trained_perceptron.predict([0, 1]) == 1, "Failed: [0, 1] should predict 1"
    assert trained_perceptron.predict([0, 0]) == 0, "Failed: [0, 0] should predict 0"

@pytest.mark.xfail
def test_failing_perceptron(trained_perceptron):
    # GIVEN a Preceptron object with known trainingset values
    # the_perceptron = Perceptron()
    # the_perceptron.train([
    #     [1,1],
    #     [1,0],
    #     [0,1],
    #     [0,0],
    # ], [1,1,1,0])
    
    # WHEN we call predict() on the object with known values
    # THEN the result will be an integer of known value
    assert trained_perceptron.predict([1, 0]) == 0, "Negative test: [1, 0] should not predict 0"

@pytest.mark.skipif(not platform.system() == 'Linux',
                    reason="Test requires Linux Ubuntu")
def test_system():
    # GIVEN a system with known free memory
    # Getting all memory using os.popen()
    total_memory, used_memory, free_memory = map(
        int, os.popen('free -t -m').readlines()[-1].split()[1:])
    
    # WHEN we compare it to a desired threshold
    min_memory_required = 1  # Minimum required memory in GB

    # THEN we can determine if the memory required will be sufficient
    assert free_memory >= min_memory_required, f"Insufficient memory. Expected at least {min_memory_required} GB, but only found {free_memory:.2f} GB."

@pytest.mark.skip(reason="This test is not yet ready for prime time")
def test_bogus():
    true = True
    false = True
    assert true == false, "true should equal false"

@pytest.mark.parametrize("training_set, labels, expected_predictions", [
    ([[1, 1], [1, 0], [0, 1], [0, 0]], [1, 0, 0, 0], [1, 0, 0, 0]),
    ([[1, 1], [1, 0], [0, 1], [0, 0]], [1, 1, 0, 0], [1, 1, 0, 0]),
    ([[1, 1], [1, 0], [0, 1], [0, 0]], [1, 1, 1, 0], [1, 1, 1, 0]),
    ([[1, 1], [1, 0], [0, 1], [0, 0]], [1, 1, 1, 1], [1, 1, 1, 1]),
    ([[1, 1], [1, 0], [0, 1], [0, 0]], [0, 0, 0, 1], [0, 0, 0, 1]),
    ([[1, 1], [1, 0], [0, 1], [0, 0]], [0, 0, 1, 1], [0, 0, 1, 1]),
    ([[1, 1], [1, 0], [0, 1], [0, 0]], [0, 1, 1, 1], [0, 1, 1, 1]),
])
def test_perceptron_multi(training_set, labels, expected_predictions):
    # GIVEN a Preceptron object with known trainingset values
    the_perceptron = Perceptron()
    the_perceptron.train(training_set, labels)

    for i, input_data in enumerate(training_set):
        # WHEN we call predict() on the object with known values
        prediction = the_perceptron.predict(input_data)
        # THEN the result will be an integer of known value
        assert prediction == expected_predictions[i], f"Failed: {input_data} should predict {expected_predictions[i]}"
