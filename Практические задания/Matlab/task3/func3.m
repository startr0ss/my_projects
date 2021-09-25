function [y] = func3(x1, x2, x3, x4) 
y = sqrt(x1 ^ 2 + x2 ^ 2 + x3 ^ 2) * atan(x4 / (x1 + x2 + x3 + x4));