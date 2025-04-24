![Hungry_Tiger](https://github.com/user-attachments/assets/e534bd06-de2e-45d9-9ebf-9fac514df9da)

# Hungry Tiger interview-task
<h2>Advanced Multi-Tenant E-commerce API with Role-Based Access Control (RBAC)</h2>

<br />
<br />

<h2>✨ Features</h2>
<ul>
  <li>
    <h3><b>Authentication & User Roles:</b></h3>
    <ul>
      <li><h3><b>JWT authentication using djangorestframework-simplejwt</b></h3></li>
      <li>
        <h3>Three distinct user roles:</h3>
        <ul>
          <li><h3><b>Admin:</b> Access to all vendors, products, and orders</h3></li>
          <li><h3><b>Vendor:</b> Management of own products and related orders.</h3></li>
          <li><h3><b>Customer:</b> Product browsing and order placement.</h3></li>
        </ul>
      </li>
    </ul>
  </li>
  <li>
    <h3><b>Core Models:</b></h3>
    <ul>
      <li><h3><b>User:</b> Extended Django's built-in User model</h3></li>
      <li><h3><b>Vendor:</b> Linked to User model via ForeignKey</h3></li>
      <li><h3><b>Product:</b> Associated with a specific Vendor</h3></li>
      <li><h3><b>Order:</b> Connected to a Customer with various products</h3></li>
      <li><h3><b>OrderItem:</b> Implements Many-to-Many relationship between Orders & Products</h3></li>
    </ul>
  </li>
</ul>

<br />

<h2>🛠️ Tech Stack</h2>

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
[![Django](https://img.shields.io/badge/Django-%23092E20.svg?logo=django&logoColor=white)](#)
[![DjangoREST](https://img.shields.io/badge/Django%20REST-ff1709?logo=django&logoColor=white&color=ff1709)](#)

<ul>
  <h3><li><b>Backend:</b> Django, Django REST Framework</li></h3>
  <h3><li><b>Authentication:</b> Djoser + JWT (Simple JWT)</li></h3>
  <h3><li><b>Database:</b> SQLite</li></h3>
</ul>

<br />

<h2>📡 REST API Endpoints</h2>

| Method | Endpoint                         | Description                                      |
|--------|----------------------------------|--------------------------------------------------|
| POST   | `/user/register/customer/`       | Customer registration                            |
| POST   | `/user/register/vendor/`         | Vendor registration                              |
| POST   | `/user/login/`                   | JWT token acquisition (login)                    |
| POST   | `/user/token/refresh`            | Acquire a new access token using refresh token   |
| POST   | `/user/token/verify`             | Verify validity of a token                       |
| POST   | `/user/logout/`                  | User logout                                      |
| GET    | `/api/vendors/`                  | List all vendors                                 |
| GET    | `/api/vendors/<id>/`             | Retrieve vendor details                          |
| GET    | `/api/products/`                 | List products                                    |
| POST   | `/api/products/`                 | Create a new product                             |
| GET    | `/api/products/<id>/`            | Retrieve product details                         |
| PUT    | `/api/products/<id>/`            | Update product details                           |
| DELETE | `/api/products/<id>/`            | Delete a product                                 |
| GET    | `/api/orders/`                   | List all orders                                  |
| POST   | `/api/orders/`                   | Create a new order                               |
| GET    | `/api/orders/<id>/`              | Retrieve order details                           |


<br />

<h2>🧪 Local Development</h2>

<h3>1. Clone the repository:</h3>

```bash
git clone https://github.com/sikatanju/hungry-tiger-interview-task.git
```
<h3>2. Navigate to the project directory:</h3>

```bash
cd hungry-tiger-interview-task
```
<h3>3. Create a virtual environment and activate it:</h3>

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```
<h3>4. Install the dependencies:</h3>

```bash
pip install -r requirements.txt
```
<h3>5. Apply migrations and run the development server:</h3>

```bash
python manage.py migrate
python manage.py runserver
```

<br />

<h2>📱 Screenshots</h2>

![chrome_7y9mzLWkzf](https://github.com/user-attachments/assets/cbbc00f2-864e-4831-8257-1f43e178f6f2)
![chrome_vqogtckL9f](https://github.com/user-attachments/assets/3981be9b-79eb-43ad-8f8d-bf9f2c20c84d)
![chrome_GgXvz4cZtU](https://github.com/user-attachments/assets/5829434b-a23f-431b-9e77-29bad68d7bdc)
![chrome_hYdQqlxolr](https://github.com/user-attachments/assets/3719c623-823d-46bb-b309-aa41cef7da61)

<br />



<h2>🤝 Contributing</h2>

<h3>Contributions are welcome! Please feel free to submit a Pull Request.</h3>

<h3>1. Fork the project</p> 
<h3>2. Create your feature branch (git checkout -b feature/AmazingFeature)</p> 
<h3>3. Commit your changes (git commit -m 'Add some AmazingFeature')</p> 
<h3>4. Push to the branch (git push origin feature/AmazingFeature)</p> 
<h3>5. Open a Pull Request</p> 

<br />


