# OrderlyTk

OrderlyTk is a simple order management system built using Python's Tkinter library. This application allows users to add, edit, delete, and export orders to a CSV file. It's designed to provide a straightforward graphical user interface for managing orders efficiently.

## Features

- **Add Orders**: Input order details including name, order, and quantity.
- **Edit Orders**: Modify existing orders by specifying the order ID.
- **Delete Orders**: Remove orders from the list by specifying the order ID.
- **Export to CSV**: Save the current order list to a CSV file for easy data handling and analysis.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/orderlytk.git
    cd orderlytk
    ```

2. **Install Dependencies**:
    - Ensure you have Python installed (preferably version 3.6 or later).
    - Install the required packages (Tkinter is usually included with Python installations).

## Usage

1. **Run the Application**:
    ```bash
    python orderlytk.py
    ```

2. **Add Orders**:
    - Click on the "ADD" button.
    - Enter the name, order, and quantity, then click "ADD".

3. **Edit Orders**:
    - Click on the "EDIT" button.
    - Enter the Order ID of the order you wish to edit, then click "ENTER".
    - Modify the details and click "EDIT".

4. **Delete Orders**:
    - Click on the "DELETE" button.
    - Enter the Order ID of the order you wish to delete, then click "DELETE".

5. **Export Orders to CSV**:
    - Click on the "CSV" button to save the current list of orders to a CSV file.

## Project Structure

- `orderlytk.py`: Main application file containing the UI and logic.
- `README.md`: Project documentation.

## Contributing

Feel free to submit issues and enhancement requests. Contributions are welcome!

## License

This project is licensed under the Apache-2.0 License.
