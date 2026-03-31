import json, os, re, shutil, sys
TARGET_SENTENCE = "如果没有明确直接的论文指向，则认为不能被证明有效，不能满足要求。"
def extract_choice_letter(text):
    if not text: return None
    idx = text.find("答案")
    sub = text[idx:] if idx != -1 else text
    for ch in sub:
        if ch in "ABCDEFG": return ch
    for ch in text:
        if ch in "ABCDEFG": return ch
    return None
def split_options(s):
    pat = re.compile(r'(?m)(^|\n)([A-G])([\.、\)．:：])\s*')
    ms = list(pat.finditer(s or ""))
    if not ms: return s, []
    pre = s[:ms[0].start()]
    opts = []
    for i, m in enumerate(ms):
        start = m.end()
        end = ms[i+1].start() if i+1 < len(ms) else len(s)
        opts.append({"sep":m.group(1),"letter":m.group(2),"punc":m.group(3),"content":s[start:end]})
    return pre, opts
def process_text(s, letter):
    if not s or not letter: return s
    pre, opts = split_options(s)
    if not opts:
        return s.replace(TARGET_SENTENCE, "") if TARGET_SENTENCE in s else s
    changed = False
    out = []
    for o in opts:
        c = o["content"]
        if o["letter"] == letter and TARGET_SENTENCE in c:
            c = c.replace(TARGET_SENTENCE, "")
            changed = True
        out.append(f'{o["sep"]}{o["letter"]}{o["punc"]} {c}')
    return pre + "".join(out) if changed else s
def main():
    base = os.path.dirname(os.path.abspath(__file__))
    inp = sys.argv[1] if len(sys.argv)>=2 else os.path.join(base,"openai_batch_output.filtered.json")
    outp = sys.argv[2] if len(sys.argv)>=3 else inp
    if not os.path.exists(inp):
        print(f"文件不存在: {inp}"); return
    data = json.load(open(inp,"r",encoding="utf-8"))
    if not isinstance(data,list):
        print("JSON 格式不是数组"); return
    changed = 0
    for it in data:
        letter = extract_choice_letter(it.get("answer",""))
        q = it.get("question","")
        r = it.get("raw_output","")
        nq = process_text(q, letter)
        nr = process_text(r, letter)
        if nq != q or nr != r:
            it["question"] = nq
            it["raw_output"] = nr
            changed += 1
    if outp == inp:
        shutil.copyfile(inp, inp + ".bak")
    json.dump(data, open(outp,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"处理完成，修改题目数: {changed}")
    if outp == inp: print(f"已备份到: {inp}.bak")
if __name__ == "__main__":
    main()