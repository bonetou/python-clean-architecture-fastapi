class QuantityGreaterThanCopiesAvailable(Exception):
    def __init__(self):
        super().__init__("Quantity is greater than the number of copies available")
