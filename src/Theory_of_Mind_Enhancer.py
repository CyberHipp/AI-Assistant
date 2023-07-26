class TheoryOfMindEnhancer:
    def __init__(self, model, memory):
        self.model = model  # Some model
        self.memory = memory  # Use Memory instance to access the conversation history

    def enhance_response(self, controlled_response):
        # Enhance the response with theory of mind
        # For now, let's just make the assistant refer back to the previous user input in its response
        last_user_input = self.memory.get_last_n(1)[0].prompt  # Get the last user input from memory

        # Use the model to enhance the response
        enhanced_response = self.model.enhance_response(controlled_response)

        # Append a reference to the last user input to the assistant's response
        enhanced_response = f"In response to what you said about '{last_user_input}', {enhanced_response}"

        return enhanced_response
