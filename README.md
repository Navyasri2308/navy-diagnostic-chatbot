# NAVY Hub — Indian Navy Knowledge Assistant

A domain-specific conversational workspace designed to answer core historical and structural questions about the Indian Navy. It integrates a clean web interface dashboard with a localized, intelligent search-matching retrieval system to answer queries accurately without relying on external cloud processing.

---

## ⚓ Chosen Domain & Knowledge Base
This application specializes in **Naval Systems and Historical Operations**. The underlying knowledge base resides entirely inside a local structured plain-text catalog (`data/files 1.txt`). It includes operational parameters, foundational history, and definitions including:
* **Historical Landmarks:** Key operational context regarding Chhatrapati Shivaji Maharaj, Navy Day foundations, and Operation Trident.
* **Fleet Formations:** Core engineering definitions of Aircraft Carriers, Stealth Frigates, and Guided-Missile Destroyers.
* **Specialized Commands:** Positional profiles for the Andaman and Nicobar Command alongside elite tactical operations (MARCOS).

---

## 🛠️ Architectural Approach
This system utilizes a **Pretrained Foundation Layer + Localized Vector-Augmented Retrieval (RAG)** layout built using Python and Flask.

### Why this approach was chosen:
1. **Zero Fine-Tuning Overload:** Training a custom language model from scratch or executing a fine-tuning process requires immense computational power and thousands of clean documents. 
2. **Deterministic Data Mapping:** Navy documentation requires absolute precision. By using standard natural language processing vector matrices (`TfidfVectorizer` and `cosine_similarity`), the system isolates matching segments of documentation down to the exact paragraph block.
3. **Resilient Fallback Design:** If a query fails to match local technical parameters, the core framework switches automatically to a zero-credentials public web lookup mapping against the Wikipedia API matrix.

---

## ⚙️ Setup & Installation Instructions

Follow these steps to deploy and execute the workspace environment on your local development machine:

### 1. Clone & Organize the Files
Ensure your project workspace is organized using this structure:
```text
navy-diagnostic-chatbot/
│
├── data/
│   └── files 1.txt        # Your naval technical documentation text
├── app.py                 # Core Flask backend application script
├── index.html             # Responsive engineering UI dashboard
├── style.css              # Dashboard formatting stylesheet
├── requirements.txt       # Active application package registry
└── wsgi.py                # Server gateway deployment entry point

###2. Install Project Dependencies
Open your choice of terminal application (Command Prompt or PowerShell) inside your root workspace directory and install the necessary dependencies via pip:

Bash
pip install -r requirements.txt

###3. Launch the Backend Server Application
Run the Python file to spin up the local Flask web app environment:

Bash
python app.py

###4. Open the Interface Workspace
Simply double-click your index.html file or right-click and select Open with Live Server inside your web browser to open the chat layout panel.

##⚖️ Navigated Engineering Tradeoff
Accuracy & Security vs. Conversational Fluency
The Tradeoff: We chose a strict programmatic text retrieval system over an unconstrained, generative large language model framework (like raw, ungrounded generative AI models).

The Resolution: While a pure conversational generative AI produces highly fluid paragraphs, it risks hallucinations—making up incorrect structural details or historical dates.

By structuring the chatbot around programmatic semantic matching of our local text documents, we guarantee that the output sent back to the dashboard is 100% accurate to the manual text file, prioritizing technical data safety over small talk.
***
