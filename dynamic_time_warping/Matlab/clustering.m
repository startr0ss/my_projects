function [nClust, cClust, sumDist, rslt] = clustering(amnt, vect, p)
amntClust = 3;
for i = 1 : amnt
    for j = 1 : amnt
        d(i, j) = DTW(vect(:, :, i), vect(:, :, j), p);
    end
end
[nClust, cClust] = kmeans(d', amntClust);
e = zeros(1, amntClust);
for i = 1 : amnt
    switch nClust(i)
        case 1
            e(1) = e(1) + 1;
            dist1(e(1), :) = d(i, :);
        case 2
            e(2) = e(2) + 1;
            dist2(e(2), :) = d(i, :);
        case 3
            e(3) = e(3) + 1;
            dist3(e(3), :) = d(i, :);
    end
end

for i = 1 : e(1)
    dist1(i, :) = (dist1(i, :) - cClust(1, :)) .^ 2;
end
for i = 1 : e(2)
    dist2(i, :) = (dist2(i, :) - cClust(2, :)) .^ 2;
end
for i = 1 : e(3)
    dist3(i, :) = (dist3(i, :) - cClust(3, :)) .^ 2;
end
tmV1 = sqrt(sum(dist1, 2));
tmV2 = sqrt(sum(dist2, 2));
tmV3 = sqrt(sum(dist3, 2));

for i = 1 : amntClust
    switch i
        case 1
            sumDist(i) = sum(tmV1);
        case 2
            sumDist(i) = sum(tmV2);
        case 3
            sumDist(i) = sum(tmV3);
    end
end
rslt = sum(sumDist);