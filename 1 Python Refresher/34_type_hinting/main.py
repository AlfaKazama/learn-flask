def list_avg(sequence):
  return sum(sequence) / len(sequence)

print(list_avg({1, 2, 3})) # ini akan error, karena sum() menerima masukan list