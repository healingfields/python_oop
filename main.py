from Item import Item
from Phone import  Phone

item1 = Item("myItem",55)
item1.name = "skdgg"
item1.apply_discount()
print(item1.price)
item1.apply_increment(0.1)
print(item1.price)

item1.send_mail()
phone1 = Phone("akfdf",400,10,1)
print(phone1.calculate_total_price())
print(Item.all)
print(Phone.all)

Item.instantiate_from_csv()
print(Item.is_integer(70.1  ))

item1 = Item("phone",500)
# print(item1.calculate_total_price())
item1.apply_discount()
print(item1.price)

item2 = Item("laptop",1000,5)
# print(item2.calculate_total_price())
item2.pay_rate = 0.6
item2.apply_discount()
print(item2.price)

item3 = Item("keyboard",100,41)
item4 = Item("Cable",50,14)
item5 = Item("Mouse",75,20)

print(len(Item.all))
print(Item.all)
for instance in Item.all :
    print(instance.name)


print(item2.name)
print(item2.quantity)
print(item2.price)
print(Item.pay_rate)
print(item2.pay_rate)
print(Item.__dict__)
print(item2.__dict__)