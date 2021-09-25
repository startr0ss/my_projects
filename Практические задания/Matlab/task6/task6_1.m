clc;
clear all;
close all hidden;

n = 100;
r = 1000; 
amountSt = zeros(1, 3);
amountHora = zeros(1, 3);
m = [0, 0, 1];
pRealSt = zeros(3, 20);
pRealHora = zeros(3, 20);
w = 1;
for i = 100 : 100 : 2000
    for j = 1 : r
        x = zeros(3, i);
        x(1, :) = normrnd(0, 1, 1, i); % norm
        x(2, :) = unifrnd(-sqrt(3), sqrt(3), 1, i); % unif
        x(3, :) = exprnd(1, 1, i); % exp
        p = 0.95;
        t = tinv(0.5 * (1 + p), i - 1);
        k = sqrt((-log((1 - p) / 2)) / (2 * i)) - 1 / (6 * i);
        average = sum(x, 2) ./ i;
        s = zeros(1, 3);
        st = zeros(2, 3);
        hora = zeros(2, 3);
        for e = 1 : 3
            s = sqrt((1 / (i - 1)) * sum((x(e, :) - average(e)) .^ 2));
            st(1, e) = average(e) - (s / sqrt(i)) * t;
            st(2, e) = average(e) + (s / sqrt(i)) * t;
            hora(1, e) = average(e) - (max(x(e, :)) - min(x(e, :))) * k;
            hora(2, e) = average(e) + (max(x(e, :)) - min(x(e, :))) * k;
            if ((m(e) > st(1, e)) && (m(e) < st(2, e))) 
                amountSt(e) = amountSt(e) + 1;
            end
            if ((m(e) > hora(1, e)) && (m(e) < hora(2, e))) 
                amountHora(e) = amountHora(e) + 1;
            end
        end
    end
    for j = 1 : 3
        pRealSt(j, w) = amountSt(j) / i / (r / n);
        pRealHora(j, w) = amountHora(j) / i / (r / n); 
    end
    [p, cint] = binofit(amountSt(1), i * (r / n)); 
    w = w + 1;
end
n = 100 : 100 : 2000;
plot(n, pRealSt(1, :), n, pRealSt(2, :), n, pRealSt(3, :));
% plot(n, pRealHora(1, :), n, pRealHora(2, :), n, pRealHora(3, :));
legend('norm', 'unif', 'exp');
grid on;