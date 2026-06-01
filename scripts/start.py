import os
import re
from collections import Counter

# 1. 内置通用中文停用词（过滤助词、连词、代词等无意义词汇）
STOP_WORDS = {
    "的", "了", "是", "在", "我", "你", "他", "她", "它", "们",
    "和", "与", "及", "或", "而", "就", "也", "都", "还", "又",
    "很", "太", "最", "更", "不", "没", "无", "非", "这", "那",
    "这个", "那个", "这里", "那里", "这样", "那样", "啊", "哦",
    "呢", "吗", "吧", "呀", "于", "对", "把", "被", "让", "给",
    "到", "向", "从", "由", "为", "所", "之", "以", "然", "却"
}

# 脚本所在目录
base_dir = os.path.dirname(os.path.abspath(__file__))
corpus_path = os.path.join(base_dir, "data")
docs_dir = os.path.join(base_dir, "docs")
os.makedirs(docs_dir, exist_ok=True)
report_path = os.path.join(docs_dir, "corpus_statistics.md")

# 全局汇总变量
total_all_char = 0
total_all_para = 0
total_all_words = Counter()
file_list = []

# 遍历所有txt文件
for root, dirs, files in os.walk(corpus_path):
    for f in files:
        if f.endswith(".txt"):
            file_path = os.path.join(root, f)
            file_list.append(file_path)

# 开始逐个文件统计
md_content = "# 语料库统计报告\n\n## 一、各文件独立统计\n\n"

for idx, file_path in enumerate(file_list, 1):
    print(f"正在读取：{file_path}")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        # 基础字数统计（纯文本，去除换行、空格）
        clean_text = text.strip().replace("\n", "").replace(" ", "")
        char_num = len(clean_text)

        # 段落统计（非空行算一个段落）
        paragraphs = [p for p in text.split("\n") if p.strip()]
        para_num = len(paragraphs)

        # 提取两字及以上中文词汇 + 过滤停用词
        raw_words = re.findall(r"[\u4e00-\u9fa5]{2,}", text)
        # 核心过滤：剔除停用词
        filter_words = [w for w in raw_words if w not in STOP_WORDS]
        word_counter = Counter(filter_words)
        top10 = word_counter.most_common(10)

        # 累加全局汇总
        total_all_char += char_num
        total_all_para += para_num
        total_all_words.update(word_counter)

        # 写入单文件markdown
        file_name = os.path.basename(file_path)
        md_content += f"### {idx}. {file_name}\n"
        md_content += f"- 总字数：{char_num} 字\n"
        md_content += f"- 总段落数：{para_num} 段\n"
        md_content += "- 高频词 TOP10（已过滤停用词）：\n"
        for w, c in top10:
            md_content += f"  - {w}：{c}\n"
        md_content += "\n"

    except Exception as e:
        md_content += f"### {idx}. {os.path.basename(file_path)} 读取失败：{e}\n\n"
        print(f"读取失败 {file_path}：{e}")

# 写入全局汇总
md_content += "## 二、全部文件汇总统计\n"
md_content += f"- 文件总数：{len(file_list)} 个\n"
md_content += f"- 合计总字数：{total_all_char} 字\n"
md_content += f"- 合计总段落数：{total_all_para} 段\n"
md_content += "- 全库高频词 TOP20（已过滤停用词）：\n"
for w, c in total_all_words.most_common(20):
    md_content += f"  - {w}：{c}\n"

# 保存md文件
with open(report_path, "w", encoding="utf-8") as f:
    f.write(md_content)

# 控制台打印汇总
print("\n===== 统计完成 =====")
print(f"文件总数：{len(file_list)} 个")
print(f"合计总字数：{total_all_char} 字")
print(f"合计总段落数：{total_all_para} 段")
print(f"报告已生成：{report_path}")