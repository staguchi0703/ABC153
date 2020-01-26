# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\D\D_input.txt', 'r', encoding="utf-8")
# inputをフルパスで指定
# win10でファイルを作るとs-jisで保存されるため、読み込みをutf-8へエンコードする必要あり
# VScodeでinput file開くとutf8になってるんだけど中身は結局s-jisになっているらしい
sys.stdin=f

#
# 入力スニペット
# num = int(input())
# num_list = [int(item) for item in input().split()]
# num_list = [input() for _ in range(3)]
##################################
# %%
# 以下ペースト可
import heapq as hp

N = int(input())
a = []
hp.heappush(a, -N)

cnt = 0

while len(a) > 0:
    temp = hp.heappop(a)

    if -temp ==  1:
        pass
    else:
        hp.heappush(a, -1 *int(-1* temp/2))
        hp.heappush(a, -1 *int(-1* temp/2))
    
    cnt += 1

print(cnt)

