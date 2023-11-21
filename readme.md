# PaddlePaddle Repository Contributors List

This script allows you to fetch the list of contributors for PaddlePaddle suite repositories, such as PaddleOCR and PaddleNLP. It utilizes the GitHub Command Line Interface (CLI) to retrieve merged pull requests (PRs) labeled as 'contributor' and stores the information in an Excel file.

## Prerequisites
- GitHub CLI: Make sure you have GitHub CLI installed and configured on your system. You can download it from the official GitHub CLI repository and follow the installation instructions provided.

## Installation
1. Clone the repository containing this script to your local machine.

2. Install the required dependencies by running the following command:
    ```
    pip install subprocess 
    pip install openpyxl 
    pip install json
    ```

## Usage
1. Open a terminal or command prompt and navigate to the directory where the script is located.

2. Run the following command to execute the script if you are using mac with python3:
    ```
    python3 gh-tool.py
    ```
    Otherwise, you can run in this way:
    ```
    python gh-tool.py
    ```
3. The script will execute the GitHub CLI command to fetch the merged PRs labeled as 'contributor' and store the data in an Excel file named `github_prs_with_author_1.1_merged.xlsx`.

4. Once the script completes execution, you will see a message indicating that the GitHub PR list (including author login names) has been saved to the `github_prs_with_author_1.1_merged.xlsx` file.

## Output
The output of the script is an Excel file (`github_prs_with_author_1.1_merged.xlsx`) containing the following columns:

- PR Number: The number assigned to the pull request.
- PR Title: The title of the pull request.
- PR URL: The URL of the pull request.
- Author: The login name of the author who submitted the pull request.

You can open the Excel file using software such as Microsoft Excel or Google Sheets to view and analyze the data.

## Customization
- To fetch PRs with different labels, you can modify the `--label` parameter in the `github_cli_command` variable in the script.
- To fetch PRs with different states (e.g. open, closed), you can modify the `--state` parameter in the `github_cli_command` variable in the script.

## Limitations
- The script has a limit of fetching a maximum of 10,000 merged pull requests. If there are more PRs labeled as 'contributor,' you need to modify the `--limit` parameter in the `github_cli_command` variable to increase the limit.

## License
This script is released under the [MIT License](https://opensource.org/licenses/MIT).

## Disclaimer
This script is provided as-is without any warranty. Use it at your own risk.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please create an issue or submit a pull request.

