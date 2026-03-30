# 3_set.py
# 2개의 집합 정의
set1= {1, 2, 3, 'a', "Goodbye"}
set2= {"Goodbye", 3, 4, 5, 'a'}

# 합집합
union_set = set1 | set2

# 교집합
int_set = set1 & set2 # && = and

# 차집합
diff_set = set1 - set2

# 대칭차집합
sym_diff_set = set1 ^ set2 # 합집합 - 교집합

print('union', union_set)
print(f"intersection: {int_set}")
print(f"intersection: {diff_set}")
print(f"intersection: {sym_diff_set}")