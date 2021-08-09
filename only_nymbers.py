temps = [221, 234, 340, -9999, 230]
#-9999 means no data

new_temps = [temp / 10 for temp in temps if temp != -9999]
print(new_temps)
  #[22.1, 23.4, 34.0, 23.0]
  #-9999 is excluded from the loop/execution

#will display only numbers, no strings
def foo(lst):
    new_lst = []
    for i in lst:
        if isinstance(i, int):
            new_lst.append(i)
    return new_lst

  
print(foo([99, "no data", 45]))

#will display only positive numbers
numbers = [-5, 3, -1, 101]
 
def num(numbers):
    return [numb for numb in numbers if numb > 0]
 
print(num(numbers))