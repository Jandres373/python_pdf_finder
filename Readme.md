# PDF Finder 

The PDF Finder is a Python application that allows you to quickly and easily find PDF files on the web. This one is only written in spanish but could be translated if requested.

![PDF Finder](https://res.cloudinary.com/dwzcbbipf/image/upload/v1714504413/portfolio/ai8vj7r9sziklnrkq6tl.png)

## Features
- **PDF File Search:** This application uses the Google API to perform specific searches for PDF files on the web, providing you with accurate and relevant results.
- **User-Friendly Graphic Interface:** The PDF Finder has an intuitive graphic interface developed with Tkinter, which allows for a smooth and easy-to-use user experience.
- **Direct Access to Results:** Once you find the PDF file you are looking for, you can open it directly from the application with just one click, thanks to integration with the webbrowser module in Python.

## Modules Used
- **Tkinter:** Tkinter is a standard Python module used to create graphical user interfaces (GUIs). In this project, Tkinter is used to develop the user interface for the PDF Finder, providing buttons, labels, and other interface elements.
- **re:** The re module provides regular expression operations in Python. It is used in this project to perform search and filtering operations on results.
- **webbrowser:** The webbrowser module provides a high-level interface to allow viewing of web documents. In the PDF Finder, this module is used to open PDF files directly in the user's default web browser.
- **googlesearch:** This module allows for Google searches from Python. It is used in the PDF Finder to search for specific PDF files on the web.

## Execution Requirements
To run the PDF Finder, you will need to have a compatible version of Python installed on your system. Additionally, make sure you have the following packages installed:
```bash
pip install tkinter
pip install google
