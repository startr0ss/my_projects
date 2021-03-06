function [erSD, erMAD] = Formula(n, dn, sdN)
meanN = mean(n);
erD = (2 ./ (length(n) - 1)) .* sum((n - meanN) .* dn);
erSD = max([sdN - sqrt(sdN .^ 2 - erD), sqrt(sdN .^ 2 + erD) - sdN]);
dwnN = n - dn;
upN = n + dn;
dwnMed = median(dwnN);
upMed = median(upN);
erMed = max([median(n) - dwnMed, upMed - median(n)]);
erMAD = median(dn + erMed);
   