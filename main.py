transactions = [
    ("ali", 120),
    ("sara", 200),
    ("ali", 80),
    ("hamza", 150),
    ("sara", 50),
    ("ali", -20),
]
def summarize_transactions(transactions):
  summary={}
  for node in transactions:
     if node[0]  not in summary:
       summary[node[0]]=node[1]
     else:
      summary[node[0]]=node[1]+summary[node[0]]
  return summary
print(summarize_transactions(transactions))
