M = 4;                   
Ns = 500;                
Rs = 3.84e6;             
sps = 16;               
fc = 1950e6; 
fS=fc*sps


Ts = 1 / Rs;            


symbols = randi([0 M-1], [1, Ns]);

 Vd = 1;
levels= (-Vd/2-(M/2-1)*Vd):Vd:(Vd/2+(M/2-1)*Vd)  

mapped = levels(symbols + 1);
        
t_map = (0:Ns-1) * Ts;               


upsampled_signal = upsample(mapped, sps);
fs = Rs * sps;
t_up = (0:length(upsampled_signal)-1) / fs;


%%%%%%%%%%%

%%%%%%%%%%%
span=6
r=0.22
%%h = ones(1, sps);                     
%%pulse_shaped_signal = conv(upsampled_signal, h);
%%t_ps = (0:length(pulse_shaped_signal)-1) / fs;

tx_pulse = rcosdesign(r, span, sps, 'sqrt'); 
pulse_shaped_signal = conv(upsampled_signal, tx_pulse);
t_ps = (0:length(pulse_shaped_signal)-1) / fs;

fs_new = fc * 10;                      
t_old = t_ps;
t_new = 0 : 1/fs_new : t_old(end);

dac_signal = interp1(t_old, pulse_shaped_signal, t_new, 'linear');


carrier = cos(2*pi*fc*t_new);
T_R = dac_signal .* carrier;





figure;
scatter(levels, zeros(size(levels)), 'filled');
title('Constellation');
xlabel('Amplitude');
ylabel('0');
grid on;


figure;
stem(t_map, mapped); hold on;
plot(t_up, upsampled_signal, '--');
plot(t_ps, pulse_shaped_signal);
legend('Mapped', 'Upsampled', 'Pulse-shaped');
grid on;


figure; pwelch(mapped); title('PSD - Mapped Signal');
figure; pwelch(upsampled_signal); title('PSD - Upsampled Signal');
figure; pwelch(pulse_shaped_signal); title('PSD - Pulse-shaped Signal');

figure;
plot(t_new, dac_signal); hold on;
plot(t_new, T_R , ':');
legend('DAC', 'Modulated');
grid on;


figure;
pwelch(T_R );
title('PSD - Modulated Signal');




Rs=3.84e6;
r=0.22;
band_min=1920e6;
band_max=1980e6;
fc = 1950e6; 
snr=10;


received_signal = awgn(T_R, snr, 'measured');

dmodulated_signal = received_signal .* cos(2*pi*fc*t_new );
load('lpf_coeff.mat');
% hd=low_pass();
ftrec=filter(Num,1,dmodulated_signal)*2;
fs_tar = Rs * sps; % The baseband sampling rate

dt_tar=1/fs_tar;
t0_new=t_new(1):dt_tar:t_new(end);
sig_resampled=interp1(t_new,ftrec,t0_new,'spline')




span = 6;       

%%s_pulse = rcosdesign(r, span, sps, 'normal');  % transmit pulse
%%mf_output = conv(ftrec, fliplr(s_pulse), 'same'); % matched filter
rx_pulse = rcosdesign(r, span, sps, 'sqrt'); 
mf_output = conv(sig_resampled, rx_pulse, 'same'); 

% Normalization: ensure the peaks align with your 'levels'
% If you used 'sqrt' at both ends, the gain is sum(rx_pulse.^2)
mf_output = mf_output / sum(rx_pulse.^2);
%%%%




t_pulse = (0:length(rx_pulse)-1)/Rs;        
t_ftrec = (0:length(sig_resampled)-1)/Rs;          
t_mf = (0:length(mf_output)-1)/Rs;  



figure;

subplot(3,1,1);
plot(t_pulse, t_pulse, 'LineWidth',2);
title('Raised-Cosine Transmit Pulse (s\_pulse)');
xlabel('Time (s)'); ylabel('Amplitude'); grid on;

subplot(3,1,2);
plot(t_ftrec(1:100), ftrec(1:100), 'LineWidth',1.5);
title('Received Baseband Signal (ftrec) with Noise');
xlabel('Time (s)'); ylabel('Amplitude'); grid on;

subplot(3,1,3);
plot(t_mf(1:100), mf_output(1:100), 'LineWidth',2);
title('Matched Filter Output (mf\_output)');
xlabel('Time (s)'); ylabel('Amplitude'); grid on;

%%%%
sampled_symbols = mf_output(1 : sps : (Ns * sps)); 

% Decision Logic (Minimum Distance)
% Find the closest level in the constellation for each sample
[~, idx] = min(abs(sampled_symbols' - levels), [], 2);
estimated_symbols_index = (idx - 1)';

%% 6. Performance Evaluation
num_errors = sum(symbols(1:length(estimated_symbols_index)) ~= estimated_symbols_index);
ser = num_errors / length(estimated_symbols_index);

fprintf('\n--- Detector Results ---\n');
fprintf('SNR Used: %d dB\n', snr);
fprintf('Total Symbol Errors: %d\n', num_errors);
fprintf('Symbol Error Rate (SER): **%.5f**\n', ser);

%% Visualization
figure;
subplot(2,1,1);
plot(sampled_symbols, 'o'); hold on;
yline(levels, 'r--');
title('Sampled Symbol Values vs. Ideal Levels');
grid on;

subplot(2,1,2);
scatter(sampled_symbols, zeros(size(sampled_symbols)), 'bx'); hold on;
scatter(levels, zeros(size(levels)), 'ro', 'filled');
title('Constellation Mapping');
legend('Received', 'Ideal');
grid on;



%%%%
Vd = 1;
M = 4;
levels = (-Vd/2-(M/2-1)*Vd):Vd:(Vd/2+(M/2-1)*Vd);
thresholds = [levels(1)+Vd/2, levels(2)+Vd/2, levels(3)+Vd/2]; % [-1.0, 0.0, 1.0]



initial_offset = round(sps/2); 
if initial_offset == 0
    initial_offset = 1;
end

sampled_symbols = mf_output(initial_offset : sps : end);

Ns_received = min(Ns, length(sampled_symbols));
sampled_symbols = sampled_symbols(1:Ns_received);



[~, estimated_symbols_index] = quantiz(sampled_symbols, thresholds, 0:(M-1));

estimated_symbols_levels = levels(estimated_symbols_index + 1);


original_symbols = symbols(1:Ns_received); % Transmitted symbols indices [0, 1, 2, 3]

num_errors = sum(original_symbols ~= estimated_symbols_index);

ser = num_errors / Ns_received;

fprintf('\n--- Detector (MARGE) Results ---\n');
fprintf('Original Symbols (Ns): %d\n', Ns);
fprintf('Received Symbols (Ns\_received): %d\n', Ns_received);
fprintf('Total Symbol Errors: %d\n', num_errors);
fprintf('Symbol Error Rate (SER): **%.5f**\n', ser);



figure;

subplot(2,1,1);
plot(sampled_symbols, 'o'); hold on;
yline(levels(1), 'r--'); yline(levels(2), 'r--');
yline(levels(3), 'r--'); yline(levels(4), 'r--');
title('Sampled Symbol Values Over Time');
xlabel('Symbol Index'); ylabel('Amplitude'); grid on;

subplot(2,1,2);
scatter(sampled_symbols, zeros(size(sampled_symbols)), 'bx'); hold on;
scatter(levels, zeros(size(levels)), 'ro', 'filled');
for th = thresholds
    xline(th, 'k--');
end
title('Received Samples and Decision Thresholds');
xlabel('Sampled Matched Filter Output');
legend('Received Samples', 'Constellation Points', 'Decision Thresholds');
grid on;
