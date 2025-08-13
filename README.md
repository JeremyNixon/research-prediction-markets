# Research Prediction Markets

A project to evaluate AI models' ability to predict machine learning research outcomes by analyzing recent papers and their benchmark improvements.

## Overview

This project aims to build a dataset of recent ML/AI research papers and develop evaluation methods for predicting research outcomes. We focus on papers with clear improvements on established benchmarks to create structured prediction tasks.

## Objective

Collect and analyze 100+ recent ML papers (last 6 months) that demonstrate:
- Clear ML/AI research proposals for improvements
- Measurable benchmarks for evaluation
- Quantified before/after performance metrics
- Papers outside major AI model training cutoffs (Claude 4.1, Gemini 2.5, GPT-5)

## Data Structure

Each paper entry contains:
```json
{
  "research_proposal": "string - description of the ML/AI improvement",
  "benchmark": "structured string - evaluation benchmark(s) used",
  "performance_metrics": "number - magnitude of improvement per metric per dataset",
  "paper_link": "string - URL to the paper",
  "full_text": "string - complete paper content"
}
```

## Data Sources

- **Primary**: [arXiv Computer Science - Machine Learning](https://arxiv.org/list/cs.LG/recent?skip=0&show=50)
- **Benchmarks**: [Artificial Analysis Leaderboards](https://artificialanalysis.ai/)

## Deliverables

1. **Dataset**: 100+ structured paper entries with performance metrics
2. **Extraction Pipeline**: Automated prompt system for paper analysis
3. **Evaluation Framework**: Methods to assess AI models' prediction accuracy on research outcomes

## Getting Started

1. Clone this repository
2. Review recent arXiv papers in the ML category
3. Use the data structure template for paper analysis
4. Submit findings in the specified JSON format

---

*This project evaluates whether AI models can effectively predict machine learning research breakthroughs by analyzing patterns in recent publications.*
