# to run pure tdd-see files allure_tdd_run.bat and allure_tdd_report.bat. Code from here can be used in Jenkins job/s

# run all tests refactored
pytest --alluredir=allure_reports_refactored -k "test_refactored_1.py or test_refactored_2.py or test_refactored_3.py or test_refactored_4.py or test_refactored_5.py or test_refactored_6.py"

# allure report
allure serve allure_reports_refactored