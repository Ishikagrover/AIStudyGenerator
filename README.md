# AIStudyGenerator
# AIStudyGenerator# 📚 GPT-2 Based AI Study Tip Generator

### ETMMGA304 – Generative AI and Its Applications
**Assignment 5: Generative AI Creative Solution**

## 1. Project Overview

The GPT-2 Based AI Study Tip Generator is a Generative AI application designed to help students get practical study suggestions for different academic topics.

The application accepts a topic from the user and generates one short, actionable study tip using a fine-tuned GPT-2 language model.

The main objective is to make studying new and technical topics easier by providing simple and useful suggestions.

## 2. Problem Statement

Beginners often find it difficult to decide how to start studying a new topic. They may not know which practice method or learning approach to follow.

This project uses Generative AI to provide topic-specific study tips that can help students begin their learning process.

## 3. Objectives

- Generate short and actionable study tips.
- Fine-tune GPT-2 using a custom topic-tip dataset.
- Compare the original GPT-2 model with the adapted model.
- Evaluate outputs based on relevance, readability and usefulness.
- Develop an interactive application using Streamlit.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Google Colab | Development environment |
| PyTorch | Model training |
| Hugging Face Transformers | GPT-2 implementation |
| GPT-2 | Pre-trained language model |
| Pandas | Dataset preparation and evaluation |
| Streamlit | Application interface |

## 5. Project Workflow

The project follows five main stages:

1. **Define:** Identify the problem and project objectives.
2. **Prepare:** Create training and held-out topic-tip datasets.
3. **Adapt:** Fine-tune the last Transformer block of GPT-2.
4. **Evaluate:** Compare base and adapted model outputs.
5. **Demonstrate:** Build an interactive Streamlit application.

## 6. Dataset Description

A custom dataset containing topic and study-tip pairs is used for fine-tuning.

- Training dataset: 30 topic-tip examples.
- Held-out dataset: 10 separate topics.
- Data format: CSV.
- Training and evaluation topics are kept separate.

The dataset is prepared for academic demonstration and should be reviewed by the instructor for approval and suitability.

## 7. Model Training

The project uses the pre-trained GPT-2 model from Hugging Face.

Fine-tuning configuration:

- Model: GPT-2
- Learning rate: 0.00002
- Optimizer: AdamW
- Epochs: 3
- Trainable parameters: Last Transformer block
- Device: CPU

The model is saved after fine-tuning for later use in the application.

## 8. Model Evaluation

The original and adapted GPT-2 models are tested using the same 10 held-out topics.

Each generated output is evaluated using three criteria:

- **Relevance:** Is the tip related to the given topic?
- **Readability:** Is the tip easy to understand?
- **Usefulness:** Does the tip provide an actionable suggestion?

Each criterion receives a score from 0 to 2, giving a maximum total score of 6.

The mean scores of both models are compared to understand whether fine-tuning improved the generated tips.

## 9. Application Features

- Simple topic input field.
- AI-generated study tips.
- Fine-tuned GPT-2 model.
- Empty input validation.
- Easy-to-use Streamlit interface.
- AI-generated content disclosure.

## 10. How to Run the Project

### Step 1: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Check the project structure

```text
Lab_5_Study_Tip_Generator/
│
├── dataset/
│   ├── training_dataset.csv
│   └── heldout_dataset.csv
│
├── model/
│   └── study_tip_gpt2/
│
├── evaluation/
│   ├── base_vs_adapted.csv
│   └── evaluation_scores.csv
│
├── lab_outputs/
│   └── training_log.csv
│
├── app/
│   ├── app.py
│   └── requirements.txt
│
└── README.md
```

### Step 3: Run the application

Navigate to the folder containing the Streamlit application and execute:

```bash
streamlit run app.py
```

Make sure the fine-tuned model folder is available at the path configured in the application.

## 11. Privacy, Bias and Limitations

**Disclosure:** Every generated tip is AI-generated and intended for instructor review.

**Privacy:** The model runs locally when used in a local environment. Users should not enter personal or sensitive information.

**Bias:** GPT-2 was trained on WebText and may reflect biases in its training data. Its suggestions may not suit every student or learning style.

**Limitations:**
- The model may generate incorrect or generic suggestions.
- It is designed for English academic topics.
- Output length is limited to 45 new tokens.
- Greedy decoding produces deterministic outputs for the same input and model.

## 12. Conditions for Use

This application is intended for teacher-reviewed drafting only. Generated tips should be checked for accuracy, clarity and suitability before being shared with students.

It should not be used for unsupervised student guidance.

## 13. Future Scope

- Support for Hindi and other languages.
- Larger and more diverse training datasets.
- Improved response quality.
- Additional academic subjects.
- Better user interface and deployment.
- Human feedback and review system.

## 14. Conclusion

The GPT-2 Based AI Study Tip Generator demonstrates how a pre-trained Generative AI model can be adapted for a specific educational task.

By fine-tuning GPT-2, comparing its outputs with the original model and developing a Streamlit interface, this project provides practical experience with model adaptation, evaluation and application development.

---

**Course:** ETMMGA304 – Generative AI and Its Applications  
**Programme:** Master of Computer Applications (MCA)  
**Project:** Assignment 5 – Study Tip Generator
