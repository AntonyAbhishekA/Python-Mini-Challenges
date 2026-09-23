words = ["python", "java", "c", "javascript", "go"]

words.sort(key=lambda word: len(word))

print(words)
# Output: ['c', 'go', 'java', 'python', 'javascript']
