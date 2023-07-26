# Agent.py

class Agent:
    def __init__(self, experts):
        self.experts = experts
        self.memory = Memory()

    def receive_input(self, input):
        # Check memory for similar interactions
        past_interaction = self.memory.recall(input)

        # If there's a relevant past interaction, use it to inform the conversation
        if past_interaction:
            return past_interaction.response

        # Otherwise, choose an expert to respond
        chosen_expert = self.choose_expert(input)
        response = chosen_expert.respond(input)

        # Remember the interaction
        interaction = Interaction(input, response, chosen_expert.specialty)
        self.memory.remember(interaction)

        return response

    def choose_expert(self, prompt):
        # Define a mapping of keywords/topics to experts. The Agent scans the prompt for those keywords to select an expert.
        # We will need to define this mapping based on the specialties of the experts.
        keyword_to_expert_mapping = {}

        for keyword, expert in keyword_to_expert_mapping.items():
            if keyword in prompt:
                return expert

        # If no expert is found via keyword matching, default to a generalist expert
        # This could be enhanced to use more advanced routing methods later
        return self.experts[0]
        pass
