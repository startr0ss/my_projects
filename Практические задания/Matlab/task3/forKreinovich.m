function [y] = forKreinovich(d, error, kolvo)
s = 0;
for j = 1 : kolvo
    s = s + (d ^ 2 ./ (d ^ 2 + error(j) ^ 2));
end
y = s - (kolvo / 2);