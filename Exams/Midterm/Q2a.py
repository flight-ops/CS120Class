#print the price and name of the lowest cost item

groceries_for_sale = ("apple juice", "ice-cream","pizza","pasta","eggs")
cost_of_groceries = (5.00,2.50,12.50,3.00,6.12)

def find_min_cost(sale_list,cost_list):
    min_cost = (min(cost_list))
    min_cost_index = cost_list.index(min_cost)
    min_cost_item = sale_list[min_cost_index]
    print("The item that costs the least is:", min_cost_item, "at", min_cost,"dollars.")

def find_max_cost(sale_list,cost_list):
    max_cost = (max(cost_list))
    max_cost_index = cost_list.index(max_cost)
    max_cost_item = sale_list[max_cost_index]
    print("The item that costs the most is:", max_cost_item, "at",max_cost,"dollars.")



find_min_cost(sale_list=groceries_for_sale, cost_list=cost_of_groceries)
find_max_cost(sale_list=groceries_for_sale, cost_list=cost_of_groceries)