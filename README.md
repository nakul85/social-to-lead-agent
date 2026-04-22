# social-to-lead-agent
AI-powered conversational agent with RAG, intent detection, and lead capture
# Social-to-Lead Agentic Workflow

This project is a conversational AI agent built for a fictional SaaS product called AutoStream. The goal of the agent is to handle user queries, provide accurate product information, identify users with high purchase intent, and capture leads through a simulated backend function.

## Features

- Intent detection (greeting, pricing queries, high-intent users)
- Retrieval-based responses using a local knowledge base (RAG)
- Multi-turn conversation with memory
- Lead qualification and structured data collection
- Tool execution using a mock API

## Project Structure

social-to-lead-agent/
│
├── app.py  
├── requirements.txt  
│  
├── agent/  
│   ├── agent_graph.py  
│   ├── intent_classifier.py  
│   ├── tools.py  
│  
├── rag/  
│   ├── knowledge.json  
│   ├── rag_pipeline.py  

## How to Run

1. Clone the repository:
git clone https://github.com/nakul85/social-to-lead-agent.git  
cd social-to-lead-agent  

2. Install dependencies:
pip install -r requirements.txt  

3. Run the application:
python app.py  

4. Example interaction:
Hi  
Tell me pricing  
I want to try Pro plan  

The agent will respond with pricing details and then collect user information before triggering the lead capture function.

## Architecture Explanation

The system is divided into three main components: intent classification, retrieval pipeline, and agent workflow. The retrieval part uses a local JSON file as a knowledge base, which is converted into vector embeddings using HuggingFace embeddings. FAISS is used as the vector store to perform similarity search and retrieve relevant information based on user queries.

The agent logic is responsible for managing the conversation flow. It maintains state across multiple turns, allowing it to collect user details step by step once a high-intent signal is detected. A simple rule-based intent classifier is used to categorize user input, which is sufficient for this scenario and keeps the system predictable.

The lead capture process is implemented as a mock function, which is only triggered after all required details (name, email, and platform) are collected. This ensures proper control over the workflow and avoids premature execution.

## WhatsApp Integration Approach

To integrate this agent with WhatsApp, a webhook-based setup can be used. A backend service (such as Flask or FastAPI) would receive incoming messages from the WhatsApp Business API. Each message would be passed to the agent along with a session state for that user.

The agent’s response would then be sent back to the user through the WhatsApp API. For handling multiple users and maintaining conversation history, a storage system like Redis or a database can be used. This allows the agent to function in real time and manage multiple conversations efficiently.
