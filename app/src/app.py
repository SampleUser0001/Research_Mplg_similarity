# -*- coding: utf-8 -*-
import MeCab

# 辞書ファイルパス
DIC_PATH = ' -d /usr/local/mecab/lib/mecab/dic/mecab-ipadic-neologd'

if __name__ == '__main__':
  sample_text = '国境の長いトンネルを抜けると雪国であった。'
  print(MeCab.Tagger(DIC_PATH).parse(sample_text))
