from . import models

def get_state(db, phone):
    return db.query(models.ConversationState).filter_by(phone=phone).first()

def set_state(db, phone, step, **kwargs):
    state = get_state(db, phone)
    if not state:
        state = models.ConversationState(phone=phone, step=step)
        db.add(state)

    state.step = step

    for key, value in kwargs.items():
        setattr(state, key, value)

    db.commit()
    db.refresh(state)
    return state


def create_review(db, data):
    review = models.Review(**data.dict())
    db.add(review)
    db.commit()
    db.refresh(review)
    return review
