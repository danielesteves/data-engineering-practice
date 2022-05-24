from datetime import datetime
import psycopg2
import csv
import datetime


def main():
    host = 'postgres'
    database = 'postgres'
    user = 'postgres'
    pas = 'postgres'
    conn = psycopg2.connect(host=host, database=database, user=user, password=pas)
    # your code here

    SQL_INSERT_ACCOUNT = "INSERT INTO account (customer_id, first_name, last_name, address_1, address_2, city, state, zip_code, join_date) VALUES (%(customer_id)s, %(first_name)s, %(last_name)s, %(address_1)s, %(address_2)s, %(city)s, %(state)s, %(zip_code)s, %(join_date)s)"
    SQL_INSERT_PRODUCT = "INSERT INTO product (product_id, product_code, product_description) VALUES (%(product_id)s, %(product_code)s, %(product_description)s)"
    SQL_INSERT_TRANSACTION = "INSERT INTO transaction (transaction_id, transaction_date, product_id, product_code, product_description, quantity, account_id) VALUES (%(transaction_id)s, %(transaction_date)s, %(product_id)s, %(product_code)s, %(product_description)s, %(quantity)s, %(account_id)s)"


    def create_database(cur):
        cur.execute(open("schema.sql", "r").read())

    def do_inserts(cur):
        #reading accounts file
        with open('./data/accounts.csv') as accounts_file:
            accounts = csv.DictReader(accounts_file, skipinitialspace=True)
            for a_account in accounts:
                insert_account(cur, a_account)
        
        with open('./data/products.csv') as products_file:
            products = csv.DictReader(products_file, skipinitialspace=True)
            for a_product in products:
                insert_product(cur, a_product)

        with open('./data/transactions.csv') as transactions_file:
            transactions = csv.DictReader(transactions_file, skipinitialspace=True)
            for a_transaction in transactions:
                insert_transaction(cur, a_transaction)

    def insert_account(cur, account):
        account['join_date'] = date_to_datetime(account['join_date'])
        cur.execute(SQL_INSERT_ACCOUNT, account)

    def insert_product(cur, product):
        cur.execute(SQL_INSERT_PRODUCT, product)

    def insert_transaction(cur, transaction):
        transaction["transaction_date"] = date_to_datetime(transaction["transaction_date"])
        cur.execute(SQL_INSERT_TRANSACTION, transaction)

    def date_to_datetime(a_date):
        return datetime.date(int(a_date[0:4]), int(a_date[5:7]), int(a_date[8:10]))

    with conn.cursor() as cur:
        create_database(cur)

        do_inserts(cur)

        conn.commit()
        cur.close()
        conn.close()



if __name__ == '__main__':
    main()
