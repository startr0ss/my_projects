clc;
clear all;
close all hidden;

x = [1.00, 0.73, 2.54, 10.3];
delta = [0.01, 0.05, 0.1];
deltaX1 = 0.00 : 0.01 : 1.00; 
n1 = length(deltaX1);
error = zeros(3, n1);
% complex-step:
alpha = 10 ^ (-200);
d = 1i * alpha;
for i = 1 : n1       
    df1 = abs((imag(func3(x(1) + d, x(2), x(3), x(4)))) / alpha);
    df2 = abs((imag(func3(x(1), x(2) + d, x(3), x(4)))) / alpha);
    df3 = abs((imag(func3(x(1), x(2), x(3) + d, x(4)))) / alpha);
    df4 = abs((imag(func3(x(1), x(2), x(3), x(4) + d))) / alpha);
    error(1, i) = df1 * deltaX1(i) + df2 * delta(1) + df3 * delta(2) + df4 * delta(3);
end
% Monte - Carlo:
y0 = func3(x(1), x(2), x(3), x(4));
n2 = 10000;
for i = 1 : n1
    delta2 = [deltaX1(i), delta];
    downB = x - delta2;
    upB = x + delta2;
    x1 = unifrnd(downB(1), upB(1), 1, n2);
    x2 = unifrnd(downB(2), upB(2), 1, n2);
    x3 = unifrnd(downB(3), upB(3), 1, n2);
    x4 = unifrnd(downB(4), upB(4), 1, n2);
    y2 = zeros(1, n2);
    for j = 1 : n2
        y2(j) = func3(x1(j), x2(j), x3(j), x4(j));
    end
    error(2, i) = max(abs(y0 - max(y2)), abs(y0 - min(y2)));
end
% Kreinovich:
n3 = 300;
koef = 0.01;
for i = 1 : n1
    delta3 = [deltaX1(i), delta];
    x3 = zeros(4, n3);
    r = unifrnd(0, 1, 4, n3);
    for j = 1 : n3
        for e = 1 : 4
            x3(e, j) = x(e) + koef * delta3(e) * tan(pi * (r(e, j) - 0.5));
        end
    end
    y3 = zeros(1, n3);
    for j = 1 : n3
        y3(j) = func3(x3(1, j), x3(2, j), x3(3, j), x3(4, j));
    end
    errorY3 = y3 - y0;
    maxErrorY3 = max(abs(errorY3));
    a = 0;
    b = maxErrorY3;
    l = b - a;
    while l > 10 ^ (-4)
        if forKreinovich(a, errorY3, n3) * forKreinovich(b, errorY3, n3) < 0
            c = (a + b) / 2;
            if forKreinovich(a, errorY3, n3) * forKreinovich(c, errorY3, n3) < 0 
                b = c;
            else
                a = c;
            end
        end
        l = b - a;
    end
    error(3, i) = ((b + a) / 2) / koef;
end
%
plot(deltaX1, error(1, :), deltaX1, error(2, :), deltaX1, error(3, :));
legend('complex-step', 'Monte-Carlo', 'Kreinovich');
grid on;