clear all
close all
clc

% Méndez Pérez Emmanuel y Villaseñor Cisneros Damian Alfonso
% I7039 D04
% Ejercicio 4

load data

N = numel(xp); %Población Total

m= size(xp,1);

g= @(w) w(1) + w(2)*xp + w(3)*xp.^2 + w(4)*xp.^3 + w(5)*xp.^4;

f= @(w) (0.5/m)*sum((yp - g(w)).^2);


xl = [-10 -5 -1 -0.1 -0.1]';
xu = [10 5 1 0.1 0.1]';

G = 10000;
mu = 250;
D = 5;

x = zeros(D,mu+1);
sigma = zeros(D,mu+1);
fitness = zeros(1,mu+1);

plot(xp,yp,'*');

for i=1:mu
    x(:,i) = xl+(xu-xl).*rand(D,1);
    sigma(:,i) = 0.5*rand(D,1);
    fitness(i) = f(x(:,i));
end

for t=1:G
    r1 = randi([1 mu]);
    r2 = randi([1 mu]);
    r3 = randi([1 mu]);
    r4 = randi([1 mu]);
    r5 = randi([1 mu]);
    while r1==r2 
        r2 = randi([1 mu]);
    end
   
    
    x(:,mu+1) = Recombination(x(:,r1),x(:,r2));
    sigma(:,mu+1) = Recombination(sigma(:,r1),sigma(:,r2));

    r = normrnd(0,sigma(:,mu+1),[D 1]);
    x(:,mu+1) = x(:,mu+1) + r;
    
    fitness(mu+1) = f(x(:,mu+1));

    [~,I] = sort(fitness);
    x = x(:,I);
    sigma = sigma(:,I);
    fitness = fitness(I);
end

[~,ib] = min(fitness);

emma = 0:0.01:15;
y = x(1,ib) + x(2,ib)*emma + x(3,ib)*emma.^2 + x(4,ib)*emma.^3 + x(5,ib)*emma.^4; 
hold on
plot(emma,y);

disp([' mínimo global en: W=' num2str(x(1,ib)) ' f(W)=' num2str(f(x(:,ib)))])

%% Funciones
function y = Recombination (x1,x2)
    y = 0.5*(x1+x2);
end