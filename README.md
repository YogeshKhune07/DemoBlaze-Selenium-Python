# DemoBlaze-Selenium-Python   

Automation using selenium with python. 

This repository contains automated test scripts for the DemoBlaze e-commerce website using Selenium with Python and unittest framework.

*Table of Contents
Overview
 
Features

Prerequisites

Installation

Running Tests

Test Scenarios



*Overview

This project automates the testing of the DemoBlaze e-commerce platform. It covers multiple functionalities, including user login, signup, product browsing, adding products to the cart, checkout, and logout.

*Features

Test Automation using Selenium and unittest framework.

Test Suite to manage execution of various test cases.

Test Reports providing a summary of test execution


*Prerequisites

selenium==4.12.0

Python 3.12.6

WebDriver - ChromeDriver  

*Installation

1.Clone this repository:

git clone https://github.com/YogeshKhune07/DemoBlaze-Selenium-python.git

2.Navigate into the project directory:

cd DemoBlaze-Selenium-python

3.Install required dependencies:

pip install -r requirements.txt

*Running Tests

python -m unittest discover -s tests

*Test Scenarios

User SignUp - Positive and negative scenarios.

User Login - Valid and invalid login credentials.

Product Browsing - Checking product categories and product display on the homepage.

Add to Cart - Navigating to the last page and adding last product of last page to the cart.

Checkout - Positive and negative scenarios for completing a purchase.i.e checkout with empty cart and checkout by adding product to cart.

Logout - Successfully logging out.
