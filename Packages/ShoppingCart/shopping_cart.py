"""
Shopping cart module
"""
print(__name__)

class ShoppingCart():
    """
    Shopping cart object.
    """
    def __init__(self):
        self.contents = []
        self.total_cost = 0
        
    def add_to_cart(self,item):
        """
        Info: Helper method to to add items to the cart
        """
        self.contents.append(item)
        self.total_cost += 10.00


    def remove_from_cart(self, item):
        """
        Info: Helper to remove item from cart
        """
        self.contents.remove(item)
        self.total_cost -= 10.00

    
    def reset_cart(self):
        """
        Info: Helper to empty cart. 
        """
        self.contents.clear()
        self.total_cost = 0