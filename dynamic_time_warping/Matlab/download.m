function [vect, vectForClsf] = download(n)
fileNames1 = {'ce.txt', 'cp.txt', 'se.txt', 'ts1.txt', 'ts2.txt', 'ts3.txt', 'ts4.txt', 'vs1.txt'}; % Samplimg rate = 1 Hz
fileNames2 = {'fs1.txt', 'fs2.txt'}; % Samplimg rate = 10 Hz
fileNames3 = {'eps1.txt', 'ps1.txt', 'ps2.txt', 'ps3.txt', 'ps4.txt', 'ps5.txt', 'ps6.txt'}; % Samplimg rate = 100 Hz
lngth = zeros(1, 3);
lngth(1) = length(fileNames1);
lngth(2) = length(fileNames2);
lngth(3) = length(fileNames3);
for i = 1 : lngth(1)
    dataSR1(:, :, i) = load(string(fileNames1(i)));
end
for i = 1 : lngth(2)
    dataSR10(:, :, i) = load(string(fileNames2(i)));
end
for i = 1 : lngth(3)
    dataSR100(:, :, i) = load(string(fileNames3(i)));
end
% Matrix decimate:
for i = 1 : size(dataSR1(:, :, 1), 1)
    e = lngth(1) + 1;
    for j = 1 : lngth(2)
        dataSR1(i, :, e) = decimate(dataSR10(i, :, j), 10);
        e = e + 1;
    end
    for j = 1 : lngth(3)
        dataSR1(i, :, e) = decimate(dataSR100(i, :, j), 100);
        e = e + 1;
    end
end
vect = zeros(sum(lngth), size(dataSR1(:, :, 1), 2), n);
for i = 1 : n
    for j = 1 : sum(lngth)
        vect(j, :, i) = dataSR1(i, :, j);
    end
end
vectForClsf = zeros(sum(lngth), size(dataSR1(:, :, 1), 2));
for i = 1 : sum(lngth)
    vectForClsf(i, :) = dataSR1(n + 1, :, i);
end