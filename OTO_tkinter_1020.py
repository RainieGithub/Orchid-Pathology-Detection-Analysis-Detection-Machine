import time
import csv
#import tk
import Tkinter as tk
import ttk
import tkMessageBox
import numpy as np
import matplotlib.backends.backend_tkagg
from numpy import arange, sin, pi
import matplotlib.pyplot as plt
#from PIL import Image
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.widgets import Button
import urllib
import glob
import os
import ntplib
import struct
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def wavelengthWindows():
    def scan():
        os.system("./dsm.sh")
        print(os.system)
        response=os.system('ping -c 1 www.google.com')
        
        with open('Lambda.txt', "r") as f:
            Lambda = np.loadtxt(f,delimiter=",")
           
        with open('Intensity.txt', "r") as k:
            Intensity = np.loadtxt(k,delimiter=",")
        
            Lambda_temp = Lambda
            Intensity_for_web = Intensity
            print(Lambda_temp)
            print(Intensity_for_web)
            
            x = len(Lambda_temp)
            y = len(Intensity_for_web)
            print(x)
            print(y)
            
            if x < 2 and y < 2:
                if response==0:
                    plot1.clear()
                    plot1.set_title('spectrum', fontsize=32)
                    plot1.set_xlabel('nm',size='20')
                    plot1.set_ylabel('Intensity',fontsize=32)
                    plot1.set_title('Wifi V\nDevice X',loc='right',color='R',fontsize=20)
                    plot1.plot(Lambda_temp,Intensity_for_web)
                    canvas.show()
                    tkMessageBox.showinfo('message', 'scan successfully')
                else:
                    plot1.set_title('spectrum', fontsize=32)
                    plot1.set_xlabel('nm',size='20')
                    plot1.set_ylabel('Intensity',fontsize=32)
                    plot1.set_title('Wifi X\nDevice X',loc='right',color='R',fontsize=20)
                    plot1.plot(Lambda_temp,Intensity_for_web)
                    canvas.show()
                    tkMessageBox.showinfo('message', 'scan successfully')  
            else:
                if response==0:
                    plot1.clear()
                    plot1.set_title('spectrum', fontsize=32)
                    plot1.set_xlabel('nm',size='20')
                    plot1.set_ylabel('Intensity',fontsize=32)
                    plot1.set_title('Wifi V\nDevice V',loc='right',color='G',fontsize=20)
                    plot1.plot(Lambda_temp,Intensity_for_web)
                    canvas.show()
                    tkMessageBox.showinfo('message', 'scan successfully')
                else:
                    plot1.clear()
                    plot1.set_title('spectrum', fontsize=32)
                    plot1.set_xlabel('nm',size='20')
                    plot1.set_ylabel('Intensity',fontsize=32)
                    plot1.set_title('Wifi X\nDevice V',loc='right',color='R',fontsize=20)
                    plot1.plot(Lambda_temp,Intensity_for_web)
                    canvas.show()
                    tkMessageBox.showinfo('message', 'scan successfully')
    def save():
        os.system("./mountUsb.sh")
        tkMessageBox.showinfo('message', os.system)
        
        print(os.system)

        file_dir = '/media/orangepi/usb/'
        filepath_name = ('/media/orangepi/usb/'+output_name)
        csv_read_list = glob.glob(file_dir + output_name)
        csv_read_num = len(csv_read_list)
        print(csv_read_num)
        
        f = open('j_number.txt')
        number_j = f.read()
        str_to_int_j=int(number_j)
                
        j=str_to_int_j
        
        data = ("data_"+number_j)
        
        with open('Lambda.txt', "r") as f:
            Lambda = f.read()
           
        with open('Intensity.txt', "r") as k:
            Intensity = k.read()
        
            Lambda_temp = Lambda
            Intensity_for_web = Intensity

            print(Lambda_temp)
            print(Intensity_for_web)
            
            if csv_read_num > 0:
                if j==1:
                    file = open(filepath_name, mode='a')
                    with open(filepath_name, "a") as f:
                        Intensity_for_web_data = [[data,Intensity_for_web]]
                        np.savetxt(f, Intensity_for_web_data, delimiter =",",fmt ='% s')
                        print("Already have output.csv at Desktop, so add the data.")
                        tkMessageBox.showinfo('message', 'save successfully1')
                else:    
                    file = open(filepath_name, mode='a')
                    with open(filepath_name, "a") as f:
                        Intensity_for_web_data = [[data,Intensity_for_web]]
                        np.savetxt(f, Intensity_for_web_data, delimiter =",",fmt ='% s')
                        print("Already have output.csv at Desktop, so add the data.")
                        tkMessageBox.showinfo('message', 'save successfully2')
            else:
                with open(filepath_name, "a") as f:
                    Intensity_for_web_data = [[data,Intensity_for_web]]
                    np.savetxt(f, Intensity_for_web_data, delimiter =",",fmt ='% s')
                    print("Don't have any output.csv, so create a .csv. And add the data to ooutpu.csv")
                    time.sleep(1)
                    tkMessageBox.showinfo('message', 'save successfully3')
        new_j=int(j)
        new_j+=1
        f = open("j_number.txt", "w")
        int_to_str_j=str(new_j)
        f.write(int_to_str_j)
        f.close()

        
        os.system("./umountUsb.sh")
        tkMessageBox.showinfo('message', os.system)


    def umountusb():
        os.system("./mountUsb.sh")
        tkMessageBox.showinfo('message', os.system)

        f = open('i_number.txt')
        number_i = f.read()
        str_to_int_i=int(number_i)
            
        q=str_to_int_i
    
        new_i=int(q)
        new_i+=1
        f = open("i_number.txt", "w")
        int_to_str_i=str(new_i)
        f.write(int_to_str_i)
        print("Next is",int_to_str_i,"execute code")    
        f.close()
        
        k=1
        f = open("j_number.txt", "w")
        int_to_str_j=str(k)
        f.write(int_to_str_j)
        f.close()

        os.system("./umountUsb.sh")
        tkMessageBox.showinfo('message', os.system)
        
        wavelength_window.destroy()
        Setting()
    
    
        
    def upload(): 
        c = ntplib.NTPClient()
        response = c.request('clock.stdtime.gov.tw', port='ntp',version =1, timeout=5)
        ts = response.tx_time
        time.stamp = int(time.mktime(time.localtime(ts)))
        new_stamp= time.stamp + 28800
        print(new_stamp)
        new_struct_time = time.localtime(new_stamp)
        timeString = time.strftime("%Y/%m/%d %H:%M:%S", new_struct_time)
        print(timeString)
        k = ('time,'+timeString)

        os.system("./mountUsb.sh")
        print(os.system)
        
        file_dir = '/media/orangepi/usb/'
        filepath_name = ('/media/orangepi/usb/'+output_name)
        with open(filepath_name, "a") as f:
            url = ('https://script.google.com/macros/s/AKfycbwa_ebPhErEbg7zfA9zlgJDXXim3Q315m8GJmP_NgB66CvTujv04jin1YKttXtTrfwMEA/exec?data=')
            urllib.urlretrieve(url+str(k))
            Inform = [[k]]
            np.savetxt(f, Inform, delimiter =",",fmt ='% s')
        
        #https://script.google.com/macros/s/AKfycbwa_ebPhErEbg7zfA9zlgJDXXim3Q315m8GJmP_NgB66CvTujv04jin1YKttXtTrfwMEA/exec?data=
        filepath_name = ('/media/orangepi/usb/'+output_name)      
        with open(filepath_name, "r") as f:     
            data = f.read()
            all_data = data.splitlines()
            tkMessageBox.showinfo('message', 'upload all data?')
            progressbarOne['maximum']=len(all_data)-1
            progressbarOne['value']=0
            i=1
            for i in range(len(all_data)-1):
                print(all_data[i])
                url = 'https://script.google.com/macros/s/AKfycbwa_ebPhErEbg7zfA9zlgJDXXim3Q315m8GJmP_NgB66CvTujv04jin1YKttXtTrfwMEA/exec?data='
                urllib.urlretrieve(url+all_data[i])
                progressbarOne['value']+=1
                wavelength_window.update()
            print("upload successfully")
            wavelength_window.update()

            time.sleep(1)
            
            os.system("./umountUsb.sh")    
            print(os.system)
            
            tkMessageBox.showinfo('message', 'upload successfully')

        f = open('i_number.txt')
        number_i = f.read()
        str_to_int_i=int(number_i)
            
        q=str_to_int_i
    
        new_i=int(q)
        new_i+=1
        f = open("i_number.txt", "w")
        int_to_str_i=str(new_i)
        f.write(int_to_str_i)
        print("Next is",int_to_str_i,"execute code")    
        f.close()
        
        k=1
        f = open("j_number.txt", "w")
        int_to_str_j=str(k)
        f.write(int_to_str_j)
        f.close()        
        wavelength_window.destroy()
        Setting()

    wavelength_window = tk.Tk()
    wavelength_window.title('wavelenthWindow')
    wavelength_window.attributes('-fullscreen', True)
    response=os.system('ping -c 1 www.google.com')
    f = open('i_number.txt')
    number_i = f.read()
    str_to_int_i=int(number_i)
                
    i=str_to_int_i
            
    new_output_name="output_"+str(i).zfill(3)
    output_name = new_output_name+".csv"
    
    scan_button = tk.Button(master = wavelength_window, command = scan, height = 2, width = 10, text = "scan")
    scan_button.grid(row=5, column=1)
    scan_button.config(font=("Comic Sans MS",32))
    scan_button.place(x = 10, y = 620, width=400, height=70)
    
    save_button = tk.Button(master = wavelength_window, command = save, height = 2, width = 10, text = "save")
    save_button.grid(row=5, column=1)
    save_button.config(font=("Comic Sans MS",32))
    save_button.place(x = 430, y = 620, width=400, height=55)
 
    MountSDcard = tk.Button(master = wavelength_window, command = umountusb, height = 2, width = 10, text = "UmountSDcard")
    MountSDcard.grid(row=5, column=1)
    MountSDcard.config(font=("Comic Sans MS",28))
    MountSDcard.place(x = 430, y = 680, width=400, height=40)

    upload_button = tk.Button(master = wavelength_window, command = upload, height = 2, width = 10, text = "upload")
    upload_button.grid(row=5, column=1)
    upload_button.config(font=("Comic Sans MS",32))
    upload_button.place(x = 850, y = 620, width=400, height=55)

    progressbarOne = ttk.Progressbar(wavelength_window)
    progressbarOne.place(x = 850, y = 680, width=400, height=35)

    if response==0:
        fig = Figure(figsize = (15,6), dpi = 100)
        plot1 = fig.add_subplot(111)
        plot1.set_title('spectrum', fontsize=28)
        plot1.set_xlabel('nm',size='20')
        plot1.set_ylabel('Intensity',fontsize=28)
        plot1.set_title('Wifi V\nDevice V',loc='right',color='G',fontsize=20)
        canvas = FigureCanvasTkAgg(fig, master = wavelength_window)
        canvas.get_tk_widget().pack()
    else:
        fig = Figure(figsize = (15,6), dpi = 100)
        plot1 = fig.add_subplot(111)
        plot1.set_title('spectrum', fontsize=28)
        plot1.set_xlabel('nm',size='20')
        plot1.set_ylabel('Intensity',fontsize=28)
        plot1.set_title('Wifi X\nDevice V',loc='right',color='G',fontsize=20)
        canvas = FigureCanvasTkAgg(fig, master = wavelength_window)
        canvas.get_tk_widget().pack()        
    
    wavelength_window.mainloop()

def Setting():
    def judge_event():
        #print(var.get())
        if fileInput.get() == "" or conditionInput.get() == "" :
            if fileInput.get() == "" and conditionInput.get() == "":
                tkMessageBox.showwarning('message', 'Please enter filename and condition.')
            elif fileInput.get() == "":
                tkMessageBox.showerror('message', 'Please enter filename.')
            else:
                tkMessageBox.showerror('message', 'Please enter condition.')
        else:
            print(fileInput.get())
            print(conditionInput.get())
            
            os.system("./mountUsb.sh")
            
            filepath_name = ('/media/orangepi/usb/'+output_name)
            file = open(filepath_name, mode='a')
            file_dir = '/media/orangepi/usb/'
            filepath_name = ('/media/orangepi/usb/'+output_name)

            csv_read_list = glob.glob(file_dir + output_name)
            csv_read_num = len(csv_read_list)
            print(csv_read_num)
            
            with open(filepath_name, "a") as f:
                Inform = [['filename', fileInput.get()],
                          ['condition', conditionInput.get()]]
                np.savetxt(f, Inform, delimiter =",",fmt ='% s')
            
            if csv_read_num > 0:
                file = open(filepath_name, mode='a')
                with open(filepath_name, "a") as f:
                    listdata = [['spectrum',199.63,200.16,200.7,201.23,201.77,202.3,202.84,203.37,203.91,204.44,204.98,205.51,206.05,206.58,207.12,207.66,208.19,208.73,209.27,209.8,210.34,210.88,211.42,211.95,212.49,213.03,213.57,214.11,214.65,215.18,215.72,216.26,216.8,217.34,217.88,218.42,218.96,219.5,220.04,220.58,221.13,221.67,222.21,222.75,223.29,223.83,224.38,224.92,225.46,226.0,226.55,227.09,227.63,228.18,228.72,229.26,229.81,230.35,230.9,231.44,231.98,232.53,233.07,233.62,234.17,234.71,235.26,235.8,236.35,236.9,237.44,237.99,238.54,239.08,239.63,240.18,240.73,241.27,241.82,242.37,242.92,243.47,244.02,244.57,245.11,245.66,246.21,246.76,247.31,247.86,248.41,248.96,249.51,250.07,250.62,251.17,251.72,252.27,252.82,253.38,253.93,254.48,255.03,255.59,256.14,256.69,257.24,257.8,258.35,258.91,259.46,260.01,260.57,261.12,261.68,262.23,262.79,263.34,263.9,264.46,265.01,265.57,266.12,266.68,267.24,267.79,268.35,268.91,269.47,270.02,270.58,271.14,271.7,272.26,272.81,273.37,273.93,274.49,275.05,275.61,276.17,276.73,277.29,277.85,278.41,278.97,279.53,280.09,280.66,281.22,281.78,282.34,282.9,283.46,284.03,284.59,285.15,285.71,286.28,286.84,287.4,287.97,288.53,289.1,289.66,290.23,290.79,291.35,291.92,292.48,293.05,293.62,294.18,294.75,295.31,295.88,296.45,297.01,297.58,298.15,298.71,299.28,299.85,300.42,300.99,301.55,302.12,302.69,303.26,303.83,304.4,304.97,305.54,306.11,306.68,307.25,307.82,308.39,308.96,309.53,310.1,310.67,311.24,311.81,312.38,312.96,313.53,314.1,314.67,315.25,315.82,316.39,316.96,317.54,318.11,318.69,319.26,319.83,320.41,320.98,321.56,322.13,322.71,323.28,323.86,324.43,325.01,325.58,326.16,326.74,327.31,327.89,328.47,329.04,329.62,330.2,330.78,331.35,331.93,332.51,333.09,333.67,334.25,334.83,335.4,335.98,336.56,337.14,337.72,338.3,338.88,339.46,340.04,340.62,341.21,341.79,342.37,342.95,343.53,344.11,344.69,345.28,345.86,346.44,347.02,347.61,348.19,348.77,349.36,349.94,350.52,351.11,351.69,352.28,352.86,353.45,354.03,354.62,355.2,355.79,356.37,356.96,357.54,358.13,358.72,359.3,359.89,360.48,361.06,361.65,362.24,362.83,363.41,364.0,364.59,365.18,365.77,366.36,366.94,367.53,368.12,368.71,369.3,369.89,370.48,371.07,371.66,372.25,372.84,373.43,374.02,374.62,375.21,375.8,376.39,376.98,377.57,378.17,378.76,379.35,379.94,380.54,381.13,381.72,382.32,382.91,383.5,384.1,384.69,385.29,385.88,386.48,387.07,387.67,388.26,388.86,389.45,390.05,390.64,391.24,391.84,392.43,393.03,393.63,394.22,394.82,395.42,396.01,396.61,397.21,397.81,398.41,399.0,399.6,400.2,400.8,401.4,402.0,402.6,403.2,403.8,404.4,405.0,405.6,406.2,406.8,407.4,408.0,408.6,409.2,409.8,410.41,411.01,411.61,412.21,412.81,413.42,414.02,414.62,415.22,415.83,416.43,417.03,417.64,418.24,418.85,419.45,420.05,420.66,421.26,421.87,422.47,423.08,423.68,424.29,424.89,425.5,426.11,426.71,427.32,427.93,428.53,429.14,429.75,430.35,430.96,431.57,432.17,432.78,433.39,434.0,434.61,435.22,435.82,436.43,437.04,437.65,438.26,438.87,439.48,440.09,440.7,441.31,441.92,442.53,443.14,443.75,444.36,444.97,445.58,446.2,446.81,447.42,448.03,448.64,449.26,449.87,450.48,451.09,451.71,452.32,452.93,453.54,454.16,454.77,455.39,456.0,456.61,457.23,457.84,458.46,459.07,459.69,460.3,460.92,461.53,462.15,462.76,463.38,464.0,464.61,465.23,465.85,466.46,467.08,467.7,468.31,468.93,469.55,470.17,470.78,471.4,472.02,472.64,473.26,473.87,474.49,475.11,475.73,476.35,476.97,477.59,478.21,478.83,479.45,480.07,480.69,481.31,481.93,482.55,483.17,483.79,484.41,485.03,485.66,486.28,486.9,487.52,488.14,488.77,489.39,490.01,490.63,491.26,491.88,492.5,493.13,493.75,494.37,495.0,495.62,496.24,496.87,497.49,498.12,498.74,499.37,499.99,500.62,501.24,501.87,502.49,503.12,503.74,504.37,505.0,505.62,506.25,506.88,507.5,508.13,508.76,509.38,510.01,510.64,511.27,511.89,512.52,513.15,513.78,514.41,515.04,515.66,516.29,516.92,517.55,518.18,518.81,519.44,520.07,520.7,521.33,521.96,522.59,523.22,523.85,524.48,525.11,525.74,526.37,527.01,527.64,528.27,528.9,529.53,530.16,530.8,531.43,532.06,532.69,533.33,533.96,534.59,535.22,535.86,536.49,537.12,537.76,538.39,539.03,539.66,540.29,540.93,541.56,542.2,542.83,543.47,544.1,544.74,545.37,546.01,546.64,547.28,547.92,548.55,549.19,549.83,550.46,551.1,551.73,552.37,553.01,553.65,554.28,554.92,555.56,556.2,556.83,557.47,558.11,558.75,559.39,560.03,560.66,561.3,561.94,562.58,563.22,563.86,564.5,565.14,565.78,566.42,567.06,567.7,568.34,568.98,569.62,570.26,570.9,571.54,572.18,572.82,573.47,574.11,574.75,575.39,576.03,576.67,577.32,577.96,578.6,579.24,579.89,580.53,581.17,581.81,582.46,583.1,583.74,584.39,585.03,585.68,586.32,586.96,587.61,588.25,588.9,589.54,590.19,590.83,591.48,592.12,592.77,593.41,594.06,594.7,595.35,595.99,596.64,597.29,597.93,598.58,599.23,599.87,600.52,601.17,601.81,602.46,603.11,603.76,604.4,605.05,605.7,606.35,606.99,607.64,608.29,608.94,609.59,610.24,610.88,611.53,612.18,612.83,613.48,614.13,614.78,615.43,616.08,616.73,617.38,618.03,618.68,619.33,619.98,620.63,621.28,621.93,622.58,623.24,623.89,624.54,625.19,625.84,626.49,627.15,627.8,628.45,629.1,629.75,630.41,631.06,631.71,632.36,633.02,633.67,634.32,634.98,635.63,636.28,636.94,637.59,638.25,638.9,639.55,640.21,640.86,641.52,642.17,642.83,643.48,644.14,644.79,645.45,646.1,646.76,647.41,648.07,648.72,649.38,650.04,650.69,651.35,652.01,652.66,653.32,653.98,654.63,655.29,655.95,656.6,657.26,657.92,658.58,659.23,659.89,660.55,661.21,661.87,662.52,663.18,663.84,664.5,665.16,665.82,666.48,667.13,667.79,668.45,669.11,669.77,670.43,671.09,671.75,672.41,673.07,673.73,674.39,675.05,675.71,676.37,677.03,677.7,678.36,679.02,679.68,680.34,681.0,681.66,682.33,682.99,683.65,684.31,684.97,685.64,686.3,686.96,687.62,688.29,688.95,689.61,690.27,690.94,691.6,692.26,692.93,693.59,694.25,694.92,695.58,696.25,696.91,697.57,698.24,698.9,699.57,700.23,700.9,701.56,702.23,702.89,703.56,704.22,704.89,705.55,706.22,706.89,707.55,708.22,708.88,709.55,710.22,710.88,711.55,712.22,712.88,713.55,714.22,714.88,715.55,716.22,716.89,717.55,718.22,718.89,719.56,720.22,720.89,721.56,722.23,722.9,723.57,724.23,724.9,725.57,726.24,726.91,727.58,728.25,728.92,729.59,730.26,730.93,731.6,732.27,732.94,733.61,734.28,734.95,735.62,736.29,736.96,737.63,738.3,738.97,739.64,740.31,740.98,741.66,742.33,743.0,743.67,744.34,745.01,745.69,746.36,747.03,747.7,748.38,749.05,749.72,750.39,751.07,751.74,752.41,753.09,753.76,754.43,755.11,755.78,756.45,757.13,757.8,758.48,759.15,759.82,760.5,761.17,761.85,762.52,763.2,763.87,764.55,765.22,765.9,766.57,767.25,767.92,768.6,769.27,769.95,770.63,771.3,771.98,772.65,773.33,774.01,774.68,775.36,776.04,776.71,777.39,778.07,778.74,779.42,780.1,780.78,781.45,782.13,782.81,783.49,784.17,784.84,785.52,786.2,786.88,787.56,788.24,788.92,789.59,790.27,790.95,791.63,792.31,792.99,793.67,794.35,795.03,795.71,796.39,797.07,797.75,798.43,799.11,799.79,800.47,801.15,801.83,802.51,803.19,803.87,804.55,805.24,805.92,806.6,807.28,807.96,808.64,809.33,810.01,810.69,811.37,812.05,812.74,813.42,814.1,814.78,815.47,816.15]]
                    np.savetxt(f, listdata, delimiter =",",fmt ='% s')
            else:
                with open(filepath_name, "a") as f:
                    listdata = [['spectrum',199.63,200.16,200.7,201.23,201.77,202.3,202.84,203.37,203.91,204.44,204.98,205.51,206.05,206.58,207.12,207.66,208.19,208.73,209.27,209.8,210.34,210.88,211.42,211.95,212.49,213.03,213.57,214.11,214.65,215.18,215.72,216.26,216.8,217.34,217.88,218.42,218.96,219.5,220.04,220.58,221.13,221.67,222.21,222.75,223.29,223.83,224.38,224.92,225.46,226.0,226.55,227.09,227.63,228.18,228.72,229.26,229.81,230.35,230.9,231.44,231.98,232.53,233.07,233.62,234.17,234.71,235.26,235.8,236.35,236.9,237.44,237.99,238.54,239.08,239.63,240.18,240.73,241.27,241.82,242.37,242.92,243.47,244.02,244.57,245.11,245.66,246.21,246.76,247.31,247.86,248.41,248.96,249.51,250.07,250.62,251.17,251.72,252.27,252.82,253.38,253.93,254.48,255.03,255.59,256.14,256.69,257.24,257.8,258.35,258.91,259.46,260.01,260.57,261.12,261.68,262.23,262.79,263.34,263.9,264.46,265.01,265.57,266.12,266.68,267.24,267.79,268.35,268.91,269.47,270.02,270.58,271.14,271.7,272.26,272.81,273.37,273.93,274.49,275.05,275.61,276.17,276.73,277.29,277.85,278.41,278.97,279.53,280.09,280.66,281.22,281.78,282.34,282.9,283.46,284.03,284.59,285.15,285.71,286.28,286.84,287.4,287.97,288.53,289.1,289.66,290.23,290.79,291.35,291.92,292.48,293.05,293.62,294.18,294.75,295.31,295.88,296.45,297.01,297.58,298.15,298.71,299.28,299.85,300.42,300.99,301.55,302.12,302.69,303.26,303.83,304.4,304.97,305.54,306.11,306.68,307.25,307.82,308.39,308.96,309.53,310.1,310.67,311.24,311.81,312.38,312.96,313.53,314.1,314.67,315.25,315.82,316.39,316.96,317.54,318.11,318.69,319.26,319.83,320.41,320.98,321.56,322.13,322.71,323.28,323.86,324.43,325.01,325.58,326.16,326.74,327.31,327.89,328.47,329.04,329.62,330.2,330.78,331.35,331.93,332.51,333.09,333.67,334.25,334.83,335.4,335.98,336.56,337.14,337.72,338.3,338.88,339.46,340.04,340.62,341.21,341.79,342.37,342.95,343.53,344.11,344.69,345.28,345.86,346.44,347.02,347.61,348.19,348.77,349.36,349.94,350.52,351.11,351.69,352.28,352.86,353.45,354.03,354.62,355.2,355.79,356.37,356.96,357.54,358.13,358.72,359.3,359.89,360.48,361.06,361.65,362.24,362.83,363.41,364.0,364.59,365.18,365.77,366.36,366.94,367.53,368.12,368.71,369.3,369.89,370.48,371.07,371.66,372.25,372.84,373.43,374.02,374.62,375.21,375.8,376.39,376.98,377.57,378.17,378.76,379.35,379.94,380.54,381.13,381.72,382.32,382.91,383.5,384.1,384.69,385.29,385.88,386.48,387.07,387.67,388.26,388.86,389.45,390.05,390.64,391.24,391.84,392.43,393.03,393.63,394.22,394.82,395.42,396.01,396.61,397.21,397.81,398.41,399.0,399.6,400.2,400.8,401.4,402.0,402.6,403.2,403.8,404.4,405.0,405.6,406.2,406.8,407.4,408.0,408.6,409.2,409.8,410.41,411.01,411.61,412.21,412.81,413.42,414.02,414.62,415.22,415.83,416.43,417.03,417.64,418.24,418.85,419.45,420.05,420.66,421.26,421.87,422.47,423.08,423.68,424.29,424.89,425.5,426.11,426.71,427.32,427.93,428.53,429.14,429.75,430.35,430.96,431.57,432.17,432.78,433.39,434.0,434.61,435.22,435.82,436.43,437.04,437.65,438.26,438.87,439.48,440.09,440.7,441.31,441.92,442.53,443.14,443.75,444.36,444.97,445.58,446.2,446.81,447.42,448.03,448.64,449.26,449.87,450.48,451.09,451.71,452.32,452.93,453.54,454.16,454.77,455.39,456.0,456.61,457.23,457.84,458.46,459.07,459.69,460.3,460.92,461.53,462.15,462.76,463.38,464.0,464.61,465.23,465.85,466.46,467.08,467.7,468.31,468.93,469.55,470.17,470.78,471.4,472.02,472.64,473.26,473.87,474.49,475.11,475.73,476.35,476.97,477.59,478.21,478.83,479.45,480.07,480.69,481.31,481.93,482.55,483.17,483.79,484.41,485.03,485.66,486.28,486.9,487.52,488.14,488.77,489.39,490.01,490.63,491.26,491.88,492.5,493.13,493.75,494.37,495.0,495.62,496.24,496.87,497.49,498.12,498.74,499.37,499.99,500.62,501.24,501.87,502.49,503.12,503.74,504.37,505.0,505.62,506.25,506.88,507.5,508.13,508.76,509.38,510.01,510.64,511.27,511.89,512.52,513.15,513.78,514.41,515.04,515.66,516.29,516.92,517.55,518.18,518.81,519.44,520.07,520.7,521.33,521.96,522.59,523.22,523.85,524.48,525.11,525.74,526.37,527.01,527.64,528.27,528.9,529.53,530.16,530.8,531.43,532.06,532.69,533.33,533.96,534.59,535.22,535.86,536.49,537.12,537.76,538.39,539.03,539.66,540.29,540.93,541.56,542.2,542.83,543.47,544.1,544.74,545.37,546.01,546.64,547.28,547.92,548.55,549.19,549.83,550.46,551.1,551.73,552.37,553.01,553.65,554.28,554.92,555.56,556.2,556.83,557.47,558.11,558.75,559.39,560.03,560.66,561.3,561.94,562.58,563.22,563.86,564.5,565.14,565.78,566.42,567.06,567.7,568.34,568.98,569.62,570.26,570.9,571.54,572.18,572.82,573.47,574.11,574.75,575.39,576.03,576.67,577.32,577.96,578.6,579.24,579.89,580.53,581.17,581.81,582.46,583.1,583.74,584.39,585.03,585.68,586.32,586.96,587.61,588.25,588.9,589.54,590.19,590.83,591.48,592.12,592.77,593.41,594.06,594.7,595.35,595.99,596.64,597.29,597.93,598.58,599.23,599.87,600.52,601.17,601.81,602.46,603.11,603.76,604.4,605.05,605.7,606.35,606.99,607.64,608.29,608.94,609.59,610.24,610.88,611.53,612.18,612.83,613.48,614.13,614.78,615.43,616.08,616.73,617.38,618.03,618.68,619.33,619.98,620.63,621.28,621.93,622.58,623.24,623.89,624.54,625.19,625.84,626.49,627.15,627.8,628.45,629.1,629.75,630.41,631.06,631.71,632.36,633.02,633.67,634.32,634.98,635.63,636.28,636.94,637.59,638.25,638.9,639.55,640.21,640.86,641.52,642.17,642.83,643.48,644.14,644.79,645.45,646.1,646.76,647.41,648.07,648.72,649.38,650.04,650.69,651.35,652.01,652.66,653.32,653.98,654.63,655.29,655.95,656.6,657.26,657.92,658.58,659.23,659.89,660.55,661.21,661.87,662.52,663.18,663.84,664.5,665.16,665.82,666.48,667.13,667.79,668.45,669.11,669.77,670.43,671.09,671.75,672.41,673.07,673.73,674.39,675.05,675.71,676.37,677.03,677.7,678.36,679.02,679.68,680.34,681.0,681.66,682.33,682.99,683.65,684.31,684.97,685.64,686.3,686.96,687.62,688.29,688.95,689.61,690.27,690.94,691.6,692.26,692.93,693.59,694.25,694.92,695.58,696.25,696.91,697.57,698.24,698.9,699.57,700.23,700.9,701.56,702.23,702.89,703.56,704.22,704.89,705.55,706.22,706.89,707.55,708.22,708.88,709.55,710.22,710.88,711.55,712.22,712.88,713.55,714.22,714.88,715.55,716.22,716.89,717.55,718.22,718.89,719.56,720.22,720.89,721.56,722.23,722.9,723.57,724.23,724.9,725.57,726.24,726.91,727.58,728.25,728.92,729.59,730.26,730.93,731.6,732.27,732.94,733.61,734.28,734.95,735.62,736.29,736.96,737.63,738.3,738.97,739.64,740.31,740.98,741.66,742.33,743.0,743.67,744.34,745.01,745.69,746.36,747.03,747.7,748.38,749.05,749.72,750.39,751.07,751.74,752.41,753.09,753.76,754.43,755.11,755.78,756.45,757.13,757.8,758.48,759.15,759.82,760.5,761.17,761.85,762.52,763.2,763.87,764.55,765.22,765.9,766.57,767.25,767.92,768.6,769.27,769.95,770.63,771.3,771.98,772.65,773.33,774.01,774.68,775.36,776.04,776.71,777.39,778.07,778.74,779.42,780.1,780.78,781.45,782.13,782.81,783.49,784.17,784.84,785.52,786.2,786.88,787.56,788.24,788.92,789.59,790.27,790.95,791.63,792.31,792.99,793.67,794.35,795.03,795.71,796.39,797.07,797.75,798.43,799.11,799.79,800.47,801.15,801.83,802.51,803.19,803.87,804.55,805.24,805.92,806.6,807.28,807.96,808.64,809.33,810.01,810.69,811.37,812.05,812.74,813.42,814.1,814.78,815.47,816.15]]  
                    np.savetxt(f, listdata, delimiter =",",fmt ='% s')

            time.sleep(1)        
            os.system("./umountUsb.sh")
            
            tkMessageBox.showinfo('message', 'successfully enter')
            tkMessageBox.showinfo('message', 'Data filename = '+ output_name)
            
            
            time.sleep(1)
            Input_windows.destroy()
            wavelengthWindows()
            
    def continue_Last():
        tkMessageBox.showinfo('message', 'close the subwindow')
        time.sleep(1)
        Input_windows.destroy()
        
        wavelengthWindows()

    def shutdown():
        os.system("./shutdown.sh")


        
    
    Input_windows = tk.Tk()
    Input_windows.title('Enter filename and condition')
    Input_windows.attributes('-fullscreen', True)
    
    f = open('i_number.txt')
    number_i = f.read()
    str_to_int_i=int(number_i)
            
    i=str_to_int_i
            
    new_output_name="output_"+str(i).zfill(3)
    output_name = new_output_name+".csv"
    sd_card = '/media/orangepi/usb/'
    
    space = tk.Label(Input_windows, text=' \n')
    space.grid(row=0, column=0)
    
    filename = tk.Label(Input_windows, text='Setting filename = ')
    filename.config(font=("Comic Sans MS",28))
    filename.grid(row=1, column=0)
    
    fileInput = tk.Entry(Input_windows)
    fileInput.grid(row=0, column=1)
    fileInput.config(font=("Comic Sans MS",28))
    fileInput.place(x = 440, y = 10, width=800, height=100)
    #fileInput.pack()
    
    spacet = tk.Label(Input_windows, text=' \n')
    spacet.grid(row=2, column=0)

    spacek = tk.Label(Input_windows, text=' \n')
    spacek.grid(row=3, column=0)

    spacea = tk.Label(Input_windows, text=' \n')
    spacea.grid(row=4, column=0)

    spaceg = tk.Label(Input_windows, text=' \n')
    spaceg.grid(row=5, column=0)
    
    conditionname = tk.Label(Input_windows, text='Setting test condition= ')
    conditionname.grid(row=6, column=0)
    conditionname.config(font=("Comic Sans MS",28))

    
    conditionInput = tk.Entry(Input_windows)
    conditionInput.grid(row=1, column=1)
    conditionInput.config(font=("Comic Sans MS",28))
    conditionInput.place(x = 440, y = 155, width=800, height=300)
    #conditionInput.pack()


    
    Enter_button = tk.Button(Input_windows, text='Enter', command=judge_event)
    Enter_button.grid(row=5, column=1)
    Enter_button.config(font=("Comic Sans MS",36))
    Enter_button.place(x = 800, y = 470, width=400, height=140)
    
    Continue_button = tk.Button(Input_windows, text='Continue Last', command=continue_Last)
    Continue_button.grid(row=5, column=1)
    Continue_button.config(font=("Comic Sans MS",36))
    Continue_button.place(x = 100, y = 470, width=400, height=70)
    Continue_button.focus()

    shutdown_button = tk.Button(Input_windows, text='Shutdown', command=shutdown)
    shutdown_button.grid(row=5, column=1)
    shutdown_button.config(font=("Comic Sans MS",36))
    shutdown_button.place(x = 100, y = 550, width=400, height=70)
    
    
    Input_windows.mainloop()
    
Setting()



















