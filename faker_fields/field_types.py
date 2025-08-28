class FieldType:
    """Base class for field types."""
    def generate(self, fake):
        raise NotImplementedError

class FullNameField(FieldType):
    def generate(self, fake):
        return fake.name()

class PhoneField(FieldType):
    def generate(self, fake):
        return fake.phone_number()

class EmailField(FieldType):
    def generate(self, fake):
        return fake.email()

class DepartmentField(FieldType):
    def generate(self, fake):
        return fake.job()

class ISBNField(FieldType):
    def generate(self, fake):
        return fake.isbn13()

class AddressField(FieldType):
    def generate(self, fake):
        return fake.address().replace('\n', ', ')

class CityField(FieldType):
    def generate(self, fake):
        return fake.city()

class CountryField(FieldType):
    def generate(self, fake):
        return fake.country()

class DateField(FieldType):
    def generate(self, fake):
        return fake.date()

class CompanyField(FieldType):
    def generate(self, fake):
        return fake.company()

class IntegerField(FieldType):
    def generate(self, fake):
        return str(fake.random_int(min=1, max=999999))

class TextField(FieldType):
    def generate(self, fake):
        return fake.text(max_nb_chars=20)
