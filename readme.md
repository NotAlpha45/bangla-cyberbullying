# Bangla Cyberbullying Text Classification

This repository contains research and implementation for cyberbullying text classification in the Bangla language.

## Overview

This project aims to develop and evaluate machine learning models for detecting cyberbullying content in Bangla text data. The system is designed to identify harmful content across various cyberbullying categories.

## Requirements

- Python 3.12.4
- Dependencies listed in requirements.txt

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/bangla-cyberbullying.git
   cd bangla-cyberbullying
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

   > **Note:** You can also create a virtual environment using the `uv` package manager to suit the Python version:
>
   > ```bash
   > uv venv venv python=3.12.4
   > ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

[Include basic usage instructions here once implementation is ready]

## Dataset

[Description of the dataset used for training and evaluation]

## Model Architecture

### Hyperparameters

The hyperparameters used for training the model are as follows:

Below are the hyperparameters used for different machine learning classifiers in this project:

#### Table 1: Support Vector Classifier Hyperparameters

| Parameter | Value |
|-----------|-------|
| C (Regularization Parameter) | 10 |
| Kernel | rbf |

#### Table 2: Random Forest Classifier Hyperparameters

| Parameter | Value |
|-----------|-------|
| n_estimators | 200 |
| max_depth | None (No limit on tree depth) |
| min_samples_split | 10 |
| min_samples_leaf | 4 |
| max_features | sqrt |

#### Table 3: XGBoost Classifier Hyperparameters

| Parameter | Value |
|-----------|-------|
| n_estimators | 200 |
| max_depth | 6 |
| learning_rate | 0.1 |
| min_child_weight | 1 |
| gamma | 0 |
| subsample | 0.8 |
| colsample_bytree | 0.8 |
| scale_pos_weight | 1 |
| objective | binary:logistics, multi:softprob |
| num_class | 5 |

## Results

### Results Comparison of Models in Binary Classification

| Model Name | Augmentation | Label Name | Precision (%) | Recall (%) | F1 Score (%) | Accuracy (%) |
|------------|--------------|------------|--------------|------------|--------------|--------------|
| Random Forest | Not Augmented | not bully | 78 | 60 | 68 | 81 |
|  |  | bully | 81 | 91 | 86 |  |
|  | Augmented | not bully | 82 | 55 | 66 | 81 |
|  |  | bully | 80 | 94 | 86 |  |
| SVC | Not Augmented | not bully | 72 | 78 | 75 | 82 |
|  |  | bully | 88 | 84 | 86 |  |
|  | Augmented | not bully | 74 | 77 | 76 | 83 |
|  |  | bully | 88 | 86 | 87 |  |
| XGBoost | Not Augmented | not bully | 79 | 65 | 72 | 82 |
|  |  | bully | 84 | 91 | 87 |  |
|  | Augmented | not bully | 81 | 60 | 69 | 82 |
|  |  | bully | 82 | 93 | 97 |  |
| BanglaBERT + XGBoost | Not Augmented | not bully | 78 | 66 | 72 | 82 |
|  |  | bully | 84 | 91 | 87 |  |
|  | Augmented | not bully | 82 | 62 | 70 | 82 |
|  |  | bully | 83 | 93 | 87 |  |
| BiLSTM | Not Augmented | not bully | 78 | 60 | 68 | 81 |
|  |  | bully | 81 | 91 | 86 |  |
|  | Augmented | not bully | 82 | 76 | 79 | 86 |
|  |  | bully | 88 | 92 | 90 |  |

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Specify license information]
