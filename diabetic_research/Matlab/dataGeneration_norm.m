clc;
clear all;
close all hidden;

k = 5; % The amount of clusters
c = 5; % The amount of coordinates
N = [577, 1575, 1373, 1942, 3513]; % Amounts of patients

% Centers of clusters:
% Hba1c|BMI|Age|HOMA2-B|HOMA2-IR
centers = [80.03, 27.45, 50.48, 56.71, 2.16; % SAID
           101.85, 28.86, 56.74, 47.64, 3.18; % SIDD
           54.07, 33.85, 65.25, 150.47, 5.54; % SIRD
           57.70, 35.71, 48.96, 95.03, 3.35; % MOD
           50.08, 27.94, 67.37, 86.59, 2.55]; % MARD

% The downer border of clusters:
% Hba1c|BMI|Age|HOMA2-B|HOMA2-IR
dwnBrdrs = [52, 22, 36, 23, 1.1; % SAID
            88, 26, 50, 25, 2.2; % SIDD
            45, 31, 60, 120, 3.7; % SIRD
            47, 32, 39, 74, 2.5; % MOD
            43, 26, 61, 70, 2.0]; % MARD

% The upper border of clusters:
% Hba1c|BMI|Age|HOMA2-B|HOMA2-IR
upBrdrs = [105, 31, 64, 80, 2.5; % SAID
           115, 32, 64, 60, 3.7; % SIDD
           57, 37, 72, 170, 5.9; % SIRD
           66, 39, 57, 115, 4.1; % MOD
           54, 30, 73, 105, 2.8]; % MARD

% Means SD for all clusters:
koef = 1.349;
SD = (upBrdrs - dwnBrdrs) ./ koef;

% Data generation:
allData = zeros(sum(N), c);
for i = 1 : c
    l = 1;
    r = 0;
    for j = 1 : k
        r = r + N(j);
        allData(l : r, i) = normrnd(centers(j, i), SD(j, i), N(j), 1);
        for e = l : r
            if allData(e, i) < dwnBrdrs(j, i)
                allData(e, i) = dwnBrdrs(j, i);
            end
            if allData(e, i) > upBrdrs(j, i)
                allData(e, i) = upBrdrs(j, i);
            end
        end
        l = l + N(j);
    end
end

save dataWithoutErrorsNorm.mat allData;