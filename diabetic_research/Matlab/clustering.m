clc;
clear all;
close all hidden;

load('allDataWithErrorsNorm.mat'); % Load the generated data with errors

load('sumDistNorm.mat');

% Clustering kmeans:
i = 16; % The number of clusters
M = 1000;
minNumClustFound = 0;
while ~minNumClustFound
    curSumDist = zeros(M, 1);
    for j = 1 : M
        [nClust, cClust, curDist] = kmeans(allData(:, :, j), i, 'Replicates', 10);
        curSumDist(j) = sum(curDist);
    end
    sumDist(i, 1 : 2) = [min(curSumDist), max(curSumDist)];
    sumDist(i, 3 : 4) = mean(curSumDist) + 2 * [-1, 1] * std(curSumDist);
    curSumDist = sort(curSumDist);
    sumDist(i, 5 : 6) = [curSumDist(floor(0.025 * M)), curSumDist(ceil(0.975 * M))];
    if (i > 1) && (sumDist(i, 2) >  sumDist(i-1, 1)) && (sumDist(i, 4) >  sumDist(i-1, 3)) && (sumDist(i, 6) >  sumDist(i-1, 5))
        minNumClustFound = 1;
    end
    i = i + 1;
end

save sumDistNorm.mat sumDist;