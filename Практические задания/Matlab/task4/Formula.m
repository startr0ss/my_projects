function [erMean, erMed] = Formula(n, dn, medN)
erMean = (1 / length(dn)) * sum(dn);
dwnN = n - dn;
upN = n + dn;
dwnMed = median(dwnN);
upMed = median(upN);
erMed = max([medN - dwnMed, upMed - medN]);