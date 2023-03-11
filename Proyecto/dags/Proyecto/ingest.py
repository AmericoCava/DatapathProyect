import process.name as n
from process.extract import Extract
from process.load import Load

extract = Extract()
load = Load()

df_categories = extract.read_adls("retail","categories", n.categories)
df_customer = extract.read_adls("retail","customer", n.customer)
df_departments = extract.read_adls("retail","departments", n.departments)
df_order_items = extract.read_adls("retail","order_items", n.order_items)
df_orders = extract.read_adls("retail","orders", n.orders)
df_products = extract.read_xml("/opt/airflow/dags/Proyecto/process/resource/products.xml")

load.load_to_adls(df_categories,"datalake", "americo/landing/categories")
load.load_to_adls(df_customer,"datalake", "americo/landing/customer")
load.load_to_adls(df_departments,"datalake", "americo/landing/departments")
load.load_to_adls(df_order_items,"datalake", "americo/landing/order_items")
load.load_to_adls(df_orders,"datalake", "americo/landing/orders")
load.load_to_adls(df_products,"datalake", "americo/landing/products")
