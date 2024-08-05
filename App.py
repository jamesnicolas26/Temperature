from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, QComboBox
import sys

def convert_temperature():
    """Convert temperature based on the selected conversion."""
    try:
        temp = float(temp_input.text())
        conversion_type = combo_conversion.currentText()
        if conversion_type == 'Celsius to Fahrenheit':
            converted_temp = temp * 9 / 5 + 32
        elif conversion_type == 'Fahrenheit to Celsius':
            converted_temp = (temp - 32) * 5 / 9
        label_result.setText(f"Converted Temperature: {converted_temp:.2f}")
    except ValueError:
        label_result.setText("Invalid input. Please enter a valid temperature.")

def create_temperature_converter():
    """Create a simple temperature converter GUI."""
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Temperature Converter")

    global temp_input, combo_conversion, label_result

    layout = QVBoxLayout()

    # Temperature input
    layout.addWidget(QLabel("Temperature:"))
    temp_input = QLineEdit()
    layout.addWidget(temp_input)

    # Conversion options
    layout.addWidget(QLabel("Conversion:"))
    combo_conversion = QComboBox()
    combo_conversion.addItems(["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
    layout.addWidget(combo_conversion)

    # Convert button
    convert_button = QPushButton("Convert")
    convert_button.clicked.connect(convert_temperature)
    layout.addWidget(convert_button)

    # Result label
    label_result = QLabel("Converted Temperature:")
    layout.addWidget(label_result)

    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    create_temperature_converter()
