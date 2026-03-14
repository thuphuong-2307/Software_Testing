# config.py

BS_USERNAME = "phngnghthu_jkKTrM"
BS_ACCESS_KEY = "4xSNs81Li2rpzNg9zqcv"
BUILD_NAME = "Odoo_Regression_1"

TEST_ENVIRONMENTS = {
    "win10_chrome": {
        "os": "Windows",
        "osVersion": "10",
        "browser": "chrome",
        "browserVersion": "latest",
        "sessionName": "Windows 10 Chrome Test"
    },
    "win10_edge": {
        "os": "Windows",
        "osVersion": "10",
        "browser": "edge",
        "browserVersion": "latest",
        "sessionName": "Windows 10 Edge Test"
    },
    "win11_chrome": {
        "os": "Windows",
        "osVersion": "11",
        "browser": "chrome",
        "browserVersion": "latest",
        "sessionName": "Windows 11 Chrome Test"
    },
    "win11_edge": {
        "os": "Windows",
        "osVersion": "11",
        "browser": "edge",
        "browserVersion": "latest",
        "sessionName": "Windows 11 Edge Test"
    },
    "mac_monterey_chrome": {
        "os": "OS X",
        "osVersion": "Monterey",
        "browser": "chrome",
        "browserVersion": "latest",
        "sessionName": "macOS Monterey Chrome Test"
    },
    "mac_monterey_edge": {
        "os": "OS X",
        "osVersion": "Monterey",
        "browser": "edge",
        "browserVersion": "latest",
        "sessionName": "macOS Monterey Edge Test"
    },
    "local_chrome": {
        "os": "Windows",
        "osVersion": "11",
        "browser": "chrome",
        "browserVersion": "local",
        "sessionName": "Local Chrome Test"
    },
    "local_edge": {
        "os": "Windows",
        "osVersion": "11",
        "browser": "edge",
        "browserVersion": "local",
        "sessionName": "Local Edge Test"
    }
}
