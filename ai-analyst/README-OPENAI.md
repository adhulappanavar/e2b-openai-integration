# AI Analyst with OpenAI Integration

This is an AI-powered data analysis tool built with Next.js, E2B Sandbox, and OpenAI. It allows you to upload CSV files and get AI-generated insights with interactive charts.

## Features

- 🔸 **OpenAI Integration**: Uses GPT-4o, GPT-4 Turbo, and other OpenAI models
- 🔸 **E2B Sandbox**: Secure code execution environment for data analysis
- 🔸 **CSV Analysis**: Upload CSV files and get AI-powered insights
- 🔸 **Interactive Charts**: Generate beautiful visualizations using ECharts
- 🔸 **Function Calling**: AI can execute Python code to analyze your data

## Quick Start

### 1. Install Dependencies

```bash
npm install
```

### 2. Set up Environment Variables

Copy `.example.env` to `.env.local` and add your API keys:

```bash
cp .example.env .env.local
```

Required environment variables:
- `E2B_API_KEY`: Get from [E2B Dashboard](https://e2b.dev/dashboard)
- `OPENAI_API_KEY`: Get from [OpenAI Platform](https://platform.openai.com/api-keys)

### 3. Run the Development Server

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

## How It Works

1. **Upload CSV**: Upload your data file through the web interface
2. **AI Analysis**: OpenAI analyzes your data and generates Python code
3. **Code Execution**: E2B Sandbox safely executes the generated code
4. **Visualization**: Interactive charts are created and displayed
5. **Insights**: Get AI-generated insights about your data

## Supported Models

- GPT-4o (Recommended)
- GPT-4o Mini
- GPT-4 Turbo
- GPT-4
- GPT-3.5 Turbo
- o1 Preview
- o1 Mini

## Technology Stack

- **Frontend**: Next.js, React, TypeScript
- **AI**: OpenAI API with function calling
- **Sandbox**: E2B Code Interpreter
- **Charts**: ECharts for interactive visualizations
- **UI**: Tailwind CSS, Radix UI components

## Example Use Cases

- Sales data analysis and trend visualization
- Customer behavior insights
- Financial data exploration
- Marketing campaign performance analysis
- Any CSV data that needs AI-powered insights

## Security

- All code execution happens in secure E2B sandboxes
- Your data is processed securely and not stored permanently
- API keys are kept secure in environment variables

## Contributing

This project is based on the [E2B AI Analyst](https://github.com/e2b-dev/ai-analyst) repository, modified to prioritize OpenAI integration.

## License

Apache-2.0 License
