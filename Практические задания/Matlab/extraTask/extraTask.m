clc;
clear all;
close all hidden;

a = 1;
b = -1;
n = 100;
x = 0 : (3 / (n - 1)) : 3;
y0 = a * (x .^ 2) + b * x;
amount = 10;
y = zeros(amount, n);
for i = 1 : amount
    eps = normrnd(0, 0.1, 1, n);
    y(i, :) = y0 + eps;
end
nZv = 200;
aZv = -3 : (6 / (nZv - 1)) : 3;
bZv = -3 : (6 / (nZv - 1)) : 3;
yZv = zeros(nZv ^ 2, n);
for i = 1 : nZv
    for j = 1 : nZv
        yZv((i - 1) * nZv + j, :) = aZv(i) * (x .^ 2) + bZv(j) * x;
    end
end
% классический критерий
meanYi = (1 / amount) * sum(y, 1);
meanYiMatrix1 = repmat(meanYi, amount, 1);
sI = (1 / (amount - 1)) * sum(((y - meanYiMatrix1) .^ 2), 1);
sVospr = (1 / n) * sum(sI);
meanYiMatrix2 = repmat(meanYi, nZv ^ 2, 1);
l = 2;
sAdek = (l / (n - amount)) * sum(((yZv - meanYiMatrix2) .^ 2), 2);
koef = sAdek / sVospr;
alpha = 0.05;
border1 = finv(1 - alpha, n - l, n * (amount - 1));
count1 = 1;
for i = 1 : nZv ^ 2
    if (koef(i) < border1)
        a1(count1) = aZv(floor((i - 1) / nZv) + 1);
        b1(count1) = bZv(mod((i - 1), nZv) + 1);
        count1 = count1 + 1;
    end
end
% критерий Вальда-Вольфовица
yMean = (1 / amount) * sum(y, 1);
yMatrix = repmat(yMean, nZv ^ 2, 1);
rMatrix = yMatrix - yZv;
count2 = 1;
for i = 1 : nZv ^ 2
    r = rMatrix(i, :);
    ind = 2;
    numSer = 1;
    while ind <= n
        numSer = numSer + (r(ind) * r(ind-1) < 0);
        ind = ind + 1;
    end
    numPos = sum(r > 0);
    numNeg = sum(r < 0);
    es = ((2 * numPos * numNeg) / (numPos + numNeg)) + 1;
    ds = ((2 * numPos * numNeg) / ((numPos + numNeg) ^ 2)) * (((2 * numPos * numNeg) - (numPos + numNeg)) / (numPos + numNeg - 1));
    v = (numSer - es) / sqrt(ds);
    border2 = norminv(1 - alpha / 2, 0, 1);
    if (abs(v) < border2)
        tmV = fix(i / nZv) + 1;
        a2(count2) = aZv(floor((i - 1) / nZv) + 1);
        b2(count2) = bZv(mod((i - 1), nZv) + 1);
        count2 = count2 + 1;
    end
end
plot(a1, b1, 'b.', a2, b2, 'r.');
grid on;