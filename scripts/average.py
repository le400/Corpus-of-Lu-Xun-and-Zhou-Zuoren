# ==============================
# 鲁迅 & 周作人 语料深度统计
# 词种数 / 词汇丰富度 / 句长分布 / 自动平均
# ==============================

def get_full_info(file_path):
    total_sent = 0          # 总句数
    total_word = 0          # 总词数
    word_types = set()      # 不重复词（词种数）
    
    # 句长分布：1-5 短句 | 6-15 中句 | 16+ 长句
    short = 0
    middle = 0
    long = 0

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            total_sent += 1
            words = line.split()
            wc = len(words)

            # 累加词数 & 词种
            total_word += wc
            for w in words:
                word_types.add(w)

            # 句长分类
            if wc <= 5:
                short += 1
            elif wc <= 15:
                middle += 1
            else:
                long += 1

    # 计算指标
    word_type_count = len(word_types)
    avg_len = round(total_word / total_sent, 2) if total_sent else 0
    vocab_diversity = round(word_type_count / total_word * 100, 2) if total_word else 0  # 词汇丰富度百分比

    # 占比
    short_pct = round(short / total_sent * 100, 2)
    middle_pct = round(middle / total_sent * 100, 2)
    long_pct = round(long / total_sent * 100, 2)

    return {
        "总句数": total_sent,
        "总词数": total_word,
        "词种数": word_type_count,
        "词汇丰富度%": vocab_diversity,
        "平均句长": avg_len,
        "短句数": short,
        "中句数": middle,
        "长句数": long,
        "短句占比%": short_pct,
        "中句占比%": middle_pct,
        "长句占比%": long_pct
    }

# ===================== 你的文件 =====================
lu = get_full_info("data/luxun_clean.txt")
zhou = get_full_info("data/zhouzuoren_clean.txt")

# ===================== 生成汇总报告 =====================
report = """# 鲁迅 & 周作人 语料深度统计报表（自动平均+标准化）

## 一、词汇丰富度对比
------------------------------------
【鲁迅】
- 总词数：{}
- 词种数（不重复词）：{}
- 词汇丰富度：{}%
- 平均句长：{} 词/句

【周作人】
- 总词数：{}
- 词种数（不重复词）：{}
- 词汇丰富度：{}%
- 平均句长：{} 词/句

## 二、句式风格对比（短句/中句/长句）
------------------------------------
【鲁迅】
- 短句(1-5词)：{} 句，占比 {}%
- 中句(6-15词)：{} 句，占比 {}%
- 长句(16+词)：{} 句，占比 {}%

【周作人】
- 短句(1-5词)：{} 句，占比 {}%
- 中句(6-15词)：{} 句，占比 {}%
- 长句(16+词)：{} 句，占比 {}%

## 三、风格结论（自动分析）
------------------------------------
1. 词汇丰富度：{} 比 {} 高 {}%
2. 平均句长：{} 更长，文风更舒缓
3. 句式偏好：{} 更爱用短句，文风更犀利紧凑
""".format(
    lu["总词数"], lu["词种数"], lu["词汇丰富度%"], lu["平均句长"],
    zhou["总词数"], zhou["词种数"], zhou["词汇丰富度%"], zhou["平均句长"],
    lu["短句数"], lu["短句占比%"], lu["中句数"], lu["中句占比%"], lu["长句数"], lu["长句占比%"],
    zhou["短句数"], zhou["短句占比%"], zhou["中句数"], zhou["中句占比%"], zhou["长句数"], zhou["长句占比%"],
    "鲁迅" if lu["词汇丰富度%"] > zhou["词汇丰富度%"] else "周作人",
    "周作人" if lu["词汇丰富度%"] > zhou["词汇丰富度%"] else "鲁迅",
    round(abs(lu["词汇丰富度%"] - zhou["词汇丰富度%"]), 2),
    "周作人" if zhou["平均句长"] > lu["平均句长"] else "鲁迅",
    "鲁迅" if lu["短句占比%"] > zhou["短句占比%"] else "周作人"
)

# 保存报告
with open("语料深度统计报告.md", "w", encoding="utf-8") as f:
    f.write(report)

print("✅ 统计完成！已生成：语料深度统计报告.md")
print("\n==== 鲁迅 =====")
for k, v in lu.items():
    print(f"{k}：{v}")
print("\n==== 周作人 =====")
for k, v in zhou.items():
    print(f"{k}：{v}")