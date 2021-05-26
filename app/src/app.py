# -*- coding: utf-8 -*-
import MeCab
from difflib import SequenceMatcher 

# 辞書ファイルパス
DIC_PATH = ' -d /usr/local/mecab/lib/mecab/dic/mecab-ipadic-neologd'

if __name__ == '__main__':
  mplg_parser = MeCab.Tagger(DIC_PATH)
  
  text_01 = '私はその人を常に先生と呼んでいた。だからここでもただ先生と書くだけで本名は打ち明けない。これは世間を憚かる遠慮というよりも、その方が私にとって自然だからである。私はその人の記憶を呼び起すごとに、すぐ「先生」といいたくなる。筆を執っても心持は同じ事である。よそよそしい頭文字などはとても使う気にならない。'
  mplg_result_01 = mplg_parser.parse(text_01)

  text_02 = '私はその人を常に先生と呼んでいた。だからここでもただ先生と書くだけで本名は打ち明けない。私はその人の記憶を呼び起すごとに、すぐ「先生」といいたくなる。筆を執っても心持は同じ事である。よそよそしい頭文字などはとても使う気にならない。'
  mplg_result_02 = mplg_parser.parse(text_02)

  # 類似度取得
  text_ratio = SequenceMatcher(None, text_01, text_02).ratio()
  mplg_result_ratio = SequenceMatcher(None, mplg_result_01, mplg_result_02).ratio()
  
  print("text_01: {}".format(text_01))
  print("text_02: {}".format(text_02))
  
  print("text_raito: {}".format(text_ratio))
  print("mplg_result_ratio: {}".format(mplg_result_ratio))
