from transformers import pipeline
import gradio as gr
def story(StoryLength,StoryPrompt):
    model= pipeline("text-generation", model="e-tony/gpt2-rnm")
    return model(StoryPrompt, max_length=StoryLength, num_return_sequences=1)[0]["generated_text"]
    
    
interface = gr.Interface(fn=story, 
                        inputs=["number","text"],
                         outputs="text", 
                        title='Bilal Story Generator')
                        

interface.launch(inline=False)
