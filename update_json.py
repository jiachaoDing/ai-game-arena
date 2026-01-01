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

    # 2. 获取文件夹下的 HTML 文件
    if not os.path.exists(target_dir):
        print(f"错误: 找不到目录 {target_dir}")
        return

    html_files = [f for f in os.listdir(target_dir) if f.endswith(".html") and f != "index.html"]

    changes_made = False

    for filename in html_files:
        # 判断是 R1 还是 R2
        is_r2 = "-r2" in filename.lower()
        # 统一提取基础 Model ID (例如 qwen3-Max-r2 -> qwen3-Max)
        model_id = filename.replace(".html", "").replace("-r1", "").replace("-r2", "")
        
        # 在现有数据中查找该模型
        existing_model = next((m for m in data[GAME_ID]["models"] if m["id"] == model_id), None)

        if is_r2:
            # 如果是 R2，尝试更新现有模型
            if existing_model:
                if existing_model.get("r2_file") is None:
                    existing_model["r2_file"] = f"../games/{GAME_ID}/{filename}"
                    existing_model["status"] = "Fixed" # 发现 R2 后状态改为 Fixed
                    existing_model["tries"] = 2       # 尝试次数更新为 2
                    print(f"已为模型 {model_id} 添加 Round 2 修复文件")
                    changes_made = True
            else:
                # 如果 R2 先于 R1 被发现且模型不存在，先创建一个占位模型
                new_model = create_empty_model(model_id)
                new_model["r2_file"] = f"../games/{GAME_ID}/{filename}"
                new_model["status"] = "Fixed"
                new_model["tries"] = 2
                data[GAME_ID]["models"].append(new_model)
                print(f"已创建模型并添加 R2: {model_id}")
                changes_made = True
        else:
            # 如果是 R1 且模型不存在，则创建
            if not existing_model:
                new_model = create_empty_model(model_id)
                new_model["r1_file"] = f"../games/{GAME_ID}/{filename}"
                data[GAME_ID]["models"].append(new_model)
                print(f"已添加新模型: {model_id}")
                changes_made = True
            elif existing_model.get("r1_file") is None:
                # 如果模型已存在（可能先被 R2 创建了），更新其 R1 路径
                existing_model["r1_file"] = f"../games/{GAME_ID}/{filename}"
                print(f"已为模型 {model_id} 补全 Round 1 文件")
                changes_made = True

    # 3. 写回 JSON
    if changes_made:
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print("\nJSON 数据更新成功！")
    else:
        print("\n没有发现需要更新的内容。")

def create_empty_model(model_id):
    """创建一个基础模型对象"""
    return {
        "id": model_id,
        "name": model_id.replace("-", " ").upper(),
        "status": "Pass",
        "r1_file": None,
        "r2_file": None,
        "notes": "Added via improved python script.",
        "tries": 1
    }

if __name__ == "__main__":
    main()