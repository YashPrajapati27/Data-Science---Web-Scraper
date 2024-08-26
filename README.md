# Doctor Finder - Practo.com

## Overview

**Doctor Finder** is a simple and intuitive Streamlit-based web application that allows users to search for doctors based on their location and specialization using data scraped from Practo.com. This tool provides an easy way to find doctors in a specific area and field of expertise, displaying important details like experience, clinic name, locality, and consultation fees.

![Doctor Finder Header Image](https://t4.ftcdn.net/jpg/02/74/73/01/360_F_274730119_ht4FXz4R6RnIJgPk7WeNALxxaf524Jrb.jpg)

## Features

- **Search by Location**: Enter the desired location to find doctors available in that area.
- **Select Specialization**: Choose a specific medical specialization from a dropdown menu to narrow down the search.
- **Scrape and Display**: The application scrapes doctor profiles from Practo.com based on the provided inputs and displays the results in a well-organized and styled manner.
- **Responsive Design**: The application is designed with a responsive layout, making it easy to use on various devices.

## How It Works

1. **User Input**:
   - The user inputs a location (e.g., "Delhi").
   - The user selects a specialization (e.g., "Dermatologist") from the dropdown menu.

2. **Scraping**:
   - Upon clicking the "Scrape" button, the app fetches doctor profiles from Practo.com based on the provided location and specialization.

3. **Display Results**:
   - The app displays the total number of doctors found.
   - Each doctor's profile is shown in a card format, displaying the name, specialization, experience, clinic name, locality, and consultation fees.

## Installation

To run the application locally, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/doctor-finder-practo.git
   cd doctor-finder-practo
2. **Create a Virtual Environment (optional but recommended):**

    ```bash
    pip install -r requirements.txt
3. **Install Required Packages:**
    Make sure you have `pip` installed and run:

   ```bash
   pip install -r requirements.txt
   ```
# Doctor Finder - Practo.com

## Dependencies

- **Streamlit:** Used to build the web application.
- **Requests:** Used to make HTTP requests to Practo.com.
- **BeautifulSoup:** Used to parse HTML and extract doctor profile information.

**You can install these dependencies by running:**
 
```bash
  pip install streamlit requests beautifulsoup4
```

## Usage

1. **Run the Application:**

   
```bash
   streamlit run app.py
```

2. **Access the App:**

   Open your browser and navigate to `http://localhost:8501` to use the Doctor Finder application.

3. **Enter the location and select the specialization, then click the "Scrape" button to fetch and display doctor profiles.**

## Code Explanation
- **app.py:** The main script containing the Streamlit application logic.
- **Page Configuration:** Sets up the page title and icon.
- **Custom CSS:** Applies custom styles to the application.
- **UI Elements:** Includes input fields for location and specialization, and a button to trigger the scraping.
- **Data Scraping:** Defines the fetch_doctor_profiles function to scrape doctor data from Practo.com and display it.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any questions or feedback, please contact your-prajapatiyash2026@gmail.com

