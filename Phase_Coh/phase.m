clear all 
clc
% Loading the data
ismr_load = xlsread('ismr.xls');
nino3_load = xlsread('nino3.xls');
for i=1:133
    for j=1:12
        ismr_v((i-1)*12+j) = ismr_load(i,j);
        nino3((i-1)*12+j) = nino3_load(i,j);
    end
end
ismr=ismr_v/10;


% Since our work focuses on the inference of phase relations of inter-annual
% oscillations, we low-pass filtered the data in the spectral domain by multiplying the Fourier
% transformation of the data with a hyperbolic tangent, i.e. high frequency variability with
% frequencies higher than 0.7 cycles per year is damped.
% (reference : Maruan 2006)

% Testing Hyperbolic tangens filter 
% x = -5:0.01:5;
% plot(x,-tanh(x-0.7)), grid on
% 0.7 cycles per year means 0.7/12 cycles per month
% 0.0583 cycles per month

N = size(ismr,2);
x = 1:N;
years = x/12+1871;
filt = (-tanh(x-0.00583)+1)/2;

% Filtering the ISMR data 

ismrt = fft(ismr);
ismrt = real(ismrt) .* filt;
ismr_filt = ifft(real(ismrt));
ismrt_filt_dtr = detrend(ismr_filt);

% Filtering the NINO3 data

nino3t = fft(nino3);
nino3t = nino3t .* filt;
nino3_filt = ifft(nino3t);
nino3_filt_dtr = detrend(nino3_filt);

% estimate derivatives by second order difference scheme and running
ismr_sec_diff(1:N-2) = 0.0;
nino3_sec_diff(1:N-2) = 0.0;
% Second order differencing done as per 
% http://robjhyndman.com/talks/RevolutionR/8-Differencing.pdf
ismr_sec_diff(1:N-2) = ismrt_filt_dtr(1:N-2) - 2*ismrt_filt_dtr(2:N-1) + ismrt_filt_dtr(3:N);
nino3_sec_diff(1:N-2) = nino3_filt_dtr(1:N-2) - 2*nino3_filt_dtr(2:N-1) + nino3_filt_dtr(3:N);

% running mean with window width 2l + 1 = 13 data points
n1 = 1594;
%ismrr(1:n1) = 0.0;
%nino3r(1:n1) = 0.0;
Running = 13;
for i=1:n1-Running
        ismrr(i)  = sum(ismr_sec_diff(i:i+Running-1))/Running;
        nino3r(i) = sum(nino3_sec_diff(i:i+Running-1))/Running;
end
n2 = 1594-13+1;
x = 1:n2;
years = x/12+1871;
% Embed by Hilbert transformation with phase defined according to Eq. (4.7).

ismr_hilbert  = hilbert(ismrr);
nino3_hilbert = hilbert(nino3r);
ismr_real = real(ismr_hilbert);
ismr_imag = imag(ismr_hilbert);
nino3_real = real(nino3_hilbert);
nino3_imag = imag(nino3_hilbert);

% Phase unwrapped as per
% https://in.mathworks.com/matlabcentral/answers/295635-why-the-phase-obtained-with-hilbert-transform-and-phase-unwrap-is-different-from-the-actual-phase

phase_ismr = unwrap(angle(ismr_hilbert));
phase_nino3 = unwrap(angle(nino3_hilbert));

phase_coh = phase_ismr - phase_nino3;
plot(years,phase_coh);
xlabel('years');
ylabel('Phase coherence')
Title('Phase coherence between ISMR and NINO3')




