import ingest as i
from process.transform import Transform

transform = Transform()

df_categories = i.df_categories
df_customer = i.df_customer
df_departments = i.df_departments
df_order_items = i.df_order_items
df_orders = i.df_orders
df_products = i.df_products

df_enunciado1 = transform.enunciado1(df_customer, df_orders, df_order_items)
df_enunciado2 = transform.enunciado2(df_order_items, df_products, df_categories)
df_enunciado3 = transform.enunciado3(df_customer, df_orders,df_order_items, df_products, df_categories)
df_enunciado4 = transform.enunciado4(df_customer, df_orders,df_order_items, df_products, df_categories)