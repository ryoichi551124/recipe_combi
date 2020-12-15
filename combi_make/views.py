from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
import random
from . import method
import pandas as pd


main = pd.read_csv('rakuten_main.csv')
sub = pd.read_csv('rakuten_sub.csv')
soup = pd.read_csv('rakuten_soup.csv')

#基本の空のデータ
combi =pd.read_csv('combi.csv', index_col=0)
#トータル(train)データの初期化
combis = combi.copy(deep=True)

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
judge = False


def index(request):
    params = recipe
    return render(request, 'combi_make/index.html', params)

def ok(request):
    global main_num, sub_num, soup_num, judge

    judge = True
    method.choice(main_num, sub_num, soup_num, judge)
#    method.judge()
    params, main, sub, soup = method.random_choice()
    main_num = main
    sub_num = sub
    soup_num = soup
    return render(request, 'combi_make/index.html', params)

def no(request):
    global main_num, sub_num, soup_num, judge

    judge = False
    method.choice(main_num, sub_num, soup_num, judge)
    params, main, sub, soup = method.random_choice()
    main_num = main
    sub_num = sub
    soup_num = soup
    return render(request, 'combi_make/index.html', params)


def download(request):
    train = pd.read_csv('train.csv')
    train.drop(0, inplace=True)
    train.to_csv('train.csv')
    response = HttpResponse(open("train.csv", 'rb').read()) 
    response['Content-Type'] = 'text/csv' 
    response['Content-Disposition'] = 'attachment; filename=train.csv' 
    return response 