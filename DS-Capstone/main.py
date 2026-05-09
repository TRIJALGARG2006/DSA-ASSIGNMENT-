from sne_engine import SocialNetwork

def demo():
    sne = SocialNetwork()
    
    # 1. Add 6-8 users
    users = [
        ("Alice", ["Coding", "Guitar"], "Delhi"),
        ("Bob", ["Guitar", "Gaming"], "Noida"),
        ("Charlie", ["Coding", "Chess"], "Delhi"),
        ("David", ["Gaming", "Chess"], "Gurgaon"),
        ("Eve", ["Coding", "Gaming"], "Noida"),
        ("Frank", ["Guitar", "Chess"], "Delhi"),
        ("Grace", ["Biking"], "Gurgaon")
    ]
    for u, i, l in users: sne.add_user(u, i, l)

    # 2. Update 2 profiles, show 3
    sne.update_profile("Alice", interests=["Coding", "Guitar", "MERN"])
    sne.update_profile("Bob", location="Gurgaon")
    print(f"Profile Alice: {sne.get_profile('Alice')}")
    print(f"Profile Bob: {sne.get_profile('Bob')}")
    print(f"Profile Charlie: {sne.get_profile('Charlie')}\n")

    # 3. Create connections (8-12) & Remove 1
    edges = [("Alice", "Bob"), ("Alice", "Charlie"), ("Bob", "David"), 
             ("Charlie", "Eve"), ("David", "Eve"), ("Eve", "Frank"),
             ("Frank", "Alice"), ("Bob", "Frank")]
    for u, v in edges: sne.add_friendship(u, v)
    sne.remove_friendship("Alice", "Frank")

    # 4. BFS Shortest Path
    print(f"Path Alice to David: {sne.shortest_path('Alice', 'David')}")
    print(f"Path Charlie to Bob: {sne.shortest_path('Charlie', 'Bob')}\n")

    # 5. DFS Exploration
    print(f"Alice's FoF (Depth 2): {sne.explore_fof('Alice', 2)}")
    print(f"Alice's FoF (Depth 3): {sne.explore_fof('Alice', 3)}\n")

    # 6. Suggestions
    print(f"Suggestions for Alice: {sne.suggest_friends('Alice')}")

if __name__ == "__main__":
    demo()