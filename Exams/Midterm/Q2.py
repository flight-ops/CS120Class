#print the price and name of the lowest cost item

groceries_for_sale = ("apple juice", "ice-cream","pizza","pasta","eggs")
cost_of_groceries = (5.00,2.50,12.50,3.00,6.12)

#find lowest cost, and associated item
def find_min_cost(sale_list,cost_list):
    #find value of lowest cost
    min_cost = (min(cost_list))
    #find index of lowest cost
    min_cost_index = cost_list.index(min_cost)
    #find index of lowest item
    min_cost_item = sale_list[min_cost_index]
    #print to user
    print("The item that costs the least is:", min_cost_item, "at", min_cost,"dollars.")

#find highest cost, and associated item
def find_max_cost(sale_list,cost_list):
    #find value of highest cost
    max_cost = (max(cost_list))
    #find index with highest cost
    max_cost_index = cost_list.index(max_cost)
    #find item with highest cost
    max_cost_item = sale_list[max_cost_index]
    #print to user
    print("The item that costs the most is:", max_cost_item, "at",max_cost,"dollars.")

#find items that cost less than a user identified value
def afford_finder():
    user_cash = float(input("How much money do you have?\n"))
    #loop through all items in list to see if they cost more or less than user identified value
    for i in range (len(cost_of_groceries)):
        #if the cost is affordable, print the item and cost to the user
        if cost_of_groceries[i] <= user_cash:
            print("You can afford:", groceries_for_sale[i], "which costs", cost_of_groceries[i], "dollars.")



def main():
    find_min_cost(sale_list=groceries_for_sale, cost_list=cost_of_groceries)
    find_max_cost(sale_list=groceries_for_sale, cost_list=cost_of_groceries)
    afford_finder()

main()
