from transformers import AutoTokenizer, AutoModel

def easychat(model_path):
    
    print('\033[4;32m正在加载模型，请稍后...\033[0m')
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    model = AutoModel.from_pretrained(model_path, trust_remote_code=True).half().cuda()
    model = model.eval()

    print('\033[4;32m模型加载完毕！\033[0m')

    print('\033[4;32m开始对话，请输入：\033[0m')
    print(' ')
    
    talk = input('我: ')
    while True:
        
        if talk == '再见':
            print('\033[1;36mGLM_6B: 欢迎下次使用\033[0m')
            print('  ')
            print('\033[4;32m已结束对话。\033[0m')
            break
        
        try:
        
            _talk = talk.split(': ')[-1]
            response, history = model.chat(tokenizer, _talk, history=[])

            print('\033[1;36mGLM_6B: ' + response + '\033[0m')
            print(' ')

            talk = input('我: ')
            
        except:
            print('\033[1;36mGLM_6B: 我无法回答，请重新描述你的问题。\033[0m')
            print(' ')

            talk = input('我: ')
