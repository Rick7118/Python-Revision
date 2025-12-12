# write (creates file or truncates existing)
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Hello world\n")
    f.write("This is a second line.\n")

# append (adds to end)
with open("notes.txt", "a", encoding="utf-8") as f:
    f.write("Appended line.\n")

# read whole file
with open("notes.txt", "r", encoding="utf-8") as f:
    text = f.read()
print(text)

# read line-by-line (memory friendly)
with open("notes.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
