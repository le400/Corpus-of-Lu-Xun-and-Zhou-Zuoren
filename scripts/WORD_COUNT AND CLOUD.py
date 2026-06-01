from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# ========== 文件路径 ==========
FILE_LU = "data/LX_FINAL_OK.txt"
FILE_ZHOU = "data/ZZR_FINAL_OK.txt"

# ========== 你提供的停用词 ==========
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

# ========== 处理函数 ==========
def process_words(filename):
    """读取文本、过滤单字+停用词，返回词语字符串 & 词频列表"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()
        # 拆分词语
        words = [w.strip() for w in text.split() if w.strip()]
        # 过滤：只保留两字及以上 + 不在停用词内
        words = [w for w in words if len(w) >= 2 and w not in STOP_WORDS]
        # 拼接成空格分隔字符串（词云需要格式）
        word_str = " ".join(words)
        # 统计词频TOP500
        cnt = Counter(words)
        top500 = cnt.most_common(500)
        return word_str, top500
    except Exception as e:
        print(f"读取失败：{e}")
        return "", []

def create_wordcloud(text, title, save_name):
    """生成并保存词云图"""
    wc = WordCloud(
        font_path="C:/Windows/Fonts/simhei.ttf",  # 中文字体（Windows）
        background_color="white",
        width=1000,
        height=600,
        max_words=500,
        collocations=False
    )
    wc.generate(text)
    # 绘图
    plt.figure(figsize=(10, 6))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.title(title, fontsize=16)
    plt.tight_layout()
    plt.savefig(save_name, dpi=300, bbox_inches="tight")
    plt.show()

# ========== 主程序执行 ==========
if __name__ == "__main__":
    # 处理两份文本
    lu_text, lu_top500 = process_words(FILE_LU)
    zhou_text, zhou_top500 = process_words(FILE_ZHOU)

    # 1. 生成TOP500统计报告
    report = "# 鲁迅 & 周作人 高频词统计报告（TOP500 · 已过滤停用词）\n\n"
    report += "## 一、鲁迅 高频词 TOP500\n"
    for i, (w, c) in enumerate(lu_top500, 1):
        report += f"{i:3d}. {w}：{c}\n"

    report += "\n## 二、周作人 高频词 TOP500\n"
    for i, (w, c) in enumerate(zhou_top500, 1):
        report += f"{i:3d}. {w}：{c}\n"

    with open("高频词统计报告_TOP500.md", "w", encoding="utf-8") as f:
        f.write(report)
    print("✅ 统计报告已生成：高频词统计报告_TOP500.md")

    # 2. 生成词云图
    print("🔍 正在生成鲁迅词云...")
    create_wordcloud(lu_text, "鲁迅作品词云", "鲁迅_词云.png")

    print("🔍 正在生成周作人词云...")
    create_wordcloud(zhou_text, "周作人作品词云", "周作人_词云.png")

    print("✅ 全部完成！已生成两张词云图片")