#!/bin/bash
cd "$(dirname "$(realpath "$0")")"

NAME=KvArcDolphin
CONFIGNAME=$NAME.kvconfig
SVGNAME=$NAME.svg 
cp /usr/share/Kvantum/KvArc/KvArc.kvconfig $CONFIGNAME

#双击
kwriteconfig5 --file $CONFIGNAME --group %General --key click_behavior 2
kwriteconfig5 --file $CONFIGNAME --group %General --key translucent_windows true
kwriteconfig5 --file $CONFIGNAME --group %General --key blurring true

kwriteconfig5 --file $CONFIGNAME --group Hacks --key transparent_dolphin_view true

#Toolbar部分
kwriteconfig5 --file $CONFIGNAME --group Toolbar --key interior.element rect
#frame上开一个botton,作为阴影,来自Lenny
kwriteconfig5 --file $CONFIGNAME --group Toolbar --key frame.element rect
kwriteconfig5 --file $CONFIGNAME --group Toolbar --key frame true
kwriteconfig5 --file $CONFIGNAME --group Toolbar --key frame.left 0
kwriteconfig5 --file $CONFIGNAME --group Toolbar --key frame.right 0
kwriteconfig5 --file $CONFIGNAME --group Toolbar --key frame.top 0
kwriteconfig5 --file $CONFIGNAME --group Toolbar --key frame.bottom 4

#删除尾部的</svg>
sed '$d' /usr/share/Kvantum/KvArc/KvArc.svg > $SVGNAME
cat patch.svg >> $SVGNAME

#python roundmenu.py $SVGNAME "opacity:0.3;fill:#ffffff;"
python roundmenu.py $NAME "opacity:0.3;fill:#ffffff;"    
