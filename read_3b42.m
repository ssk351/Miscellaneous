A sample program in Matlab
% This program is to read a TRMM 3B42 daily binary file

fid = fopen('3B42_daily.2009.05.31.7.bin', 'r');
a = fread(fid, 'float','b');
fclose(fid)

data = a';

count = 1;
for i_lat = 1:400
    for j_lon = 1:1440
        lat = -49.875 + 0.25*(i_lat - 1)
        if j_lon <= 720
        lon = 0.125 + 0.25*(j_lon - 1)
  else
  lon = 0.125 + 0.25*(j_lon - 1) - 360.0
  end
        daily_rain_total = data(count)
        count = count + 1;
    end
end

