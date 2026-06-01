def get_corpus_all_info(file_path):
    total_sent = 0
    total_word = 0
    word_set = set()

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total_sent += 1
            words = line.split()
            total_word += len(words)
            for w in words:
                word_set.add(w)
    
    word_type = len(word_set)
    avg_len = round(total_word / total_sent, 2) if total_sent != 0 else 0
    return total_sent, total_word, word_type, avg_len

f1 = "data/luxun_clean.txt"
f2 = "data/zhouzuoren_clean.txt"

lu_sent, lu_word, lu_type, lu_avg = get_corpus_all_info(f1)
zhou_sent, zhou_word, zhou_type, zhou_avg = get_corpus_all_info(f2)

report = """# 语料综合信息汇总
## 鲁迅（luxun_clean.txt）
- 总句数：{}
- 总词数（词频总数）：{}
- 词种数（不重复词汇）：{}
- 平均句长（词/句）：{}

## 周作人（zhouzuoren_clean.txt）
- 总句数：{}
- 总词数（词频总数）：{}
- 词种数（不重复词汇）：{}
- 平均句长（词/句）：{}
""".format(lu_sent, lu_word, lu_type, lu_avg,
           zhou_sent, zhou_word, zhou_type, zhou_avg)

with open("语料综合信息汇总.md", "w", encoding="utf-8") as f:
    f.write(report)
print("✅ 综合信息报表生成完成")