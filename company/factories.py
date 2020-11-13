# import factory
#
# from company.models import Company, Category, Address
#
#
# class CategoryFactory(factory.Factory):
#     class Meta:
#         model = Category
#
#     name = 'Test'
#
#
# class AddressFactory(factory.Factory):
#     class Meta:
#         model = Address
#
#     street = factory.Faker('street_address')
#     city = factory.Faker('city')
#     post_code = factory.Faker('zipcode')
#
#
# class CompanyFactory(factory.Factory):
#     class Meta:
#         model = Company
#
#     name = factory.Faker('company')
#     registration_date = factory.Faker('date')
#     owner = factory.Faker('name')
#     description = factory.Faker('text')
#     category = factory.SubFactory(Category)
#     email = factory.Faker('email')
#     address = factory.RelatedFactory(Address)
#     created_at = factory.Faker('date')
#     phone_number = factory.Faker('name')
#     is_active = True
#
#     @factory.post_generation
#     def address(self, create, extracted, **kwargs):
#         if not create:
#             # Simple build, do nothing.
#             return
#
#         if extracted:
#             # A list of groups were passed in, use them
#             for asd in extracted:
#                 self.address.add(asd)
#
