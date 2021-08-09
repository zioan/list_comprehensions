temps = [221, 234, 340, -9999, 230]
#-9999 means no data

new_temps = [temp / 10 for temp in temps if temp != -9999]
print(new_temps)
  #[22.1, 23.4, 34.0, 23.0]
  #-9999 is excluded from the 
