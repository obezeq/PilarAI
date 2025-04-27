# 🚀 **PilarAI: The Smart Learning Revolution** 🌟  
*Where AI doesn't just do your homework - it makes you a GENIUS!*  

<div align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2Y5Zjg0YzE0OGJmYzQ4M2I4YzQ5YmJkMWQyYmNlYjY1ZTAzYjE3ZSZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/26tn33aiTi1jkl6H6/giphy.gif" width="400" alt="PilarAI in action">
</div>

---

## 📖 Wiki Page Documentation
**Checkout the official PilarAI Wiki Documentation Page**
- [https://obezeq.github.io/PilarAI/wiki](https://obezeq.github.io/PilarAI/)

## 🔥 **What is PilarAI?**  
**PilarAI isn't just another homework AI.** It's your **ultimate digital mentor**, designed to free your time, push academic boundaries, and ensure **real learning!**  

🌟 **Mission:**  
*Transform education by automating repetitive tasks and enhancing critical learning. Copy-paste is dead - now we evolve!*

---

## 🛠️ **EPIC Features**  

### 📚 **Multidisciplinary & Adaptive**  
- **Master any subject!** Computer systems, programming, literature, biology, physics... Even Riemann Hypothesis solutions!  
- **Deep Thinking Mode 🧠**: Analyze, synthesize, and create solutions with flawless logic.  
- **Smart Verification 🔍**: Intelligent cross-checking with reliable sources (goodbye questionable Wikipedia!).  

### 🎨 **HyperCustom PDF**  
- **Design your PDF template**: Colorful, minimalist, academic... or even *Cyberpunk 2077* style!  
- **Writing Levels**:  
  AI adapts output to match appropriate student level:  
  - 🧒🐶 "My dog ate my homework" (Elementary)  
  - 🧑🎓 "Critical analysis of quantum theory" (High School)  
  - 👨🔬 "Fluid simulation with Navier-Stokes equations" (University)  
- **Anti-Detection Ninja 🥷**: Human-like text that even you'll doubt you wrote.  

### 🚨 **Explosive Learning!**  
- **Key Explanations 🔑**: Step-by-step breakdowns after generating solutions.  
- **Lightning Challenges ⚡**: Mini-quizzes based on your work. Prove you're not a bot!  
- **Teacher Mode 👩🏫**: Perfect for educators creating cheat-proof assignments.  

---

## 🌐 **How It Works**  
1. **📥 User Input**: Submit your task, select subject and difficulty.  
2. **⚙️ Epic Processing**:  
   - AI analysis with real-time source verification  
   - Specialized language models for each subject  
3. **📄 PDF Generation**: Customize fonts, colors, and layouts.  
4. **🧠 Learning Mode**: Study interactive explanations and solve challenges.  
5. **🚀 Submit & Conquer!**  

---

## 🏆 **Why PilarAI Beats ChatGPT**  
| **Feature**            | **Other AI**               | **PilarAI**              |
|------------------------|----------------------------|--------------------------|
| **Customization**      | Basic                      | Hyper-adaptive           |
| **Anti-Detection**     | Easy to spot               | 100% "human" text        |
| **Built-in Learning**  | None                       | Explanations + Challenges|
| **Education Focus**    | Low-quality work           | **Teach while doing**    |

---

## 🔮 **Future Roadmap**
- **🤖 Web-Based Work Generation**: Interactive task creation via web interface
- **🏦 Template Marketplace**: Premium PDF templates and teacher resources
- **🗣️ Pro Visual Explanations**: Interactive videos, audio guides & metaverse integration
- **🌍 50+ Language Support**: Including Latin, Greek, Chinese & Klingon!
- **📊 Teacher Analytics**: Detect usage patterns and improve classes

---

## 💻 **Try It Now!**  
Developers, designers, and educators - **Join us!**  

### 🚀 Installation

**Requirements**
- **Python 3**  
  [Download latest Python 3](https://www.python.org/downloads/)  
  *Enable PATH during installation*

- **Git**  
  [Download Git](https://git-scm.com/downloads)  

- [OpenAI Account](https://platform.openai.com/)  

**Terminal Commands**  
```bash
git clone https://github.com/obezeq/PilarAI.git
cd PilarAI
python main.py
```

**Dependencies**  
```bash
pip install openai python-dotenv markdown fpdf2 beautifulsoup4
```

---

## ⚙️ Configuration

1. Create `.env` file:  
```env
OPENAI_ORGANIZATION=your_openai_organization_key_here
OPENAI_PROJECT=your_openai_project_key_here
OPENAI_API_KEY=your_openai_key_here
```

2. File structure:  
```
├── config/
│   ├── template.json
│   └── user.json
├── results/
```

3. Template Configuration (`config/template.json`):  
```json
{
    "styles": {
        "main_font": "Arial",
        "text_color": "#333333",
        "header_colors": {
            "primary": "#2c3e50",
            "secondary": "#34495e",
            "tertiary": "#4a6572"
        },
        "sizes": {
            "h1": 24,
            "h2": 20,
            "h3": 16
        }
    },
    "header": {
        "title": "My Academic Work"
    },
    "footer": {
        "style": {
            "color": "#666666"
        }
    }
}
```

4. User Data (`config/user.json`):  
```json
{
    "firstName": "Hiram",
    "lastName": "Abiff",
    "course": "1stDAW B"
}
```

---

## 🖥️ Usage

1. Run:  
```bash
python main.py
```

2. Enter your task:  
```
📝 Enter the task you need to solve:
> Explain the main components of an operating system
```

3. Results saved in:  
```
results/
├── solution.txt
└── solution.pdf
```

---

## 🛠️ Troubleshooting

**API Key Error**  
```bash
❌ Error: Missing API Key. Verify .env file
```
*Solution: Ensure valid OpenAI key in .env*

**Font Issues**  
```bash
❌ Error: Arial font not found
```
*Solution: Add .ttf files to fonts/ folder*

**Encoding Issues**  
*Always use:*  
```python
with open("file.txt", "w", encoding="utf-8") as f:
```

---

## 📌 Future Improvements
- [ ] Enhanced multi-subject support
- [ ] Interactive template selector
- [ ] Image support in PDFs
- [ ] DOCX export
- [ ] Task history system
- [ ] 100% Humanizer Anti-AI Detection
