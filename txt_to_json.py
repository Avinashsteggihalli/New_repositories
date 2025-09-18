import json

input_file = 'ecommerce_qa.txt'
output_file = 'sample_finetune_data2.jsonl'
system_prompt = "You are an e-commerce assistant with expertise in Amazon, Flipkart, and Ajio."

data = []
with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')
    qa_pairs = []
    q, a = None, None
    for line in lines:
        if line.startswith('Q:'):
            q = line[2:].strip()
        elif line.startswith('A:'):
            a = line[2:].strip()
        elif line.strip() == '' and q and a:
            qa_pairs.append((q, a))
            q, a = None, None
    if q and a:
        qa_pairs.append((q, a))

with open(output_file, 'w', encoding='utf-8') as f:
    for q, a in qa_pairs:
        obj = {
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": q},
                {"role": "assistant", "content": a}
            ]
        }
        f.write(json.dumps(obj, ensure_ascii=False) + '\n')

print("Conversion complete. Check sample_finetune_data.jsonl")