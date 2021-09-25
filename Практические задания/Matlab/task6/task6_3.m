clc;
clear all;
close all hidden;

upB = 5000;
step = 100;
r = 1000;
pReal = zeros(3, upB / step);
averageW = zeros(3, upB / step);
dis = 1; 
q = 1;
for i = 100 : step : upB
    k = zeros(1, 3);
    p = 0.95;
    koef1 = chi2inv(0.5 * (1 + p), i - 1);
    koef2 = chi2inv(0.5 * (1 - p), i - 1);
    w = zeros(3, r);
    for j = 1 : r
        x = zeros(3, i);
        x(1, :) = normrnd(0, 1, 1, i); % norm
        x(2, :) = unifrnd(-sqrt(3), sqrt(3), 1, i); % unif
        x(3, :) = exprnd(1, 1, i); % exp
        d = zeros(1, 3);
        borders = zeros(2, 3);
        for e = 1 : 3
            d(e) = var(x(e, :));
            borders(1, e) = (d(e) * (i - 1)) / koef1;
            borders(2, e) = (d(e) * (i - 1)) / koef2;
            w(e, j) = borders(2, e) - borders(1, e); 
            if ((dis > borders(1, e)) && (dis < borders(2, e))) 
                k(e) = k(e) + 1;
            end
        end
    end
    pReal(:, q) = k ./ r;
    averageW(:, q) = sum(w, 2) ./ r;
    q = q + 1;
end
n = 100 : step : upB;
plot(n, pReal(1, :), n, pReal(2, :), n, pReal(3, :));
% plot(n, averageW(1, :), n, averageW(2, :), n, averageW(3, :));
legend('norm', 'unif', 'exp');
grid on;