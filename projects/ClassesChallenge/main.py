import pandas as pd
from datetime import datetime
from Pipe import Pipe
from General_Data import General_Data
from Customer import Customer
from Order import Order
from Product import Product

database = pd.read_csv(r'.\dataset\dataset.csv', encoding='utf-8')
dataframe = Pipe(database)

general_data = General_Data()
customer = Customer(general_data)
order = Order(general_data)
product = Product(general_data)

# for x in range(5):
while not dataframe.data.empty:
    row = dataframe.separate_lifo_data()
    row = General_Data.replace_column_value(row)

    general_data.customer_id = row['customer_id']
    general_data.customer_zip_code_prefix = int(row['customer_zip_code_prefix'])
    general_data.customer_city = row['customer_city']
    general_data.customer_state = row['customer_state']

    general_data.order_id = row['order_id']
    general_data.order_purchase_timestamp = datetime.strptime(row['order_purchase_timestamp'], '%Y-%m-%d %H:%M:%S')
    general_data.order_approved_at = datetime.strptime(row['order_approved_at'], '%Y-%m-%d %H:%M:%S')

    general_data.product_id = row['product_id']
    general_data.product_category_name = row['product_category_name']
    general_data.product_weight_g = float(row['product_weight_g'])
    general_data.product_length_cm = float(row['product_length_cm'])
    general_data.product_height_cm = float(row['product_height_cm'])
    general_data.product_width_cm = float(row['product_width_cm'])


    # customer.display_data()
    # customer.is_empty()
    # customer.get_zip_code_data(customer.customer_zip_code_prefix)
    # customer.validate_city_state(customer.customer_zip_code_prefix, customer.customer_city, customer.customer_state)


    # order.display_data()
    # order.is_empty()
    # order.approval_delay(order.order_purchase_timestamp, order.order_approved_at)


    # product.display_data()
    # product.is_empty()
    # product.calculate_cubage(product.product_height_cm, product.product_width_cm, product.product_length_cm)


    dataframe.remove_data_from_dataframe()