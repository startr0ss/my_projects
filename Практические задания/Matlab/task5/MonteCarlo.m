function [erSD, erMAD] = MonteCarlo(n, dn, sdN, madN)
m = 10 ^ 3;
k = length(n);
errors = zeros(k, m);
for i = 1 : k
    errors(i, :) = unifrnd(-dn(i), dn(i), 1, m);
end
tmN = repmat(n, m, 1);
inacN = tmN' + errors;
inacSD = zeros(1, m);
inacMAD = zeros(1, m);
for i = 1 : m
    inacSD(i) = std(inacN(:, i));
    inacMAD(i) = MAD(inacN(:, i));
end
minErSD = abs(sdN - min(inacSD));
maxErSD = abs(sdN - max(inacSD));
erSD = max(minErSD, maxErSD);
minErMAD = abs(madN - min(inacMAD));
maxErMAD = abs(madN - max(inacMAD));
erMAD = max(minErMAD, maxErMAD);