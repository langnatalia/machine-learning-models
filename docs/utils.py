# utils.py
import os
import math
import random
import logging
from typing import Union, List, Dict

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def load_config(file_path: str) -> Dict:
    """
    Loads configuration from a JSON file.

    Args:
    file_path (str): Path to the JSON file.

    Returns:
    dict: Configuration dictionary.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error(f"File not found at {file_path}")
        return None

def save_config(file_path: str, config: Dict):
    """
    Saves configuration to a JSON file.

    Args:
    file_path (str): Path to the JSON file.
    config (dict): Configuration dictionary.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(config, file, indent=4)
    except Exception as e:
        logging.error(f"Error saving config: {e}")

def calculate_distance(point1: List[float], point2: List[float]) -> float:
    """
    Calculates Euclidean distance between two points.

    Args:
    point1 (List[float]): First point coordinates.
    point2 (List[float]): Second point coordinates.

    Returns:
    float: Euclidean distance.
    """
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))

def split_data(data: List, test_size: float) -> Tuple[List, List]:
    """
    Splits data into training and testing sets.

    Args:
    data (List): Data to split.
    test_size (float): Proportion of data to use for testing.

    Returns:
    Tuple[List, List]: Training and testing sets.
    """
    random.shuffle(data)
    test_size = int(len(data) * test_size)
    return data[:test_size], data[test_size:]

def calculate_performance(prediction: List, actual: List) -> Dict:
    """
    Calculates performance metrics for a prediction.

    Args:
    prediction (List): Predictions.
    actual (List): Actual values.

    Returns:
    dict: Performance metrics.
    """
    accuracy = sum(1 for p, a in zip(prediction, actual) if p == a) / len(actual)
    precision = sum(1 for p, a in zip(prediction, actual) if p == a and p == 1) / sum(1 for a in actual if a == 1)
    recall = sum(1 for p, a in zip(prediction, actual) if p == a and p == 1) / (sum(1 for a in actual if a == 1) + 1e-9)
    return {"accuracy": accuracy, "precision": precision, "recall": recall}

def get_timestamp() -> str:
    """
    Returns current timestamp.

    Returns:
    str: Timestamp.
    """
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")