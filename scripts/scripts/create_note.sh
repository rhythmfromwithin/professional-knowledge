#!/bin/bash
# 用法: ./scripts/create-note.sh "文件名" engineering
FILE=$1
CATEGORY=$2

if [ -f "inbox/$FILE" ]; then
    # 简单的复制并重命名示例，实际可结合模板填充
    cp "inbox/$FILE" "notes/$CATEGORY/$FILE"
    echo "Note created: notes/$CATEGORY/$FILE"
else
    echo "File not found in inbox."
fi