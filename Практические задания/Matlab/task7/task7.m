clc;
clear all;
close all hidden;

upB = 10;
step = 0.1;
sd = 0 : step : upB;
n = 4;
N = 4;
r = 1000;
p = 0.95;
e = 1;
q = 1;
arrayR = -1 * ones(1, upB / step);
for i = 1 : (upB / step)
    noSign = 0;
    for j = 1 : r
        y0 = [0.73, 1.24, 1.54, 1.90;
            0.75, 1.27, 1.50, 1.74;
            0.75, 1.35, 1.43, 1.92;
            0.74, 1.20, 1.60, 1.79];
        error = normrnd(0, sd(i), n, N);
        y = y0 + error;
        means = mean(y, 1);
        s = var(y, 0,1);
        sV = (1 / n) * sum(s);
        sT = var(means);
        koef = (N * sT) / sV;
        alpha = 0.01;
        border = finv(1-alpha, n-1, n * (N - 1));
        if (koef < border)
            noSign = noSign + 1;      
        end
    end
    arrayR(e) = noSign / r;
    e = e + 1;
    if (noSign / r >= p)
        result(q) = sd(i);
        q = q + 1;
    end
end