import requests
import json
import gradio as gr

url = "http://localhost:11434/api/generate"
headers = {
    'Content-Type': 'application/json'
}

history = []

def generateResponse(prompt):
    
    history.append(prompt)
    finalPrompt = "\n".join(history)
    
    data = {
        "model": "Opaque",
        "prompt": finalPrompt,
        "stream": False
    }
    
    response = requests.post(url, headers = headers, data = json.dumps(data))
    
    if response.status_code == 200:
        response = response.text
        data = json.loads(response)
        finalResponse = data['response']
        return finalResponse
    else:
        print("Error: ", response.text)
        return "An error occurred while generating the response." # Add a return in the else case.

interface = gr.Interface(
    fn = generateResponse,
    inputs = gr.Textbox(lines = 5, placeholder = "Enter your prompt here..."),
    outputs = "text", # Add the outputs argument
)

interface.launch()