# -离线GLM知识库问答-
无需langchain，单卡即可运行的全离线模型

## 环境配置
进入命令行，执行以下命令：
```Shell
pip install -r requirements.txt
pip install -U sentence-transformers
```

## 模型下载
通过网盘下载GLM6B离线模型和语义搜索模型：
* GLM6B离线模型：链接：https://pan.baidu.com/s/1avLpfjI50B-SHpibj2IijA 提取码：gr25 
* text2vec离线模型：链接：https://pan.baidu.com/s/1L99LQmJwmvcGs9FZ7LbyyQ 提取码：5dhi 

将模型放在如下目录：
```
────workspace
    ├───GLM6B_model
    ├───text2vec
    ├───Chat_simple
    ├───Doclib
    ├───GLM.py
    ├───...
    └───requirements.txt
```

## 快速使用Demo
```Shell
python client.py
```
