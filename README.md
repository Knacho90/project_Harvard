# Project

### Video Demo:
[https://youtu.be/lH4P-isr8pw?si=4OlJt-Ve7MWmfhFV]

### Description:
AidGenius is an interactive platform developed in Python that allows users to create accounts, log in, and access a variety of features aimed at enhancing user experience in both educational and everyday activities. This platform offers modules for playing games, performing calculations, managing inventory, and shopping in an online supermarket.

- **User Registration and Login**: Users can register accounts and log in to access personalized content. The login system ensures secure access by validating user credentials.
- **Games Section**: Once logged in, users can play a variety of interactive games, such as rock-paper-scissors and a football penalty shootout game. These games add a fun and engaging element to the platform.
- **Calculator**: The platform also includes a versatile calculator that allows users to perform basic arithmetic operations, making it a handy tool for quick calculations.
- **Inventory Management**: This feature allows users to add, update, and view an inventory of items. This could be useful for keeping track of products in a small business or personal collections.
- **Online Supermarket**: Users can shop for items, add them to a virtual cart, and view the total cost, mimicking a real-world online shopping experience.

### Files Included:
- **project.py**: This is the main file that contains all the functionalities of the platform, including user registration, login, games, calculator, inventory management, and the online supermarket.
- **test_project.py**: This file contains unit tests implemented using `pytest` to ensure that the main functions of the program work as expected.
- **requirements.txt**: This file lists the dependencies required to run the project, including `pytest`.
- **README.md**: This file, which provides a detailed explanation of the project, its purpose, and how to use it.

### Design Choices:
The project is modularized to ensure that each section is self-contained, allowing for easy maintenance and further development. Functions for user interaction, games, and inventory management are separated to improve readability and scalability. Pytest was chosen for unit testing due to its simplicity and wide usage in the Python community.

### How to Run:
- Clone the repository and navigate to the project directory.
- Ensure that Python is installed on your system.
- Run the main program:
  ```bash
  python3 project.py
