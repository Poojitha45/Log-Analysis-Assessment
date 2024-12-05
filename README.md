# Log-Analysis-Assessment
# Project Description
The Log Analysis Script is a Python-based tool designed to process and analyze log files to extract valuable insights. This script provides detailed analysis by:
  1.Identifying the total number of requests made by each IP address.
  2.Determining the most frequently accessed endpoints.
  3.Flagging suspicious activities, such as multiple failed login attempts.
The results are saved as CSV files for easy access and review.
# File Structure
1.log_analysis.py: The main Python script for log analysis.
2.sample.log: A sample log file used for testing the script.
3.Suspicious Activity.csv: Contains flagged IPs for suspicious activities.
4.Most Accessed Endpoint.csv: Summarizes the most accessed endpoints.
5.Requests per IP.csv: Lists the request count per IP.
6.README.md: Documentation of the project.
7..gitignore (Optional): Specifies files to exclude from version control.
8.requirements.txt (Optional): Lists Python dependencies required for the script.
# Installation and Setup
# 1.Clone the Repository
  git clone <repository-url>
  cd log-analysis
# 2.Install Dependencies
Ensure Python 3 is installed. Install necessary libraries using:
  pip install -r requirements.txt
# 3.Run the Script
Execute the script to analyze the log file:
  python log_analysis.py
# 4.How to Use
1.Place your log file in the same directory as log_analysis.py.
Update the script to point to your log file if the file name is different.
2.Run the script as described above.
3.View the generated CSV files for analysis results.
# 5.Output Files
1.Requests per IP.csv
    Contains IP addresses and the corresponding number of requests.
2.Most Accessed Endpoint.csv
    Displays the most frequently accessed endpoints and their counts.
3.Suspicious Activity.csv
    Lists IP addresses with suspicious activity, such as multiple failed login attempts.
# 6.Customization
Modify the threshold for detecting suspicious activity in the script:
    FAILED_LOGIN_THRESHOLD = 5
# 7.Sample Output
Terminal Output
Log Analysis Complete!
Results saved to:
- Requests per IP.csv
- Most Accessed Endpoint.csv
- Suspicious Activity.csv
# 8.Sample CSV Output
Requests per IP.csv
# IP Address	  Requests
192.168.0.1	     25
172.16.254.2	   12
# 9.Known Issues
Large log files may require optimization or additional memory.
# 10.Contributing
Contributions are welcome!
Fork the repository.
Create a new feature branch.
Submit a pull request.
# Contact
For questions or support, contact Poojitha at poojithaps2k3@gmail.com.










  
