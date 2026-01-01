import os

# 配置 - 修改 GAME_ID 即可在不同目录下生成文件
GAME_ID = "tetris" 
target_dir = f"games/{GAME_ID}"

# 需要创建的文件列表
MODEL_FILES = [
    "deepseek-v3.2-r1.html",
    "glm-4.7-r1.html",
    "gpt-5.2-r1.html",
    "grok-code-fast-v1-r1.html",
    "kimi-k2-r1.html",
    "qwen3-Max-r1.html",
    "qwen3-Max-r2.html",
    "sonnet-4.5-r1.html"
]

def main():
    # 1. 确保目标目录存在
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"已创建目录: {target_dir}")

    # 2. 批量创建空文件
    count = 0
    for filename in MODEL_FILES:
        file_path = os.path.join(target_dir, filename)
        
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                # 写入一个基础占位符，方便之后识别
                f.write("<!-- Placeholder for AI Generated Game -->")
            print(f"已新建: {filename}")
            count += 1
        else:
            print(f"跳过已存在文件: {filename}")

    print(f"\n任务完成！共新建了 {count} 个文件。")

if __name__ == "__main__":
    main()
