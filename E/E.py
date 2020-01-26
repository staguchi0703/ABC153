# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\E\E_input.txt', 'r', encoding="utf-8")
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
H, N = [int(item) for item in input().split()]
magic_list = [[int(item) for item in input().split()] for _ in range(N)]
# print('E', magic_list)

new_list = []
for a, m in magic_list:
    new_list.append([a, m, a/m])

new_list.sort(key=lambda x:x[2], reverse=True)
# print(new_list)

dp = [[1 if j == 0 else 0 for j in range(H+1)] for _ in range(N+1)]

for i in range(N):
    for j in range(H+1):
        if magic_list[i][0] + j > H:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j+magic_list[i][0]] = dp[i+1][j] + magic_list[i][1]

print(max(dp[N]))




