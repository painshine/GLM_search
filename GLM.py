# GPU 1
# Prompt
import os
from transformers import AutoTokenizer, AutoModel

# Select GPU
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

# Load Model
tokenizer = AutoTokenizer.from_pretrained("./GLM6B_model/", trust_remote_code=True)
model = AutoModel.from_pretrained("./GLM6B_model/", trust_remote_code=True).half().cuda()
model = model.eval()

# response
def GLMresp(content,question):
    #prompt_template = f"""用户不知道文档资料，将文档资料的详细内容转述给用户，以此回答用户问题。
    #    回答内容不允许编造文档资料内不存在的内容。回答内容只涉及移动云的云空间。
    #    如果用户的问题与文档资料不相关，请回答“抱歉，我无法回答您的问题。”。另外，答案请使用中文。
    #    文档资料:
    #    {content}
    #    用户问题:
    #    {question}"""
    
    prompt_template = f"""基于以下已知信息，简洁和专业的来回答移动云的云空间产品用户的问题。
    如果无法从中得到答案，请说 "根据已知信息无法回答该问题" 或 "没有提供足够的相关信息"，不允许在答案中添加编造成分，答案请使用中文。
    
    已知内容:
    {content}
    
    问题:
    {question}"""
    
    response, history = model.chat(tokenizer, prompt_template, history=[])
    return response