# -*- coding: utf-8 -*-
# flake8: noqa

from qiniu import Auth, put_file, etag
import qiniu.config
import os
import os.path as osp

#需要填写你的 Access Key 和 Secret Key
access_key = 
secret_key = 

#构建鉴权对象
q = Auth(access_key, secret_key)

website = "http://cdn.wangng.com/"

#要上传的空间
bucket_name = 'jaywnag'

def get_md_files(rootpath):
    """
    Args: 
        rootpath: md文件的根目录
    Return:
        所有md文件的一个list集合
    """
    mdlist = []
    for root, parent, files in os.walk(rootpath):
        for md in files:
            if md.endswith('.md'):
                mdpath = osp.join(root,md)
                mdlist.append(mdpath)
    return mdlist

def read_md(filepath):
    """
    Args:
        filepath:   .md文件路径
    
    Return:
        md文件读取的每一行
    """
    with open(filepath,'r', encoding='UTF-8') as fr:
        data = fr.read()
    lines = data.split('\n')
    return lines

if __name__ == "__main__":
    rootpath = './'
    mdlist = get_md_files(rootpath)
    for mdfile in mdlist:
        print(mdfile)
        lines = read_md(mdfile)
        local_root = mdfile.split('\\')[0]
        with open(mdfile,'w', encoding='UTF-8') as fw:
            for line in lines:
                if "![" in line:
                    old_url = line.split('(')[-1][:-1]
                    localfile = osp.join(local_root,old_url)
                    key = local_root.split('/')[-1]+'/'+old_url
                    token = q.upload_token(bucket_name, key, 3600)
                    ret, info = put_file(token, key, localfile)
                    assert ret['key'] == key
                    assert ret['hash'] == etag(localfile)

                    new_urls = website + key

                    line = line.replace(old_url,new_urls)
                new_line = line + '\n'
                fw.write(new_line)
        
            

            
        
                    
                    

            







# #上传后保存的文件名
# key = 'hexo为博客创建唯一链接/abbrlink.png'

# #生成上传 Token，可以指定过期时间等
# token = q.upload_token(bucket_name, key, 3600)

# #要上传文件的本地路径
# localfile = './md/hexo为博客创建唯一链接/abbrlink.png'

# ret, info = put_file(token, key, localfile)
# print(info)
# assert ret['key'] == key
# assert ret['hash'] == etag(localfile)

# urls = "http://cdn.wangng.com/"+key

# with open("./md/hexo为博客创建唯一链接.md",'r', encoding='UTF-8') as fr:
#     data = fr.read()
# lines = data.split('\n')
# with open("./md/hexo为博客创建唯一链接.md",'w',encoding='UTF-8') as fw:
#     for line in lines:
#         if '![]' in line:
#             old = line.split('(')[-1][:-1]
#             line = line.replace(old,urls)
#         newline = line + '\n'
#         fw.write(newline)
