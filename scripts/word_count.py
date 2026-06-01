from collections import Counter

# 文件路径
FILE_LU = "data/LX_FINAL_OK.txt"
FILE_ZHOU = "data/ZZR_FINAL_OK.txt"

# 你提供的停用词表
STOP_WORDS = {
"的", "了", "一", "不", "是", "个", "也", "都", "在", "有", "和",
"就", "而", "但", "或", "与", "且", "并", "则", "却", "只", "可",
"还", "便", "又", "亦", "即", "乃", "竟", "皆", "均", "俱", "每",
"各", "某", "本", "该", "那", "这", "哪", "怎", "么", "那", "这",
"么", "那", "么", "怎", "么", "什", "么", "哪", "里", "哪", "儿",
"这", "里", "那", "里", "这", "些", "那", "些", "这", "个", "那",
"个", "这", "么", "那", "么", "着", "来", "着", "罢", "了", "而",
"已", "呢", "吗", "吧", "啊", "哦", "嗯", "哈", "呵", "嘿", "哟",
"呀", "哇", "啦", "哩", "咯", "啰", "喽", "耶", "呕", "喔", "呗",
"罢", "了", "噫", "兮", "欤", "矣", "焉", "耳", "乎", "哉", "噢",
"啵", "诶", "哎", "哟", "唉", "呦", "嘻", "吼", "哼", "啧", "呸",
"呃", "嚯", "咧", "啰", "噜", "哪", "哈", "嘿", "哟", "哦", "噢",
"嗯", "唔", "嘎", "噗", "嘶", "嘟", "哔", "咚", "锵", "铛", "噼",
"啪", "叽", "喳", "啾", "唧", "喵", "汪", "嗷", "咩", "哞", "呣",
"哼", "哈", "嘻", "呵", "嗻", "噻", "我", "你", "他", "没", "不",
"已", "如", "多", "大", "无", "他", "她", "它", "一", "二", "三",
"四", "五", "六", "七", "八", "九", "十", "谓", "先", "谁", "本",
"云", "颇", "两", "我", "你", "他", "们", "人", "大", "第", "约",
"现", "正"
}

# 统计函数（TOP500）
def get_top_words(filename, top_n=500):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()

        words = [w.strip() for w in text.split() if w.strip()]
        words = [w for w in words if len(w) >= 2]          # 只留词语
        words = [w for w in words if w not in STOP_WORDS]  # 过滤停用词

        cnt = Counter(words)
        return cnt.most_common(top_n)
    
    except Exception as e:
        print("错误：", e)
        return []

# 开始统计
lu_words = get_top_words(FILE_LU, 500)
zhou_words = get_top_words(FILE_ZHOU, 500)

# 生成报告
report = "# 鲁迅 & 周作人 高频词统计报告（TOP500 · 已过滤停用词）\n\n"

report += "## 一、鲁迅 高频词 TOP500\n"
for i, (w, c) in enumerate(lu_words, 1):
    report += f"{i:3d}. {w}：{c}\n"

report += "\n## 二、周作人 高频词 TOP500\n"
for i, (w, c) in enumerate(zhou_words, 1):
    report += f"{i:3d}. {w}：{c}\n"

# 保存
with open("高频词统计报告_TOP500.md", "w", encoding="utf-8") as f:
    f.write(report)

print("✅ 统计完成！已生成：高频词统计报告_TOP500.md")