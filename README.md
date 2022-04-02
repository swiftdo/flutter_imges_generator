# 生成 flutter 结构的图片

做重复的工作是很烦人的。

```
Do not repeat yourself!
```

本工具直接将 3x 图生成到 assets 目录中，

assets 目录中包含 1x，2x, 3x 的图片，已帮你做好按 flutter 标准目录归类。

## 使用

拉取项目：

```py
git clone https://github.com/swiftdo/flutter_imges_generator.git
```

**直接将你要生成的图片放入到该项目里面。**

然后执行：

```sh
$ python3 -m venv .venv 
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ python resize.py
```


执行完成后，会生成如下目录：

```
$ tree .
.
├── README.md
├── add_success.png
├── address_check_def.png
├── assets
│   ├── 2x
│   │   ├── add_success.png
│   │   └── address_check_def.png
│   ├── 3x
│   │   ├── add_success.png
│   │   └── address_check_def.png
│   ├── add_success.png
│   └── address_check_def.png
├── requirements.txt
└── resize.py
```

**assets** 目录就是你要的文件。当然为了更小的资源，可以用工具 [ImageOptim](https://imageoptim.com/mac) 批量压缩