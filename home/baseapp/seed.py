from .models import Emp
from faker import Faker
faker = Faker()

def seed_db(n):
    for i in range(0,n):
        Emp.objects.create(
            name = faker.name(),
            phone = faker.phone_number(),
            email = faker.email()
        )