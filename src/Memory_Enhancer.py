# MemoryEnhancer.py

class MemoryEnhancer:

    def __init__(self):
        self.model = None # Some model

    def construct_prompt(self, last_n_thoughts):
        # Construct a prompt given the last n thoughts
        # This function will need to be fleshed out with the specifics of how the prompt is constructed.
        # This could involve concatenating the thoughts, adding specific formatting or keywords, etc.
        # Since this is highly dependent on the specifics of the AI model and the memory enhancer being used, it's left as a placeholder here.
        return self.model.construct_prompt(last_n_thoughts)

    def __init__(self, memory):
        self.memory = memory

    def construct_prompt(self, n):
        # Get the last n interactions from memory
        last_n_interactions = self.memory.get_last_n(n)

        # Extract the textual prompts
        last_n_prompts = [interaction.prompt for interaction in last_n_interactions]

        # Join the prompts into a single context string 
        prompt_context = " ".join(last_n_prompts)

        return prompt_context
