
# **** First attempt a seistest file converter ****


# So far - seems OK!!!   - for reading from orig csv file.
#   This file staying "as is" as "read_seis_7.py" includes writes to "X" and "Y" files and modified header
#   Next work in "read_seis_7.py" - Will try to tidy up and list future suggestions.


# Specify name of file to read - remember file extention
#       .txt or .csv etc.

# For testing - use Seismograph131104034846.csv    or
#                   Seis_test_file.csv
#                   Seis_test_file2.csv

#        **********************************************************


# Initial setup, "File Names" to be used -  to Read and Write

# "Read" file name - Selection and Open
read_file_name = raw_input("Enter file name to open (with file extention) : ")
read_text_file = open(read_file_name, "r")

# "Write" file name - Selection
print "Write files will be split over 'X', 'Y' and 'Z'"
print "'X', 'Y' and 'Z' will be added automatically with file extention."
print " "

# "Write" files - Names Setup  -  (for "X", "Y" and "Z" axis)
write_file_name = raw_input("Enter Base filename to write WITHOUT file extention : ")
write_file_name_X = write_file_name +"_X.sg2"
write_file_name_Y = write_file_name +"_Y.sg2"
write_file_name_Z = write_file_name +"_Z.sg2"

# "Write" files - Open
write_text_file_X = open(write_file_name_X, "w")
write_text_file_Y = open(write_file_name_Y, "w")
write_text_file_Z = open(write_file_name_Z, "w")


# Basic variables setup
line_count = 0
mils_count = 0
sec_count = 0
start_time = 0
clock_time = 0
delta_time = 0
write_time = "0.00"
percent_done = 0



# Establish no of lines in file to read in total
lines = read_text_file.readlines()
                       


# *****  //   START LOOP SEQUENCE  \\   *****


# Reading in one line at a time.
for line in lines:

# Format and split "read-in" line    
    l = line
    n = '"'+ line
    n = n.replace('\n','"')
    o = n.replace(', ','","')
    p = eval(o)
    line_split = (p[0],p[1],p[2],p[3])


# Analyze out the date and time p[0]
    date_time = p[0]
    date = date_time[0:10]
    time = date_time[-12:]

# Date Calculations    
    year = date[0:4]
    month = date[5:7]
    day = date[8:10]
    if month == "01": jday = 0 + int(day)
    elif month == "02": jday = 31 + int(day) # Need to modify to allow
    elif month == "03": jday = 59 + int(day) # for Leap Year calculations.
    elif month == "04": jday = 90 + int(day)
    elif month == "05": jday = 120 + int(day)
    elif month == "06": jday = 151 + int(day)
    elif month == "07": jday = 181 + int(day)
    elif month == "08": jday = 212 + int(day)
    elif month == "09": jday = 243 + int(day)
    elif month == "10": jday = 273 + int(day)
    elif month == "11": jday = 304 + int(day)
    elif month == "12": jday = 334 + int(day)


# Time Calculations    
    if line_count >= 1:
        mils = int(time[-3:])
        secs = int(time[-6:-4])
        mins = int(time[-9:-7])
        hours = int(time[-12:-10])
        clock_time = (hours*360000) + (mins*60000) + (secs*1000) + mils
        if line_count == 1:
            start_time = clock_time 
        else:
            delta_time = clock_time - start_time
            if delta_time < 10:
                write_time = "0.00" + str(delta_time)
            elif delta_time < 100:
                write_time = "0.0" + str(delta_time)
            elif delta_time < 1000:
                write_time = "0." + str(delta_time)
            else:
                temp_write = str(delta_time)
                write_time = temp_write[:-3] + "." + temp_write[-3:]
            
        
        

    
#   Start work on writing data - for files "X", "Y" and "Z".


# Header Line (line 1)
    if line_count == 1:
        header_line_X = "SG2K_ASCII  event=? year=" + year + " " + "jday=" + str(jday) + " " + "hour=" + str(hours) + " " +  "min=" + str(mins) + " " + "sec=" + str(secs) + " " + "begTime=0.0000  network=ER sta=EMYR inst=? chan=BHX comp=BHX comp.az=0.0  comp.inc=0.0  sta.lat=Infinity  sta.lon=Infinity  sta.depth=Infinity  sta.elev=Infinity  nPoints=47098 sampleInt=0.009  ampUnits=counts timeUnits=sec hypo.lat=Infinity hypo.lon=Infinity hypo.depth=Infinity hypo.otime=9999,01,01,00,00,0.0 hypo.ms=-9.9 hypo.mb=-9.9 hypo.mw=-9.9 hypo.ml=-9.9 hypo.mo=-9.9 hypo.mag=-9.9 gcarc=0.0 dist=0.0 az=0.0 baz=0.0\n"
        write_text_file_X.write(header_line_X)
        header_line_Y = "SG2K_ASCII  event=? year=" + year + " " + "jday=" + str(jday) + " " + "hour=" + str(hours) + " " +  "min=" + str(mins) + " " + "sec=" + str(secs) + " " + "begTime=0.0000  network=ER sta=EMYR inst=? chan=BHY comp=BHY comp.az=0.0  comp.inc=0.0  sta.lat=Infinity  sta.lon=Infinity  sta.depth=Infinity  sta.elev=Infinity  nPoints=47098 sampleInt=0.009  ampUnits=counts timeUnits=sec hypo.lat=Infinity hypo.lon=Infinity hypo.depth=Infinity hypo.otime=9999,01,01,00,00,0.0 hypo.ms=-9.9 hypo.mb=-9.9 hypo.mw=-9.9 hypo.ml=-9.9 hypo.mo=-9.9 hypo.mag=-9.9 gcarc=0.0 dist=0.0 az=0.0 baz=0.0\n"
        write_text_file_Y.write(header_line_Y)
        header_line_Z = "SG2K_ASCII  event=? year=" + year + " " + "jday=" + str(jday) + " " + "hour=" + str(hours) + " " +  "min=" + str(mins) + " " + "sec=" + str(secs) + " " + "begTime=0.0000  network=ER sta=EMYR inst=? chan=BHZ comp=BHZ comp.az=0.0  comp.inc=0.0  sta.lat=Infinity  sta.lon=Infinity  sta.depth=Infinity  sta.elev=Infinity  nPoints=47098 sampleInt=0.009  ampUnits=counts timeUnits=sec hypo.lat=Infinity hypo.lon=Infinity hypo.depth=Infinity hypo.otime=9999,01,01,00,00,0.0 hypo.ms=-9.9 hypo.mb=-9.9 hypo.mw=-9.9 hypo.ml=-9.9 hypo.mo=-9.9 hypo.mag=-9.9 gcarc=0.0 dist=0.0 az=0.0 baz=0.0\n"
        write_text_file_Z.write(header_line_Z)


# Data Lines (line 2 onwards)
    if line_count > 1:
        line_to_write_X = write_time + " " + p[1] + "\n"
        write_text_file_X.write(line_to_write_X)
        line_to_write_Y = write_time + " " + p[2] + "\n"
        write_text_file_Y.write(line_to_write_Y)
        line_to_write_Z = write_time + " " + p[3] + "\n"
        write_text_file_Z.write(line_to_write_Z)


# Increase line count by 1            
    line_count +=1
    


# Print Output Calculations

    #percent_done = (float(len(lines)) / 100) * line_count    ***** NEED TO SORT  *****
    #percent_done = (line_count / 100) * len(lines)           ***** PERCENT CALCS ****

    #print "Lines Total : " + str(len(lines)) + "  " + "Done : " + str(line_count) + "   " + "Percent Done : %" + str(percent_done) + "  " + "Sample Time : " + str(write_time)
    print ("Lines  :   " + str(len(lines)) + "  " +
          "Done  :   " + str(line_count) + "   " +
          "Percentage : %" + str(percent_done) + "     " +
          "Milisecs  :  " + str(write_time))


    
# *****   //   END LOOP SEQUENCE   \\   *****
    
    
read_text_file.close()
write_text_file_X.close()
write_text_file_Y.close()
write_text_file_Z.close()

