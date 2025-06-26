# 🚗 Vintage Vogue Car Rental

**Vintage Vogue** is a stylish and user-friendly car rental web application built using **Flask** and **HTML/CSS**. It provides an elegant interface for exploring and booking premium and vintage cars for rent.

---

## 🛠️ Features

- 🌐 **Homepage** with animated car video background
- 🚘 **Explore Cars**: Browse featured vehicles with detailed specs and rental pricing
- 📄 **About Us**: Learn about the company's mission and story
- 📰 **Blog Section**: Explore recent news and insights
- 📅 **Booking Form**: Fill in details to reserve a car
- 🧾 **Payment Gateway UI** (UI only, mock)
- 🔐 **Signup Page** for user registration
- ✅ **Success Page** UI with animation for post-payment confirmation
- 🗃️ **Data Persistence** using SQLite3

---

## 🧰 Tech Stack

| Layer        | Technology       |
|--------------|------------------|
| Backend      | Python (Flask)   |
| Frontend     | HTML, CSS        |
| Database     | SQLite3          |
| Template Engine | Jinja2        |

---

## 📂 Project Structure

```
├── app_1.py               # Main Flask application
├── templates/
│   ├── index.html         # Homepage
│   ├── Explore_car.html   # Explore car listings
│   ├── AboutUs.html       # About page
│   ├── Blog.html          # Blog section
│   ├── form.html          # Booking form
│   ├── paymentPage.html   # Payment gateway UI
│   ├── successPage.html   # Payment success UI
│   ├── Signin.html        # Signup page
├── static/
│   ├── css/
│   ├── images/
│   └── js/
├── Form.db                # Database for car rental form submissions
├── Signup.db              # Database for signup info
```

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.x
- Flask

### 📦 Install Dependencies

```bash
pip install flask
```

### ▶️ Run the Application

```bash
python app_1.py
```

Visit http://localhost:2389 in your browser.

---

## 🛡️ Security Notes

- Passwords are currently stored in plaintext. For production, use **hashing** (e.g., `werkzeug.security.generate_password_hash`).
- Payment gateway is a **UI prototype** and does not perform real transactions.
- CSRF protection are not implemented yet.

---

## ✍️ Contributions

Feel free to fork this project and submit pull requests for improvements like:

- Adding login functionality
- Integrating a real payment gateway (e.g., Razorpay, Stripe)
- Enhancing form validations
- Adding user dashboards