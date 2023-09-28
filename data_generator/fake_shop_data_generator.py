import csv
import random
from faker import Faker
from datetime import datetime

fake = Faker()

# Function to generate fake data for customers
def generate_customers(num_customers):
    customers = []
    for i in range(num_customers):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = f"{first_name.lower()}.{last_name.lower()}@example.com"
        address = fake.street_address()
        city = fake.city()
        post_code = fake.postcode()
        email_marketing_status = fake.random_element(elements=['opted_in', 'opted_out'])
        if email_marketing_status == 'opted_out':
            email_opted_out_date = fake.date_time_this_year()
        else:
            email_opted_out_date = None

        customer = {
            'id': i + 1,
            'created_at': fake.date_time_this_decade(),
            'updated_at': fake.date_time_this_month(),
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'address': address,
            'city': city,
            'post_code': post_code,
            'email_marketing_status': email_marketing_status,
            'email_opted_out_date':email_opted_out_date
        }
        customers.append(customer)

    return customers

# Function to generate fake data for categories
def generate_categories():
    categories = [
        {'id': 1, 'created_at': fake.date_time_this_decade(), 'updated_at': fake.date_time_this_month(), 'name': 'Home & Kitchen'},
        {'id': 2, 'created_at': fake.date_time_this_decade(), 'updated_at': fake.date_time_this_month(), 'name': 'Beauty & Personal Care'},
        {'id': 3, 'created_at': fake.date_time_this_decade(), 'updated_at': fake.date_time_this_month(), 'name': 'Clothing, Shoes & Jewelry'},
        {'id': 4, 'created_at': fake.date_time_this_decade(), 'updated_at': fake.date_time_this_month(), 'name': 'Toys & Games'},
        {'id': 5, 'created_at': fake.date_time_this_decade(), 'updated_at': fake.date_time_this_month(), 'name': 'Health, Household & Baby Care'},
        {'id': 6, 'created_at': fake.date_time_this_decade(), 'updated_at': fake.date_time_this_month(), 'name': 'Baby'},
        {'id': 7, 'created_at': fake.date_time_this_decade(), 'updated_at': fake.date_time_this_month(), 'name': 'Electronics'},
        {'id': 8, 'created_at': fake.date_time_this_decade(), 'updated_at': fake.date_time_this_month(), 'name': 'Sports & Outdoors'},
        {'id': 9, 'created_at': fake.date_time_this_decade(), 'updated_at': fake.date_time_this_month(), 'name': 'Pet Supplies'},
        {'id': 10, 'created_at': fake.date_time_this_decade(), 'updated_at': fake.date_time_this_month(), 'name': 'Office Supplies'},
    ]
    return categories

# Function to generate random product names using adjectives and nouns
def generate_product_name(category_name):
    if category_name == 'Home & Kitchen':
        adjectives = ['Stylish', 'Modern', 'Elegant', 'Premium', 'Functional', 'Compact', 'Versatile', 'Durable', 'Ergonomic', 'Sleek']
        nouns = ['Blender', 'Coffee Maker', 'Dinner Set', 'Cutting Board', 'Pillow', 'Towel', 'Rug', 'Curtain', 'Lamp', 'Vacuum Cleaner']

    elif category_name == 'Beauty & Personal Care':
        adjectives = ['Luxurious', 'Natural', 'Refreshing', 'Gentle', 'Nourishing', 'Invigorating', 'Fragrant', 'Hydrating', 'Rejuvenating', 'Silky']
        nouns = ['Lipstick', 'Moisturizer', 'Hair Dryer', 'Razor', 'Perfume', 'Nail Polish', 'Face Mask', 'Shampoo', 'Conditioner', 'Toothbrush']

    elif category_name == 'Clothing, Shoes & Jewelry':
        adjectives = ['Trendy', 'Classic', 'Stylish', 'Elegant', 'Comfortable', 'Chic', 'Fashionable', 'Dazzling', 'Casual', 'Sophisticated']
        nouns = ['Dress', 'Sneakers', 'Earrings', 'Watch', 'Jacket', 'Jeans', 'Necklace', 'Handbag', 'Sunglasses', 'Ring']

    elif category_name == 'Toys & Games':
        adjectives = ['Fun', 'Educational', 'Interactive', 'Entertaining', 'Imaginative', 'Colorful', 'Engaging', 'Creative', 'Exciting', 'Challenging']
        nouns = ['Puzzle', 'Doll', 'Building Blocks', 'Ball', 'Board Game', 'Stuffed Animal', 'Action Figure', 'Playset', 'Remote Control Car', 'Educational Toy']

    elif category_name == 'Health, Household & Baby Care':
        adjectives = ['Healthy', 'Safe', 'Gentle', 'Eco-friendly', 'Effective', 'Hypoallergenic', 'Antibacterial', 'Natural', 'Non-Toxic', 'Odorless']
        nouns = ['Vitamin', 'Disinfectant', 'Diaper', 'Baby Wipes', 'Thermometer', 'First Aid Kit', 'Laundry Detergent', 'Toothpaste', 'Air Purifier', 'Cleaning Cloth']

    elif category_name == 'Baby':
        adjectives = ['Adorable', 'Soft', 'Comfortable', 'Practical', 'Portable', 'Lightweight', 'Cozy', 'Reversible', 'Adjustable', 'Easy-to-clean']
        nouns = ['Stroller', 'Baby Monitor', 'Bib', 'High Chair', 'Pacifier', 'Baby Bottle', 'Teething Toy', 'Crib', 'Baby Carrier', 'Diaper Bag']

    elif category_name == 'Electronics':
        adjectives = ['High-Tech', 'Cutting-edge', 'Advanced', 'Sleek', 'Portable', 'Powerful', 'Innovative', 'User-friendly', 'Smart', 'Multifunctional']
        nouns = ['Smartphone', 'Laptop', 'Smartwatch', 'Headphones', 'Tablet', 'Camera', 'TV', 'Gaming Console', 'Bluetooth Speaker', 'Wireless Earbuds']

    elif category_name == 'Sports & Outdoors':
        adjectives = ['Active', 'Outdoor', 'Sturdy', 'Waterproof', 'Lightweight', 'Durable', 'Breathable', 'Athletic', 'Resilient', 'Adventure-ready']
        nouns = ['Bicycle', 'Camping Tent', 'Yoga Mat', 'Dumbbells', 'Running Shoes', 'Fishing Rod', 'Backpack', 'Swimming Goggles', 'Hiking Boots', 'Soccer Ball']

    elif category_name == 'Pet Supplies':
        adjectives = ['Pet-friendly', 'Paw-some', 'Furry', 'Interactive', 'Pet-safe', 'Chewable', 'Comfy', 'Entertaining', 'Durable', 'Odor-resistant']
        nouns = ['Cat Tree', 'Dog Bed', 'Pet Carrier', 'Food Bowl', 'Cat Litter Box', 'Chew Toy', 'Grooming Brush', 'Bird Cage', 'Aquarium', 'Hamster Wheel']

    elif category_name == 'Office Supplies':
        adjectives = ['Productive', 'Organized', 'Efficient', 'Sleek', 'Professional', 'Functional', 'Reliable', 'Ergonomic', 'Practical', 'Space-saving']
        nouns = ['Desk Organizer', 'Notebooks', 'Ballpoint Pen', 'Stapler', 'Whiteboard', 'File Folder', 'Calculator', 'Paper Shredder', 'Sticky Notes', 'Desk Lamp']

    product_name = f'{random.choice(adjectives)} {random.choice(nouns)}'
    return product_name.capitalize()

# Function to generate fake data for products
def generate_products(num_products, categories):
    products = []
    for product_id in range(1, num_products + 1):
        category = random.choice(categories)
        category_id = category['id']
        product_name = generate_product_name(category['name'])
        product_description = f'{product_name} - {fake.sentence(nb_words=6, variable_nb_words=True)}'
        price = round(random.uniform(10, 250), 2)
        sale_price = round(price * random.uniform(0.7, 0.9), 2)
        in_stock = random.choice([True, False])
        on_sale = random.choice([True, False])
        products.append({
            'id': product_id,
            'created_at': fake.date_time_this_decade(),
            'updated_at': fake.date_time_this_month(),
            'name': product_name,
            'description': product_description,
            'price': price,
            'sale_price': sale_price,
            'in_stock': in_stock,
            'on_sale': on_sale,
            'category_id': category_id
        })
    return products

# Function to generate fake data for orders and order_items
def generate_orders_and_items(num_orders, customers, products):
    orders = []
    order_items = []
    for order_id in range(1, num_orders + 1):
        customer_id = random.choice(customers)['id']
        order_total = 0
        num_items = random.randint(1, 5)
        created_at = fake.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S')
        updated_at = fake.date_time_this_month().strftime('%Y-%m-%d %H:%M:%S')
        for _ in range(num_items):
            product = random.choice(products)
            product_id = product['id']
            quantity = random.randint(1, 10)
            if product['on_sale']:
                item_total = product['sale_price'] * quantity
            else:
                item_total = product['price'] * quantity
            order_total += item_total
            order_items.append({
                'id': len(order_items) + 1,
                'created_at': created_at,
                'updated_at': updated_at,
                'order_id': order_id,
                'product_id': product_id,
                'quantity': quantity
            })
        payment_method = random.choice(['credit_card', 'paypal', 'bank_transfer'])
        order_status = random.choice(['pending', 'accepted', 'rejected', 'delivered', 'refunded'])
        orders.append({
            'id': order_id,
            'created_at': created_at,
            'updated_at': updated_at,
            'customer_id': customer_id,
            'order_total': order_total,
            'payment_method': payment_method,
            'order_status': order_status
        })
    return orders, order_items

# Function to generate fake data for refunds
def generate_refunds(orders):
    refund_reasons = ['Damaged Product', 'Wrong Item Shipped', 'Product Not as Described', 'Unsatisfied with Product', 'Duplicate Order']
    refunds = []
    for order in orders:
        if order['order_status'] == 'refunded':
            refund_id = order['id']
            amount_refunded = round(random.uniform(1, order['order_total']), 2)
            refund_reason = random.choice(refund_reasons)
            order_date = datetime.strptime(order['created_at'],'%Y-%m-%d %H:%M:%S')
            
            refunds.append({
                'id': refund_id,
                'created_at': fake.date_between(order_date),
                'updated_at': fake.date_between(order_date),
                'order_id': order['id'],
                'amount_refunded': amount_refunded,
                'refund_reason': refund_reason
            })
    return refunds

def generate_emails(customers):
    emails = []
    email_id = 1

    for customer in customers:
        if random.random() < 0.6:  # 60% chance of a customer receiving an email
            num_emails = random.randint(1, 3)  # Random number of emails for each customer (1 to 3)
            for _ in range(num_emails):
                sent_date = fake.date_time_this_year()
                subject = f"Special Offer for {customer['first_name']}"
                opened = random.choice([True, False])
                clicked = random.choice([True, False])

                email = {
                    'id': email_id,
                    'customer_id': customer['id'],
                    'sent_date': sent_date,
                    'subject': subject,
                    'opened': opened,
                    'clicked': clicked,
                }
                emails.append(email)
                email_id += 1

    return emails

if __name__ == '__main__':
    num_customers = 500
    num_products = 500
    num_orders = 1000

    customers = generate_customers(num_customers)
    categories = generate_categories()
    products = generate_products(num_products, categories)
    orders, order_items = generate_orders_and_items(num_orders, customers, products)
    refunds = generate_refunds(orders)
    emails = generate_emails(customers)

    # Save data to CSV files
    with open('customers.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'created_at', 'updated_at', 'first_name', 'last_name', 'email', 'address', 'city', 'post_code', 'email_marketing_status', 'email_opted_out_date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(customers)

    with open('categories.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'created_at', 'updated_at', 'name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(categories)

    with open('products.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'created_at', 'updated_at', 'name', 'description', 'price', 'sale_price', 'in_stock', 'on_sale', 'category_id']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)

    with open('orders.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'created_at', 'updated_at', 'customer_id', 'order_total', 'payment_method', 'order_status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(orders)

    with open('order_items.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'created_at', 'updated_at', 'order_id', 'product_id', 'quantity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(order_items)

    with open('refunds.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'created_at', 'updated_at', 'order_id', 'amount_refunded', 'refund_reason']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(refunds)
        
    with open('emails.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'customer_id', 'sent_date', 'subject', 'opened', 'clicked']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(emails)

