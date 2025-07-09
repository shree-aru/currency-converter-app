# Currency Converter App

## 1. Introduction

## 2. Features

## 3. Installation

## 4. Usage

## 5. Technologies Used

## 6. Project Structure

## 7. Contributing

## 8. Contact


### 1.1 Problem Statement
In an increasingly interconnected global economy, individuals and businesses frequently encounter situations requiring currency conversion. Whether for international travel, online shopping, financial planning, or simply understanding global economic news, a quick and reliable tool to convert between different currencies is invaluable. Many existing solutions are often overly complex, laden with advertisements, or require constant internet connectivity, making them less ideal for simple, on-the-go conversions or for users who prefer a straightforward, minimalist approach. There is a clear need for a simple, accessible, and efficient currency converter that provides accurate conversions without unnecessary complexities.

### 1.2 Project Objective
This project aims to develop a user-friendly Currency Converter application that facilitates quick and accurate conversions between various currencies. The primary objective is to provide a practical tool that can be used either via a command-line interface (CLI) or potentially a graphical user interface (GUI), offering flexibility to the user. The application will utilize mocked (static) exchange rates to demonstrate the core conversion logic, making it suitable for educational purposes, rapid prototyping, and scenarios where real-time API calls are not feasible or desired. This project will serve as an excellent demonstration of fundamental programming concepts, including input/output handling, conditional logic, and modular design.

### 1.3 Expected Outcome
The expected outcome of this project is a functional and intuitive Currency Converter application. The application will accept an amount, a source currency, and a target currency as input, and then output the converted amount. The core conversion logic will be robust, handling various currency pairs based on predefined exchange rates. While the initial implementation will focus on a CLI, the architecture will be designed to allow for easy extension to a Tkinter-based GUI with dropdowns for currency selection, as an optional enhancement. The project will also include comprehensive documentation, such as this README.md file, detailing its features, installation, usage, and technical implementation, suitable for academic submission and understanding fundamental programming principles.


## 2. Features

The Currency Converter App is designed with simplicity and functionality at its core, offering the following key features:

### 2.1 Straightforward Currency Conversion
The primary function of the application is to convert a specified amount from one currency to another. Users provide the amount, the source currency, and the target currency, and the application returns the converted value.

### 2.2 Mocked Exchange Rates
For simplicity and to ensure the application is functional without external API dependencies, the converter uses a set of predefined, mocked exchange rates. These rates are static and embedded within the application's logic, making it ideal for demonstrations, offline use, and understanding the underlying conversion mechanics without the complexities of real-time data fetching.

### 2.3 Command-Line Interface (CLI)
The application provides a clear and interactive command-line interface. Users can easily input their conversion details through prompts, making it accessible for those comfortable with terminal environments. The CLI is designed to be intuitive, guiding the user through the necessary inputs.

### 2.4 Error Handling and User Feedback
The converter includes basic error handling to manage invalid inputs, such as non-numeric amounts or unsupported currency codes. It provides clear and concise error messages to guide the user in correcting their input, enhancing the user experience.

### 2.5 Supported Currencies
The application supports a predefined set of major global currencies (e.g., USD, EUR, GBP, JPY). The list of supported currencies is clearly displayed to the user at the start of the application, ensuring transparency.

### 2.6 Modular Design
The conversion logic is separated from the user interface (CLI). This modular design promotes code reusability, makes the application easier to maintain, and allows for future expansion, such as integrating a graphical user interface (GUI) or connecting to a real-time exchange rate API, without significant refactoring of the core conversion functionality.


## 3. Installation

To set up and run the Currency Converter App on your local machine, follow these simple steps:

### 3.1 Prerequisites
Ensure you have **Python 3.x** installed on your system. You can download the latest version from the official Python website: [python.org](https://www.python.org/downloads/). Python typically comes with `pip`, its package installer, which is not strictly necessary for this project as there are no external Python library dependencies beyond standard built-in modules.

### 3.2 Clone the Repository (if applicable)
If you are obtaining this project from a version control system like GitHub, you can clone the repository to your local machine using the following command:

```bash
git clone https://github.com/shree-aru/currency-converter-app.git
cd currency-converter-app
```


### 3.3 No External Dependencies
This project is designed to be lightweight and self-contained. It does not require any external Python libraries to be installed via `pip`. All necessary modules (like `input()` for CLI interaction) are part of Python's standard library.

Once you have Python installed and the project files on your machine, you are ready to run the application.


## 4. Usage

The Currency Converter App is designed for straightforward use via the command-line interface.

### 4.1 Running the Application
Navigate to the project directory in your terminal. Then, execute the `cli_app.py` file using Python:

```bash
python cli_app.py
```

This command will start the application, and you will be greeted with a welcome message and a list of supported currencies.

### 4.2 Interacting with the Converter
The application will prompt you for the following information:

1.  **Amount to Convert:** Enter the numerical value you wish to convert. For example, `100`.
2.  **Source Currency:** Enter the three-letter currency code of the currency you are converting *from*. For example, `USD`.
3.  **Target Currency:** Enter the three-letter currency code of the currency you are converting *to*. For example, `EUR`.

After providing these inputs, the application will display the converted amount. You can perform multiple conversions in a single session. To exit the application, type `exit` when prompted to enter the amount.

### 4.3 Example Interaction

```
--- Currency Converter CLI ---
Supported Currencies:  USD, EUR, GBP, JPY
Enter amount to convert (or 'exit' to quit): 100
Enter source currency (e.g., USD): USD
Enter target currency (e.g., EUR): EUR
100.00 USD is equal to 92.00 EUR
Enter amount to convert (or 'exit' to quit): 50
Enter source currency (e.g., EUR): EUR
Enter target currency (e.g., GBP): GBP
50.00 EUR is equal to 43.00 GBP
Enter amount to convert (or 'exit' to quit): exit
--- Exiting Currency Converter ---
```

### 4.4 Error Handling
*   If you enter a non-numeric value for the amount, the application will prompt you to enter a valid number.
*   If you enter an unsupported currency code, it will inform you that the currency is not supported.

This interactive process makes the converter easy to use for quick calculations.


## 5. Technologies Used

This project is developed using fundamental programming concepts and standard Python features, making it highly accessible and easy to understand. The primary technologies involved are:

*   **Python 3.x:** The core programming language used for developing the entire application, including the conversion logic and the command-line interface. Python was chosen for its readability, simplicity, and extensive standard library, which allows for rapid development without external dependencies.
*   **Standard Python Libraries:** The application exclusively uses built-in Python functionalities, such as basic input/output operations (`input()`, `print()`) and string manipulation. This ensures maximum compatibility and eliminates the need for any `pip` installations.

This minimalist approach highlights the power of core programming principles and demonstrates how functional applications can be built with basic tools.


## 6. Project Structure

The project is organized into the following files:

```
currency_converter/
├── cli_app.py
├── converter_logic.py
└── README.md
└── todo.md
```

*   `cli_app.py`: This is the main executable file for the command-line interface. It handles user input and output, and calls the `converter_logic.py` for currency conversion.
*   `converter_logic.py`: Contains the core business logic for currency conversion, including the predefined exchange rates and the `convert_currency` function.
*   `README.md`: This document, providing a comprehensive overview of the project, including its purpose, features, installation, usage, and technical details.
*   `todo.md`: A markdown file used for tracking the project's development progress and outstanding tasks.


## 7. Contributing

Contributions to this project are welcome! If you have suggestions for improvements, new features, or bug fixes, please consider:

1.  **Forking the repository.**
2.  **Creating a new branch** for your feature or bug fix: `git checkout -b feature/your-feature-name` or `bugfix/your-bug-name`.
3.  **Making your changes** and ensuring they adhere to the existing code style.
4.  **Writing clear, concise commit messages.**
5.  **Pushing your branch** to your forked repository.
6.  **Opening a Pull Request** to the `main` branch of this repository, describing your changes in detail.

Your contributions will help make this simple tool even more useful!


## 8. Contact

For any inquiries or further information regarding this project, please feel free to reach out.

---

