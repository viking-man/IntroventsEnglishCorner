## [English Doc](english_doc.md)
# IntroventsEnglishCorner
A spoken English education chatbot based on ChatGPT/whsiper and qTTS.

# 社恐人士的英语角
#### 程序采用flask框架，数据库用了sqlite来存储音频文件，音频->文本使用openai的开源whsiper，文本->音频使用qTTS，聊天对话使用chatGPT的官方API。所以使用本项目需要有chatgpt账号的api授权。  

  
#### 介绍视频：https://www.bilibili.com/video/BV15w411m75j/?vd_source=7dc010c6db2003327fcc3177974e71f7

## 基本流程
->前端读取音频信息  
->flask服务端  
->whsiper转化成文本  
->请求openai的ChatCompetition接口  
->返回文本通过qtts转化成音频文件，数据落库，返回音频响应  
->前端直接播放音频文件

## 使用流程  
python版本需要为3.10  

1. 下载程序
```
git clone https://github.com/viking-man/IntroventsEnglishCorner.git
cd IntroventsEnglishCorner
```
2. 初始化项目虚拟环境  
```
  python -m venv venv
  . venv/bin/activate
```

windows用户在使用`python -m venv venv`创建虚拟环境后，通过命令`cd venv/Scripts/`到Scripts目录，直接使用activate命令激活创建的虚拟环境
3. 安装对应python包

   `pip install -r requirements.txt`
4. 初始化对应数据库
   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```
5. 运行启动
   

   `flask run`

6. 网页打开环境运行地址
   

   `127.0.0.1:5000`

## 注意事项
1. .flaskenv中的OPENAI_API_KEY需要换成你自己的openai_api_key
2. whsiper第一次使用会默认下载small的模型，大概500M，需要等待；如果觉得转换效果不好，可以到WhisperModel.py文件中将small换成medium或者large


