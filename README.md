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

## 知识库配置
知识库目录：./Doclib/DocFiles/

知识库格式：
```
────DocFiles
    ├───0000_知识库标题1.txt
    ├───0001_知识库标题2.txt
    ├───0002_知识库标题3.txt
    ├───...
```

## 快速使用Demo
注意：本Demo只搜索知识库标题，未搜索知识库内容，可根据具体需求稍作改动。
```Shell
python client.py
```
