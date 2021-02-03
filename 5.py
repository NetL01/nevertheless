mat = [[1, 2, 1],
       [4, 9, 6],
       [4, 9, 9]]

st = set()
count = 0
for i in range(len(mat)):
    for j in range(len(mat)):
        st.add(mat[i][j])
        if len(st) == 3:
            count += 1
    st.clear()
print(count)
