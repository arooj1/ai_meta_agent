app_registry = {
    "summarizer": {
        "description": "Summarizes input text.",
        "input_keys": ["text"],
        "output_keys": ["summary"]
    },
    "deadline_extractor": {
        "description": "Extracts deadlines from summaries.",
        "input_keys": ["summary"],
        "output_keys": ["deadlines"]
    }
}