import torch  # 追加
from transformers import AutoModelForCausalLM, AutoTokenizer

class ChatBotModel:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("rinna/japanese-gpt2-medium", legacy=False)
        self.model = AutoModelForCausalLM.from_pretrained("rinna/japanese-gpt2-medium")
        # GPUが利用可能ならGPUを使用し、そうでなければCPUを使用する
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def generate_response(self, user_input):
        inputs = self.tokenizer.encode(user_input, return_tensors="pt").to(self.device)
        outputs = self.model.generate(
            inputs,
            max_length=100,
            do_sample=True,
            top_p=0.85,
            top_k=50
        )
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
