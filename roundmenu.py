#!/bin/python
"""
这里只处理svg,因为svg中有大段的依赖,我们无法分析,只能如此直接复制

kvconfig则是必须要分析的,不能直接引入覆盖
"""
import sys
import re

dst,opacity=sys.argv[1:]


s1=open('./KvRoughGlassRoundMenu.svg').read()
s2=open('%s.svg'%(dst,)).read()
#除了数字以外的id
ids1=re.findall('id=("[a-z\-A-Z]+?")',s1)
ids2=re.findall('id=("[a-z\-A-Z]+?")',s2)
#排除s2中没有的id,
for _id in set(ids1)-set(ids2):
    if 'menu-shadow' not in _id and '"menu-normal"' not in _id:
        s1=s1.replace(_id,_id[:-1]+'discard"')
        #同时替换ref,不替换会在console显示大量svg引用缺失错误.替换了不知道会不会造成什么影响
        s1=s1.replace('"#'+_id[1:],'"#'+_id[1:-1]+'discard"')

#去掉头尾<svg>
s1=[line for line in s1.split('\n') if '<svg' not in line and 'svg>' not in line]
#s1=s1[1:-1]
s1='\n'.join(s1)
#插入opacity,也可以加入其他样式
s1=s1.replace('replaceme1',opacity)

#去除s2中的menu-shadow
s2=s2.replace('menu-shadow','menu-noshadow')
s2=s2.replace('"menu-normal"','"menu-noshadow"')
s2=s2.split('\n')
#插入s1
s2=s2[:1]+[s1]+s2[1:]
s2='\n'.join(s2)
open('%s.svg'%(dst,),'w').write(s2)

import configparser
file_path='%s.kvconfig'%(dst,)
config = configparser.ConfigParser()
config.read(file_path)

config['%General']['menu_shadow_depth']='7'
config['%General']['spread_menuitems']='true'
with open(file_path, 'w') as configfile:
    config.write(configfile)
