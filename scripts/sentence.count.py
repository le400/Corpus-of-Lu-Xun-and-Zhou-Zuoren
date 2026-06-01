def get_corpus_info(file_path):
    total_sentence = 0   # 总句数
    total_word = 0       # 总词数

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total_sentence += 1
            words = line.split()
            total_word += len(words)

    # 计算平均句长
    if total_sentence == 0:
        avg_sent_len = 0.0
    else:
        avg_sent_len = round(total_word / total_sentence, 2)

    return total_sentence, total_word, avg_sent_len

# 你的文件路径
file_lu = "data/luxun_clean.txt"
file_zhou = "data/zhouzuoren_clean.txt"

# 分别统计
lu_sent, lu_word, lu_avg = get_corpus_info(file_lu)
zhou_sent, zhou_word, zhou_avg = get_corpus_info(file_zhou)

# 生成汇总报表
report_content = """# 鲁迅 & 周作人 清洗后语料基础信息汇总

## 一、鲁迅语料（luxun_clean.txt）
- 总句数：{}
- 总词汇量：{}
- 单句平均词数：{}

## 二、周作人语料（zhouzuoren_clean.txt）
- 总句数：{}
- 总词汇量：{}
- 单句平均词数：{}
""".format(lu_sent, lu_word, lu_avg, zhou_sent, zhou_word, zhou_avg)

# 保存报表
with open("语料基础信息汇总.md", "w", encoding="utf-8") as f:
    f.write(report_content)

print("✅ 统计完成，已生成：语料基础信息汇总.md")
print(f"\n鲁迅：总句数 {lu_sent} | 总词数 {lu_word} | 平均句长 {lu_avg}")
print(f"周作人：总句数 {zhou_sent} | 总词数 {zhou_word} | 平均句长 {zhou_avg}")