clear all; close all; clc; format compact;

% Circuit component values (static)
C1 = 51.*10^(-12); % 51pF
C2 = 0.047.*10^(-6); % 0.047uF
R1 = 51.*10^3; % 51k Ohms
R2 = 4.7.*10^3; % 4.7k Ohms
Is = 2.5*10^-9; % Saturation current, ~2.5nA (play with if results are undesirable)
Vt = 0.026; % Thermal Vo_guessltage, 26mV@300K

%Drive control, variable between 0 and 500k Ohms
Rd = 500.*10^3;

% Signal parameters
freq = 1000;
w = 2.*pi.*freq;
samplerate = 500*10^3;
amp = .03;
t0 = 0;
tf = .01;
samples = (tf-t0).*(samplerate);
h = (tf-t0)/samples;
t = linspace(t0,tf,samples);

vi = amp.*sin(w.*t);
vi_prime = w.*amp.*cos(w.*t);

%va = (amp.*C2.*R2.*w.*(C2.*R2.*w.*sin(w.*t)-e^(-t/(C2.*R2))+cos(w.*t)))./(C2^2.*R^2.*w^2+1);
for n= 1:samples
    va(n) = (amp.*C2.*R2.*w.*(C2.*R2.*w.*sin(w.*t(n))-exp((-t(n)/(C2.*R2)))+cos(w.*t(n))))./(C2^2.*R2^2.*w^2+1);
end

maxiter = 10000; %Maximum # of iterations for any looping structure
incr = .0001; % used for derivative approximation
eps = 0.000001;

Vo = zeros(samples,1);
fprime_hold = zeros(samples,1);
Vo(1) = 0;

for n = 2:samples %Sample looping
    Vo_guess_old = Vo(n-1);
    for i = 1:maxiter
        %i
        Vo_guess = Vo_guess_old;
        Vo_guess_inc = Vo_guess+incr;
        % F is the equation to be solved
        f = (Vo_guess-vi(n))./(R1+Rd)+Is.*exp((Vo_guess-vi(n))/Vt)-Is.*exp((vi(n)-Vo_guess)/Vt)+C1.*(((Vo_guess-vi(n))-(Vo(n-1)-vi(n-1)))./h)-C2.*(((vi(n)-va(n))-(vi(n-1)-va(n-1)))./h);
        f2 = (Vo_guess_inc-vi(n))./(R1+Rd)+Is.*exp((Vo_guess_inc-vi(n))/Vt)+Is.*exp((vi(n)-Vo_guess_inc)/Vt)+C1.*(((Vo_guess_inc-vi(n))-(Vo(n-1)-vi(n-1)))./h)-C2.*(((vi(n)-va(n))-(vi(n-1)-va(n-1)))./h);
        fprime = (f2-f)/incr; %approximate the derivative
        
        Vo_guess_old = Vo_guess_old - f./fprime;
        check = abs(Vo_guess_old - Vo_guess);
        %eps
        %n
        if(check <= eps || i >= maxiter)
            
            if(i >= maxiter)
                disp('Solution did not converge at n = ')
                n
                i
                Vo(n) = Vo_guess_old;
                pause
            end
            %}
            Vo(n,1) = Vo_guess_old;
            f_hold(n) = f;
            f2_hold(n) = f2;
            fprime_hold(n) = fprime;
            break;
        end
        
    end
end

Fs = samplerate;
T = 1/Fs;
L = length(Vo);
Y = fft(Vo);
P2 = abs(Y/L);
P1 = P2(1:L/2+1);
P1(2:end-1) = 2*P1(2:end-1);
f = Fs*(0:(L/2))/L;

disp('Finished');

title1 = sprintf('Signals Rd = %d A = %d f = %d' ,Rd,amp,freq);
title2 = sprintf('FFT Rd = %d A = %d f = %d', Rd,amp,freq);

figure(1)
plot(t,vi,t,Vo)
legend('Vin','Vo')
title(title1);

figure(2)
loglog(f,P1);
title('FFT of Vo');
xlabel('f(Hz)')
ylabel('|P1(f)|')
axis([0 20000 0 1])
title(title2);
grid on;
