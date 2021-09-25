clc;
clear all;
close all hidden;

% Download of data:
n = 10;
% [vect, vectForClsf] = download(n);
% save vect.mat vect;
% save vectForClsf.mat vectForClsf;
load('vect.mat');
load('vectForClsf.mat');
% p = [1, 1.5, 2, 3, 4, -1, -2];
% p = [1, 1.5, 2, 3, 4, 5, 6, 7, 8, 9, 10];
p = 1 : 0.1 : 20;
amntClust = 3;
for i = 1 : length(p)
    [nClust, cClust, sumDist, rslt] = clustering(n, vect, p(i));
    for j = 1 : n
        dVectClsf(j) = DTW(vectForClsf, vect(:, :, j), p(i)); 
    end
    arrd = zeros(amntClust, 1);
    for j = 1 : amntClust
        arrd(j) = sqrt(sum((dVectClsf - cClust(j, :)) .^ 2));
    end
    r(i) = rslt;
end
[minVal, num] = min(r);
plot(p, r);
xlabel('p');
ylabel('sumDist');
grid on;