class ContactInfo:
    def __init__(self, address, phone_number, email):
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Contact Info:\nEmail: {self.email}\nPhone Number: {self.phone_number}\nAddress: {self.address}"
    def __repr__(self):
        return f"ContactInfo('{self.email}', '{self.phone_number}', '{self.address}')"
