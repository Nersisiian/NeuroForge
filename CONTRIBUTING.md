# Contributing to NeuroForge

First off, thank you for considering contributing to NeuroForge! 🎉

NeuroForge is a revolutionary self-assembling operating environment, and we welcome contributions from everyone — from AI researchers to Rust developers, from UI/UX wizards to DevOps engineers.

## Code of Conduct

This project and everyone participating in it is governed by our high standards of respect and professionalism. Be kind, be constructive, and be awesome.

## How Can I Contribute?

### 🐛 Reporting Bugs

If you find a bug, please open an issue with:
- A clear, descriptive title
- Steps to reproduce the bug
- Expected behavior vs actual behavior
- Screenshots (if applicable)
- Your environment (OS, Docker version, etc.)

### 💡 Suggesting Enhancements

Have an idea to make NeuroForge even more powerful? Open an issue with:
- A clear description of the enhancement
- Why it would be valuable
- Possible implementation approach (if you have one)

### 🔧 Pull Requests

1. **Fork** the repository
2. **Create a branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**: Write clean, documented code
4. **Test thoroughly**: Ensure all services run correctly
5. **Commit**: `git commit -m ''Add amazing feature''`
6. **Push**: `git push origin feature/amazing-feature`
7. **Open a Pull Request**: Describe your changes in detail

### 🏗️ Development Setup

```bash
# Clone the repository
git clone https://github.com/Nersisiian/NeuroForge.git
cd NeuroForge

# Start all services
cd docker
docker compose up -d --build

# Run tests
# Rust tests
cd neuroforge-core && cargo test
cd ../neuroforge-orchestrator && cargo check

# Python tests
cd ../neuroforge-cortex
python -m pytest tests/

# Frontend
cd ../neuroforge-genesis-ui
npm run build
🎯 Priority Areas
We are currently focusing on:

gRPC Streaming: Real-time communication between services

WebGPU Fluid Canvas: Next-gen generative UI

CRDT State: Immortal, conflict-free state management

Real LLM Integration: Moving beyond demo to production AI

Kubernetes Deployment: Cloud-native orchestration

📝 Style Guide
Rust: Follow standard Rust conventions (cargo fmt, cargo clippy)

Python: Follow PEP 8, use type hints

TypeScript: Use ESLint and Prettier

Documentation: Comment complex logic, update README if needed

❓ Questions?
Open an issue or contact the maintainer directly through GitHub.

Every line of code brings us closer to a truly intelligent operating environment. Let''s build the future together. 🚀
