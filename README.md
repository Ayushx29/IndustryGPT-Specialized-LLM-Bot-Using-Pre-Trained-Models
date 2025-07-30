# IndustryGPT-Specialized LLM Bot Using Pre Trained Models


A capstone project that demonstrates how to fine-tune a pre-trained Large Language Model (LLM) for a specific industry — in this case, **Finance** — using QLoRA and PEFT (Parameter-Efficient Fine-Tuning). The final product is a lightweight, finance-savvy chatbot that runs efficiently on limited hardware and can be deployed as a real-time API.

---

## 🚀 Project Highlights

- ✅ Fine-tuning **TinyLlama-1.1B-Chat-v1.0** using **domain-specific financial datasets**
- ✅ Used **QLoRA + LoRA** for efficient, low-resource training
- ✅ Built a custom instruction-response formatting pipeline
- ✅ Integrated a **Flask-based API** with **ngrok** for live chatbot demo
- ✅ Published the trained model to **Hugging Face Hub**
- ✅ Ideal for finance Q&A, support bots, and internal assistants


---

## 📊 Dataset Sources

- [finance-alpaca-1k-test](https://huggingface.co/datasets/poornima9348/finance-alpaca-1k-test)
- [alpaca_finance_en](https://huggingface.co/datasets/ssbuild/alpaca_finance_en)

---

## 🛠️ Tech Stack

- `transformers` (Hugging Face)
- `datasets`
- `peft` + `trl` (for QLoRA training)
- `Flask` + `ngrok` (for deployment)
- `Kaggle Notebooks` (training environment)
- `Hugging Face Hub` (model hosting)

---

## 🧪 Model Testing

Once trained and saved, test your chatbot using:

```python
from transformers import pipeline

pipe = pipeline("text-generation", model="Ayushx29/finance_finetune_model")
prompt = "Explain the concept of compound interest."
result = pipe(f"<s>[INST] {prompt} [/INST]")
print(result[0]['generated_text'])

```
---

## 🧾 Model on Hugging Face
👉 Ayushx29/finance_finetune_model

---
## 🧪 TensorBoard Monitoring (Optional)
```python
%load_ext tensorboard
%tensorboard --logdir results/runs
```
---
## 🧠 Final Thoughts

This project illustrates how open-source LLMs can be repurposed into industry-specific experts using lightweight, efficient techniques.
By focusing on a structured training pipeline, realistic datasets, and deployment readiness, IndustryGPT proves that custom AI assistants are within reach, even without massive hardware or enterprise budgets.
---

## 👨‍💻 Author
Ayush Bhagat

Capstone Project – Deep Learning for NLP | AlmaBetter



