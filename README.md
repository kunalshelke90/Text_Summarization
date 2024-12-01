# Text_Summarization

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Dataset Information](#dataset-information)
- [Pegasus Model](#pegasus-model)
- [Workflows](#workflows)
- [How to run Backend?](#how-to-run-backend)
- [License](#license)

## Project Overview
This project introduces an innovative approach to abstractive text summarization, focusing on conversational text using the Pegasus model and the SAMSum dataset...

## Features
- ### Advanced Summarization Capabilities:
  Fine-tuned Pegasus model to summarize conversational texts with high accuracy.
- ### Contextual Understanding:
  Special focus on maintaining the integrity and context of the original conversation in the summaries.
- ### Optimized for Conversational Data:
  Utilization of the SAMSum dataset ensures the model is specifically trained for dialogue-based texts.
- ### Comprehensive Model Evaluation:
  Rigorous testing using both objective metrics and subjective human assessments to ensure the quality of summaries.
- ### User-Friendly Interface:
  Incorporation of a frontend with technologies like Next.js and TailwindCSS for ease of use and accessibility.
- ### Logging and Custom Exception Handling:
  The system incorporates extensive logging and custom exception handling mechanisms to monitor the application's performance...

### Benefits and Impact:
The Text-Summarizer-Project offers several benefits and potential applications, including:

- Time-saving: Users can quickly obtain condensed summaries of lengthy texts, enabling them to digest information more efficiently.
- Research and Knowledge Management: Researchers, students, and professionals can leverage the system to extract key insights from large volumes of academic papers, reports, and other research materials.
- Content Curation: Journalists, content creators, and publishers can utilize the system to generate succinct summaries of news articles, blog posts, and online content, aiding in content curation and enhancing reader engagement.
- Language Learning: Language learners can use the summarizer to practice comprehension skills and extract key information from foreign language texts.
- Information Retrieval: Search engines and information retrieval systems can integrate the summarizer to provide concise summaries alongside search results, enhancing user experience.

The Text-Summarizer-Project aims to revolutionize the way we consume and process information, empowering users with efficient and accurate text summarization capabilities.

## Dataset Information
The SAMSum dataset, central to this project, is a collection of conversational texts designed specifically for summarization tasks...

### Dataset Link
[Hugging Face SAMSum Dataset](https://huggingface.co/datasets/samsum)

## Pegasus Model on Hugging Face (CNN/DailyMail)

### Overview
Pegasus is an advanced text summarization model developed by Google and available on Hugging Face...

### Unique Features
- **Pre-training Technique:** Pegasus is pre-trained with a novel gap-sentence objective, enhancing its ability to generate coherent and concise summaries.
- **Abstractive Summarization:** Unlike extractive models, Pegasus paraphrases and condenses the original text, providing more fluent and readable summaries.

### Fine-Tuning on CNN/DailyMail
The model has been fine-tuned on the CNN/DailyMail dataset, a collection of news articles...

### Performance and Evaluation
- **Objective Metrics:** The model's performance is evaluated using metrics like ROUGE-N, ROUGE-L, and BLEU.
- **Subjective Assessments:** In addition to objective metrics, subjective human assessments are used to ensure the quality of summaries...

### Applications
Ideal for applications in news summarization...

### Further Information
For more details, visit the [Hugging Face Pegasus model page](https://huggingface.co/google/pegasus-cnn_dailymail).

## Workflows
1. config.yaml
2. params.yaml
3. entity
4. configuration manager in src config
5. components
6. pipeline
7. main.py
8. app.py

## How to run Backend?
### STEPS:

Clone the repository
```bash
git clone https://github.com/kunalshelke90/Text_Summarization.git

```
### STEP 01- Create a Python environment after opening the repository

```bash
conda create -n summarize python=3.8 -y
```

```bash
conda activate summarize
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```
### STEP 03- Run the FastAPI Backend
```bash
python app.py
```
### STEP 04- Run the Training Pipeline
```bash
python main.py
```

## License
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
