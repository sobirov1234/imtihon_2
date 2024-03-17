import classes


def address():
    address_1 = input("""
            ______________________________\n
                         SERVICES

            ------------------------------\n
                1. SELECT _>
                2. INSERT _>
                3. UPDATE _>
                4. DELETE _>
                0. Back _>

                    """)

    if address_1 == "1":
        if len(classes.Address.select("address")) == 0:
            print("""
                ------------------------------\n
                    MA'LUMOTLAR MAVJUD EMAS
                ------------------------------\n
                    """)

        else:
            for i in classes.Address.select("address"):
                print(f"""
                            ID: {i[0]}
                            Name: {i[1]}
                            City_id: {i[2]}
                            Create Date: {i[3]}
                                """)
        return city()

    elif address_1 == "2":
        name = input("Name: ")
        city_id = input("City ID: ")
        address_1_1 = classes.City(name, city_id)
        print(address_1_1.insert())
        return address()

    elif address() == "3":
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        new_data = input("New date: ")
        if column_name.lower() == "id":
            print(classes.Address.address_update_id(int(old_data), int(new_data)))

        else:
            print(classes.Address.address_update(column_name.lower(), old_data, new_data))

        return address()

    elif address_1 == "4":
        table = "address"
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        if column_name.lower() == "id":
            print(classes.Address.delete_id(int(old_data)))

        else:
            print(classes.Address.delete(table, column_name.lower(), old_data))

        return address()

    elif address_1 == "0":
        return main()
    else:
        print("""
            ----------------------------------\n
             BUNDAY SERVIS XIZMATI MAVJUD EMAS
            -----------------------------------\n
            """)
    return address()


def city():
    city_1 = input("""
            ______________________________\n
                         SERVICES

            ------------------------------\n
                1. SELECT _>
                2. INSERT _>
                3. UPDATE _>
                4. DELETE _>
                0. Back _>

                    """)

    if city_1 == "1":
        if len(classes.City.select("city")) == 0:
            print("""
                ------------------------------\n
                    MA'LUMOTLAR MAVJUD EMAS
                ------------------------------\n
                    """)

        else:
            for i in classes.City.select("city"):
                print(f"""
                                    ID: {i[0]}
                                    Name: {i[1]}
                                    Countr_id: {i[2]}
                                    Create Date: {i[3]}
                                """)
        return city()

    elif city_1 == "2":
        name = input("Name: ")
        county_id = input("County ID: ")
        city_1_1 = classes.City(name, county_id)
        print(city_1_1.insert())
        return city()

    elif city_1 == "3":
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        new_data = input("New date: ")
        if column_name.lower() == "id":
            print(classes.City.city_update_id(int(old_data), int(new_data)))

        else:
            print(classes.City.city_update(column_name.lower(), old_data, new_data))

        return city()

    elif city_1 == "4":
        table = "city"
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        if column_name.lower() == "id":
            print(classes.City.delete_id(int(old_data)))

        else:
            print(classes.City.delete(table, column_name.lower(), old_data))

        return city()

    elif city_1 == "0":
        return main()
    else:
        print("""
            ----------------------------------\n
             BUNDAY SERVIS XIZMATI MAVJUD EMAS
            -----------------------------------\n
            """)
    return city()


def payment_status_table():
    payment_status = input("""
        ______________________________\n
                     SERVICES

        ------------------------------\n
            1. SELECT _>
            2. INSERT _>
            3. UPDATE _>
            4. DELETE _>
            0. Back _>

                """)

    if payment_status == "1":
        if len(classes.Payment_status.select("payment_status")) == 0:
            print("""
            ------------------------------\n
                MA'LUMOTLAR MAVJUD EMAS
            ------------------------------\n
                """)

        else:
            for i in classes.Payment_status.select("payment_status"):
                print(f"""
                                ID: {i[0]}
                                Name: {i[1]}
                                Create Date: {i[2]}
                            """)
        return payment_status_table()

    elif payment_status == "2":
        name = input("Name: ")
        payment_status = classes.Payment_status(name)
        print(payment_status.insert())
        return payment_status_table()

    elif payment_status == "3":
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        new_data = input("New date: ")
        if column_name.lower() == "id":
            print(classes.Payment_status.payment_status_update_id(int(old_data), int(new_data)))

        else:
            print(classes.Payment_status.payment_status_update(column_name.lower(), old_data, new_data))

        return payment_status_table()

    elif payment_status == "4":
        table = "payment_type"
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        if column_name.lower() == "id":
            print(classes.Payment_status.delete_id(int(old_data)))

        else:
            print(classes.Payment_status.delete(table, column_name.lower(), old_data))

        return payment_status_table()

    elif payment_status == "0":
        return main()
    else:
        print("""
        ----------------------------------\n
         BUNDAY SERVIS XIZMATI MAVJUD EMAS
        -----------------------------------\n
        """)
    return payment_status_table()


def payment_type_table():
    payment_type = input("""
            ______________________________\n
                         SERVICES

            ------------------------------\n
            1. SELECT _>
            2. INSERT _>
            3. UPDATE _>
            4. DELETE _>
            0. Back _>

            """)

    if payment_type == "1":
        if len(classes.Payment_type.select("payment_type")) == 0:
            print("""
                    ------------------------------\n
                        MA'LUMOTLAR MAVJUD EMAS
                    ------------------------------\n
                    """)

        else:
            for i in classes.Payment_type.select("payment_type"):
                print(f"""
                            ID: {i[0]}
                            Name: {i[1]}
                            Create Date: {i[2]}
                        """)
        return payment_type_table()

    elif payment_type == "2":
        name = input("Name: ")
        payment_type = classes.Payment_type(name)
        print(payment_type.insert())
        return payment_type_table()

    elif payment_type == "3":
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        new_data = input("New date: ")
        if column_name.lower() == "id":
            print(classes.Payment_type.payment_type_update_id(int(old_data), int(new_data)))

        else:
            print(classes.Payment_type.payment_type_update(column_name.lower(), old_data, new_data))

        return payment_type_table()

    elif payment_type == "4":
        table = "payment_type"
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        if column_name.lower() == "id":
            print(classes.Payment_type.delete_id(int(old_data)))

        else:
            print(classes.Payment_type.delete(table, column_name.lower(), old_data))

        return payment_type_table()

    elif payment_type == "0":
        return main()
    else:
        print("""
        ----------------------------------\n
         BUNDAY SERVIS XIZMATI MAVJUD EMAS
        -----------------------------------\n
        """)
    return payment_type_table()


def customer_table():
    customer = input("""
            ______________________________\n
                     SERVICES

            ------------------------------\n
            1. SELECT _>
            2. INSERT _>
            3. UPDATE _>
            4. DELETE _>
            0. Back _>

        """)

    if customer == "1":
        if len(classes.Customer.select("customer")) == 0:
            print("""
                ------------------------------\n
                    MA'LUMOTLAR MAVJUD EMAS
                ------------------------------\n
                """)
        else:
            for i in classes.Customer.select("customer"):
                print(f"""
                        ID: {i[0]}
                        First Name: {i[1]}
                        Last Name: {i[2]}
                        Password: {i[3]}
                        Email: {i[4]}
                        Birth Date: {i[5]}
                        Create Date: {i[7]}
                    """)

        return customer_table()

    elif customer == "2":
        first_name = input("First_name: ")
        last_name = input("Last_name: ")
        password = input("Parol oylab toping ‣‣: ")
        password_1 = input("Oylab topgan parolingizni yana bir bor kiriting ‣‣: ")
        while password != password_1:
            print("Kiritilgan parolar bir xil bolishi kerak")
            print("Iltimos bir xiligni tekshiring!:")
            password_1 = input("Kiritish ‣‣:")
        email = input("Email: ")
        a = ["@gmail.com", "@gmail.ru", "@mail.com", "@mail.ru"]
        k = True
        while k:
            if not (email.endswith(a[0]) or email.endswith(a[1]) or email.endswith(a[2]) or email.endswith(a[3])):
                print("""
                        Namuna: qwert123@gmail.com \n 
                        """)
                print("@gmail.com kiritilgan bolishi shart !!")
                email = input("@gmail: oylab toping  ")
            else:
                k = False
        birth_date = input("Birth Date: ")
        customer = classes.Customer(first_name, last_name, password, email, birth_date)
        print(customer.insert())
        return customer_table()

    elif customer == "3":
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        new_data = input("New date: ")
        if column_name.lower() == "id":
            print(classes.Customer.customer_id(int(old_data), int(new_data)))

        else:
            print(classes.Customer.customer_update(column_name.lower(), old_data, new_data))

        return customer_table()

    elif customer == "4":
        table = "customer"
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        if column_name.lower() == "id":
            print(classes.Customer.delete_id(int(old_data)))

        else:
            print(classes.Customer.delete(table, column_name.lower(), old_data))

        return customer_table()

    elif customer == "0":
        return main()

    else:
        print("""
                ----------------------------------\n
                 BUNDAY SERVIS XIZMATI MAVJUD EMAS
                -----------------------------------\n
                """)
        return customer_table()

def country_table():
    country = input("""
            ______________________________\n
                     SERVICES

            ------------------------------\n
            1. SELECT _>
            2. INSERT _>
            3. UPDATE _>
            4. DELETE _>
            0. Back _>

        """)

    if country == "1":
        if len(classes.Country.select("country")) == 0:
            print("""
                ------------------------------\n
                    MA'LUMOTLAR MAVJUD EMAS
                ------------------------------\n
                """)

        else:
            for i in classes.Country.select("country"):
                print(f"""
                        ID: {i[0]}
                        Name: {i[1]}
                        Create Date: {i[2]}
                    """)
        return country_table()

    elif country == "2":
        name = input("Name: ")
        country = classes.Country(name)
        print(country.insert())
        return country_table()

    elif country == "3":
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        new_data = input("New date: ")
        if column_name.lower() == "id":
            print(classes.Country.country_update_id(int(old_data), int(new_data)))

        else:
            print(classes.Country.country_update(column_name.lower(), old_data, new_data))

        return country_table()

    elif country == "4":
        table = "country"
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        if column_name.lower() == "id":
            print(classes.Country.delete_id(int(old_data)))

        else:
            print(classes.Country.delete(table, column_name.lower(), old_data))

        return country_table()

    elif country == "0":
        return main()
    else:
        print("""
        ----------------------------------\n
         BUNDAY SERVIS XIZMATI MAVJUD EMAS
        -----------------------------------\n
        """)
    return country_table()


def color_table():
    color_s = input("""
        ______________________________\n
                 SERVICES

        ------------------------------\n
        1. SELECT _>
        2. INSERT _>
        3. UPDATE _>
        4. DELETE _>
        0. Back _>

    """)

    if color_s == "1":
        if len(classes.Color.select("color")) == 0:
            print("""
            ------------------------------\n
                MA'LUMOTLAR MAVJUD EMAS
            ------------------------------\n
            """)

        else:
            for i in classes.Color.select("color"):
                print(f"""
                    ID: {i[0]}
                    Name: {i[1]}
                """)
        return color_table()

    elif color_s == "2":
        name = input("Name: ")
        color = classes.Color(name)
        print(color.insert())
        return color_table()

    elif color_s == "3":
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        new_data = input("New date: ")
        if column_name.lower() == "id":
            print(classes.Color.color_update_id(int(old_data), int(new_data)))

        else:
            print(classes.Color.color_update(column_name.lower(), old_data, new_data))

        return color_table()

    elif color_s == "4":
        table = "color"
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        if column_name.lower() == "id":
            print(classes.Color.delete_id(int(old_data)))

        else:
            print(classes.Color.delete(table, column_name.lower(), old_data))

        return color_table()

    elif color_s == "0":
        return main()
    else:
        print("""
        ----------------------------------\n
         BUNDAY SERVIS XIZMATI MAVJUD EMAS
        -----------------------------------\n
        """)
    return color_table()




def product__detail():
    product_detail = input("""
        ______________________________\n
                 SERVICES

        ------------------------------\n
        1. SELECT _>
        2. INSERT _>
        3. UPDATE _>
        4. DELETE _>
        0. Back _>

    """)

    if product_detail == "1":
        if len(classes.ProductDetail.select("product_detail")) == 0:
            print("""
            ------------------------------\n
                MA'LUMOTLAR MAVJUD EMAS
            ------------------------------\n
            """)
        else:
            for i in classes.ProductDetail.select("product_detail"):
                print(f"""
                    ID: {i[0]}
                    Name: {i[1]}
                    Description: {i[2]}
                    price: {i[3]}
                    Count: {i[5]}
                    Rating: {i[7]}
                    Create Date: {i[8]}
                """)

        return product__detail()

    elif product_detail == "2":
        name = input("Name: ")
        description = input("Description: ")
        price = input("Price: ")
        count = input("Count: ")
        rating = input("Rating: ")
        product = classes.ProductDetail(name, description, price, count, rating)
        print(product.insert())
        return product__detail()

    elif product_detail == "3":
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        new_data = input("New date: ")
        if column_name.lower() == "id":
            print(classes.ProductDetail.product_detail_id(int(old_data), int(new_data)))

        else:
            print(classes.ProductDetail.product_detail_update(column_name.lower(), old_data, new_data))

        return product__detail()

    elif product_detail == "4":
        table = "product_detail"
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        if column_name.lower() == "id":
            print(classes.ProductDetail.delete_id(int(old_data)))

        else:
            print(classes.ProductDetail.delete(table, column_name.lower(), old_data))

        return product__detail()

    elif product_detail == "0":
        return main()

    else:
        print("""
            ----------------------------------\n
             BUNDAY SERVIS XIZMATI MAVJUD EMAS
            -----------------------------------\n
            """)
        return product__detail()

def product_table():
    product = input("""
        ______________________________\n
                 SERVICES

        ------------------------------\n
        1. SELECT _>
        2. INSERT _>
        3. UPDATE _>
        4. DELETE _>
        0. Back _>
        """)

    if product == "1":
        if len(classes.Product.select("product")) == 0:
            print("""
                ------------------------------\n
                    MA'LUMOTLAR MAVJUD EMAS
                ------------------------------\n

                """)
        else:
            for i in classes.Product.select("product"):
                print(f"""
                        ID: {i[0]}
                        Product Name: {i[1]}
                        Create Date: {i[3]}
                    """)

        return product_table()

    elif product == "2":
        name = input("Name: ")
        product = classes.Product(name)
        print(product.insert())
        return product_table()

    elif product == "3":
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        new_data = input("New date: ")
        if column_name.lower() == "id":
            print(classes.Product.product_update_id(int(old_data), int(new_data)))

        else:
            print(classes.Product.product_update(column_name.lower(), old_data, new_data))

        return product_table()

    elif product == "4":
        table = input("Table name: ")
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        if column_name.lower() == "id":
            print(classes.Category.delete_id(int(old_data)))

        else:
            print(classes.Category.delete(table, column_name.lower(), old_data))

        return product_table()

    elif product == "0":
        return main()

    else:
        print("""
            ----------------------------------\n
             BUNDAY SERVIS XIZMATI MAVJUD EMAS
            -----------------------------------\n
            """)
    return product_table()


def category_table():
    servic = input("""
    ______________________________\n
             SERVICES
               
    ------------------------------\n
    1. SELECT _>
    2. INSERT _>
    3. UPDATE _>
    4. DELETE _>
    0. Back _>
    """)

    if servic == "1":
        if len(classes.Category.select("category")) == 0:
            print("""
            ------------------------------\n
                MA'LUMOTLAR MAVJUD EMAS
            ------------------------------\n
            
            """)
        else:
            for i in classes.Category.select("category"):
                print(f"""
                    ID: {i[0]}
                    Name: {i[1]}
                    Last Update: {i[2]}
                    Create Date: {i[3]}
                """)

        return category_table()

    elif servic == "2":
        name = input("Name: ")
        category = classes.Category(name)
        print(category.insert())
        return category_table()

    elif servic == "3":
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        new_data = input("New date: ")
        if column_name.lower() == "id":
            print(classes.Category.update_id(int(old_data), int(new_data)))

        else:
            print(classes.Category.update(column_name.lower(), old_data, new_data))

        return category_table()

    elif servic == "4":
        table = input("Table name: ")
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        if column_name.lower() == "id":
            print(classes.Category.delete_id(int(old_data)))

        else:
            print(classes.Category.delete(table, column_name.lower(), old_data))

        return category_table()

    elif servic == "0":
        return main()

    else:
        print("""
        ----------------------------------\n
         BUNDAY SERVIS XIZMATI MAVJUD EMAS
        -----------------------------------\n
        """)
    return category_table()



def main():
    tables = input("""
    1. Category _>
    2. Product _>
    3. Product Detail _>
    4. Color _>
    5. Country _>
    6. Customer _>
    7. Payment Type _>
    8. Payment Status _>
    9. City _>
    10. Address _>
    """)

    if tables == '1':
        return category_table()

    elif tables == '2':
        return product_table()

    elif tables == '3':
        return product__detail()

    elif tables == '4':
        return color_table()

    elif tables == '5':
        return country_table()

    elif tables == '6':
        return customer_table()

    elif tables == '7':
        return payment_type_table()

    elif tables == '8':
        return payment_status_table()

    elif tables == '9':
        return city()

    elif tables == '10':
        return address()

    else:
        print("""
        --------------------------------\n
            BUNDAY SERVIS MAVJUD EMAS
        --------------------------------\n
        """)
        return main()


if __name__ == '__main__':
    main()