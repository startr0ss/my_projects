clc;
clear all;
close all hidden;

upB = 5000;
step = 100;
r = 1000;
pReal = zeros(3, upB / step); 
q = 1;
for i = 100 : step : upB
    k = zeros(1, 3);
    p = 0.95;
    koef = norminv(0.5 * (1 + p), 0, 1);
    for j = 1 : r
        x = zeros(3, i);
        x(1, :) = normrnd(0, 1, 1, i); % norm
        x(2, :) = unifrnd(-sqrt(3), sqrt(3), 1, i); % unif
        x(3, :) = exprnd(1, 1, i); % exp
        med = zeros(1, 3);
        borders = zeros(2, 3);
        for e = 1 : 3
            med(e) = median(x(e, :));
            borders(1, e) = x(e, floor(0.5 * i - 0.5 * sqrt(i) * koef));
            borders(2, e) = x(e, ceil(0.5 * i + 0.5 * sqrt(i) * koef));
            if ((med(e) > borders(1, e)) && (med(e) < borders(2, e))) 
                k(e) = k(e) + 1;
            end
        end
    end
    pReal(:, q) = k ./ r;
    q = q + 1;
end
n = 100 : step : upB;
plot(n, pReal(1, :), n, pReal(2, :), n, pReal(3, :));
legend('norm', 'unif', 'exp');
grid on;