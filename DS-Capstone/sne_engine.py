import collections

class SocialNetwork:
    def __init__(self):
        # Hashing: Profile storage (Username -> Data)
        self.profiles = {}
        # Graph: Adjacency List (Username -> Set of Friends)
        self.network = collections.defaultdict(set)

    # --- Profile Management ---
    def add_user(self, username, interests, location):
        self.profiles[username] = {"interests": set(interests), "location": location}
        if username not in self.network:
            self.network[username] = set()

    def get_profile(self, username):
        return self.profiles.get(username, "User not found.")

    def update_profile(self, username, interests=None, location=None):
        if username in self.profiles:
            if interests: self.profiles[username]["interests"] = set(interests)
            if location: self.profiles[username]["location"] = location
            return True
        return False

    # --- Network Management ---
    def add_friendship(self, u, v):
        if u in self.profiles and v in self.profiles:
            self.network[u].add(v)
            self.network[v].add(u)

    def remove_friendship(self, u, v):
        if v in self.network[u]: self.network[u].remove(v)
        if u in self.network[v]: self.network[v].remove(u)

    # --- Discovery (BFS: Degrees of Separation) ---
    def shortest_path(self, start, target):
        if start == target: return [start]
        queue = collections.deque([[start]])
        visited = {start}
        
        while queue:
            path = queue.popleft()
            node = path[-1]
            for neighbor in self.network[node]:
                if neighbor == target:
                    return path + [neighbor]
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(path + [neighbor])
        return None

    # --- Exploration (DFS: Depth-limited) ---
    def explore_fof(self, start, depth):
        discovered = set()
        def _dfs(curr, curr_depth):
            if curr_depth > depth: return
            if curr != start: discovered.add(curr)
            for neighbor in self.network[curr]:
                _dfs(neighbor, curr_depth + 1)
        
        _dfs(start, 0)
        return discovered

    # --- Recommendation (Interest-based Sorting) ---
    def suggest_friends(self, user):
        user_interests = self.profiles[user]["interests"]
        suggestions = []
        
        for other in self.profiles:
            if other == user or other in self.network[user]: continue
            common = user_interests.intersection(self.profiles[other]["interests"])
            if common:
                suggestions.append((other, len(common)))
        
        # Sort by count of common interests (Descending)
        return sorted(suggestions, key=lambda x: x[1], reverse=True)