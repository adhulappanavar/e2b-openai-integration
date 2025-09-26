# Open Lovable - AI-Powered React App Builder

🔥 **Chat with AI to build React apps instantly!** This is a powerful tool that lets you describe what you want and watch as AI generates a complete React application for you.

Based on the [Firecrawl Open Lovable](https://github.com/firecrawl/open-lovable) project, this version is optimized for E2B sandbox integration.

## ✨ Features

- 🤖 **AI-Powered Development**: Chat with AI to build React apps from scratch
- 🔥 **Firecrawl Integration**: Scrape and analyze websites for inspiration
- 🏗️ **E2B Sandbox**: Secure code execution environment
- ⚡ **Real-time Preview**: See your app come to life as AI builds it
- 🎨 **Modern UI**: Beautiful, responsive React components
- 📦 **Package Management**: Automatic dependency detection and installation
- 🔄 **Live Reload**: Instant updates as you iterate

## 🚀 Quick Start

### 1. Install Dependencies
```bash
npm install
```

### 2. Set Up Environment Variables
Copy `env_template.txt` to `.env.local` and add your API keys:

```bash
cp env_template.txt .env.local
```

**Required API Keys:**
- `FIRECRAWL_API_KEY`: Get from [Firecrawl](https://firecrawl.dev)
- `E2B_API_KEY`: Get from [E2B Dashboard](https://e2b.dev/dashboard)
- `OPENAI_API_KEY`: Get from [OpenAI Platform](https://platform.openai.com/api-keys)

### 3. Run Development Server
```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

## 🛠️ How It Works

1. **Describe Your App**: Tell the AI what kind of React app you want to build
2. **AI Analysis**: The AI analyzes your request and plans the implementation
3. **Code Generation**: AI generates React components, styles, and logic
4. **E2B Execution**: Code runs securely in E2B sandbox environment
5. **Live Preview**: See your app running in real-time
6. **Iterate**: Chat with AI to refine and improve your app

## 🤖 Supported AI Providers

- **OpenAI** (GPT-4o, GPT-4 Turbo) - Recommended
- **Anthropic** (Claude 3.5 Sonnet)
- **Google** (Gemini Pro)
- **Groq** (Fast inference)

## 🏗️ Sandbox Providers

- **E2B** (Recommended) - Secure, isolated code execution
- **Vercel** - Cloud-based sandbox environment

## 📁 Project Structure

```
open-lovable/
├── app/                    # Next.js app directory
│   ├── api/               # API routes for AI and sandbox
│   ├── builder/           # App builder interface
│   └── generation/        # Code generation UI
├── components/            # React components
│   ├── shared/           # Reusable UI components
│   └── ui/               # Base UI components
├── lib/                  # Utility libraries
│   └── sandbox/         # Sandbox management
├── hooks/                # React hooks
├── types/                # TypeScript type definitions
└── utils/                # Helper functions
```

## 🎯 Use Cases

- **Prototyping**: Quickly build React app prototypes
- **Learning**: Understand React patterns through AI-generated code
- **Inspiration**: Get ideas from existing websites via Firecrawl
- **Rapid Development**: Build MVPs and demos in minutes
- **Code Examples**: Generate working examples for specific features

## 🔒 Security & Privacy

- **Secure Execution**: All code runs in isolated E2B sandboxes
- **No Data Storage**: Your conversations and code are not permanently stored
- **API Key Protection**: Environment variables keep your keys secure
- **Open Source**: Full transparency with the source code

## 🎨 Example Prompts

Try these example prompts to get started:

- "Create a modern e-commerce product page with a shopping cart"
- "Build a dashboard with charts and data visualization"
- "Make a social media feed with posts and comments"
- "Create a landing page for a SaaS product"
- "Build a todo app with drag-and-drop functionality"

## 🛠️ Development

### Available Scripts

- `npm run dev` - Start development server with Turbopack
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm run lint` - Run ESLint
- `npm run test:api` - Test API endpoints
- `npm run test:code` - Test code execution
- `npm run test:all` - Run all tests

### Key Technologies

- **Next.js 15** - React framework with App Router
- **React 19** - Latest React with concurrent features
- **TypeScript** - Type-safe development
- **Tailwind CSS** - Utility-first styling
- **Framer Motion** - Smooth animations
- **Radix UI** - Accessible component primitives
- **E2B SDK** - Secure code execution
- **Firecrawl** - Website scraping and analysis

## 🤝 Contributing

This project is based on the [Firecrawl Open Lovable](https://github.com/firecrawl/open-lovable) repository.

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Firecrawl](https://firecrawl.dev) for the amazing web scraping technology
- [E2B](https://e2b.dev) for secure sandbox execution
- [OpenAI](https://openai.com) for powerful AI models
- [Vercel](https://vercel.com) for the AI SDK and deployment platform
- Original [Open Lovable](https://github.com/firecrawl/open-lovable) project

## 🔗 Links

- **Live Demo**: [Lovable.dev](https://lovable.dev/)
- **Firecrawl**: [firecrawl.dev](https://firecrawl.dev)
- **E2B**: [e2b.dev](https://e2b.dev)
- **Original Repo**: [github.com/firecrawl/open-lovable](https://github.com/firecrawl/open-lovable)
