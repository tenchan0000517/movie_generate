import os
import random
import subprocess
import sys

ffmpeg_path = r'ffmpegのフルパス'  # 実際のパスに置き換える
command = [ffmpeg_path, '...その他の引数...']

subprocess.run(command)

# 入力ディレクトリリスト
input_directories = [
    r"１番目の動画のディレクトリパス",
    r"２番目の動画のディレクトリパス",
    r"３番目の動画のディレクトリパス"
    # 他のディレクトリもここに追加
]

# 出力ディレクトリ
output_directory = "output"

# 生成する動画の数
number_of_outputs = 10

def get_random_video(directory):
    files = [f for f in os.listdir(directory) if f.lower().endswith(('.mp4', '.mov'))]

    if not files:
        print(f"No video files found in directory: {directory}")
        return None # またはデフォルトの動画ファイルを返す

    return os.path.join(directory, random.choice(files))

def convert_to_mp4(input_file, output_file):
    command = [ffmpeg_path, "-i", input_file, "-c:v", "libx264", "-crf", "23", "-c:a", "aac", "-strict", "experimental", output_file]
    subprocess.run(command, shell=True, encoding=sys.getfilesystemencoding())

def combine_videos(videos, output_path):
    with open("temp.txt", "w", encoding=sys.getfilesystemencoding()) as f:
        for video in videos:
            f.write(f"file '{video}'\n")

    command = [ffmpeg_path, "-f", "concat", "-safe", "0", "-i", "temp.txt", "-c:v", "libx264", "-crf", "23", "-c:a", "aac", "-strict", "experimental", output_path]
    subprocess.run(command, shell=True, encoding=sys.getfilesystemencoding())

    os.remove("temp.txt")

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for i in range(number_of_outputs):
    selected_videos = [get_random_video(directory) for directory in input_directories]
    output_path = os.path.join(output_directory, f"output{i}.mp4")
    combine_videos(selected_videos, output_path)
    print(f"Generated {output_path}")
