from docx2python import docx2python
l = None
example_answer = ["A", "C", "D", "B"]
def is_answer(s):
	if "A." in s or "B." in s or "C." in s or "D." in s:
		return True
	return False
with docx2python("t.docx") as f:
	l = f.text
f.close()
l = [a for a in l.split("\n")]
opt = {"add_index": [], "mark": []} # Option !
opt["index"] = [a for a in range(len(l)) if is_answer(l[a])]
choices = [l[a].split() for a in opt["index"]]
try:
	for c, choice in enumerate(choices):
		for checked in ["A.", "B.", "C.", "D."]:
			enum = choice.index(checked) if choice.count(checked) > 0 else -1
			i = enum
			if enum != -1:
				while True:
					enum += 1
					if enum < len(choice) and not is_answer(choice[enum]):
						# Nối đáp án
						choice[i] += " " + choice[enum]
						choice[enum] = ''

					else:
						# Xử lí đáp án ở đây
						# if c < len(answer) and answer[c] + "." in choice[i]:
						# 	choice[i] = choice[i] + "#"
						break
	# choices = [" ".join(choice) for choice in choices]
	opt["mark"] = [" ".join(choice) for choice in choices]
	opt["mark"] = [i for i, a in enumerate(opt["mark"]) if "A." in a]
	for i, m in enumerate(opt["mark"]):
		end = opt["mark"][i + 1] if m != max(opt["mark"]) else len(choices)
		for j in range(m, end):
			for o in range(len(choices[j])):
				if i < len(example_answer):
					if example_answer[i] + "." in choices[j][o]:
						choices[j][o] += "#"
except Exception as e:
	print(e)