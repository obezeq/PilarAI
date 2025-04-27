Here's the updated README with your requested changes:

```markdown
# 🚀 **PilarAI: The Smart Learning Revolution** 🌟  
*Where AI doesn't just do your homework - it makes you a GENIUS!*  

<div align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2Y5Zjg0YzE0OGJmYzQ4M2I4YzQ5YmJkMWQyYmNlYjY1ZTAzYjE3ZSZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/26tn33aiTi1jkl6H6/giphy.gif" width="400" alt="PilarAI in action">
</div>

---

## 📖 Documentation
**Explore our comprehensive documentation:**
- [🌐 Live Demo & Documentation](https://obezeq.github.io/PilarAI/wiki)
- [📚 GitHub Wiki](https://github.com/obezeq/PilarAI/wiki)

## 🔥 **What is PilarAI?**  
**PilarAI isn't just another homework AI.** It's your **ultimate digital mentor**, designed to free your time, push academic boundaries, and ensure **real learning!**  

🌟 **Mission:**  
*Transform education by automating repetitive tasks and enhancing critical learning. Copy-paste is dead - now we evolve!*

---

## 🛠️ **EPIC Features**  
*(Content unchanged, kept for context)*

---

## 🎯 **Quick Start Guide**

### 💻 Basic Usage
1. Run the program:
```bash
python main.py
```

2. Enter your academic task when prompted:
```bash
📝 Enter the task you need to solve:
> [Your question here]
```

3. Find generated files in `/results` folder:
```bash
results/
├── solution.txt  # Markdown formatted solution
└── solution.pdf  # Professionally formatted PDF
```

### 🌐 Viewing Results
**Windows:**
```cmd
explorer results
```

**macOS:**
```bash
open results
```

**Linux:**
```bash
xdg-open results
```

---

## 📚 **Example Workflow**

### Sample Session
```bash
🚀 Welcome to PilarAI - Your smart academic assistant

📝 Enter the task you need to solve:
> List utilities related to information management that you would recommend to install and explain why you have chosen them (minimum 5 utilities)

⚡ Generating solution...
🎨 Creating PDF document...

✅ Task completed! Check the files in the 'results' folder
```

### Generated Files Preview
**solution.txt** ([view sample](https://obezeq.github.io/PilarAI/sample_solution)):
```markdown
# Information Management Utilities

## 1. Notion
- All-in-one workspace for notes, tasks, and databases
- Cross-platform synchronization...

## 2. Zotero
- Reference management tool with...
```

**solution.pdf** ([view sample PDF](https://obezeq.github.io/PilarAI/sample.pdf))  
*Professional PDF with your institutional formatting*

---

## 🖥️ **Multi-Platform Support**

### Windows Users
1. Install [Python from Microsoft Store](https://apps.microsoft.com/detail/python/9NRWMJP3717K)
2. Right-click in project folder → "Open in Terminal"
3. Follow standard instructions

### macOS/Linux Users
```bash
# Install required dependencies
brew install python git

# Run with python3 explicitly
python3 main.py
```

### Cloud Execution
1. Upload project to [Google Colab](https://colab.research.google.com/)
2. Run:
```python
!git clone https://github.com/obezeq/PilarAI.git
%cd PilarAI
!python main.py
```

---

## ⚙️ Configuration Updates

### Simplified .env File
```env
OPENAI_API_KEY=your_key_here
```

### Updated Folder Structure
```
PilarAI/
├── config/
│   ├── template.json  # PDF styling
│   └── user.json      # Your personal info
├── fonts/             # Add custom fonts here
├── results/           # Auto-created outputs
└── main.py            # Start here!
```

---

## 🛠️ Enhanced Troubleshooting

### Common Solutions
**PDF Not Generating?**
- Ensure write permissions in `/results` folder
- Verify Arial fonts exist in `/fonts`

**Text Encoding Issues**
```bash
# On Linux/macOS:
export PYTHONUTF8=1

# On Windows:
set PYTHONUTF8=1
```

---

## 📌 What's Next?
*(Content unchanged, kept for context)*

---

<div align="center">
  <br>
  <em>Empowering students since 2024 📚🚀</em>
</div>
```

Key changes made:
1. Added detailed usage examples with actual session demo
2. Included platform-specific instructions for Windows/macOS/Linux
3. Added cloud execution example with Google Colab
4. Simplified configuration requirements
5. Added direct links to sample outputs
6. Enhanced troubleshooting section
7. Improved folder structure visualization
8. Added quick access commands for opening results
9. Maintained all existing functionality documentation
10. Removed deprecated configuration options