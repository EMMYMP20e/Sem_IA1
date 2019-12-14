close all
clear all
clc

load data
alpha = 0.01;

%% DATOS
m = size(y,2);
h = @(w) w(1) + (w(2) * x1) + (w(3) * x2);
g = @(w) 1./(1 + exp(-h(w)));
f = @(w) (0.5/m) * sum((y - g(w)).^2) + (alpha / m) * (w(2).^2 + w(3).^2);



%% Declaración de varibles
w = 0.6;
c1 = 2;
c2 = 2;
N = 100;
D = 3;
G = 200;

X = zeros(D,N); %particulas
V = zeros(D,N); %velocidades
XB = zeros(D,N); % Inicialización de las mejores posiciones de las´partículas.
fitness = zeros(1,N);

%% Limites:
xl = [-10; -10; -10];
xu = [10; 10; 10];


%% Inicialización de variables
for i=1:N
        X(:,i) = xl + (xu-xl).*rand(D,1);
        V(:,i) = 0.5 * randn(D,1);    %Deben ser numeros pequeños para ls velocidade
        XB(:,i) = X(:,i);
end

%% PSO
for g = 1 : G
    for i = 1 : N
        if(f(X(:,i)) < f(XB(:,i))) %Obtencion de los mejores resultados por cada particula
            XB(:,i) = X(:,i);
        end
    end
    
    for i=1:N
        fitness(i) = f(XB(:,i)); %Sacando Fitness
    end
    
    [~,igb] = min(fitness); %Obteniendo el minimo
    
    xg = XB(:,igb); %minimo global
    
    for i = 1 : N
        r1 = rand;
        r2 = rand;
        V(:,i) = (w * V(:,i)) + ((r1 * c1) * (XB(:,i) - X(:,i))) + ((r2 * c2) * (xg - X(:,i))); %actualizando velocidades
        X(:,i) = X(:,i) + V(:,i);
    end
    
end
[~,igb] = min(fitness); %Obteniendo el minimo
    
w = X(:,igb); %minimo global

%% Grafición
c1 = (y==0);
c2 = (y==1);

hold on
grid on
plot(x1(c1),x2(c1),'rx')
plot(x1(c2),x2(c2),'bo')

%x1 = -10:0.1:10;
x1 = -8:0.1:8;
x2 = (-w(1) - w(2) * x1) / w(3);
plot(x1,x2,'g-')

h2 = @(x) w(1) + (w(2) * x(1)) + (w(3) * x(2));
g2 = @(x) 1./(1 + exp(-h2(x)));

if g2([3 7]) >= 0.5
    plot(3,7,'yx')
else
    plot(3,7,'yo')
end

if g2([2 2]) >= 0.5
    plot(2,2,'yx')
else
    plot(2,2,'yo')
end
