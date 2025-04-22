def llm_router(user_query: str):
    query = user_query.lower()
    if "summarize" in query and "deadline" in query:
        return ["summarizer", "deadline_extractor"]
    elif "summarize" in query:
        return ["summarizer"]
    elif "deadline" in query:
        return ["deadline_extractor"]
    elif "financial" in query or "red flag" in query:
        return ["financial_analysis"]
    elif "personal" in query or "pii" in query or "redact" in query:
        return ["personal_data_agent"]
    return []