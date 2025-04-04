# An Online Human Evaluation Form Template

This online form template functions like [Google Forms](https://www.google.com/forms/about/) but is more customizable.
Please feel free to use this as a template to create your own online human evaluation form.

### Usage

1. On GitHub:
    - Using this repository as template, generate your own public or private repository.
    - Go to *settings* and enable GitHub Pages.
2. On Google Drive:
    - Create a Google Spreadsheet and copy its ID from its URL:
        ```
        https://docs.google.com/spreadsheets/d/{YOUR_SPREADSHEET_ID}/edit
        ```
    - Create a Google Apps Script from **app.gs** and fill in `YOUR_SPREADSHEET_ID` you just copied
    - Customize **the number of scripts** to meet your need (Should change)
    - Deploy it in https://script.google.com/home as a Web App (Allow *anyone, even anonymous* to access the Web App).
3. Locally:
    - Clone the repository you just created from the template.
    - Take a look at **templates** directory and several rendered HTMLs there as example.
    - Modify Web App domain in  **render_mos.py** or **render_pair_comparison.py**.
    - Modify your scripts and audios and map exactly them in `audios` folder. **The number of scripts** has been defined in **app.gs**.
    - Generate HTML: `python3 render_mos.py > index.html`
    - Commit and push all the modifications back to GitHub.

### Result

The evaluation score is in `https://docs.google.com/spreadsheets/d/{YOUR_SPREADSHEET_ID}/edit`. The score is mapped with column in `folder_to_question.json`