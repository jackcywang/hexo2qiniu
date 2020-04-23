>我的博客文章里的图片和博客放在一起,图片太多后占的内存也会越来越大，所以就想找个图床放图片，我选择的图床是七牛云，使用网页版的上传过，但由于的图片是不同我文件夹存放的，上传不方便，后来查找到七牛云开发者里支持本地上传，于是折腾了下，最后顺利的实现本地批量上传。

hexo2qiniu.py的功能是将本地博客中的图片批量上传到七牛云镜像中，并返回图片的外链(即图片链接)，然后将该该外链替换博客中的本地链接。这里你需要注册七牛云的存储服务,创建一个bucket,里面就是上传文件的目的地。
图一是原图
![](https://github.com/jackcywang/hexo2qiniu/blob/master/images/old.png)
图二是替换后的图
![](https://github.com/jackcywang/hexo2qiniu/blob/master/images/new.png)
图三是你七牛云上传的结果
![](https://github.com/jackcywang/hexo2qiniu/blob/master/images/qiniu.png)

话不多说.现在开始操作.**以防万一，一定要备份**

* md文件和图片存放形式(如果md文件不包含图片也没问题)
<div align=left>
<img src=https://github.com/jackcywang/hexo2qiniu/blob/master/images/cunfang.png>
</div>

* 安装依赖
```
pip install qiniu
```

* 上传和替换
```
python3 hexo2qiniu.py
```
