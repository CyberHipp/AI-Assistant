# Memory.py

class Memory:

    def __init__(self):
        # Initialize an empty memory
        self.records = []

    def remember(self, interaction):
        # Store the interaction in memory
        self.records.append(interaction)

    def get_last_n(self, n):
        # Get the last n records from memory
        return self.records[-n:]

    def recall(self, context):
        # Retrieve relevant memory given a context
        # This could involve complex logic like searching for similar contexts
        pass
