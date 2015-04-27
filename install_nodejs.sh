#!/bin/bash

echo "Linux下NodeJS安装"
echo "需要ROOT权限安装"
sudo sh -c 'echo "获取ROOT权限!"' 

echo "获取最新版本..."
{
wget --output-document=node-updater.html https://nodejs.org/dist/latest/

ARCH=$(uname -m)

if [ $ARCH = x86_64 ]
then
	grep -o '>node-v.*-linux-x64.tar.gz' node-updater.html > node-cache.txt 2>&1

	VER=$(grep -o 'node-v.*-linux-x64.tar.gz' node-cache.txt)
else
	grep -o '>node-v.*-linux-x86.tar.gz' node-updater.html > node-cache.txt 2>&1
	
	VER=$(grep -o 'node-v.*-linux-x86.tar.gz' node-cache.txt)
fi
rm ./node-cache.txt
rm ./node-updater.html
} &> /dev/null

echo "结束"

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

echo "Downloading latest stable Version $VER..."
{
wget https://nodejs.org/dist/latest/$VER
} &> /dev/null

echo "结束"

echo "正在安装..."
cd /usr/local && sudo tar --strip-components 1 -xzf $DIR/$VER

rm $DIR/$VER

echo "安装完成!"
