from datetime import datetime
from connect_db import Database


class Base:
    @staticmethod
    def select(table):
        query = f"SELECT * FROM {table} ORDER BY {table}_id"
        return Database.connect(query, "select")

    @staticmethod
    def update_id(id, new_id):
        query = f"UPDATE category SET category_id = {new_id} WHERE category_id = {id}"
        return Database.connect(query, "update")


    @staticmethod
    def delete_id(id):
        query = f"DELETE FROM category WHERE category_id={id}"
        return Database.connect(query, "delete")

    @staticmethod
    def delete(table, column_name, data):
        if type(data) == int:
            query = f"DELETE FROM {table} WHERE {column_name} = {data}"
        else:
            query = f"DELETE FROM {table} WHERE {column_name} = '{data}'"

        return Database.connect(query, "delete")



class Category(Base):
    def __init__(self, name):
        self.name = name
        self.last_updated = f"{datetime.now()}"
        self. table_name = "category"

    @staticmethod
    def update_id(id, new_id):
        query = f"UPDATE category SET category_id = {new_id} WHERE category_id = {id}"
        return Database.connect(query, "update")


    @staticmethod
    def update(column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE category SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

        else:
            query = f"UPDATE category SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"

        return Database.connect(query, "update")


    def insert(self):
        query = f"INSERT INTO {self.table_name}(name, last_update) VALUES ('{self.name}','{self.last_updated}');"
        return Database.connect(query, "insert")


class Product(Base):
    def __init__(self, product_name):
        self.product_name = product_name
        self.table_name = "product"

    @staticmethod
    def product_update_id(id, new_id):
        query = f"UPDATE product SET product_id = {new_id} WHERE product_id = {id}"
        return Database.connect(query, "update")


    @staticmethod
    def product_update(column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE product SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

        else:
            query = f"UPDATE product SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"

        return Database.connect(query, "update")


    def insert(self):
        query = f"INSERT INTO {self.table_name}(name) VALUES ('{self.product_name}');"
        return Database.connect(query, "insert")


class Color(Base):
    def __init__(self, name):
        self.name = name
        self.table_name = "color"

    @staticmethod
    def delete_id(id):
        query = f"DELETE FROM color WHERE color_id={id}"
        return Database.connect(query, "delete")



    @staticmethod
    def color_update_id(id, new_id):
        query = f"UPDATE color SET color_id = {new_id} WHERE color_id = {id}"
        return Database.connect(query, "update")


    @staticmethod
    def color_update(column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE color SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

        else:
            query = f"UPDATE color SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"

        return Database.connect(query, "update")


    def insert(self):
        query = f"INSERT INTO {self.table_name}(name) VALUES ('{self.name}');"
        return Database.connect(query, "insert")

class ProductDetail(Base):
    def __init__(self, name, description, price, count, rating):
        self.name = name
        self.description = description
        self.price = price
        self.count = count
        self.rating = rating
        self.table_name = "product_detail"


    @staticmethod
    def delete_id(id):
        query = f"DELETE FROM product_detail WHERE product_detail_id={id}"
        return Database.connect(query, "delete")
    @staticmethod
    def product_detail_id(id, new_id):
        query = f"UPDATE product_detail SET product_detail_id = {new_id} WHERE product_detail_id = {id}"
        return Database.connect(query, "update")

    @staticmethod
    def product_detail_update(column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE product_detail SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

        else:
            query = f"UPDATE product_detail SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"

        return Database.connect(query, "update")

    def insert(self):
        query = f"INSERT INTO {self.table_name}(name, description, price, count, rating) VALUES ('{self.name}', '{self.description}', '{self.price}', '{self.count}', '{self.rating}')"
        return Database.connect(query, "insert")



class Country(Base):
    def __init__(self, name):
        self.name = name
        self.table_name = "country"

    @staticmethod
    def delete_id(id):
        query = f"DELETE FROM country WHERE country_id={id}"
        return Database.connect(query, "delete")

    @staticmethod
    def country_update_id(id, new_id):
        query = f"UPDATE country SET country_id = {new_id} WHERE country_id = {id}"
        return Database.connect(query, "update")

    @staticmethod
    def country_update(column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE country SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

        else:
            query = f"UPDATE country SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"

        return Database.connect(query, "update")

    def insert(self):
        query = f"INSERT INTO {self.table_name}(name) VALUES ('{self.name}');"
        return Database.connect(query, "insert")

class Customer(Base):
    def __init__(self, first_name, last_name, password, email, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.birth_date = birth_date
        self.table_name = "customer"

    @staticmethod
    def delete_id(id):
        query = f"DELETE FROM customer WHERE customer_id={id}"
        return Database.connect(query, "delete")

    @staticmethod
    def customer_id(id, new_id):
        query = f"UPDATE customer SET customer_id = {new_id} WHERE customer_id = {id}"
        return Database.connect(query, "update")

    @staticmethod
    def customer_update(column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE customer SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

        else:
            query = f"UPDATE customer SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"

        return Database.connect(query, "update")

    def insert(self):
        query = f"INSERT INTO {self.table_name}(first_name, last_name, password, email, birth_date) VALUES ('{self.first_name}', '{self.last_name}', '{self.password}', '{self.email}', '{self.birth_date}')"
        return Database.connect(query, "insert")



class Payment_type(Base):
    def __init__(self, name):
        self.name = name
        self.table_name = "payment_type"

    @staticmethod
    def delete_id(id):
        query = f"DELETE FROM payment_type WHERE payment_type_id={id}"
        return Database.connect(query, "delete")

    @staticmethod
    def payment_type_update_id(id, new_id):
        query = f"UPDATE payment_type SET payment_type_id = {new_id} WHERE payment_type_id = {id}"
        return Database.connect(query, "update")

    @staticmethod
    def payment_type_update(column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE payment_type SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

        else:
            query = f"UPDATE payment_type SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"

        return Database.connect(query, "update")

    def insert(self):
        query = f"INSERT INTO {self.table_name}(name) VALUES ('{self.name}');"
        return Database.connect(query, "insert")



class Payment_status(Base):
    def __init__(self, name):
        self.name = name
        self.table_name = "payment_status"

    @staticmethod
    def delete_id(id):
        query = f"DELETE FROM payment_status WHERE payment_status_id={id}"
        return Database.connect(query, "delete")

    @staticmethod
    def payment_status_update_id(id, new_id):
        query = f"UPDATE payment_status SET payment_status_id = {new_id} WHERE payment_status_id = {id}"
        return Database.connect(query, "update")

    @staticmethod
    def payment_status_update(column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE payment_status SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

        else:
            query = f"UPDATE payment_status SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"

        return Database.connect(query, "update")

    def insert(self):
        query = f"INSERT INTO {self.table_name}(name) VALUES ('{self.name}');"
        return Database.connect(query, "insert")


class City(Base):
    def __init__(self, name, country_id):
        self.name = name
        self.country_id = country_id
        self.table_name = "city"


    @staticmethod
    def delete_id(id):
        query = f"DELETE FROM city WHERE city_id={id}"
        return Database.connect(query, "delete")

    @staticmethod
    def city_update_id(id, new_id):
        query = f"UPDATE city SET city_id = {new_id} WHERE city_id = {id}"
        return Database.connect(query, "update")

    @staticmethod
    def city_update(column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE city SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

        else:
            query = f"UPDATE city SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"

        return Database.connect(query, "update")

    def insert(self):
        query = f"INSERT INTO {self.table_name}(name, country_id) VALUES ('{self.name}', '{self.country_id}');"
        return Database.connect(query, "insert")


class Address(Base):
    def __init__(self, name, city_id):
        self.name = name
        self.city_id = city_id
        self.table_name = "address"


    @staticmethod
    def delete_id(id):
        query = f"DELETE FROM address WHERE address_id={id}"
        return Database.connect(query, "delete")

    @staticmethod
    def address_update_id(id, new_id):
        query = f"UPDATE address SET address_id = {new_id} WHERE address_id = {id}"
        return Database.connect(query, "update")

    @staticmethod
    def address_update(column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE address SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

        else:
            query = f"UPDATE address SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"

        return Database.connect(query, "update")

    def insert(self):
        query = f"INSERT INTO {self.table_name}(name, city_id) VALUES ('{self.name}', '{self.city_id}');"
        return Database.connect(query, "insert")