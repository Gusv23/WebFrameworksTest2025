from django.db import models

# === Salesperson ===
class Salesperson(models.Model):
    salesperson_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# === Customer ===
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state_province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# === Car ===
class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    serial_number = models.CharField(max_length=100)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    colour = models.CharField(max_length=30)
    year = models.IntegerField()
    car_for_sale = models.BooleanField()

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"


# === SalesInvoice ===
class SalesInvoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    invoice_number = models.CharField(max_length=50)
    date = models.DateField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salesperson = models.ForeignKey(Salesperson, on_delete=models.CASCADE)

    def __str__(self):
        return f"Invoice {self.invoice_number}"


# === Mechanic ===
class Mechanic(models.Model):
    mechanic_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# === Service ===
class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=100)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.service_name


# === ServiceTicket ===
class ServiceTicket(models.Model):
    service_ticket_id = models.AutoField(primary_key=True)
    service_ticket_number = models.CharField(max_length=50)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_received = models.DateField()
    comments = models.TextField()
    date_returned = models.DateField()

    def __str__(self):
        return f"Ticket {self.service_ticket_number}"


# === ServiceMechanic (join table) ===
class ServiceMechanic(models.Model):
    servicemechanic_id = models.AutoField(primary_key=True)
    service_ticket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    comment = models.TextField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"ServiceMechanic #{self.id}"


# === Parts ===
class Parts(models.Model):
    parts_id = models.AutoField(primary_key=True)
    part_number = models.CharField(max_length=50)
    description = models.TextField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.part_number


# === PartsUsed (join table) ===
class PartsUsed(models.Model):
    parts_used_id = models.AutoField(primary_key=True)
    part = models.ForeignKey(Parts, on_delete=models.CASCADE)
    service_ticket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)
    number_used = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.number_used}x {self.part}"
