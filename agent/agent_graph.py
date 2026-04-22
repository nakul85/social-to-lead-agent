from agent.intent_classifier import classify_intent
from agent.tools import mock_lead_capture


class AgentState:
    def __init__(self):
        self.intent = None
        self.name = None
        self.email = None
        self.platform = None
        self.lead_stage = False


def run_agent(user_input, state, vectorstore):

    if state.lead_stage:

        if state.name is None:
            state.name = user_input
            return "Great! What's your email?"

        elif state.email is None:
            state.email = user_input
            return "Which platform do you create content on?"

        elif state.platform is None:
            state.platform = user_input
            mock_lead_capture(state.name, state.email, state.platform)
            return "You're all set! Our team will contact you soon."

    intent = classify_intent(user_input)
    state.intent = intent

    if intent == "greeting":
        return "Hello. How can I help you today?"

    elif intent == "pricing":
        docs = vectorstore.similarity_search(user_input, k=2)
        response = "Here is the pricing information:\n"
        for d in docs:
            response += f"- {d.page_content}\n"
        return response

    elif intent == "high_intent":
        state.lead_stage = True
        return "Let's get started. What is your name?"

    return "Can you please clarify your request?"
