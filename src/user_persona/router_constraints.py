class RouterConstraintsEngine:
    def __init__(self, permission_map):
        self.permission_map = permission_map

    def validate(self, user_role, requested_agents):
        allowed = self.permission_map.get(user_role, {}).get("allowed_agents", [])
        if allowed == "*":
            return True, []
        denied = [agent for agent in requested_agents if agent not in allowed]
        if denied:
            return False, denied
        return True, []