# Bias Evaluation and Debiasing in Autoregressive Language Models
## Project Overview

This repository contains the code, datasets, and analysis for my Final Year Project (FYP) on *Bias Evaluation and Debiasing in Autoregressive Language Models*. The project aims to systematically assess and mitigate biases present in autoregressive models like GPT-2, LLaMA-7B, and Mistral-7B, particularly in relation to gender, race, religion, and LGBTQIA+ identities.

Given the increasing adoption of large language models (LLMs) across various applications, understanding and mitigating biases is crucial to ensuring fair and ethical AI deployments. This project explores bias measurement using established benchmarks and applies structured prompting as a debiasing strategy to improve the fairness of model-generated text.

## Objectives
- Evaluate bias in autoregressive models using benchmark datasets such as RealToxicityPrompts, BOLD, and HONEST.
- Analyze the impact of bias across different demographic groups, including gender, race, religion, and LGBTQIA+ identities.
- Implement structured prompts as a debiasing technique to reduce biased generations without modifying the model architecture.
- Compare debiased and non-debiased model outputs to assess the effectiveness of different mitigation strategies.
- Visualize and analyze bias trends across multiple models using heatmaps and other data representations.

## Models Evaluated
- GPT-2
- LLaMA-7B
- Mistral-7B

## Datasets Used
- RealToxicityPrompts: Used to evaluate toxicity in model generations.
- BOLD (Bias in Open-Ended Language Generation): Measures biases in text generation across various demographic categories.
- HONEST Benchmark: Evaluates biases specific to different identity groups, particularly for LGBTQIA+ identities.

## Bias Evaluation Metrics
The project employs multiple metrics to measure bias in model-generated text:
- Regard Score: Measures the sentiment or regard expressed toward different demographic groups.
- Toxicity Ratio: Evaluates the likelihood of the model producing toxic outputs.
- HONEST Score: Assesses how models respond to identity-based prompts.

## Debiasing Approach
The primary debiasing strategy explored in this project is structured prompting. Instead of modifying model parameters, structured prompts are designed to guide the model’s responses toward less biased outputs. The effectiveness of this approach is analyzed by comparing the outputs before and after debiasing.

## Findings & Insights
- Biases were observed across multiple demographic groups, with some groups receiving more negative or toxic outputs than others.
- Structured prompts significantly reduced toxicity in text generation, though results varied across different identity categories.
- Debiasing was more effective for certain biases (e.g., gender) than others (e.g., LGBTQIA+ identities), highlighting the challenges in mitigating nuanced biases.
- Among the evaluated models, Mistral-7B showed the most improvement after debiasing, while GPT-2 exhibited higher baseline biases.

## Future Work
- Exploring reinforcement learning-based debiasing to dynamically adjust outputs.
- Applying contrastive debiasing techniques to further refine structured prompts.
- Extending bias evaluations to multilingual models to study cross-linguistic bias patterns.
