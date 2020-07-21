echo #################### PRUEBAS CON ALLURE ####################
cd .\src\tests
python -m pytest tst_013.py --alluredir ..\allure-results
python -m pytest tst_014.py --alluredir ..\allure-results
python -m pytest tst_015.py --alluredir ..\allure-results
pause