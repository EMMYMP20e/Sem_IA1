clear all
close all
clc

load data

X = xp;
y = yp;

m = numel(y);

A=X;
X = [ones(m,1), X];
theta=zeros(2,1);
alpha = 0.01;
iter_max=1500;

for i=1:m
    h(i,1)= theta'*X(i,:)';
end

J = (1/(2*m))*sum((h-y).^2);
J_conver = zeros(iter_max,1);

[~,n]=size(X);

figure(2)
plot(0,J,'*');
hold on

for iter=1:iter_max
    J_conver(iter)=J;
    for j=1:n
        gradiente_j(j,1) = (1/m)*sum((h-y).*X(:,j));
    end
    theta=theta - alpha*gradiente_j;
    
    for i=1:m
        h(i,1)= theta'*X(i,:)';
    end
    J = (1/(2*m))*sum((h-y).^2);
    %figure(2)
    %plot(iter,J,'*');
end
% figure(1)
% plot(A,y,'ob','markerFaceColor','r');
% hold on
% plot(A,h);
% hold on
% disp('Theta:')
% disp(theta)
% disp('J (Error)')
% disp(J)
% %X
% x=15;
% fx=x*theta(1)+theta(2);
%plot(x,fx)
figure(1)
plot(A,y,'ob','markerFaceColor','r');
hold on

%figure
%plot(J_conver)


x=4:0.1:24;

f=numel(x);

x=[ones(f,1),x'];
for i=1:f
    h2(i,1)=theta'*x(i,:)';
end
figure(1)
plot(x(:,2),h2)
hold on

dato1=[1 14];
precio=theta'*dato1';

figure(1)
plot(dato1(2),precio,'go')





