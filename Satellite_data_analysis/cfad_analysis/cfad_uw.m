clear all
clc
binranges = 0.1:5:50.1;
Z=ncread('solapurb9_201306_2a25.nc','corr_Zfactor'); % change the file name here
%Z=Z/100; % scaling with the scale factor provided in hdf file
Z(Z<=0) = NaN; % removing all values of reflectivity less than 0
N(1:size(binranges,2),1:80) = 0;
N_p(1:size(binranges,2),1:80) = 0.0;
for i=1:80
   
    N_dummy = histc(reshape(Z(:,:,i,:),[],1),binranges);
    N(1:size(binranges,2),i) = N_dummy;
end
sum(1:80) = 0.0;
for i=1:size(binranges,2)
    for j=1:80
        if(N(i,j)~=NaN)
        sum(j) = sum(j) + N(i,j);
        end
    end   
end
for i=1:size(binranges,2)
    for j=1:80
        if(sum(j)~=0)
   N_p(i,j) = N(i,j)/sum(j)*100; 
        end
    end
end

contour(0.1:5:50.1,0.25:0.25:20,N_p')
%contour(0.25:0.25:20,[0,10,20,30,40,50],N)
colorbar
xlabel('Radar Reflectivity Factor Z, dBZ')
ylabel('Altitude, km')
title('TRMM PR for box 9 2013 JJAS')