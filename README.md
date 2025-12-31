# Healthcare-Data-Cleaning-Patient-Trends-Analysis_pyhton
This project focuses on the end-to-end cleaning and exploratory data analysis (EDA) of a Healthcare Patient Dataset. The script addresses common data integrity issues found in medical records, such as mixed-type age entries, unformatted blood pressure readings, and inconsistent categorical labeling.

📂 Project Structure:

project1.py: The Python script containing the data cleaning pipeline and visualization logic.

healthcare_messy_data.csv: The raw dataset containing unformatted names, missing values, and inconsistent data types.

clean_healthcare_data.csv: The final sanitized dataset, optimized for analysis and reporting.

🛠️ Data Cleaning & Engineering:

The cleaning pipeline utilizes pandas and numpy to ensure medical accuracy:

Advanced Age Normalization: Replaced text-based entries (e.g., "forty") with numeric values and handled missing data using median imputation.

Blood Pressure Decomposition: Split the combined Blood Pressure string into separate Systolic_BP and Diastolic_BP numeric columns for clinical analysis.

Temporal Processing: Standardized Visit Date using mixed-format parsing and extracted the Year for time-series tracking.

Categorical Standardization: Normalized patient names and medications to title case and filled missing medical condition data with "unknown".

Contact Data Validation: Cleaned whitespace from emails and phone numbers, providing default placeholders for missing contact info

📊 Medical Data Visualizations:

The script generates several clinical insights using Seaborn and Matplotlib:

Demographic Breakdown: A bar chart comparing the average age across different medical conditions, segmented by gender.

Clinical Distribution: A histogram with a Kernel Density Estimate (KDE) for cholesterol levels.

Medication Efficacy Analysis: Dual boxplots comparing the distribution of Systolic and Diastolic blood pressure across different medication types.

Patient Volume Trends: A line plot showing the trend of patient visits between 2018 and 2020.

🚀 How to Run

Install dependencies:

Bash
pip install pandas numpy matplotlib seaborn

Run the script: Update the pd.read_csv path in project1.py to your local file location and run:

Bash
python project1.py


