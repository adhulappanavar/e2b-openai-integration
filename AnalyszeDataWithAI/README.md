# E2B Data Analysis with AI

This project demonstrates how to use E2B Sandbox with Claude AI to analyze CSV data and generate visualizations.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up your API keys:
   - Copy `env_example.txt` to `.env`
   - Get your E2B API key from [E2B Dashboard](https://e2b.dev/dashboard)
   - Get your OpenAI API key from [OpenAI Platform](https://platform.openai.com/api-keys)
   - Add both keys to your `.env` file

3. Make sure you have `dataset.csv` in the project directory

## Usage

Run the analysis:
```bash
python main.py
```

The script will:
1. Upload the CSV dataset to an E2B sandbox
2. Send a prompt to OpenAI asking for data analysis
3. OpenAI generates Python code to analyze vote averages over time
4. The code runs in the sandbox
5. Generated charts are saved as PNG files
6. Results are displayed in the console

## What it does

Based on the E2B documentation example, this analyzes a movie dataset to understand how vote averages have changed over the years, generating visualizations of the trends.
