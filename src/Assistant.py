import logs
import memory
import theoryofmindenhancer
import expert1
import expert2

class Assistant:
    def __init__(self):
        self.memory = memory.Memory()
        self.logger = logs.JsonLogger("Assistant")
        self.mind_enhancer = theoryofmindenhancer.TheoryOfMindEnhancer(self.memory)
        self.experts = {
            "expert1": expert1.Expert1(),
            "expert2": expert2.Expert2()
        }
    
    def choose_expert(self, user_input):
        # For simplicity, let's say expert1 handles inputs containing '1', and expert2 handles inputs containing '2'
        if '1' in user_input:
            return self.experts['expert1']
        elif '2' in user_input:
            return self.experts['expert2']
        else:
            return None

    def process_input(self, user_input):
        # Log the received input
        self.logger.info(f"Received user input: {user_input}")

        # Store the input in memory
        self.memory.store_input(user_input)

        # Choose the expert to handle the input
        chosen_expert = self.choose_expert(user_input)

        # If an expert is chosen, generate response with the expert, otherwise echo the input
        if chosen_expert is not None:
            response = chosen_expert.generate_response(user_input)
        else:
            response = f"I'm sorry, I can't handle this input: {user_input}"

        # Enhance the response using the Theory of Mind Enhancer
        enhanced_response = self.mind_enhancer.enhance_response(response)

        # Log the generated response
        self.logger.info(f"Generated response: {enhanced_response}")

        # Return the response
        return enhanced_response
