LƯU Ý: MỖI KHI TẠO MỘT THƯ MỤC build MỚI TRONG TỆP TIN reports, KIỂM TRA KỸ 2 HÀM CHỤP MÀN HÌNH VÀ LƯU KẾT QUẢ ĐÚNG ĐỊA CHỈ build MÌNH MONG MUỐN HAY CHƯA

-- Local Win11 Chrome (chọn làm baseline):
-Chạy tất cả file test
pytest tests --env=local_chrome --alluredir=reports/build_baseline/allure_raw
-Xem báo cáo
allure serve reports/build_baseline/allure_raw
-Chạy từng file test
pytest tests/test_home.py --env=local_chrome --alluredir=reports/build_baseline/allure_raw
pytest tests/test_navigation.py --env=local_chrome --alluredir=reports/build_baseline/allure_raw
pytest tests/test_pricing.py --env=local_chrome --alluredir=reports/build_baseline/allure_raw
pytest tests/test_trial_form.py --env=local_chrome --alluredir=reports/build_baseline/allure_raw
pytest tests/test_apps.py --env=local_chrome --alluredir=reports/build_baseline/allure_raw
pytest tests/test_contact_about.py --env=local_chrome --alluredir=reports/build_baseline/allure_raw
pytest tests/test_general.py --env=local_chrome --alluredir=reports/build_baseline/allure_raw

-- Local Win11 Edge:
-Chạy tất cả file test
pytest tests --env=local_chrome --alluredir=reports/build_1/allure_raw
-Xem báo cáo
allure serve reports/build_1/allure_raw
-Chạy từng file test
pytest tests/test_pricing.py --env=local_edge --alluredir=reports/build_1/allure_raw
pytest tests/test_home.py --env=local_edge --alluredir=reports/build_1/allure_raw
pytest tests/test_navigation.py --env=local_edge --alluredir=reports/build_1/allure_raw
pytest tests/test_trial_form.py --env=local_edge --alluredir=reports/build_1/allure_raw
pytest tests/test_apps.py --env=local_edge --alluredir=reports/build_1/allure_raw
pytest tests/test_contact_about.py --env=local_edge --alluredir=reports/build_1/allure_raw
pytest tests/test_general.py --env=local_edge --alluredir=reports/build_1/allure_raw

-- Mac Chrome 
-Chạy tất cả file test
pytest tests --env=mac_monterey_chrome --alluredir=reports/build_2/allure_raw
-Xem báo cáo
allure serve reports/build_2/allure_raw
-Chạy từng files test
pytest tests/test_pricing.py --env=mac_monterey_chrome --alluredir=reports/build_2/allure_raw
pytest tests/test_home.py --env=mac_monterey_chrome --alluredir=reports/build_2/allure_raw
pytest tests/test_navigation.py --env=mac_monterey_chrome --alluredir=reports/build_2/allure_raw
pytest tests/test_trial_form.py --env=mac_monterey_chrome --alluredir=reports/build_2/allure_raw
pytest tests/test_apps.py --env=mac_monterey_chrome --alluredir=reports/build_2/allure_raw
pytest tests/test_contact_about.py --env=mac_monterey_chrome --alluredir=reports/build_2/allure_raw
pytest tests/test_general.py --env=mac_monterey_chrome --alluredir=reports/build_2/allure_raw

--- Mac Edge 
-Chạy tất cả file test
pytest tests --env=mac_monterey_edge --alluredir=reports/build_3/allure_raw
-Xem báo cáo
allure serve reports/build_3/allure_raw
-Chạy từng files test
pytest tests/test_pricing.py --env=mac_monterey_edge --alluredir=reports/build_3/allure_raw
pytest tests/test_home.py --env=mac_monterey_edge --alluredir=reports/build_3/allure_raw
pytest tests/test_navigation.py --env=mac_monterey_edge --alluredir=reports/build_3/allure_raw
pytest tests/test_trial_form.py --env=mac_monterey_edge --alluredir=reports/build_3/allure_raw
pytest tests/test_apps.py --env=mac_monterey_edge --alluredir=reports/build_3/allure_raw
pytest tests/test_contact_about.py --env=mac_monterey_edge --alluredir=reports/build_3/allure_raw
pytest tests/test_general.py --env=mac_monterey_edge --alluredir=reports/build_3/allure_raw


