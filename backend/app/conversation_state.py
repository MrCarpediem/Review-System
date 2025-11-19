def next_prompt(step: str, text: str = ""):
    step = step or "start"
    text = text.strip()

    if step == "start":
        return "ask_name", "What's your name?"

    if step == "ask_name":
        if not text:
            return "ask_name", "Please enter your name."
        return "ask_product", "Which product is this review for?"

    if step == "ask_product":
        if not text:
            return "ask_product", "Please enter a product name."
        return "ask_review", "Please send your review."

    if step == "ask_review":
        if not text:
            return "ask_review", "Review cannot be empty."
        return "confirm", "Do you want to submit? (yes/no)"

    if step == "confirm":
        if text.lower() in ["yes", "y"]:
            return "save", "Saving your review..."
        return "cancel", "Review cancelled."

    return "start", "Let's start again."
