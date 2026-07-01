import random
class nalkiLLM:
    def __init__(self):
        print('LLM creqated')

    def predict(self,prompt):


        response_list=[
            "The capital of France is Paris. It is known for its art, culture, and history. The Eiffel Tower is one of the most famous landmarks in Paris.",
            "1. What is the capital of France? \n A: Paris\n\n2. What is Paris known for? \n A: Art, culture, and history.\n\n3. What is one of the most famous landmarks in Paris? \n A: The Eiffel Tower.\n\n4. Is the Eiffel Tower located in Paris? \n A: Yes, it is located in Paris.\n\n5. What are some of the attractions in Paris? \n A: The Louvre Museum, Notre-Dame Cathedral, and the Champs-Élysées."
        ]

        return {'response': random.choice(response_list)}



    