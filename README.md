# bilibili-download
b站视频下载

## 环境 env
 - python3.7+
 - ffmpeg

## 使用方法 quick start
```python
from bilibili_downloader import Bilibili

b = Bilibili(save_dir='./downloads')
b.set_cookies('')  # 若是尊贵的大会员，填上cookies可以获取更高画质
b.get_video(88736972)  # av88736972 这个数字
```

## 开发日志
#### 2020-03-01
 - bilibili_downloader搞定
 - 脑子一热甚至想写个GUI，选了轻量的tkinter。搞了几十分钟，觉得这布局方式太难顶，越写越觉得索然无味。于是心中想着：”罢辽罢辽，还是用console吧“。所以bilibili_gui.py是个未完成的东西。

## 声明
 - **此工具仅供学习使用，请保护视频的知识产权。**
