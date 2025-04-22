from src.registry import app_registry
from src.memory import MemoryStore
from src.router import llm_router
from src.executor import summarizer, deadline_extractor
from src.user_persona.manager import UserPersonaManager
from src.user_persona.permissions import persona_permissions
from src.user_persona.router_constraints import RouterConstraintsEngine

def run_task(user_id, user_query, users_db):
    user_manager = UserPersonaManager(users_db)
    user = user_manager.get_user(user_id)
    memory = MemoryStore(user_profile=user)

    requested_agents = llm_router(user_query)
    validator = RouterConstraintsEngine(persona_permissions)
    allowed, denied = validator.validate(user["role"], requested_agents)

    if not allowed:
        return {"error": f"Access denied for: {denied}"}

    memory.update("text", user_query)
    for app_name in requested_agents:
        if app_name == "summarizer":
            result = summarizer(text=memory.get("text"))
        elif app_name == "deadline_extractor":
            result = deadline_extractor(summary=memory.get("summary"))
        for k, v in result.items():
            memory.update(k, v)

    return memory.dump()

if __name__ == "__main__":
    users_db = {
        "user123": {
            "name": "Arooj",
            "role": "student",
            "capabilities": ["summarizer", "deadline_extractor"]
        }
    }
    result = run_task("user123", "Summarize and extract deadlines", users_db)
    print(result)