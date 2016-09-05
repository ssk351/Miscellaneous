
;***************************************************************
; Add meta data
;***************************************************************
   prc@units       = "mm/hr"
   prc@long_name   = "TRMM_3B42RT: Hourly Rain Rate" 
   prc@scale_factor= prcScale
   prc@add_offset  = 0.0
   prc@missing_value  =  prc@_FillValue

   err@units       = "mm/hr"
   err@long_name   = "TRMM_3B42RT: Error Hourly Rain Rate" 
   err@scale_factor= prcScale
   err@add_offset  = 0.0
   err@_FillValue  =  prc@_FillValue
   err@missing_value  =  prc@_FillValue

   src@long_name   = "Data Source" 
   src@missing_value  =  src@_FillValue
   src@source      = "0=no observation, 1=AMSU, 2=TMI, 3=AMSR, 4=SSMI, "+\
                     "5=SSMIS, 6=MHS, 30=AMSU&MHS avg, 31=conical avg, "+\
                     "50=IR, 1,2,3,4,5,6+100=Sparce Sample"

;*****************************************************
; Create TRMM coordinate variables. See README
;*****************************************************
   lat        = 59.875 - ispan(0,nlat-1,1)*0.25 
   lon        = ispan(0,mlon-1,1)*0.25 

   lat@long_name = "latitude"
   lat@units  = "degrees_north"
   lat!0      = "lat"
   lat&lat    =  lat

   lon@long_name = "longitude"
   lon@units  = "degrees_east"
   lon!0      = "lon"
   lon&lon    =  lon

;***************************************************************
; Associate the spatial coordinates with variables
;***************************************************************
   prc!0      = "lat"                   ; 1st ... name the dimensions
   prc!1      = "lon"
   prc&lat    =  lat                    ; create coordinate variable
   prc&lon    =  lon                    

   err!0      = "lat"                  
   err!1      = "lon"
   err&lat    =  lat                  
   err&lon    =  lon                    

   src!0      = "lat"                
   src!1      = "lon"
   src&lat    =  lat                
   src&lon    =  lon                    

   printVarSummary(prc)
   printMinMax(prc, 0)
   printVarSummary(err)
   printMinMax(err, 0)
   printVarSummary(src)
   printMinMax(src, 0)

;************************************************
; Create netCDF 
; Recommend to always create a 'time' dimension 
;************************************************
       ntim     = 1
       ncFil    = fili_prefix +"."+ yyyymmddhh+".nc"

       tunits   = "hours since 1997-01-01 00:00:0.0"
       time     = cd_inv_calendar(yyyy,mm,dd,hh, 0,0d0,tunits, 0)
       time!0   = "time"

       date     = yyyymmddhh
       date!0   = "time"
       date@long_name = "Current date as YYYYMMDDHH"

       nline    = inttochar(10)         ; new line character
       
       globeAtt              = 1
       globeAtt@netCDF_creation_date= systemfunc ("date" )

       globeAtt@reference    = nline + \
        "George J. Huffman at al, 2007                                          "+nline+\
        "   The TRMM Multisatellite Precipitation Analysis (TMPA):              "+nline+\
        "   Quasi-Global, Multiyear, Combined-Sensor Precipitation Estimates at Fine Scales" +nline+\
        "   J. Hydrometeor, 8, 38â€“55 ,  doi: http://dx.doi.org/10.1175/JHM560.1" +nline+\
        "   "+nline

       do n=0,nfld-1
          s = str_split( hdrs_parse(n), "=" )
          globeAtt@$s(0)$ = s(1)
       end do
       globeAtt@title        = "TRMM_"+fili_prefix    
     
       NCFILE = ncDir + ncFil
       system ("/bin/rm -f " +  NCFILE)    ; remove any pre-exist file 
           
       ncdf   = addfile(NCFILE,"c")     
     
      ;setfileoption(ncdf, "definemode", True)
     
       fileattdef( ncdf, globeAtt )        ; create the global [file] attributes
                                         
       dimNames = (/"time", "lat", "lon" /)  
       dimSizes = (/ ntim ,  nlat,  mlon /) 
       dimUnlim = (/ True , False, False /)   
       filedimdef(ncdf, dimNames  , dimSizes,  dimUnlim )
     
       filevardef   (ncdf, "time"  , typeof(time), getvardims(time) )
       filevarattdef(ncdf, "time", time)
     
       filevardef   (ncdf, "lat", typeof(lat), getvardims(lat))
       filevarattdef(ncdf, "lat", lat)
          
       filevardef   (ncdf, "lon", typeof(lon), getvardims(lon))
       filevarattdef(ncdf, "lon", lon)
     
       filevardef   (ncdf, "date"  , typeof(date), getvardims(date) )
       filevarattdef(ncdf, "date", date)
     
       filevardef    (ncdf, "PRC"  , typeof(prc) , (/ "time", "lat", "lon" /) )
       filevarattdef (ncdf, "PRC"  , prc)

       filevardef(ncdf, "RELERR"   , typeof(err), (/ "time", "lat", "lon" /) )
       filevarattdef(ncdf, "RELERR", err)
     
       filevardef    (ncdf, "SRC"  , typeof(src) , (/ "time", "lat", "lon" /) )
       filevarattdef (ncdf, "SRC"  , src)
     
       ncdf->time   = (/ time /)
       ncdf->lat    = (/ lat /)
       ncdf->lon    = (/ lon /)
       ncdf->date   = (/ date /)
       ncdf->PRC(0:0,:,:) = (/ prc  /)
       ncdf->RELERR(0:0,:,:) = (/ err  /)
       ncdf->SRC(0:0,:,:) = (/ src  /)

 end do      ; nf
