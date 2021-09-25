clc;
clear all;
close all hidden;

% Excel parameters:
fileName = 'HOMA2CalculatorValidation.xls';
sheetExcel = 'C-Peptide';
rangeExcelIn = 'A3:B314';
rangeExcelOut = 'F3:H314';

% Ranges of input parameters:
rangeGlucoseStart = 6 : 0.5 : 12;
rangeCPeptideStart = 0.2 : 0.1 : 2.5;
rangeGlucose = zeros(1, length(rangeGlucoseStart) * length(rangeCPeptideStart));
rangeCPeptide = repmat(rangeCPeptideStart, 1, length(rangeGlucoseStart));
for i = 1 : length(rangeGlucoseStart)
    for j = 1 : length(rangeCPeptideStart)
        rangeGlucose((i-1) * length(rangeCPeptideStart) + j) = rangeGlucoseStart(i);
    end
end
arrayIn = [rangeGlucose', rangeCPeptide'];

% Calculation of base output parameters:
xlswrite(fileName, arrayIn, sheetExcel, rangeExcelIn);
result = xlsread(fileName, sheetExcel, rangeExcelOut);
baseHOMA2_B = result(:, 1);
baseHOMA2_IR = result(:, 3);  

% CV:
cvGlucose = 0.01;
cvCPeptide = 0.04;

% Calculation of output parameters:
amount = 1000;
HOMA2_B = zeros(length(rangeGlucose), amount);
HOMA2_IR = zeros(length(rangeCPeptide), amount);
for i = 1 : amount
    % Generation input parameters:
    glucoseStart = rangeGlucoseStart + normrnd(0, rangeGlucoseStart .* cvGlucose, 1, length(rangeGlucoseStart));
    cPeptideStart = rangeCPeptideStart + normrnd(0, rangeCPeptideStart .* cvCPeptide, 1, length(rangeCPeptideStart));
    glucose = zeros(1, length(glucoseStart) * length(cPeptideStart));
    cPeptide = repmat(cPeptideStart, 1, length(glucoseStart));
    for j = 1 : length(glucoseStart)
        for e = 1 : length(cPeptideStart)
            glucose((j-1) * length(cPeptideStart) + e) = glucoseStart(j);
        end
    end  
    % Requirements of HOMA2Calculator
    for j = 1 : length(cPeptide) 
        if cPeptide(j) < 0.2
            cPeptide(j) = 0.2;
        end
        if cPeptide(j) > 2.5
            cPeptide(j) = 2.5;
        end
    end
    % Calculation: 
    arrayIn = [glucose', cPeptide'];  
    xlswrite(fileName, arrayIn, sheetExcel, rangeExcelIn);
    result = xlsread(fileName, sheetExcel, rangeExcelOut);
    HOMA2_B(:, i) = result(:, 1);
    HOMA2_IR(:, i) = result(:, 3);
end

% Calculation errors std:
baseHOMA2_B = repmat(baseHOMA2_B, 1, amount);
baseHOMA2_IR = repmat(baseHOMA2_IR, 1, amount);
errorHOMA2_B = HOMA2_B - baseHOMA2_B;
errorHOMA2_IR = HOMA2_IR - baseHOMA2_IR;

% Results:
% Special STD:
m2ErrorHOMA2_B = sqrt(sum(errorHOMA2_B .^ 2) / size(errorHOMA2_B, 1));
m2ErrorHOMA2_IR = sqrt(sum(errorHOMA2_IR .^ 2) / size(errorHOMA2_IR, 1));
resultsM2Errors = zeros(2, 3);
resultsM2Errors(1, 1) = min(m2ErrorHOMA2_B);
resultsM2Errors(2, 1) = min(m2ErrorHOMA2_IR);
resultsM2Errors(1, 2) = sum(m2ErrorHOMA2_B) / amount;
resultsM2Errors(2, 2) = sum(m2ErrorHOMA2_IR) / amount;
resultsM2Errors(1, 3) = max(m2ErrorHOMA2_B);
resultsM2Errors(2, 3) = max(m2ErrorHOMA2_IR);

save m2ErrorsHOMA.mat resultsM2Errors;