# 🤖 Ollama Setup Guide for Kognicare

## What is Ollama?

Ollama is a tool that allows you to run large language models locally on your computer. For Kognicare, we use it to power the AI medical assistant with the Phi-3.5 Mini model.

## Installation Steps

### 1. Download Ollama

Visit [ollama.com](https://ollama.com/download) and download the installer for your operating system.

### 2. Install Ollama

Run the downloaded installer and follow the installation instructions.

### 3. Verify Installation

Open a command prompt and run:
```bash
ollama --version
```

You should see the Ollama version information.

### 4. Download the Phi-3.5 Model

This is the AI model that powers our medical assistant:
```bash
ollama pull phi3.5
```

**Note**: This download is approximately 2.2GB and may take some time depending on your internet connection.

### 5. Verify Model Installation

Check that the model is installed:
```bash
ollama list
```

You should see `phi3.5` in the list of installed models.

### 6. Test the Model

Test the model with a simple query:
```bash
ollama run phi3.5 "What is a normal heart rate?"
```

## Starting Ollama

Ollama typically starts automatically when you install it. If you need to start it manually:

### Windows
```bash
ollama serve
```

### Checking if Ollama is Running

Visit `http://localhost:11434` in your browser. You should see "Ollama is running".

## Troubleshooting

### Common Issues

1. **"ollama: command not found"**
   - Restart your command prompt/terminal
   - Make sure Ollama is properly installed
   - Check if it's added to your system PATH

2. **Port 11434 already in use**
   - Another instance of Ollama might be running
   - Restart your computer or stop the existing process

3. **Model download fails**
   - Check your internet connection
   - Try again later if the server is busy
   - Make sure you have enough disk space (at least 3GB free)

4. **High memory usage**
   - Phi-3.5 Mini requires at least 4GB RAM
   - Close other applications if your system is low on memory

### Alternative Models

If Phi-3.5 doesn't work on your system, you can try smaller models:

```bash
# Smaller model (requires less memory)
ollama pull llama3.2:1b

# Medium-sized model
ollama pull llama3.2:3b
```

Then update the `AI_MODEL` setting in `config.py` to match your chosen model.

## Using Kognicare Without Ollama

If you can't install Ollama, don't worry! Kognicare will still work with a fallback mode that provides helpful predefined responses. You'll still get:

- ✅ Real-time vital monitoring
- ✅ Alert system
- ✅ Charts and data visualization
- ✅ PDF report generation
- ⚠️ Limited AI responses (predefined, not conversational)

## Performance Tips

1. **First Run**: The first time you use the AI assistant, responses may be slower as the model loads into memory.

2. **Keep Ollama Running**: Leave Ollama running in the background for faster responses.

3. **System Requirements**: 
   - Minimum: 4GB RAM
   - Recommended: 8GB+ RAM
   - Storage: 5GB free space

## Security Notes

- Ollama runs locally on your computer
- No data is sent to external servers
- All AI processing happens on your machine
- Your patient data stays private

## Getting Help

If you encounter issues:

1. Check the [Ollama GitHub repository](https://github.com/ollama/ollama)
2. Visit the [Ollama documentation](https://github.com/ollama/ollama/blob/main/README.md)
3. Ensure your system meets the requirements

---

**Ready to use AI-powered medical assistance! 🚀**
