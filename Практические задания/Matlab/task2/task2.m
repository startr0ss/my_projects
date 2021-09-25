clc;
clear all;
close all hidden;

x = [1.0, 1.0, 0];
n = 301;
d = zeros(1, n);
dy1 = zeros(1, n);
dy2 = zeros(1, n);
i = 0;
for a = -300 : 1 : 0
    i = i + 1;
    d(i) = 10 ^ a;
    dy1(i) = (func2(x(1), x(2) + d(i), x(3)) - func2(x(1), x(2), x(3))) / d(i);
    d1 = 1i * d(i);
    dy2(i) = (imag(func2(x(1), x(2) + d1, x(3)))) / d(i);
end
semilogx(d, dy1, d, dy2);
legend('конечные суммы', 'complex-step');
grid on;