# Monitoring-Urban-Black-Odorous-Water
Code and data files for examining urban black-odorous water in Guangzhou City of China
1.	Optimal band selection by machine learning Lasso regression 

a.	Input data:

i.	FinalDataforLassoN_F1.csv: reflectance data of aggregated bands from 350nm to 2500nm and band combinations with the factor scores generated based on the contribution of Factor 1 at 52 study sites.

ii.	FinalDataforLassoN_F2.csv: reflectance data of aggregated bands from 350nm to 2500nm and band combinations with the factor scores generated based on the contribution of Factor 2 at 52 study sites.


iii.	FinalDataforLassoN_F3.csv: reflectance data of aggregated bands from 350nm to 2500nm and band combinations with the factor scores generated based on the contribution of Factor 3 at 52 study sites.

Data description:
Variable	Description
s350 - s1000	reflectance data which aggregated to 10-nm increments through using mathematical operation average (the original data has 2 nm interval)
s1010 - s2500	reflectance data which aggregated to 10-nm increments through using mathematical operation average (the original data has 1 nm interval)
FAC1	factor scores generated based on the contribution of factor 1 at 52 study sites
FAC2	factor scores generated based on the contribution of factor 2 at 52 study sites
FAC3	factor scores generated based on the contribution of factor 3 at 52 study sites
SR550650	The selected optimal sensitive band combinations (spectral ratio) of 550 nm and 650 nm at 52 study sites
DR (580,650)	The selected optimal sensitive band combinations (spectral difference) of 580 nm and 650 nm at 52 study sites
SR 650750	The selected optimal sensitive band combinations (spectral ratio) of 650 nm and 750 nm at 52 study sites
DR 680750	The selected optimal sensitive band combinations (spectral difference) of 680 nm and 750 nm at 52 study sites

b.	Code

i.	Guangzhou Lasso with Alpha Values-Test1.py: The Python code of implementing band selection by Lasso regression with SciKit-Learn library. The Alpha value is selected as 0.01 and the selected test sample size is 15% for cross validation

c.	Output:

i.	Lasso_F1_Alp001_CV15_Optimal.xlsx: the optimal bands/band combination of Factor 1 selected by the Lasso regression with their coefficient values.

ii.	Lasso_F2_Alp001_CV15_Optimal.xlsx: the optimal bands/band combination of Factor 2 selected by the Lasso regression with their coefficient values.

iii.	Lasso_F3_Alp001_CV15_Optimal.xlsx: the optimal bands/band combination of Factor 3 selected by the Lasso regression with their coefficient values.

iv.	Lasso Cross Validation Results.txt: Lasso regression cross validation result of three models.


2.	Data validation by multiple regression analysis


a.	Input data:

i.	Lasso_F1_Alp001_CV15_Optimal.xlsx: explained in previous section

ii.	Lasso_F2_Alp001_CV15_Optimal.xlsx: explained in previous section

iii.	Lasso_F3_Alp001_CV15_Optimal.xlsx: explained in previous section

b.	Output:

i.	Fact1_Regression_from_Python.html: The SPSS multiple regression (backward method) result of Factor 1 and the optimal bands/band combination selected by the Lasso regression. The 6th model is used to explain the validation of the Lasso regression result. 

ii.	Fact2_Regression_from_Python.html: The SPSS multiple regression (backward method) result of Factor 1 and the optimal bands/band combination selected by the Lasso regression. The 6th model is used to explain the validation of the Lasso regression result. 
iii.	Fact3_Regression_from_Python.html: The SPSS multiple regression (backward method) result of Factor 1 and the optimal bands/band combination selected by the Lasso regression. The 8th model is used to explain the validation of the Lasso regression result. 


