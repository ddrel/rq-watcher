from netCDF4 import Dataset
import sys
from os import path
import os
from environs import Env

class extractcsv:
    env = Env()
    env.read_env()
    file_path=""
    file_name=""
    latlonlist=""
    isleapyear=False


    def __init__(self, file_path,latlonlist="global_station_path",isleapyear=False): 
        self.file_path = file_path
        self.file_name = path.splitext(path.basename(file_path))[0]
        self.latlonlist=latlonlist
        self.isleapyear = isleapyear

    def getFileName(self):
        return self.file_name

    def process(self):
        nc_File = Dataset(self.file_path, "r")

        print("nc_File :{}".format(self.file_path))

        basepath = path.dirname(__file__)
        src_path = path.join(basepath, self.env.str(self.latlonlist))

        print("src_path :{}".format(src_path))

        file_Data = open(src_path,'r')
        line_Data = file_Data.readlines()
        file_Data.close()

        output_csv_file = path.join(self.env.str("folder_output_csv"),self.file_name + ".csv")

        print("Output:{}".format(output_csv_file))
        file_Output = open(output_csv_file, 'w')
        file_Output.write(",USAF,WBAN,STATION.NAME,CTRY,ST,CALL,station_lat,station_lon,ELEV.M.,BEGIN,END,CLIMATE.REGION,era5_lat,era5_lon,dist,Latitude,Longitude,Time,precip,tavg,tmin,tmax,tskin_avg,tskin_min,tskin_max,tsoil1,tsoil2,tsoil3,tsoil4,mslp,leaf_lo,leaf_hi\n")
        
        counter = 367 if self.isleapyear else 366

        for int_Counter in range(0,7490):
            for int_TimeCounter in range(1,counter):
                file_Output.write(line_Data[int_Counter + 1].rstrip("\n") + "," )
                file_Output.write(str(nc_File.variables['latitude'][int_Counter]) + ",")
                file_Output.write(str(nc_File.variables['longitude'][int_Counter]) + ",")
                file_Output.write(str(nc_File.variables['time'][int_TimeCounter]) + ",")
                file_Output.write(str(nc_File.variables['precip'][int_TimeCounter][int_Counter]) + ",")
                file_Output.write(str(nc_File.variables['tavg'][int_TimeCounter][int_Counter]) + ",")
                file_Output.write(str(nc_File.variables['tmin'][int_TimeCounter][int_Counter]) + ",")
                file_Output.write(str(nc_File.variables['tmax'][int_TimeCounter][int_Counter]) + ",")
                file_Output.write(str(nc_File.variables['tskin_avg'][int_TimeCounter][int_Counter]) + ",")
                file_Output.write(str(nc_File.variables['tskin_min'][int_TimeCounter][int_Counter]) + ",")
                file_Output.write(str(nc_File.variables['tskin_max'][int_TimeCounter][int_Counter]) + ",")
                file_Output.write(str(nc_File.variables['tsoil1'][int_TimeCounter][int_Counter]) + ",")
                file_Output.write(str(nc_File.variables['tsoil2'][int_TimeCounter][int_Counter]) + ",")
                file_Output.write(str(nc_File.variables['tsoil3'][int_TimeCounter][int_Counter]) + ",")
                file_Output.write(str(nc_File.variables['tsoil4'][int_TimeCounter][int_Counter]) + ",")
                file_Output.write(str(nc_File.variables['mslp'][int_TimeCounter][int_Counter]) + ",")
                file_Output.write(str(nc_File.variables['leaf_lo'][int_TimeCounter][int_Counter]) + ",")
                file_Output.write(str(nc_File.variables['leaf_hi'][int_TimeCounter][int_Counter]) + "\n")

        return "success"