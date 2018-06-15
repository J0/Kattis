num_cases = input()
for i  in range(int(num_cases)):
  b, p = input().split()
  b = float(b)
  p = float(p)
  calculated_bpm = 60 * b/p
  min_abpm = calculated_bpm - calculated_bpm /b 
  max_abpm = calculated_bpm + calculated_bpm/b
  print("%.4f %.4f %.4f" %(min_abpm ,calculated_bpm, max_abpm))

