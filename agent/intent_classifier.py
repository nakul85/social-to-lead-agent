def classify_intent(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "greeting"

    if any(word in user_input for word in ["buy", "subscribe", "sign up", "start", "try", "want", "interested"]):
        return "high_intent"

    if any(word in user_input for word in ["price", "pricing", "plan", "cost", "features"]):
        return "pricing"

    return "general"
