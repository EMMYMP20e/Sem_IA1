clear all
close all
clc

%% Ingresar las funciones:
f = @(x,y,z) ((2*x) + y - 8).^2 + ((4*x) + (3*y) + (5*z) - 25).^2 + (x + (2*z) - 4).^2 + ((3*x) + y + (10*z) - 20).^2;

%% Inicializar los valores:
G = 750;
n = 50;
D = 3;
F=1.3;
cr=1;
u=zeros(D,n);
x= zeros(D,n);
v= zeros(D,n);
fitness= zeros(1, n);

%% Limites:
xl = [-2;-2;-2];
xu = [2;2;22];

%% Inicializar individuos:
    for i=1:n
    x(:,i) = xl + (xu-xl).*rand(D,1);
    end
    
%% Evolución Diferencial:
    for g=1:1:G
        for i=1:1:n
            r1= randi([1 n],1);
            while (r1 ==i)
                r1= randi([1 n],1);
            end
            r2= randi([1 n],1);
            while (r2==r1 || r2 ==i)
                r2= randi([1 n],1);
            end
            r3= randi([1 n],1);
            while(r3 == r1 || r3 == r2 || r3==i)
                r3= randi([1 n],1);
            end
            v(1,i)= x(1,r1) + F*(x(1,r2)-x(1,r3));
            v(2,i)= x(2,r1) + F*(x(2,r2)-x(2,r3));
            v(3,i)= x(3,r1) + F*(x(3,r2)-x(3,r3));
            for j=1:1:D
                ra= rand;
                if(ra <=cr)
                    u(j,i) = v(j,i);
                else
                    u(j,i)=x(j,i);
                end
            end
            if(f(u(1,i),u(2,i),u(3,i)) < f(x(1,i),x(2,i),x(3,i)))
                x(1,i)= u(1,i);
                x(2,i)= u(2,i);
                x(3,i)= u(3,i);
            end        
        end
        for i=1:1:n
            fitness(i)= f(x(1,i),x(2,i),x(3,i));
        end
    end
    
%% Resultados:
    [~,ind] = min(fitness);
    disp(['ERROR= ', num2str(fitness(ind))]);
    disp([num2str(x(1,ind)),' ',num2str(x(2,ind)),' ', num2str(x(3,ind))]);