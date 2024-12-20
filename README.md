# Text_Summarization

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
  - [Advanced Summarization Capabilities](#advanced-summarization-capabilities)
  - [Contextual Understanding](#contextual-understanding)
  - [Optimized for Conversational Data](#optimized-for-conversational-data)
  - [Comprehensive Model Evaluation](#comprehensive-model-evaluation)
  - [User-Friendly Interface](#user-friendly-interface)
  - [Logging and Custom Exception Handling](#logging-and-custom-exception-handling)
  - [Benefits and Impact](#benefits-and-impact)
- [Dataset](#dataset)
  - [Dataset Summary](#dataset-summary)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Model Information](#model-information)
- [Results](#results)
- [Applications](#applications)
- [Further Information](#further-information)
- [Workflows](#workflows)
- [How to run Backend?](#how-to-run-backend)
  - [Steps](#steps)
    - [Step 01: Create a Python environment](#step-01-create-a-python-environment)
    - [Step 02: Install the requirements](#step-02-install-the-requirements)
    - [Step 03: Run the FastAPI Backend](#step-03-run-the-fastapi-backend)
    - [Step 04: Run the Training Pipeline](#step-04-run-the-training-pipeline)
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


## Dataset 
Samsum dataset - https://huggingface.co/datasets/samsum

### Dataset Summary
The SAMSum dataset contains about 16k messenger-like conversations with summaries. Conversations were created and written down by linguists fluent in English. Linguists were asked to create conversations similar to those they write on a daily basis, reflecting the proportion of topics of their real-life messenger convesations. The style and register are diversified - conversations could be informal, semi-formal or formal, they may contain slang words, emoticons and typos. Then, the conversations were annotated with summaries. It was assumed that summaries should be a concise brief of what people talked about in the conversation in third person. The SAMSum dataset was prepared by Samsung R&D Institute Poland and is distributed for research purposes (non-commercial licence: CC BY-NC-ND 4.0).

### Data Instances
The created dataset is made of 16369 conversations distributed uniformly into 4 groups based on the number of utterances in con- versations: 3-6, 7-12, 13-18 and 19-30. Each utterance contains the name of the speaker. Most conversations consist of dialogues between two interlocutors (about 75% of all conversations), the rest is between three or more people

The first instance in the training set: {'id': '13818513', 'summary': 'Amanda baked cookies and will bring Jerry some tomorrow.', 'dialogue': "Amanda: I baked cookies. Do you want some?\r\nJerry: Sure!\r\nAmanda: I'll bring you tomorrow :-)"}

### Data Fields
- dialogue: text of dialogue.
- summary: human written summary of the dialogue.
- id: unique id of an example.

### Data Splits
- train: 14732
- val: 818
- test: 819

## Model Information
PEGASUS is a state-of-the-art model for abstractive text summarization, developed by Google AI. It is a transformer-based model that is trained on a massive dataset of text and code. PEGASUS can generate summaries that are both informative and fluent, and it has been shown to outperform other models on a variety of summarization tasks.

PEGASUS is trained using a technique called masked language modeling. In masked language modeling, the model is given a sequence of text with some of the words masked out. The model then learns to predict the missing words. This helps the model to learn the relationships between words and phrases, and it also helps the model to learn how to generate text that is fluent and grammatically correct.

PEGASUS is a powerful tool for abstractive text summarization. It can be used to generate summaries of news articles, research papers, and other long documents. PEGASUS can also be used to generate summaries of code, which can be helpful for developers who need to understand the code of a large project.

Here are some of the key features of PEGASUS:

- It is a transformer-based model, which is a type of neural network that has been shown to be effective for a variety of natural language processing tasks.
- It is trained on a massive dataset of text and code, which gives it a strong understanding of the relationships between words and phrases.
- It can generate summaries that are both informative and fluent.
- It has been shown to outperform other models on a variety of summarization tasks.

PEGASUS is a promising new model for abstractive text summarization. It has the potential to revolutionize the way that we summarize text, and it could be used in a variety of applications, such as news aggregation, research paper summarization, and code summarization.

## Results
We conducted one epoch of training due to low computing power on our model, but unfortunately, the achieved accuracy was relatively low. The model's performance during this initial training phase did not meet our expectations. We acknowledge that further iterations and adjustments are necessary to improve accuracy and enhance the model's capabilities. The low accuracy obtained after one epoch suggests that additional training or modifications to the model architecture, hyperparameters, or dataset may be required to achieve desired performance levels. Further investigation and experimentation will be conducted to address these concerns and enhance the accuracy of the model.


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
