from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "facebook/blenderbot-400M-distill"

# Load model (download on first run and reference local installation for consequent runs)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name) # optimizes the input


conversation_history = []

history_string = "\n".join(conversation_history)

input_text = "hello, how are you doing?"

inputs = tokenizer.encode_plus(history_string, input_text, return_tensors="pt")

print(inputs)
""" {'input_ids': tensor([[1710,   86,   19,  544,  366,  304,  929,   38]]), 'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1, 1]])} """

outputs = model.generate(**inputs)
print(outputs)
""" tensor([[   1,  281,  476,  929,  731,   21,  281,  632,  929,  712,  731,   21,
          855,  366,  304,   38,  946,  304,  360,  463, 5459, 7930,   38,    2]]) """
   
   
response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
print(response)
       
""" I'm doing well. I am doing very well. How are you? Do you have any hobbies? """

conversation_history.append(input_text)
conversation_history.append(response)
print(conversation_history)