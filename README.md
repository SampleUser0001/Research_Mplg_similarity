# Research_Mplg_similarity

形態素解析有りと無しの類似度の比較をする。

## 比較対象文

``` txt
similarity_diff | text_01: 私はその人を常に先生と呼んでいた。だからここでもただ先生と書くだけで本名は打ち明けない。これは世間を憚かる遠慮というよりも、その方が私にとって自然だからである。私はその人の記憶を呼び起すごとに、すぐ「先生」といいたくなる。筆を執っても心持は同じ事である。よそよそしい頭文字などはとて も使う気にならない。
similarity_diff | text_02: 私はその人を常に先生と呼んでいた。だからここでもただ先生と書くだけで本名は打ち明けない。私はその人の記憶を呼び起すごとに、すぐ「先生」といいたくなる。筆を執っても心持は同じ事である。よそよそしい頭文字などはとても使う気にならない。
```

## 実行結果

``` txt 
similarity_diff | text_raito: 0.8646616541353384
similarity_diff | mplg_result_ratio: 0.4966120218579235
```

## 備考

比較方法が悪い可能性もある。  
text_01の形態素解析結果は下記なので、単語だけを抽出した場合は同値に収まる？

``` txt
similarity_diff | 私    名詞,代名詞,一般,*,*,*,私,ワタシ,ワタシ
similarity_diff | は    助詞,係助詞,*,*,*,*,は,ハ,ワ
similarity_diff | その  連体詞,*,*,*,*,*,その,ソノ,ソノ
similarity_diff | 人    名詞,一般,*,*,*,*,人,ヒト,ヒト
similarity_diff | を    助詞,格助詞,一般,*,*,*,を,ヲ,ヲ
similarity_diff | 常に  副詞,一般,*,*,*,*,常に,ツネニ,ツネニ
similarity_diff | 先生  名詞,一般,*,*,*,*,先生,センセイ,センセイ
similarity_diff | と    助詞,格助詞,一般,*,*,*,と,ト,ト
similarity_diff | 呼ん  動詞,自立,*,*,五段・バ行,連用タ接続,呼ぶ,ヨン,ヨン
similarity_diff | で    助詞,接続助詞,*,*,*,*,で,デ,デ
similarity_diff | い    動詞,非自立,*,*,一段,連用形,いる,イ,イ
similarity_diff | た    助動詞,*,*,*,特殊・タ,基本形,た,タ,タ
similarity_diff | 。    記号,句点,*,*,*,*,。,。,。
similarity_diff | だから        接続詞,*,*,*,*,*,だから,ダカラ,ダカラ
similarity_diff | ここ  名詞,代名詞,一般,*,*,*,ここ,ココ,ココ
similarity_diff | でも  助詞,副助詞,*,*,*,*,でも,デモ,デモ
similarity_diff | ただ  接続詞,*,*,*,*,*,ただ,タダ,タダ
similarity_diff | 先生  名詞,一般,*,*,*,*,先生,センセイ,センセイ
similarity_diff | と    助詞,格助詞,引用,*,*,*,と,ト,ト
similarity_diff | 書く  動詞,自立,*,*,五段・カ行イ音便,基本形,書く,カク,カク
similarity_diff | だけ  助詞,副助詞,*,*,*,*,だけ,ダケ,ダケ
similarity_diff | で    助詞,格助詞,一般,*,*,*,で,デ,デ
similarity_diff | 本名  名詞,一般,*,*,*,*,本名,ホンミョウ,ホンミョー
similarity_diff | は    助詞,係助詞,*,*,*,*,は,ハ,ワ
similarity_diff | 打ち明け      動詞,自立,*,*,一段,未然形,打ち明ける,ウチアケ,ウチアケ
similarity_diff | ない  助動詞,*,*,*,特殊・ナイ,基本形,ない,ナイ,ナイ
similarity_diff | 。    記号,句点,*,*,*,*,。,。,。
similarity_diff | これ  名詞,代名詞,一般,*,*,*,これ,コレ,コレ
similarity_diff | は    助詞,係助詞,*,*,*,*,は,ハ,ワ
similarity_diff | 世間  名詞,一般,*,*,*,*,世間,セケン,セケン
similarity_diff | を    助詞,格助詞,一般,*,*,*,を,ヲ,ヲ
similarity_diff | 憚    名詞,一般,*,*,*,*,*
similarity_diff | かる  動詞,自立,*,*,五段・ラ行,基本形,かる,カル,カル
similarity_diff | 遠慮  名詞,サ変接続,*,*,*,*,遠慮,エンリョ,エンリョ
similarity_diff | と    助詞,格助詞,引用,*,*,*,と,ト,ト
similarity_diff | いう  動詞,自立,*,*,五段・ワ行促音便,基本形,いう,イウ,イウ
similarity_diff | より  助詞,格助詞,一般,*,*,*,より,ヨリ,ヨリ
similarity_diff | も    助詞,係助詞,*,*,*,*,も,モ,モ
similarity_diff | 、    記号,読点,*,*,*,*,、,、,、
similarity_diff | その  連体詞,*,*,*,*,*,その,ソノ,ソノ
similarity_diff | 方    名詞,非自立,一般,*,*,*,方,ホウ,ホー
similarity_diff | が    助詞,格助詞,一般,*,*,*,が,ガ,ガ
similarity_diff | 私    名詞,代名詞,一般,*,*,*,私,ワタシ,ワタシ
similarity_diff | にとって      助詞,格助詞,連語,*,*,*,にとって,ニトッテ,ニトッテ
similarity_diff | 自然  名詞,形容動詞語幹,*,*,*,*,自然,シゼン,シゼン
similarity_diff | だ    助動詞,*,*,*,特殊・ダ,基本形,だ,ダ,ダ
similarity_diff | から  助詞,接続助詞,*,*,*,*,から,カラ,カラ
similarity_diff | で    助動詞,*,*,*,特殊・ダ,連用形,だ,デ,デ
similarity_diff | ある  助動詞,*,*,*,五段・ラ行アル,基本形,ある,アル,アル
similarity_diff | 。    記号,句点,*,*,*,*,。,。,。
similarity_diff | 私    名詞,代名詞,一般,*,*,*,私,ワタシ,ワタシ
similarity_diff | は    助詞,係助詞,*,*,*,*,は,ハ,ワ
similarity_diff | その  連体詞,*,*,*,*,*,その,ソノ,ソノ
similarity_diff | 人    名詞,一般,*,*,*,*,人,ヒト,ヒト
similarity_diff | の    助詞,連体化,*,*,*,*,の,ノ,ノ
similarity_diff | 記憶  名詞,サ変接続,*,*,*,*,記憶,キオク,キオク
similarity_diff | を    助詞,格助詞,一般,*,*,*,を,ヲ,ヲ
similarity_diff | 呼び  動詞,自立,*,*,五段・バ行,連用形,呼ぶ,ヨビ,ヨビ
similarity_diff | 起す  動詞,自立,*,*,五段・サ行,基本形,起す,オコス,オコス
similarity_diff | ごと  名詞,非自立,副詞可能,*,*,*,ごと,ゴト,ゴト
similarity_diff | に    助詞,格助詞,一般,*,*,*,に,ニ,ニ
similarity_diff | 、    記号,読点,*,*,*,*,、,、,、
similarity_diff | すぐ  副詞,助詞類接続,*,*,*,*,すぐ,スグ,スグ
similarity_diff | 「    記号,括弧開,*,*,*,*,「,「,「
similarity_diff | 先生  名詞,一般,*,*,*,*,先生,センセイ,センセイ
similarity_diff | 」    記号,括弧閉,*,*,*,*,」,」,」
similarity_diff | と    助詞,格助詞,引用,*,*,*,と,ト,ト
similarity_diff | いい  動詞,自立,*,*,五段・ワ行促音便,連用形,いう,イイ,イイ
similarity_diff | たく  助動詞,*,*,*,特殊・タイ,連用テ接続,たい,タク,タク
similarity_diff | なる  動詞,自立,*,*,五段・ラ行,基本形,なる,ナル,ナル
similarity_diff | 。    記号,句点,*,*,*,*,。,。,。
similarity_diff | 筆    名詞,一般,*,*,*,*,筆,フデ,フデ
similarity_diff | を    助詞,格助詞,一般,*,*,*,を,ヲ,ヲ
similarity_diff | 執っ  動詞,自立,*,*,五段・ラ行,連用タ接続,執る,トッ,トッ
similarity_diff | て    助詞,接続助詞,*,*,*,*,て,テ,テ
similarity_diff | も    助詞,係助詞,*,*,*,*,も,モ,モ
similarity_diff | 心持  名詞,一般,*,*,*,*,心持,ココロモチ,ココロモチ
similarity_diff | は    助詞,係助詞,*,*,*,*,は,ハ,ワ
similarity_diff | 同じ  連体詞,*,*,*,*,*,同じ,オナジ,オナジ
similarity_diff | 事    名詞,非自立,一般,*,*,*,事,コト,コト
similarity_diff | で    助動詞,*,*,*,特殊・ダ,連用形,だ,デ,デ
similarity_diff | ある  助動詞,*,*,*,五段・ラ行アル,基本形,ある,アル,アル
similarity_diff | 。    記号,句点,*,*,*,*,。,。,。
similarity_diff | よそよそしい  形容詞,自立,*,*,形容詞・イ段,基本形,よそよそしい,ヨソヨソシイ,ヨソヨソシイ
similarity_diff | 頭文字        名詞,一般,*,*,*,*,頭文字,カシラモジ,カシラモジ
similarity_diff | など  助詞,副助詞,*,*,*,*,など,ナド,ナド
similarity_diff | は    助詞,係助詞,*,*,*,*,は,ハ,ワ
similarity_diff | とても        副詞,助詞類接続,*,*,*,*,とても,トテモ,トテモ
similarity_diff | 使う  動詞,自立,*,*,五段・ワ行促音便,基本形,使う,ツカウ,ツカウ
similarity_diff | 気    名詞,非自立,一般,*,*,*,気,キ,キ
similarity_diff | に    助詞,格助詞,一般,*,*,*,に,ニ,ニ
similarity_diff | なら  動詞,自立,*,*,五段・ラ行,未然形,なる,ナラ,ナラ
similarity_diff | ない  助動詞,*,*,*,特殊・ナイ,基本形,ない,ナイ,ナイ
similarity_diff | 。    記号,句点,*,*,*,*,。,。,。
similarity_diff | EOS
```