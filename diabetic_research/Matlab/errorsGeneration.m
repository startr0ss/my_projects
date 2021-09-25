clc;
clear all;
close all hidden;

load('dataWithoutErrorsNorm.mat'); % Load the generated data
load('m2ErrorsHOMA.mat'); % Load STD for HOMA2-B and HOMA2-IR

cvHba1c = 0.03; % CV of Hba1c
errorBMI = 0.02; % Error of BMI
errorAge = 0.5; % Error of Age
stdHOMA2_B = sqrt(resultsM2Errors(1, 2)); % STD for HOMA2-B
stdHOMA2_IR = sqrt(resultsM2Errors(2, 2)); % STD for HOMA2-IR

% allData = allData';

% Errors generation:
N = size(allData, 1); % length of the generated data
c = size(allData, 2); % The amount of coordinates
M = 1000; % The number of repeats
errorsAllData = zeros(N, c, M);
errorForAllBMI = allData(:, 2) .* errorBMI;
for i = 1 : M
    errorsAllData(:, 1, i) = normrnd(0, allData(:, 1) .* cvHba1c, N, 1); 
    for j = 1 : N
        errorsAllData(j, 2, i) = unifrnd(-errorForAllBMI(j), errorForAllBMI(j));
    end
    errorsAllData(:, 3, i) = unifrnd(-errorAge, errorAge, N, 1); 
    errorsAllData(:, 4, i) = normrnd(0, stdHOMA2_B, N, 1);
    errorsAllData(:, 5, i) = normrnd(0, stdHOMA2_IR, N, 1); 
end

% Calculation the data with errors
allData = repmat(allData, 1, 1, M) + errorsAllData;

save allDataWithErrorsNorm.mat allData;

% % Data for SPSS
% fileName = 'dataForSPSS.xls';
% timeArray = 1 : 20;
% for i = 1 : 20
%     sheetExcel = num2str(timeArray(i));
%     xlswrite(fileName, allData(:, :, i), sheetExcel);
% end