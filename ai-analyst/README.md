# AI Analyst with OpenAI Integration

This is an AI-powered data analysis tool built with Next.js, E2B Sandbox, and OpenAI. It allows you to upload CSV files and get AI-generated insights with interactive charts.

![Preview](preview.png)

→ **Live Demo**: [ai-analyst.e2b.dev](https://ai-analyst.e2b.dev/)  
→ **This Version**: [ai-analyst-openai](https://github.com/adhulappanavar/ai-analyst-openai)

## ✨ Features

- 🔸 **OpenAI Integration**: Uses GPT-4o, GPT-4 Turbo, and other OpenAI models
- 🔸 **E2B Sandbox**: Secure code execution environment for data analysis
- 🔸 **CSV Analysis**: Upload CSV files and get AI-powered insights
- 🔸 **Interactive Charts**: Generate beautiful visualizations using ECharts
- 🔸 **Function Calling**: AI can execute Python code to analyze your data
- 🔸 **Real-time Processing**: Stream responses and see results as they generate

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/adhulappanavar/ai-analyst-openai.git
cd ai-analyst-openai
```

### 2. Install Dependencies
```bash
npm install
```

### 3. Set Up Environment Variables
Copy `.example.env` to `.env.local` and add your API keys:

```bash
cp .example.env .env.local
```

**Required API Keys:**
- `E2B_API_KEY`: Get from [E2B Dashboard](https://e2b.dev/dashboard?tab=keys)
- `OPENAI_API_KEY`: Get from [OpenAI Platform](https://platform.openai.com/api-keys)

### 4. Run Development Server
```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

## 🤖 Supported Models

**OpenAI Models (Recommended):**
- GPT-4o (Default)
- GPT-4o Mini
- GPT-4 Turbo
- GPT-4
- GPT-3.5 Turbo
- o1 Preview
- o1 Mini

**Other Providers:**
- Anthropic Claude
- Google Gemini
- Fireworks AI
- Together AI

## 🛠️ Technology Stack

- **Frontend**: Next.js 14, React 18, TypeScript
- **AI**: OpenAI API with function calling
- **Sandbox**: E2B Code Interpreter
- **Charts**: ECharts for interactive visualizations
- **UI**: Tailwind CSS, Radix UI components
- **Deployment**: Vercel-ready

## 📊 How It Works

1. **Upload Data**: Upload your CSV file through the web interface
2. **AI Analysis**: OpenAI analyzes your data and generates Python code
3. **Code Execution**: E2B Sandbox safely executes the generated code
4. **Visualization**: Interactive charts are created and displayed
5. **Insights**: Get AI-generated insights about your data patterns

## 💡 Example Use Cases

- **Sales Analysis**: Analyze sales trends and customer behavior
- **Financial Data**: Explore financial metrics and create dashboards
- **Marketing Insights**: Analyze campaign performance and ROI
- **Research Data**: Process research data and generate visualizations
- **Any CSV Data**: Get AI-powered insights from any structured data

## 🔒 Security & Privacy

- **Secure Execution**: All code runs in isolated E2B sandboxes
- **No Data Storage**: Your data is processed securely and not stored permanently
- **API Key Protection**: Environment variables keep your keys secure
- **Open Source**: Full transparency with the source code

## 🎯 Key Improvements Over Original

- ✅ **OpenAI Default**: Prioritizes OpenAI models for better performance
- ✅ **Simplified Setup**: Clearer configuration for OpenAI integration
- ✅ **Better Error Handling**: Improved error messages and debugging
- ✅ **Enhanced Documentation**: Comprehensive setup and usage guides
- ✅ **Security Focus**: Better API key management and protection

## 📈 Supported Chart Types

All interactive chart types supported by ECharts:
- Line charts, Bar charts, Pie charts
- Scatter plots, Heatmaps, Treemaps
- 3D visualizations, Geographic maps
- And many more - see [ECharts Gallery](https://echarts.apache.org/examples/en/index.html)

## 🤝 Contributing

This project is based on the [E2B AI Analyst](https://github.com/e2b-dev/ai-analyst) repository, modified to prioritize OpenAI integration.

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

Apache-2.0 License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [E2B](https://e2b.dev) for the amazing sandbox technology
- [OpenAI](https://openai.com) for powerful AI models
- [Vercel](https://vercel.com) for the AI SDK
- Original [AI Analyst](https://github.com/e2b-dev/ai-analyst) project
