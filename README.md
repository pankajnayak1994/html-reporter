# Python Unit Test HTML JSON Report Generator

### Introduction
A [Nose2] plugin for generating detailed, searchable, and user-friendly HTML and JSON reports of your test results.

Key Features:

- Rich Test Descriptions: Automatically captures docstrings from tests as descriptions, making the reports more informative and readable.
- Failure Tracebacks: Includes complete traceback details for any failed tests, enabling quick identification and resolution of issues.
- Searchable and Filterable Reports: Allows users to search and filter results by status (e.g., passed, failed, skipped, or error), making it easy to navigate through large test suites.
- Customizable Outputs: Supports customization options to fit specific reporting needs.
- JSON Integration: Provides JSON reports for easy integration with other tools or automated workflows.
- This plugin is ideal for enhancing test visibility and making debugging more efficient.

![Report Screenshot](https://raw.githubusercontent.com/pankajnayak1994/py-html-json-reporter/master/docs/images/report.png)

### Installation
You can install the Nose2 HTML Report Plugin using `pip`:
```
pip install py-html-json-reporter
```

### Configuration
To get `nose2` to recognize the plugin add an entry into the `plugin` key of the `unittest` section of your `nose2.cfg` file. Configurations for the plugin should be placed into an `html-report` section of the configuration file. Below is a working example:
```
[unittest]
plugins = py_html_json_reporter.html_report

[html-report]
always-on = True
```

#### Additional Settings
Specify the path for the HTML report. Defaults to `report.html`
```
[unittest]
plugins = py_html_json_reporter.html_report

[html-report]
always-on = True
path = test_results/my_custom_report_file.html
```

### Usage
Command line flag:
```
nose2 --html-report
```

If you have `always-on=True` inside your `nose2.cfg`:
```
nose2
```
