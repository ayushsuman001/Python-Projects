# Computer Shop Record Management System

This project implements a simple Record Management System for a computer shop, allowing administrators to perform various operations such as managing customer transactions, editing customer details, managing stock, and handling administrative tasks. The system is implemented in Python and uses MySQL as the database.

## Prerequisites

Before running the system, ensure that you have the following installed:

- Python
- MySQL

## Database Setup

The system uses a MySQL database named `my_project`. Make sure to create this database before running the program. The default admin credentials are '0000' for the username and '1234' for the password.

```sql
CREATE DATABASE my_project;
USE my_project;
CREATE TABLE `admin` (
  `id_` varchar(10) DEFAULT NULL,
  `passwd` varchar(20) DEFAULT NULL
);
INSERT INTO admin VALUES ('0000', '1234');
```

## Running the Program

1. Clone the repository and navigate to the project directory:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. Run the program:

   ```bash
   python your_program_name.py
   ```

3. Enter your MySQL username and password when prompted.

## Features

### 1. Main Menu

- **Transactions:** Perform customer transactions.
- **Customer's Details:** View and manage customer details.
- **Manage Stock:** Handle stock-related operations.
- **Edit Admin:** Modify admin credentials.
- **Return to Admin Login Page:** Log out and return to the login page.
- **Exit:** Exit the program.

### 2. Transactions

- **Purchase an Item:** Add a new customer transaction.
- **See All Transactions:** View all customer transactions.
- **Back to Main Menu:** Return to the main menu.
- **Exit the Program:** Exit the program.

### 3. Purchasing Items

- Enter customer details and item information to make a purchase.
- Total amount to be paid is displayed.
- A purchase ID is generated and displayed.

### 4. Viewing All Transactions

- View all customer transactions stored in the database.

### 5. Customer Details

- **Search for a Customer:** Search for a customer using their purchase ID.
- **Edit Customer Details:** Edit customer information.
- **Delete Customer Data:** Delete customer records.
- **Return to Main Menu:** Return to the main menu.
- **Exit:** Exit the program.

### 6. Editing Customer's Details

- Edit customer name, address, phone number, or email.

### 7. Managing Stock

- **Add Item to Stock:** Add a new item to the stock.
- **Remove Items from Stock:** Remove items from the stock.
- **View Stock:** View the current stock.
- **Back to Main Menu:** Return to the main menu.
- **Exit:** Exit the program.

### 8. Adding Stock

- Enter details of the item to add to the stock.

### 9. Removing Stock

- Enter the name of the product to remove from the stock.

### 10. Viewing Stock

- View all items currently in stock.

### 11. Managing/Administrative Tasks

- **Add Admin:** Add a new admin user.
- **Change Admin Username:** Change the username of an admin.
- **Remove an Admin:** Remove an admin user.
- **Change Admin Password:** Change the password of an admin.
- **Back to Main Menu:** Return to the main menu.
- **Exit:** Exit the program.

### 12. Adding Admin

- Enter a new admin username and password.

### 13. Changing Admin Username

- Enter the current admin username and the new username.

### 14. Removing Admin

- Enter the admin username to be removed.

### 15. Changing Admin Password

- Enter the current admin username and password.
- Enter the new password and confirm it.

**Note:** The default admin credentials are '0000' for the username and '1234' for the password.

## Exiting the Program

To exit the program, choose the "Exit" option from the main menu or any relevant submenu.

Feel free to explore and modify the code according to your needs!
