#longer version
temps = [221, 234, 340, 230]

new_temps = []
for temp in temps:
  new_temps.append(temp / 10)

print(new_temps)
  # [22.1, 23.4, 34.0, 23.0]

####List comprehension
#better version
new_temps = [temp / 10 for temp in temps]
print(new_temps)
  # [22.1, 23.4, 34.0, 23.0]