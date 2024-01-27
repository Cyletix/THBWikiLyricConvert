"""
处理THB wiki的东方同人音乐歌词格式,转换为动态歌词格式,可以复制到musicbee或者musicolet中
https://thwiki.cc
"""

def convert_lyrics(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    with open(output_file, 'w', encoding='utf-8') as file:
        i = 0
        while i < len(lines) - 1:
            current_line = lines[i].strip()
            next_line = lines[i + 1].strip()
            
            # 检查当前行是否是时间戳，即是否以"数字:数字"格式开始
            if len(current_line.split(':')) == 2 and current_line.split(':')[1].replace('.', '', 1).isdigit():
                # 检查下一行是否是歌词（非空且非时间戳）
                if next_line and not (len(next_line.split(':')) == 2 and next_line.split(':')[1].replace('.', '', 1).isdigit()):
                    file.write(f'[{current_line}]{next_line}\n')
                    i += 1  # 跳过歌词行
            i += 1

if __name__=="__main__":
    import sys
    if len(sys.argv) != 2:
        # 设置命令行窗口的大小
        import os
        os.system('mode con: cols=70 lines=5')
        print("Usage: Drag and drop the lyric file onto this window and press Enter.")
        input_file = input("File Path: ").strip().strip('"')  # Remove any surrounding quotes
    else:
        input_file = sys.argv[1]

    format=input('please choice file saving format:\n1:lrc\n2:txt')
    output_file = input_file.rsplit('.', 1)[0] + f'_converted.{format}'
    
    convert_lyrics(input_file, output_file)
    print(f"Converted lyrics have been saved to {output_file}")
    input("Press Enter to exit...")  # Wait for user input before closing