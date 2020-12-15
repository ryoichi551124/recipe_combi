import numpy as np
import pandas as pd
import random


main = pd.read_csv('rakuten_main.csv')
sub = pd.read_csv('rakuten_sub.csv')
soup = pd.read_csv('rakuten_soup.csv')

#基本の空のデータ
combi =pd.read_csv('combi.csv', index_col=0)
#トータル(train)データの初期化
combis = combi.copy(deep=True)


def choice(main_num, sub_num, soup_num, judge):
    global combi, combis

    main_num = main_num
    sub_num = sub_num
    soup_num = soup_num

    combi['主菜'] = main['recipeTitle'][main_num]
    combi['副菜'] = sub['recipeTitle'][sub_num]
    combi['汁物'] = soup['recipeTitle'][soup_num]
    combi['主菜ID'] = main['recipeId'][main_num]

    for material in all_list:
        if material in main['recipeMaterial'][main_num]:
            combi[material] += 1
        if material in sub['recipeMaterial'][sub_num]:
            combi[material] += 1
        if material in soup['recipeMaterial'][soup_num]:
            combi[material] += 1

    print('main', main['recipeMaterial'][main_num])
    print('sub', sub['recipeMaterial'][sub_num])
    print('soup', soup['recipeMaterial'][soup_num])

    if judge:
        combi['採用/不採用'] = 1

    combis = pd.concat([combis, combi])
    #基本の空のデータをID以外初期化
    combi['ID'] += 1
    combi.iloc[0, 1:] = 0
    combis.to_csv('train.csv', index=False)

def random_choice():
    main_num = random.randint(0, len(main))
    sub_num = random.randint(0, len(sub))
    soup_num = random.randint(0, len(soup))

    recipe = {
    'main_image': main['mediumImageUrl'][main_num],
    'sub_image': sub['mediumImageUrl'][sub_num],
    'soup_image': soup['mediumImageUrl'][soup_num],
    'main_name': main['recipeTitle'][main_num],
    'sub_name': sub['recipeTitle'][sub_num],
    'soup_name': soup['recipeTitle'][soup_num],
    }
    return recipe, main_num, sub_num, soup_num

def judge():
    combi['採用/不採用'] = 1




#カテゴリーリストの作成
vegetables = ['里芋', '玉ねぎ', '大根', '人参', 'レタス', '白菜', 'ミニトマト', 'ねぎ', 'にんにく', 'キャベツ',
              'じゃがいも', 'グリーンピース', 'ほうれん草', 'しょうが', 'パセリ', 'しめじ', '白菜', 'ごぼう',
              'もやし', 'エノキ', '春菊', 'コーン', '水菜', '柚子', 'きゅうり', 'トマト', 'ブロッコリー',
              'ピーマン', 'ちんげん菜', 'ナス', '菊芋', 'かぼちゃ', '山芋', 'アスパラ' ,'パプリカ', 'バジル',
              'マッシュルーム', '大葉', 'れんこん', '椎茸', 'にら', '三つ葉', 'さつまいも', 'カリフラワー',
              'タケノコ', '枝豆', 'アボカド', '小松菜', 'かぶ', 'カリフラワー', 'セロリ', '高菜', 'エリンギ',
              'えのき', '銀杏']

meats = ['ひき肉', '鶏', '豚', 'ローストビーフ', '手羽', '牛',
         'ハム', 'ベーコン', 'ウインナー', 'ささみ', 'もつ', 'スパム']

fishes = ['ぶり', '牡蠣', 'ツナ', '鱈', 'エビ', 'サーモン', '鮭', '数の子', 'まぐろ', '鯛', 'いくら',
          'いわし', 'サバ', 'アジ', 'さんま', '干物', '白身魚', 'タコ', 'ホタテ', 'サザエ', 'じゃこ', 'あさり', 'シーフード',
          'あんこう', 'カジカ', 'イカ']

seasoning = ['片栗粉', '醤油', '砂糖', 'みりん', '酢', '揚げ油', '卵', '塩', '胡椒', 'パン粉', 'マヨネーズ', '味噌',
             'ナツメグ', 'コーヒーフレッシュ', '酒', 'ごま', 'だし', '麺つゆ', 'カレールー', 'ローリエ', 'オリーブ',
             '赤ワイン', '蜂蜜', 'コンソメ', 'バター', 'チリパウダー', 'カレー粉', 'コチュジャン', 'ごま油', 'オイスターソース',
             '鶏がらスープ', 'ソース', '鰹節', '小麦粉', 'ワイン', 'コンソメ', '生クリーム', '粉チーズ',
             '酒粕', 'かつおぶし', '唐辛子', 'ケチャップ', '豆板醤', 'ナンプラー', 'マーガリン', 'デミグラスソース',
             'クミン', 'ターメリック', 'ガラムマサラ', 'ポン酢']

noodles = ['蕎麦', 'うどん', '中華麺', 'パスタ', 'ニョッキ　', 'そうめん']

others = ['油揚げ', '卵', 'カニカマ', '牛乳', 'パスタ', '明太子', '冷凍餃子', 'こんにゃく', '豆腐',
          '葛きり', '蒲鉾', '餅', '梅干し', 'わかめ', '昆布', 'ヨーグルト', '春雨', 'たらこ', 'チーズ', 'ミートソース',
          'しらたき', '納豆', 'キムチ', '海苔', 'おから', 'パン', 'レモン']

all_list = vegetables + meats + fishes + seasoning + noodles + others