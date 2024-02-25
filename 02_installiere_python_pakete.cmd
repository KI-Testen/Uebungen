@echo off

python.exe -m pip install --upgrade pip
pip install numpy joblib scipy matplotlib pandas seaborn scikit-learn lime
:: pip install shap
pause