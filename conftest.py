import pytest, os, json, allure
from selenium import webdriver
import config
from datetime import datetime

def pytest_addoption(parser):
    parser.addoption(
        "--env", 
        action="store", 
        default="win11_chrome",
        help="Chọn môi trường test: , win11_chrome, win11_edge, mac_monterey_chrome, mac_monterey_edge"
    )

@pytest.fixture(scope="session")
def driver(request):
    env_name = request.config.getoption("--env")
    env = config.TEST_ENVIRONMENTS[env_name]
    browser = env["browser"].lower()

    if browser == "chrome":
        options = webdriver.ChromeOptions()
    elif browser == "edge":
        options = webdriver.EdgeOptions()
    else:
        raise ValueError(f"Browser '{browser}' không được hỗ trợ")

    # Nếu local thì không set capability BrowserStack
    if "local" in env_name:
        driver = webdriver.Chrome(options=options) if browser == "chrome" else webdriver.Edge(options=options)
    else:
        # cloud BrowserStack
        options.set_capability("browserVersion", env["browserVersion"])
        options.set_capability("platformName", env["os"])
        options.set_capability("bstack:options", {
            "os": env["os"],
            "osVersion": env["osVersion"],
            "buildName": config.BUILD_NAME,
            "sessionName": env["sessionName"]
        })
        driver = webdriver.Remote(
            command_executor=f"https://{config.BS_USERNAME}:{config.BS_ACCESS_KEY}@hub.browserstack.com/wd/hub",
            options=options
        )

    yield driver
    driver.quit()

# Hooks & Utility Functions
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call":
        driver = item.funcargs.get("driver", None)
        screenshot_path = None
        if rep.failed and driver:
            screenshot_path = capture_screenshot(driver, item.name)
            allure.attach.file(screenshot_path, name=item.name, attachment_type=allure.attachment_type.PNG)
        save_test_log(item, rep, "failed" if rep.failed else "passed", screenshot_path)

def capture_screenshot(driver, test_name):
    screenshot_dir = os.path.join(os.getcwd(), "reports","build_5", "screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{test_name}_{timestamp}.png"
    filepath = os.path.join(screenshot_dir, filename)
    driver.save_screenshot(filepath)
    return filepath

def save_test_log(item, report, outcome, screenshot_path=None):
    folder = os.path.join(os.getcwd(), "reports","build_5", "results")
    os.makedirs(folder, exist_ok=True)
    test_name = item.nodeid.replace("::", "_").replace("/", "_").replace("\\", "_")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(folder, f"{test_name}_{timestamp}_{outcome}.json")
    data = {
        "test_name": item.name,
        "nodeid": item.nodeid,
        "outcome": outcome,
        "timestamp": timestamp,
        "longrepr": str(report.longrepr) if outcome == "failed" else None,
        "screenshot": screenshot_path
    }
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
