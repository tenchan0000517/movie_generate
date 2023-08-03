## movie_generate

movie_generateは複数の動画ファイルをランダムに結合して新しい動画を生成するPythonスクリプトです。このスクリプトはFFmpegを使用して動画の結合と再エンコードを行います。結合された動画は再生可能なMP4ファイルとして出力されます。

## 必要なソフトウェア

- Python 3.6以上
- FFmpeg

## インストール方法

1. このリポジトリをクローンします。

```bash
git clone https://github.com/yourusername/motiongraphcs.git
```



1.必要なPythonパッケージをインストールします。
```bash
pip install -r requirements.txt
```

2.FFmpegをダウンロードして、適切な場所に配置します。FFmpegのダウンロードページ

## 使い方
1.motiongraphcsディレクトリに移動します。
```bash
cd motiongraphcs
```
2.motion.pyスクリプトを実行します。
```bash
python motion.py
```

上記コマンドを実行すると、outputディレクトリに結合された動画ファイルが生成されます。

## カスタマイズ
スクリプトの実行時に結合する動画のディレクトリと出力先をカスタマイズすることができます。

motion.pyスクリプトの以下の行で、結合元の動画ディレクトリを設定します。

```python
input_directories = [
    r"C:\path\to\input\directory1",
    r"C:\path\to\input\directory2",
    # 他のディレクトリもここに追加
]
```

motion.pyスクリプトの以下の行で、出力先のディレクトリを設定します。
```python
output_directory = "output"
```
motion.pyスクリプトの以下の行で、生成する動画の数を設定します。
```python
number_of_outputs = 10
```
# 注意事項
このスクリプトはWindows環境を想定しています。他の環境で実行する場合は、ffmpeg_pathを適切なFFmpegの実行ファイルのパスに変更してください。
動画の結合と再エンコードには一定の時間がかかる場合があります。
# ライセンス
このプロジェクトはMITライセンスのもとで公開されています。詳細についてはLICENSEファイルを参照してください。
