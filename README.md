
# 🔒 Hack Buddy

**Hack Buddy** is an AI-powered vulnerability analysis tool that automates Nmap network scanning and generates executive-level security reports. It combines AI agents, shell command execution, and intelligent workflows through n8n, all wrapped in a clean and interactive Streamlit frontend.

---

## 🚀 Features

- 🔍 **AI-Augmented Nmap Scanning**  
  Automatically detects your network IP, constructs custom Nmap vulnerability scans, and produces styled HTML reports.

- 🧠 **AI-Generated Reports**  
  Uses Google Gemini language models to generate 1000-word markdown reports detailing vulnerabilities and patch status.

- 🧰 **Interactive Streamlit UI**  
  Easily access scanning tools and reports through a streamlined, responsive web interface.

- ⚙️ **End-to-End Automation**  
  Fully automated via n8n workflows—from command generation to report rendering.

---

## 📁 Project Structure

```
HackBuddy/
├── streamlit_app.py              # Frontend dashboard using Streamlit
├── README.md                     # Project documentation
├── vuln_scan.xml                 # XML output from Nmap (generated after running the app)
├── vuln_scan.html                # Final styled vulnerability report (generated after running the app)
├── nmap.xsl                      # XSL file for report transformation (generated after running the app)
└── /n8n_workflows/               # Exported n8n workflow JSON files (generated after running the app)
```

---

## 🧑‍💻 Tech Stack

- [Streamlit](https://streamlit.io/) – Frontend UI
- [n8n](https://n8n.io/) – Workflow orchestration
- [Nmap](https://nmap.org/) – Network scanning tool
- [Google Gemini (PaLM)](https://deepmind.google/technologies/gemini/) – AI model for analysis and reporting
- PowerShell – Shell environment for executing Windows-based commands

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/hack-buddy.git
cd hack-buddy
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup Nmap and Tools

- Install [Nmap](https://nmap.org/download.html)
- Install `xsltproc` for XML to HTML transformation
- Ensure `nmap.xsl` is downloaded into the project directory

### 4. Run Streamlit App

```bash
streamlit run streamlit_app.py
```

Visit: `http://localhost:8501` in your browser.

---

## 🔗 Webhook Endpoints

These endpoints are managed through n8n:

- `POST /your unique endpoint 1` → Triggers Nmap scanning pipeline
- `POST /your unique endpoint 2` → Triggers AI report generation pipeline

> Make sure these endpoints are correctly configured in your `streamlit_app.py`.

---

## 📌 Usage Guide

1. **Select Tool:** Choose between "Network Scanner" and "Generate detailed Report and Analysis" from the sidebar.
2. **Trigger Scan:** Click to start the automated scan. The report will render and become downloadable.
3. **Generate Report:** Generate a detailed AI-based vulnerability report from past scan data in markdown format.

---

## 📄 Example Output

- `vuln_scan.html` – Rich HTML Nmap scan report
- `ai_detailed_vulnerability_report.md` – 1000-word stakeholder-ready report

---

## 🧠 AI Prompting Logic

Prompts are structured to:
- Detect device IPs and network ranges
- Construct valid, safe PowerShell and Nmap commands
- Translate XML vulnerability scan results into human-readable narratives

---

## 🔐 Security Notes

- Commands are restricted to trusted templates
- Webhooks use UUID-based access for basic endpoint security
- No user-uploaded files are executed
- Reports are stored temporarily and isolated

---

## 👨‍💻 Author

**Ankur Kumar Muduli**  
Made with ❤️ for Hackathons

---

## 📜 License

This project is licensed under the MIT License. See `LICENSE` for more details.
