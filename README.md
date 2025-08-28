# Data Faker CSV Generator

A user-friendly GUI application for generating large CSV files with realistic fake data. Built with Python and Tkinter, this tool is perfect for testing, development, and data analysis scenarios where you need substantial amounts of realistic sample data.

## Features

- **Intuitive GUI Interface**: Easy-to-use graphical interface built with Tkinter
- **Multiple Data Types**: Support for various data types including names, emails, phones, addresses, and more
- **Customizable Fields**: Add, remove, and configure field names and types
- **Large Dataset Generation**: Generate up to hundreds of thousands of rows efficiently
- **Progress Tracking**: Real-time progress bar and percentage indicator
- **Multi-threaded**: Non-blocking CSV generation using threading
- **Executable Build**: Can be packaged as a standalone Windows executable

## Supported Data Types

The application supports the following field types:

- **Full Name**: Realistic full names
- **Phone**: Phone numbers in various formats
- **Email Address**: Valid email addresses
- **Department (Corporate)**: Job titles and departments
- **ISBN**: ISBN-13 book identifiers
- **Address**: Complete street addresses
- **City**: City names
- **Country**: Country names
- **Date**: Random dates
- **Company**: Company names
- **Integer**: Random integer values (1-999,999)
- **Text**: Random text strings (up to 20 characters)

## Default Configuration

The application comes pre-configured with common fields:
- USER_ID (ISBN format)
- NAME (Full Name)
- MOBILE_NUMBER (Phone)
- DESIGNATION (Department/Corporate)
- EMAIL_ID (Email Address)

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. Clone or download this repository:
   ```bash
   git clone <repository-url>
   cd data-faker
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python data_faker_app.py
   ```

## Usage

1. **Launch the Application**: Run `python data_faker_app.py`

2. **Configure Fields**:
   - The application starts with default fields pre-configured
   - Modify field names by clicking in the "Field Name" column
   - Change data types using the dropdown in the "Type" column
   - Add new fields using the "+" button
   - Remove fields using the "-" button (minimum one field required)

3. **Set Row Count**: Specify the number of rows to generate (default: 100,000)

4. **Generate CSV**:
   - Click "Generate CSV"
   - Choose a save location and filename
   - Monitor progress with the progress bar
   - Wait for completion notification

## Building Executable

To create a standalone Windows executable:

1. Make sure you have PyInstaller installed:
   ```bash
   pip install pyinstaller
   ```

2. Run the build script:
   ```bash
   build_exe.bat
   ```

3. The executable will be created in the `dist` folder

## Project Structure

```
data-faker/
├── data_faker_app.py          # Main application file
├── requirements.txt           # Python dependencies
├── build_exe.bat             # Build script for executable
├── app_icon.ico              # Application icon
├── data_faker_app.spec       # PyInstaller specification
├── faker_fields/             # Field type modules
│   ├── field_types.py        # Field type definitions
│   ├── csv_generator.py      # CSV generation logic
│   └── __pycache__/          # Python cache files
└── build/                    # Build artifacts
    └── data_faker_app/       # PyInstaller build files
```

## Technical Details

- **Framework**: Tkinter (Python's standard GUI toolkit)
- **Fake Data Generation**: Uses the `Faker` library for realistic data
- **CSV Writing**: Built-in `csv` module for efficient file writing
- **Threading**: Uses Python's `threading` module for non-blocking UI
- **Progress Reporting**: Callback-based progress updates every 1% completion

## Dependencies

- `faker`: For generating realistic fake data
- `pyinstaller`: For building standalone executables

## Performance

- Optimized for large datasets (tested with 100,000+ rows)
- Progress updates every 1% for smooth user experience
- Memory-efficient streaming CSV writing
- Multi-threaded to keep UI responsive during generation

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source. Please check the license file for details.

## Support

For issues, bugs, or feature requests, please create an issue in the repository.

---

**Note**: This application generates fake data for testing and development purposes only. Do not use for any production systems containing real user data.
