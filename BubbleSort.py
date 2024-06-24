def bubble_sort(data):

  n = len(data)
  sudah_tertukar = True
  while sudah_tertukar:
    sudah_tertukar = False
    for i in range(n-1):
      if data[i] > data[i+1]:
        data[i], data[i+1] = data[i+1], data[i]
        sudah_tertukar = True
  return data

data = [5, 2, 4, 1, 3]
print(f"Data sebelum diurutkan: {data}")
data_urut = bubble_sort(data)
print(f"Data setelah diurutkan: {data_urut}")
