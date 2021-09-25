function [y] = MAD(n)
y = median(n - median(n));