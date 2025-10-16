# 🚛 Driver Log System

A modern, professional Django web application for managing daily driver logs with comprehensive inventory tracking and vehicle management.


## ✨ Features

### 📊 Core Functionality
- **👤 User Authentication** - Secure login/register system with session management
- **📝 Driver Log Management** - Complete daily driver log creation and tracking
- **🚛 Multi-Truck Support** - Support for multiple trucks with individual tracking
- **🖼️ Image Documentation** - Upload truck and ThermoKing unit photos (6+3 images per log)

### 🎯 Advanced Features
- **📋 Smart Checklists** - Comprehensive pre-trip inspection checklists
- **📦 Dynamic Inventory** - Multiple inventory items per airway bill with real counts
- **📈 Real-time Tracking** - Fuel levels, DEF levels, mileage, and ThermoKing hours
- **🔍 Search & Filter** - Easy log retrieval and management

## 🛠️ Technology Stack

| Layer | Technology |
|-------|------------|
| **Backend** | 🐍 Django 5.0.6 |
| **Frontend** | 🎨 Bootstrap 5.3 + Crispy Forms |
| **Database** | 💾 SQLite (Dev) / PostgreSQL (Prod) |
| **Authentication** | 🔐 Django Auth System |
| **File Handling** | 🖼️ Pillow (Image processing) |
| **Deployment Ready** | 🚀 Gunicorn + Whitenoise |

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- pip (Python package manager)

### Installation

1. **📥 Clone the Repository**
   ```bash
   git clone https://github.com/dsmxyz/Driver-log.git
   cd Driver-log
   ```

2. **🐍 Set Up Virtual Environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Mac/Linux
   source venv/bin/activate
   ```

3. **📦 Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **⚙️ Configure Database**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **👑 Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **🎯 Run Development Server**
   ```bash
   python manage.py runserver
   ```

7. **🌐 Access Application**
   - Main App: http://localhost:8000
   - Admin Panel: http://localhost:8000/admin

## 🤝 Contributing

We welcome contributions! Please:

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🔀 Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Built with ❤️ using Django & Bootstrap**

*Making driver log management modern and efficient* 🚛✨

</div>

## 📞 Contact

- **GitHub**: [@dsmxyz](https://github.com/dsmxyz)
- **Project Link**: [https://github.com/dsmxyz/Driver-log](https://github.com/dsmxyz/Driver-log)

---

*If you find this project helpful, don't forget to give it a ⭐ star on GitHub!*
