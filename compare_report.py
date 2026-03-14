import json
import os
import pandas as pd

# Đường dẫn thư mục chứa các kết quả allure
RUN_DIRS = {
    "build_baseline": "reports/build_baseline/allure_raw",
    "build_1": "reports/build_1/allure_raw",
    "build_2": "reports/build_2/allure_raw",
    "build_3": "reports/build_3/allure_raw",
}

def extract_results(build_path):
    summary = {"passed": 0, "failed": 0, "broken": 0, "skipped": 0, "total": 0}
    if not os.path.exists(build_path):
        print(f" Không tìm thấy thư mục {build_path}")
        return summary

    for file in os.listdir(build_path):
        if file.endswith("-result.json"):
            with open(os.path.join(build_path, file), encoding="utf-8") as f:
                data = json.load(f)
                status = data.get("status", "unknown")
                if status in summary:
                    summary[status] += 1
                summary["total"] += 1
    return summary

def compare_runs(base_run, compare_run):
    diff = {}
    for key in base_run.keys():
        diff[key] = compare_run[key] - base_run[key]
    return diff

# --- Tổng hợp tất cả các kết quả ---
results = {}
for name, path in RUN_DIRS.items():
    results[name] = extract_results(path)

df = pd.DataFrame(results).T
df["pass_rate"] = (df["passed"] / df["total"] * 100).round(2)

# --- So sánh baseline với các build còn lại ---
base = results["build_baseline"]
comparison = {}

for run_name, run_result in results.items():
    if run_name != "build_baseline":
        comparison[run_name] = compare_runs(base, run_result)

compare_df = pd.DataFrame(comparison).T

# --- Xuất báo cáo ---
print("Tổng hợp kết quả:")
print(df)
print(" So sánh với lần chạy đầu tiên:")
print(compare_df)

df.to_csv("allure_summary.csv", index=True)
compare_df.to_csv("compare_with_baseline.csv", index=True)
print(" Xuất file compare_with_baseline.csv thành công.")