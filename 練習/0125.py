

path_w = 'C:/Users/nakahashi/test/test_w.txt'

s = 'New file'

with open(path_w, mode='w') as f:
    f.write(s)

with open(path_w) as f:
    print(f.read())
# New file