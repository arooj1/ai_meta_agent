def llm_router(user_query: str):
    if "summarize" in user_query and "deadline" in user_query:
        return ["summarizer", "deadline_extractor"]
    elif "summarize" in user_query:
        return ["summarizer"]
    elif "deadline" in user_query:
        return ["deadline_extractor"]
    return []