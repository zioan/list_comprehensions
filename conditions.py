temps = [221, 234, 340, -9999, 230]

new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps ]
  #-9999 is changed with 0
print(new_temps)

#### exercices 1
def foo(list):
  new_list = []
  for i in list:
    if isinstance(i, int):
      new_list.append(i)
    else:
      new_list.append(0)
  return(new_list)

print(foo([99, "no data", 44, 63, "no data"]))
#[99, 0, 44, 63, 0]

#### exercices 2
def calc_sum(lst):
  new_lst = []
  for i in lst:
      number = float(i)
      new_lst.append(number)
      result = sum(new_lst)
  return(result)

print(calc_sum(["1.2", "2.6", "3.3"]))