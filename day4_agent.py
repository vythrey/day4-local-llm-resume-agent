import ollama


class MemoryAgent:
    def __init__(self):
        self.memory = {}

    def store(self, key, value):
        self.memory[key] = value

    def recall(self, key):
        return self.memory.get(key, "No memory found.")


class LocalLLMResumeAgent:
    def __init__(self, model_name="llama3.2:1b"):
        self.memory = MemoryAgent()
        self.model_name = model_name

    def improve_resume_text(self, text):
        prompt = f"""
You are a helpful resume improvement assistant.

Task:
Rewrite the following rough work experience into 2 strong professional resume bullet points.

Rules:
- Keep the meaning accurate
- Use professional business language
- Make it concise
- Output only bullet points
- Do not invent fake achievements or numbers

Input:
{text}
"""

        response = ollama.chat(
            model=self.model_name,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response["message"]["content"].strip()

    def respond(self, user_input):
        cleaned = user_input.strip()
        lower = cleaned.lower()

        if lower == "last output":
            return self.memory.recall("last_output")

        if lower.startswith("improve:"):
            text = cleaned[len("improve:"):].strip()

            result = self.improve_resume_text(text)

            self.memory.store("last_input", text)
            self.memory.store("last_output", result)

            return result

        return (
            "Use format:\n"
            "improve: your rough resume text\n"
            "Type 'last output' to recall the previous result."
        )


if __name__ == "__main__":
    agent = LocalLLMResumeAgent()

    print("Local LLM Resume Agent is running. Type 'exit' to stop.")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower().strip() == "exit":
            print("Goodbye!")
            break

        print("\nAgent:")
        print(agent.respond(user_input))