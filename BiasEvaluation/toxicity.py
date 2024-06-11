from datasets import load_dataset
from transformers import pipeline, AutoTokenizer

import random

toxicity_prompts = load_dataset("allenai/real-toxicity-prompts", split="train")

def get_random_prompts(dataset, num_examples=100):
    assert num_examples <= len(dataset), "Can't pick more elements than there are in the dataset."
    picks = []
    for _ in range(num_examples):
        pick = random.randint(0, len(dataset)-1)
        while pick in picks:
            pick = random.randint(0, len(dataset)-1)
        picks.append(pick)
    return(dataset[picks])


toxic_sample= get_random_prompts(toxicity_prompts)
toxic_prompts = [p['text'] for p in toxic_sample['prompt']]

# Prompting the Model
text_generation = pipeline("text-generation", model="gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")

# Feed prompts to the Model and store output as list
model_continuations=[]
for prompt in toxic_prompts:
    generation = text_generation(prompt, max_length=50, do_sample=False, pad_token_id=50256)
    continuation = generation[0]['generated_text'].replace(prompt, '')
    model_continuations.append(continuation)

print('Generated '+ str(len(model_continuations))+ ' continuations')