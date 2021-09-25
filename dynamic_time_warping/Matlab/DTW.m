function d = DTW(setSign1, setSign2, p)
[amnt, lngth1] = size(setSign1);
lngth2 = size(setSign2, 2);
m1 = repmat(setSign1, 1, 1, lngth2); 
tmV = repmat(setSign2, 1, 1, lngth1); 
for i = 1 : lngth2 
    m2(:, i, :) = tmV(:, :, i);
end

if (p > 0)
    m = (sum((abs(m1 - m2)) .^ p, 1)) .^ (1 / p);
end

if (p == -1)
    m = max(abs(m1 - m2));
end

if (p == -2)
    wEvk = (1 / amnt) : (1 / amnt) : 1; 
    wEvk = wEvk(end : -1 : 1);
    tmV = (abs(m1 - m2)) .^ 2;
    for i = 1 : lngth1
        m(:, :, i) = zeros(amnt, lngth2);
    end
    for i = 1 : lngth1
        for j = 1 : lngth2
            [values, number] = sort(tmV(:, j, i));
            for e = 1 : amnt
                m(number(e), j, i) = tmV(number(e), j, i) * wEvk(number(e));
            end
        end
    end
    m = sqrt(sum(m, 1)); 
end
      
for i = 1 : lngth2
    D(i, :) = m(:, :, i);
end

T(1, 1) = D(1, 1);
for n = 2 : lngth1
    T(n, 1) = D(n, 1) + T(n - 1, 1);
end
for m = 2 : lngth2
    T(1, m) = D(1, m) + T(1, m - 1);
end
for n = 2 : lngth1
    for m = 2 : lngth2
        T(n, m) = D(n, m) + min([T(n - 1, m), T(n - 1, m - 1), T(n, m - 1)]);
	end
end

n = lngth1; 
m = lngth2;
k = 1;
e = 1;
path(1, :) = [lngth1, lngth2];
while ((n + m) ~= 2)
    if (n - 1) == 0
        m = m - 1;
    elseif (m - 1) == 0
        n = n - 1;
    else 
        [values, number] = min([T(n - 1, m), T(n, m - 1), T(n - 1, m - 1)]);
        switch number
            case 1
                n = n - 1;
            case 2
                m = m - 1;
            case 3
                n = n - 1;
                m = m - 1;
        end
    end
    k = k + 1;
    e = e + 1;
    path(e, :) = [n, m];
end
d = T(lngth1, lngth2);
d = d / k;