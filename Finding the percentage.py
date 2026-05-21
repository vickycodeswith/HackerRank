n = int(input())
student_marks = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
    
# Get the list of scores for the queried student
target_scores = student_marks[query_name]
    
# Calculate the average
average = sum(target_scores) / len(target_scores)
    
# Print the result formatted to exactly 2 decimal places
print(f"{average:.2f}")
