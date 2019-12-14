close all
clear all
clc

% Méndez Pérez Emmanuel y Villaseñor Cisneros Damian Alfonso
% I7039 D04
% Ejercicio 6


%% DATOS


A = [2 1 0; 4 3 5; 1 0 2; 3 1 10 ];
B = [8 25 4 20];

m=numel(B);

g = @(w) [sum(w.*A(1,:)),sum(w.*A(2,:)), sum(w.*A(3,:)), sum(w.*A(4,:))];

f = @(w) (0.5/m)*(sum(B-g(w)).^2);


h=[1,1,1];

z=g(h);
disp(z);




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

disp(X(:,w),f(X(:,w)));
%% Grafición
