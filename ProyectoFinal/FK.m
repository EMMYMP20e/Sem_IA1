clear all
close all
clc
% Méndez Pérez Emmanuel
% I7039 D04
% Proyecto Final


%p_final = [0.8; 0.2; 0.3];
p_final = [0.5; 0.1; 0.3];

xl = [-160; -150; -135];
xu = [160; 150; 135];

%% Inicializar los valores:
G = 750;
n = 250;
D = 3;
F=0.6;
cr=0.9;
u=zeros(D,n);
x= zeros(D,n);
v= zeros(D,n);
fitness= zeros(1, n);

l1 = 0.5;
l2 = 0.5;

f = @(p,theta) (((p(1)-p_final(1)).^2 + (p(2)-p_final(2)).^2 + (p(3)-p_final(3)).^2)...
    + 1000*(g_(theta(1),1) + g_(theta(2),2) + g_(theta(3),3)));

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
            q1=[u(1,i),u(2,i),u(3,i)];
            q2=[x(1,i),x(2,i),x(3,i)];
            p1=fk(q1);
            p2=fk(q2);
            if(f(p1,q1) < f(p2,q2))
                x(1,i)= u(1,i);
                x(2,i)= u(2,i);
                x(3,i)= u(3,i);
            end        
        end
        for i=1:1:n
            q1=[x(1,i),x(2,i),x(3,i)];
            p1=fk(q1);
            fitness(i)= f(p1,q1);
        end
    end
[~,ind] = min(fitness);
disp(['ERROR= ', num2str(fitness(ind))]);
disp([num2str(x(1,ind)),' ',num2str(x(2,ind)),' ', num2str(x(3,ind))]);
q=[x(1,ind),x(2,ind),x(3,ind)];
p=fk(q);
disp([num2str(p(1)),' ',num2str(p(2)),' ', num2str(p(3))])

Dibujar_Manipulador(q,l1,l2,p_final);

%% Funcion penalizacion
function r = g_(x,i)
    xl = [-160; -150; -135];
    xu = [160; 150; 135];
    if(xl(i)<x && x<xu(i))
        r=0;
    else
        r=1;
    end
end 

%% Cinematica directa
function p = fk(q)
    l1 = 0.5;
    l2 = 0.5;
    p = [0.0; 0.0; 0.0];
    p(1) = -sin(q(1)-pi/2)*(l1*cos(q(2))+l2*cos(q(2)+q(3)));
    p(2) = cos(q(1)-pi/2)*(l1*cos(q(2))+l2*cos(q(2)+q(3)));
    p(3) = l1*sin(q(2))+l2*sin(q(2)+q(3));
end
