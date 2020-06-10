dict_word = {"find":"找到", "clear":"清理","eliminate":"消灭"}
data = "clear"
for k,v in dict_word.items():
    if data == k:
        print(v)
else:
    print("Nope")