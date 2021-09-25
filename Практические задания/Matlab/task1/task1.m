clc;
clear all;
close all hidden;

n1 = 10 ^ 2;
brdr = 1;
array1 = zeros(1, n1);
for i = 1 : n1
    array1(i) = i;
end
array2 = unifrnd(-brdr, brdr, 1, n1);
sum1 = array1 + array2;
subtract1 = array1 - array2;
multiply1 = array1 .* array2;
division1 = array1 ./ array2;
n2 = 4;
array3 = zeros(n2, n1);
for i = 1 : n2
    for j = 1 : n1
        array3(i, j) = (i - 1) * 10 + j;
    end
end
array4 = unifrnd(-brdr, brdr, n2, n1);
sum2 = array3 + array4;
subtract2 = array3 - array4;
multiply2 = array3 .* array4;
division2 = array3 ./ array4;