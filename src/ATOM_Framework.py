class ATOMFramework:
    def __init__(self, model):
        self.ai_model = AIModel(model)
        self.memory_enhancer = MemoryEnhancer()
        self.output_controller = OutputController()
        self.theory_of_mind_enhancer = TheoryOfMindEnhancer()
        self.thought_chain = ThoughtChain()
        self.experts = self._initialize_experts()
        self.agent = Agent(self.experts)

    def _initialize_experts(self):
        # Initialize expert models (this could be instances of specific AI models)
        expert_1 = Expert('expert_1', AIModel(None))
        expert_2 = Expert('expert_2', AIModel(None))
        return [expert_1, expert_2]

    def process_input(self, user_input):
        self.thought_chain.add_thought(user_input)

        last_n_thoughts = self.thought_chain.get_last_n_thoughts(5) # Get last 5 thoughts, this number can be adjusted
        prompt = self.memory_enhancer.construct_prompt(last_n_thoughts) # Use memory enhancer to construct the prompt

        raw_response = self.ai_model.generate_response(prompt)
        
        controlled_response = self.output_controller.control_output(raw_response) # Control the output of the response
        enhanced_response = self.theory_of_mind_enhancer.enhance_response(controlled_response) # Enhance the response with theory of mind

        self.thought_chain.add_thought(enhanced_response)

        return enhanced_response
