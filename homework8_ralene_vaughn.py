pizza_orders = ["Meatza", "Pepperoni", "Hawaiian", "Supreme", "Chicken Bacon Ranch"]

finished_pizzas = []

while pizza_orders:
    current_pizza = pizza_orders.pop(0)
    print(f" Your {current_pizza} pizza pie is finished!")
    finished_pizzas.append(current_pizza)

for pizza in finished_pizzas:
    print(f"The {pizza} pizza was made.")