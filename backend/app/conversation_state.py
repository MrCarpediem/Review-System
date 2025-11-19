from typing import Tuple

def next_prompt(step: str, text: str):
    step = step or "start"
    text = text.strip()

    if step == "start":
        return "ask_name", "Hi! What's your name?"

    if step == "ask_name":
        if not text:
            return "ask_name", "Please enter your name."
        return "ask_product", f"Thanks {text}! Which product would you like to review?"

    if step == "ask_product":
        if not text:
            return "ask_product", "Please enter a product name."
        return "ask_rating", "On a scale of 1–5, how would you rate the product?"

    if step == "ask_rating":
        try:
            r = int(text)
            if r < 1 or r > 5:
                raise ValueError
        except:
            return "ask_rating", "Rating must be a number between 1 and 5."
        return "ask_review", "Write your review (or type 'skip')."

    if step == "ask_review":
        return "confirm", "Do you want to submit? (yes/no)"

    if step == "confirm":
        if text.lower() in ["yes", "y"]:
            return "save", "Saving..."
        else:
            return "cancel", "Cancelled."

    return "start", "Let's start again."
