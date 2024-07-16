# Install

Install the required libraries if you haven't already:

```bash
pip install sqlalchemy datetime
```

- Ensure you have a JSON file (let's call it **invoice.json**) with the appropriate structure. You can use sample [JSON](../dataset/json/).
- Read the JSON file and parse data from JSON
- Use the [code](../db_storage/save_invoice_to_db.py) to store json data into database using `sqlalchemy`.


Make changes into below function according to your json attributes.

```bash
def save_invoice_to_db(invoice_data):

    invoice = Invoice(
        invoice_number=invoice_data['invoice_number'],
        date=datetime.strptime(invoice_data['date'], '%Y-%m-%d').date(),
        total_amount=invoice_data['amount'],
        vendor_name=invoice_data['issuer']
    )
    session.add(invoice)
    session.commit()
```