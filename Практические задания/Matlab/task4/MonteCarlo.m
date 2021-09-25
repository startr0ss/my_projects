function [erMean, erMed] = MonteCarlo(n, dn, meanN, medN)
m = 10 ^ 3;
k = length(n);
errors = zeros(k, m);
for i = 1 : k
    errors(i, :) = unifrnd(-dn(i), dn(i), 1, m);
end
tmN = repmat(n, m, 1);
inacN = tmN' + errors;
inacMean = zeros(1, m);
inacMed = zeros(1, m);
for i = 1 : m
    inacMean(i) = mean(inacN(:, i));
    inacMed(i) = median(inacN(:, i));
end
minErMean = abs(meanN - min(inacMean));
maxErMean = abs(meanN - max(inacMean));
erMean = max(minErMean, maxErMean);
minErMed = abs(medN - min(inacMed));
maxErMed = abs(medN - max(inacMed));
erMed = max(minErMed, maxErMed);