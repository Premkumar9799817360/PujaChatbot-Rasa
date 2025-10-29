# 🛕 **PujaChat Bot – Intelligent Rasa-based Chatbot**

## **📘 Project Overview**
**PujaChat Bot** is an AI-powered chatbot built using the **Rasa Framework** to assist users with **puja information, rituals, materials, and related vegan products**.  
It integrates **Natural Language Processing (NLP)** and **Machine Learning (ML)** to understand user queries and respond contextually.

---

## **1. What is Rasa?**
Rasa is an open-source framework for building **conversational AI chatbots** and **voice assistants**. Unlike rule-based bots, Rasa uses **Machine Learning (ML)** and **Natural Language Processing (NLP)** to understand and manage conversations intelligently.

It has two core components:
1. **Rasa NLU (Natural Language Understanding)** – Extracts **intents** and **entities** from user input.
2. **Rasa Core (Dialogue Management)** – Decides what to do next based on context and past conversations.

---

## **2. Architecture of Rasa Chatbot**

### **a) NLU Component**
- Converts user text into **structured data**:
  - **Intent**: Purpose of the user (e.g., `find_puja`, `buy_materials`)
  - **Entities**: Specific details (e.g., `puja_name`, `city`)
  
**Techniques Used:**
- Tokenization, Lemmatization
- Feature Extraction (Count Vectors, TF-IDF, Word Embeddings)
- **Models:**
  - **DIET Classifier** – Jointly learns intents & entities
  - **CRFEntityExtractor** – For detailed entity recognition
  - **SklearnIntentClassifier** – Uses SVM/Logistic Regression

---

### **b) Dialogue Management (Rasa Core)**
- Predicts the next action using:
  - **Rule-based policies** for fixed replies
  - **ML-based policies** for contextual conversations

**Core Policies:**
- **TEDPolicy** – Transformer-based contextual dialogue model  
- **RulePolicy** – For strict, deterministic flows  
- **MemoizationPolicy** – Remembers known conversation paths

---

## **3. Core Components of PujaChat Bot**

1. **`domain.yml`**
   - Defines intents, entities, slots, responses, and custom actions.
2. **`nlu.yml`**
   - Stores training examples for intent and entity recognition.
3. **`stories.yml`**
   - Describes conversation flows and user-bot interactions.
4. **`rules.yml`**
   - Handles simple, fixed paths like greetings or FAQs.
5. **`actions.py`**
   - Contains **custom Python actions** for dynamic responses and database/API calls.
6. **`config.yml`**
   - Defines ML pipelines and policies.

---

## **4. Working of PujaChat Bot**

### **Step 1: User Input**
User interacts with the chatbot through the website or messaging interface.  
Example:
> “Tell me about Ganesh Puja materials.”

---

### **Step 2: Natural Language Understanding (NLU)**
- User message is processed by **Rasa NLU**.
- Extracts:
  - **Intent:** `find_puja_info`
  - **Entities:** `puja_name=Ganesh`
- Uses **DIET Classifier** and **Pre-trained Embeddings (Spacy/BERT)** for high accuracy.

---

### **Step 3: Dialogue Management**
- Rasa Core predicts the **next action** based on:
  - Intent, entities, and conversation context.
- Example:
  - `find_puja_info` → `action_provide_puja_info`
  - `show_products` → `action_list_products`
  - `vegan_benefits` → `action_vegan_advice`

**ML Policy Used:** `TEDPolicy` ensures context-aware, intelligent responses.

---

### **Step 4: Actions & Custom Responses**
Custom actions are executed via `actions.py` to fetch data dynamically.  
Examples:
1. `action_provide_puja_info` → Provides details about specific pujas.  
2. `action_list_products` → Shows related puja materials.  
---
🌐 Step 5: Connect to Frontend or API

Integrate Rasa with a website or messenger platform for real-time user interaction.
---
6. Example Conversation

User: "What materials are needed for Saraswati Puja?"
Bot: "You’ll need items like books, veena, incense sticks, flowers, and fruits for Saraswati Puja."
---
7. Technologies Used

Rasa Framework

Python

Spacy / BERT Embeddings

NLU + ML Pipelines

SQLite / API Integration
```bash
pip install rasa
