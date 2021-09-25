clc;
clear all;
close all hidden;

m = 10 : 10 : 1010;
k = length(m);
erFormula = zeros(2, k);
erMonteCarlo = zeros(2, k);
for i = 1 : k
    n = unifrnd(-1, 1, 1, m(i));
    dn = unifrnd(0.1, 0.2, 1, m(i));
    meanN = mean(n);
    medN = median(n);
    [erFormula(1, i), erFormula(2, i)] = Formula(n, dn, medN);
    [erMonteCarlo(1, i), erMonteCarlo(2, i)] = MonteCarlo(n, dn, meanN, medN);
end
% мат ожидание:
plot(m, erFormula(1, :), m, erMonteCarlo(1, :))
xlabel("n")
ylabel("Error of Mean")
legend("Formula", "Monte-Carlo")
grid on
% медиана:
% plot(m, erFormula(2, :), m, erMonteCarlo(2, :))
% xlabel("n")
% ylabel("Error of Med")
% legend("Formula", "Monte-Carlo")
% grid on