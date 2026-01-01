import json
import os

# 配置 - 可以修改这些值以处理不同游戏
GAME_ID = "snake"  # 修改此值以处理其他游戏
json_path = "data/games.json"
target_dir = f"games/{GAME_ID}"

def main():
    # 1. 读取现有的 JSON
    if not os.path.exists(json_path):
        print(f"错误: 找不到 {json_path}")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            # 如果文件为空，初始化基础结构
            data = {}

    # 确保游戏结构存在（保留现有元数据）
    if GAME_ID not in data:
        data[GAME_ID] = {
            "title": f"{GAME_ID.capitalize()} Benchmark",
            "emoji": "🎮",
            "description": f"Test AI models with {GAME_ID}",
            "keywords": f"{GAME_ID}, AI coding, game benchmark",
            "models": []
        }
    if "models" not in data[GAME_ID]:
        data[GAME_ID]["models"] = []

    # 2. 获取文件夹下的 HTML 文件 (排除 index.html)
    if not os.path.exists(target_dir):
        print(f"错误: 找不到目录 {target_dir}")
        return

    html_files = [f for f in os.listdir(target_dir) 
                  if f.endswith(".html") and f != "index.html"]

    # 获取当前已有的 ID
    existing_ids = [m["id"] for m in data[GAME_ID]["models"]]
    new_models_count = 0

    for filename in html_files:
        # 推断 ID (去掉扩展名和 -r1 后缀)
        model_id = filename.replace(".html", "").replace("-r1", "")
        
        if model_id in existing_ids:
            continue

        # 格式化名字
        model_name = model_id.replace("-", " ").upper()
        
        # 构造新对象 (已移除 type 和 thinking_time)
        new_model = {
            "id": model_id,
            "name": model_name,
            "status": "Pass",
            "r1_file": f"/games/{GAME_ID}/{filename}",
            "r2_file": None,
            "notes": "Initial generation added via python script.",
            "tries": 1
        }

        data[GAME_ID]["models"].append(new_model)
        new_models_count += 1
        print(f"已添加新模型: {model_name} ({model_id})")

    # 3. 写回 JSON
    if new_models_count > 0:
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"\n更新成功！共增加了 {new_models_count} 个模型。")
    else:
        print("\n没有发现新的 HTML 文件需要添加。")

if __name__ == "__main__":
    main()