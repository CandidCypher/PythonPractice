"""
Mock shopping application.
"""

from ShoppingCart.shopping_cart import ShoppingCart as sc


if __name__ == "__main__":
    cart = sc()
    cart.add_to_cart("Totes")
    cart.add_to_cart("Shampoo")
    cart.add_to_cart("Cereal")
    print(cart.contents)
    print(cart.total_cost)
    cart.remove_from_cart("Totes")
    print(f"Shopping cart contains \n{cart.contents}\n and total cost is: {cart.total_cost}")