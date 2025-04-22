persona_permissions = {
    "student": {
        "allowed_agents": ["summarizer", "deadline_extractor"],
        "restricted": ["financial_analysis", "personal_data_agent"]
    },
    "admin": {
        "allowed_agents": "*",
        "restricted": []
    }
}