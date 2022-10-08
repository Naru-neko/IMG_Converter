# ディレクトリ内の特定の拡張子の画像ファイルの拡張子を一斉変更する
# 元の画像ファイルは削除

from PIL import Image, ImageTk
import os
import glob



#dir_path = 'D:/image/anime_thumbs_test' # 対象のディレクトリへのパス
dir_path = input('対象のディレクトリのパスを入力：\n')

raw_extention = input('変換対象の拡張子を入力（例：.png）：\n')

conved_extension = input('変換後の拡張子を入力（例：.jpg）：\n')


files = glob.glob(dir_path + '/*') # ディレクトリ内のファイルパス一覧リストを取得

try:
    for file in files:
        file = file.replace('\\', '/') # パスの区切り文字を置換
        file_name = os.path.basename(file).split('.', 1)[0] # 拡張子を除いたファイル名
        print(file_name)
        current_extension = '.' + os.path.basename(file).split('.', 1)[1]
        if current_extension == raw_extention: #対象の拡張子であれば
            saves = dir_path + '/' + file_name + conved_extension
            img = Image.open(file).convert('RGB')
            img.save(saves)
            os.remove(file) # 元ファイルを削除
            print(saves + 'を保存しました')
except:
    print('ERROR：' + saves + 'を保存できませんでした')
