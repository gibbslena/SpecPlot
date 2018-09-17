from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib.font_manager import FontProperties
from tkinter import *
import click
from tkinter import ttk
plt.close("all")
from tkinter import messagebox
from tkinter import Widget
import tkinter
###MAKE SURE THE BACKGROUND UNDER PREFERENCES IS SET TO TKinter!!! Then you must restart spyder.###
###The interactive graphics will not work if this is not done.###

###Please enter the path to your spectera data files.###
Path = '//volumes/ricedata/Lena/CRB_Goniometer_Spectra/Individual_Rocks/'

global active_fig
active_fig = None

global active_data
active_data = None

global active_ax
active_ax = None

global active_labels
active_labels = None

global active_colors
active_colors = None

global active_thickness
active_thickness = None

#This creates a popup window that presents the rock faces within the foulder which you can select one to view

    
def plot():
        #Plotting data################################################################################################################################################################################################################################################
    file=options.get(ACTIVE)
    #Replace this with the path to your file
    filename = Path+file+'.txt'
    #Load your data into this program
    #filename is the name of your file, which you defined above
    #skip_header tells the program how many rows to skip at the start of your file (i.e. column headers)
    #dtype tells your program what kind of data you are looking at. If it is all numbers, use float
    #If your data is not all numbers, use None. You'll have to do more processing before you plot though.
    #delimiter tells the program how to separate different values. I am using tab-separated values which means I use \t. If you are using comma-separated values use ',' as your delimiter. If you are using data separated by newline characters, use '\n'.    
    
    data = np.genfromtxt(filename, skip_header=1, dtype=float,delimiter='\t')
    
    #data starts out as a list where every row is a pair of (wavelength, reflectance). I want 2 lists, one of all of my wavelengths, which will go on the x axis, the other of my reflectance values, which will go on the y-axis.
    data=zip(*data)
    
    nm=[]
    reflectance=[]
    for i, d in enumerate(data):
        if i==0: nm=d #the first column in my .tsv (now first row) was wavelength in nm
        else:
            d=np.array(d)
            #d2=d/np.max(d)
            reflectance.append(d) #the second columnn in my .tsv (now 2nd row) was reflectance
            #reflectance[1].append(d2)
    
    labels=['i=30 e=0 g=30','i=30 e=50 g=80','i=50 e=-30 g=20'] #i= e= and g=
    Colors=[(.38,.55,.33),(.65,.38,.09),(.11,.48,.54)]
    Thickness=[2.3,1,1.5]  
        
    #make a plot
    fig = plt.figure(figsize=(20,10))
    #figs.append(plt.figure(figsize=(20,10)))
    
    ax=fig.add_axes((0.1,0.2,0.8,0.7))
    
    #plot your data
    for j, spectrum in enumerate(reflectance):
        if labels[j] in ['i=30 e=0 g=30','i=30 e=50 g=80','i=50 e=-30 g=20']:
            ax.plot(nm, spectrum, label=labels[j], color=Colors[j],linewidth=Thickness[j])
    
        ax.legend()
        
        #Decide how big you want your tick markers to be
    ax.tick_params(labelsize=14)
        #ax.set_yticklabels([])
    ax.grid()
    
    #Decide on a title and font size for that title
    ax.set_title(file, size=24)
    
    #Decide on x-axis label and size
    ax.set_xlabel('Wavelength (nm)', size=20)
    
    #Setting the y axis for the first plot
    ax.set_ylabel("Reflectance",size=20)

    #Creating grid lines that start at 300nm and go to 2600nm every 100nm, only labeling 500 to 2500 every 500nm    
    ax.xaxis.set_ticks(np.arange(300, 2600, 100))
    ax.xaxis.set_ticklabels(['','','500','','','','','1000','','','','','1500','','','','','2000','','','','','2500'])
    
    

    
    global active_fig
    active_fig = fig
    
    global active_data
    active_data = [nm, reflectance]
    
    global active_ax
    active_ax = ax
    
    global active_labels
    active_labels = labels
    
    global active_colors
    active_colors = Colors
    
    global active_thickness
    active_thickness = Thickness
    
    
    #This section is to make sure that all the list box's only show the active plot's goniometer orientations
    orientation.delete(0, END)
    if active_labels == ['i=30 e=0 g=30','i=30 e=50 g=80','i=50 e=-30 g=20']:
        orientation.insert(END,'i=30 e=0 g=30')
        orientation.insert(END,'i=30 e=50 g=80')
        orientation.insert(END,'i=50 e=-30 g=20')
        
    slope_listbox.delete(0,END)
    if active_labels == ['i=30 e=0 g=30','i=30 e=50 g=80','i=50 e=-30 g=20']:
        slope_listbox.insert(END,'i=30 e=0 g=30')
        slope_listbox.insert(END,'i=30 e=50 g=80')
        slope_listbox.insert(END,'i=50 e=-30 g=20')
    
    #Show your plot
    plt.show()
    

def plot_GS():
        #Plotting Goniometer Sweep!###################################################################################################################################################################################################################    
    file=options.get(ACTIVE)
    #Replace this with the path to your file
    filename=Path+file+'.txt'
    #Load your data into this program
    #filename is the name of your file, which you defined above
    #skip_header tells the program how many rows to skip at the start of your file (i.e. column headers)
    #dtype tells your program what kind of data you are looking at. If it is all numbers, use float
    #If your data is not all numbers, use None. You'll have to do more processing before you plot though.
    #delimiter tells the program how to separate different values. I am using tab-separated values which means I use \t. If you are using comma-separated values use ',' as your delimiter. If you are using data separated by newline characters, use '\n'.    
    
    data = np.genfromtxt(filename, skip_header=1, dtype=float,delimiter='\t')
    
    #data starts out as a list where every row is a pair of (wavelength, reflectance). I want 2 lists, one of all of my wavelengths, which will go on the x axis, the other of my reflectance values, which will go on the y-axis.
    data=zip(*data)
    
    nm=[]
    reflectance=[]
    for i, d in enumerate(data):
        if i==0: nm=d #the first column in my .tsv (now first row) was wavelength in nm
        else:
            d=np.array(d)
            #d2=d/np.max(d)
            reflectance.append(d) #the second columnn in my .tsv (now 2nd row) was reflectance
            #reflectance[1].append(d2)
    if len(reflectance) == 5 and file.endswith('L2R)'):
        labels=['i=50 e=40 g=10','i=50 e=20 g=30','i=50 e=0 g=50','i=50 e=-20 g=70','i=50 e=-40 g=90']#i= e= and g=
    elif len(reflectance) == 5 and file.endswith('R2L)'):
        labels=['i=-40 e=-50 g=10','i=20 e=-50 g=30','i=0 e=-50 g=50','i=20 e=-50 g=70','i=40 e=-50 g=90']#i= e= and g=
    elif len(reflectance) == 3 and file.endswith('L2R)'):
        labels=['i=30 e=20 g=10','i=30 e=0 g=30','i=30 e=-20 g=50']
    elif len(reflectance) == 3 and file.endswith('R2L)Clipped'):
        labels=['i=-20 e=-30 g=10','i=0 e=-30 g=30','i=20 e=-30 g=50']
    offset=[0,.02,.03,.04,.02]
    Colors=[(.38,.55,.33),(.65,.38,.09),(.11,.48,.54),(.38,.17,.09),(.13,.14,.16)]
    Thickness=[1,1,1,1,1]  
        
    #make a plot
    fig = plt.figure(figsize=(20,10))
    #figs.append(plt.figure(figsize=(20,10)))
    
    ax=fig.add_axes((0.1,0.2,0.8,0.7))
    
    #plot your data
    for j, spectrum in enumerate(reflectance):
       if labels[j] in ['i=50 e=40 g=10','i=50 e=20 g=30','i=50 e=0 g=50','i=50 e=-20 g=70','i=50 e=-40 g=90'] or['i=-40 e=-50 g=10','i=20 e=-50 g=30','i=0 e=-50 g=50','i=20 e=-50 g=70','i=40 e=-50 g=90'] or ['i=30 e=20 g=10','i=30 e=0 g=30','i=30 e=-20 g=50'] or['i=-20 e=-30 g=10','i=0 e=-30 g=30','i=20 e=-30 g=50']:
           ax.plot(nm, spectrum, label=labels[j], color=Colors[j],linewidth=Thickness[j])
           #ax.plot(nm, spectrum + offset[j], label=labels[j],linewidth=Thickness[j])
    
    ax.legend()
        
        #Decide how big you want your tick markers to be
    ax.tick_params(labelsize=14)
        #ax.set_yticklabels([])
    ax.grid()
    
    #Decide on a title and font size for that title
    ax.set_title(file, size=24)
    
    #Decide on x-axis label and size
    ax.set_xlabel('Wavelength (nm)', size=20)
    
    #Setting the y axis for the first plot
    ax.set_ylabel("Reflectance",size=20)

    #Creating grid lines that start at 300nm and go to 2600nm every 100nm, only labeling 500 to 2500 every 500nm    
    ax.xaxis.set_ticks(np.arange(300, 2600, 100))
    ax.xaxis.set_ticklabels(['','','500','','','','','1000','','','','','1500','','','','','2000','','','','','2500'])

    
    global active_fig
    active_fig = fig
    
    global active_data
    active_data = [nm, reflectance]
    
    global active_ax
    active_ax = ax
    
    global active_labels
    active_labels = labels
    
    global active_colors
    active_colors = Colors
    
    global active_thickness
    active_thickness = Thickness


    #This section is to make sure that all the list box's only show the active plot's goniometer orientations    
    orientation.delete(0, END)
    if active_labels == ['i=50 e=40 g=10','i=50 e=20 g=30','i=50 e=0 g=50','i=50 e=-20 g=70','i=50 e=-40 g=90']:
        orientation.insert(END,'i=50 e=40 g=10')
        orientation.insert(END,'i=50 e=20 g=30')
        orientation.insert(END,'i=50 e=0 g=50')
        orientation.insert(END,'i=50 e=-20 g=70')
        orientation.insert(END,'i=50 e=-40 g=90')
    elif active_labels == ['i=-40 e=-50 g=10','i=20 e=-50 g=30','i=0 e=-50 g=50','i=20 e=-50 g=70','i=40 e=-50 g=90']:
        orientation.insert(END,'i=-40 e=-50 g=10')
        orientation.insert(END,'i=20 e=-50 g=30')
        orientation.insert(END,'i=0 e=-50 g=50')
        orientation.insert(END,'i=20 e=-50 g=70')
        orientation.insert(END,'i=40 e=-50 g=90')
    elif active_labels == ['i=30 e=20 g=10','i=30 e=0 g=30','i=30 e=-20 g=50']:
        orientation.insert(END,'i=30 e=20 g=10')
        orientation.insert(END,'i=30 e=0 g=30')
        orientation.insert(END,'i=30 e=-20 g=50')
    elif active_labels == ['i=-20 e=-30 g=10','i=0 e=-30 g=30','i=20 e=-30 g=50']:
        orientation.insert(END,'i=-20 e=-30 g=10')
        orientation.insert(END,'i=0 e=-30 g=30')
        orientation.insert(END,'i=20 e=-30 g=50')
        
    slope_listbox.delete(0,END)
    if active_labels == ['i=50 e=40 g=10','i=50 e=20 g=30','i=50 e=0 g=50','i=50 e=-20 g=70','i=50 e=-40 g=90']:
        slope_listbox.insert(END,'i=50 e=40 g=10')
        slope_listbox.insert(END,'i=50 e=20 g=30')
        slope_listbox.insert(END,'i=50 e=0 g=50')
        slope_listbox.insert(END,'i=50 e=-20 g=70')
        slope_listbox.insert(END,'i=50 e=-40 g=90')
    elif active_labels == ['i=-40 e=-50 g=10','i=20 e=-50 g=30','i=0 e=-50 g=50','i=20 e=-50 g=70','i=40 e=-50 g=90']:
        slope_listbox.insert(END,'i=-40 e=-50 g=10')
        slope_listbox.insert(END,'i=20 e=-50 g=30')
        slope_listbox.insert(END,'i=0 e=-50 g=50')
        slope_listbox.insert(END,'i=20 e=-50 g=70')
        slope_listbox.insert(END,'i=40 e=-50 g=90')
    elif active_labels == ['i=30 e=20 g=10','i=30 e=0 g=30','i=30 e=-20 g=50']:
        slope_listbox.insert(END,'i=30 e=20 g=10')
        slope_listbox.insert(END,'i=30 e=0 g=30')
        slope_listbox.insert(END,'i=30 e=-20 g=50')
    elif active_labels == ['i=-20 e=-30 g=10','i=0 e=-30 g=30','i=20 e=-30 g=50']:
        slope_listbox.insert(END,'i=-20 e=-30 g=10')
        slope_listbox.insert(END,'i=0 e=-30 g=30')
        slope_listbox.insert(END,'i=20 e=-30 g=50')
    
    #Show your plot
    plt.show()
    
    
def normalize_from_click ():
        #Normalizing Data!############################################################################################################################################################################################################################
    global active_fig
    x = active_fig.ginput(1)
    x_point = int(round(x[0][0])) #Rounding x to the nearest whole number
    normalize(x_point)

def normalize_from_entry ():
    normalize(int(yup.get()))
    
def normalize(x_point):
    file=options.get(ACTIVE)
    #Replace this with the path to your file
    filename=Path+file+'.txt'    
     
     #NEW NORMALIZED FIGURE
     
    data = np.genfromtxt(filename, skip_header=1, dtype=float,delimiter='\t')
     
     #data starts out as a list where every row is a pair of (wavelength, reflectance). I want 2 lists, one of all of my wavelengths, which will go on the x axis, the other of my reflectance values, which will go on the y-axis.
    data=zip(*data)
     
    nm=[]
    reflectance=[]
    for i, d in enumerate(data):
        if i==0: nm=np.array(d).astype(int) #the first column in my .tsv (now first row) was wavelength in nm
        else:
            d=np.array(d)
            index = np.where(nm == x_point)
            y = d[index]
            d = d * 1 / y
            reflectance.append(d) #the second columnn in my .tsv (now 2nd row) was reflectance
     
    labels = active_labels #i= e= and g=
    Colors= active_colors
    Thickness=active_thickness   
    #make a plot
    fig2 = plt.figure(figsize=(20,10))
    #figs.append(plt.figure(figsize=(20,10)))
    
    ax=fig2.add_axes((0.1,0.2,0.8,0.7))
     
     #plot your data
    for j, spectrum in enumerate(reflectance):
        if labels[j] in active_labels:
            ax.plot(nm, spectrum, label=labels[j], color=Colors[j],linewidth=Thickness[j])
     
        ax.legend()
         
         #Decide how big you want your tick markers to be
    ax.tick_params(labelsize=14)
         #ax.set_yticklabels([])
    ax.grid()
     
     #Decide on a title and font size for that title
    ax.set_title(file, size=24)
     
     #Decide on x-axis label and size
    ax.set_xlabel('Wavelength (nm)', size=20)
     #Labeling yaxis
    ax.set_ylabel("Normalized Reflectance",size=20)
    
    #Creating grid lines that start at 300nm and go to 2600nm every 100nm, only labeling 500 to 2500 every 500nm
    ax.xaxis.set_ticks(np.arange(300, 2600, 100))
    ax.xaxis.set_ticklabels(['','','500','','','','','1000','','','','','1500','','','','','2000','','','','','2500'])
     
    plt.text(200,-.05, r"$\bf{Figure:}$" + 'Spectra were taken from '+file+'. Plot 1 is absolute reflectance, Plot 2 \nis the reflectance that has been normalized to 1.0 at '+str(x_point)+' nm.',fontsize = 20)
     #plt.text(200,-.1, r"$\bf{Figure:}$" + 'Spectra were taken from '+file+' with three different orientations of incidence and emission \nangles as indicated by their color and the legend. Each spectra was taken from the exact same location with a white \nreference to periodically callobrate the spectrum was taken using spectralon. Plot 1 is absolute reflectance, Plot 2 \nis the reflectance that has been normalized to 1.0 at '+str(x_point)+' nm.',fontsize = 20) 
     
     #Set range of your plot (will do this automatically, but not always how you'd like).
     #plt.ylim([0,1])
     
     #Show your plot
    global active_fig
    active_fig = fig2
    
    global active_data
    active_data = [nm, reflectance]
    
    global active_ax
    active_ax = ax

def calc_banddepth():
    #Determining Band Depth######################################################################################################################################################################################################################################    
    global active_data
    nm = active_data[0]
    reflectance = active_data[1]
    
    nm=list(nm)
    
    bdpoints = active_fig.ginput(3) #choosing left shoulder, right shoulder and middle points for determinig band depth.
    xLS = int(round(bdpoints[0][0])) 
    yLS = bdpoints[0][1]
    xRS = int(round(bdpoints[1][0])) 
    yRS = bdpoints[1][1]
    xMid = int(round(bdpoints[2][0]))   #Middle Value!
    yMid = bdpoints[2][1]
    
    #Finding actual y-value for selected point corresponding to selected x-value (Left Shoulder)
    #index = np.where(nm == xLS)
    index = nm.index(xLS)
    yLS = reflectance[orientation.curselection()[0]][index].item()
    
    #Finding actual y-value for selected point corresponding to selected x-value (Right Shoulder)
    index = nm.index(xRS)
    yRS = reflectance[orientation.curselection()[0]][index].item()
    
    #Finding actual y-value for selected point corresponding to selected x-value (Middle)
    index = nm.index(xMid)
    sliced_refl = reflectance[orientation.curselection()[0]][index-25:index+25]
    yMid = np.amin(sliced_refl).item()
    
    #Mathematical Equation Determining the Band Depth
    band_depth = ((yLS - yRS)/(xLS - xRS))*(xMid - xLS) + yLS - yMid
#    bd_label = Label(master, text="The band depth of this feature is "+str(band_depth)+" reflectance.").pack()
    messagebox.showinfo("Band Depth","The band depth of this feature is "+str(band_depth)+".")

    

def calc_slope():
    #Determining Slope#####################################################################################################################################################################################################################################################################################
    
    global active_data
    nm = active_data[0]
    reflectance = active_data[1]
    nm=list(nm)
    
    global active_ax
    
    
    #This is great! But... I want this to show up as a button as an option for someone to click on if they would like to determine slope_listbox. And for them to choose to do this before or after normalizing
    xy1= active_fig.ginput(1)
    x1_point = int(round(xy1[0][0])) #rounded x-value
    y1_point = xy1[0][1]
        #Finding actual y-value for selected point corresponding to selected x-value (Point A)
    index = nm.index(x1_point)
    y1_point = reflectance[slope_listbox.curselection()[0]][index].item()
    y1_pointr = round(y1_point,4) #rounded y-value
    a_label = Label(slope_frame, text="Point A: ("+str(x1_point)+","+str(y1_point)+")").pack()
    
    xy2=plt.ginput(1)
    x2_point = int(round(xy2[0][0]))#rounded-value
    y2_point = xy2[0][1]   
        #Finding actual y-value for selected point corresponding to selected x-value (Point B)
    index = nm.index(x2_point)
    y2_point = reflectance[slope_listbox.curselection()[0]][index].item()
    y2_pointr = round(y2_point,4)#rounded y-value
    b_label = Label(slope_frame, text="Point B: ("+str(x2_point)+","+str(y2_point)+")").pack()
    
    xy3=plt.ginput(1)
    x3_point = int(round(xy3[0][0]))
    y3_point = xy3[0][1]
        #Finding actual y-value for selected point corresponding to selected x-value (Point B)
    index = nm.index(x3_point)
    y3_point = reflectance[slope_listbox.curselection()[0]][index].item()
    y3_pointr = round(y3_point,4)#rounded y-value
    c_label = Label(slope_frame, text="Point C: ("+str(x3_point)+","+str(y3_point)+")").pack()
    
    slope1=(y2_point - y1_point)/(x2_point - x1_point)
    abslope_label = Label(slope_frame, text="The slope from point A to B is, "+"{:.2e}".format(slope1)+".").pack()
    slope2=(y3_point - y2_point)/(x3_point - x2_point)
    bcslope_label = Label(slope_frame, text="The slope from point B to C is, "+"{:.2e}".format(slope2)+".").pack()
    
    points=['A', 'B', 'C']
    x = [x1_point, x2_point, x3_point]
    y = [y1_point, y2_point, y3_point]
    
    for i, txt in enumerate(points):
        active_ax.annotate(txt, (x[i],y[i]), color = 'r')
    
    active_ax.plot([x1_point, x2_point], [y1_point, y2_point], 'k-', lw=2)
    active_ax.plot([x2_point, x3_point], [y2_point, y3_point], 'k-', lw=2)
    
    plt.show()
    


def annotate():
    #Drop Down Lines over selected Reflectance########################################################################################################################################################################################################################################################################
    global active_fig
    global active_ax
    
    pnt = active_fig.ginput(1)
    xpnt = int(round(pnt[0][0])) #pulling out and rounding the wavelength value selected
    
    active_ax.plot([xpnt, xpnt], active_ax.get_ylim(), 'r--', lw=1) #plotting a vertical dashed line through the selected point
    plt.show() #Show vertical line   
    
    
def raise_above_all(master):
    master.attributes('-topmost', True)
master = Tk()
notebook=ttk.Notebook(master)
raise_above_all(master)
master.winfo_toplevel().title('CRB Goniometer Spectra') #Laeling the popup window

#Instructions to the user
rockface_frame = Frame(notebook)
rockface_frame.pack()
rockface_label = Label(rockface_frame, text="Please select the rock face you wish to view from the \nlist below. Then select ''Show Spectra'' at the bottom of the screen. \nTo quit the program, click on the exit button at the top of this box.")
rockface_label.pack()


  
#This creates the frame in which the scrollbar is going to be placed
scroll_frame = Frame(rockface_frame)
scroll_frame.pack()

#This creates the scrollbar and places it in the frame
scrollbar = Scrollbar(scroll_frame, orient="vertical")
scrollbar.pack(side=RIGHT, fill=Y)

options = Listbox(scroll_frame, selectmode='SINGLE', exportselection=False)#This extracts all of the file names within the foulder.
for file in os.listdir(Path): #//volumes/ricedata/Lena/CRB_Goniometer_Spectra/Individual_Rocks
    if not file.startswith('.'):#This cleans up what files are shown
        options.insert(END, file.strip('.txt'))#This removes the .txt from being shown to clean up what is seen, so that just a rock face is presented.
options.pack() #This is the location on the popup window where the list is shown
  

  
#This syncs the scrollbar and the mouse so that you can scroll with either and they both track
options.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=options.yview)
  
#This creates the show spectra button that starts the function to plot the spectra of the selected rock face.
plot_button = tkinter.Button(rockface_frame, text = 'Show Spectra', command = plot)
plot_button.pack()

GS_button = Button(rockface_frame, text="Show Goniometer Sweep", command = plot_GS)
GS_button.pack()

##Creating Tab for Normalization Function with listbox and activation button
norm_frame = Frame(notebook)
norm_frame.pack()
norm_label = Label(norm_frame, text="Please, click on an x value to normalize data. \nOr enter a value for x to which you would like to normalize \nin the space below. Then, click anywhere inside the plot.").pack()
yup = Entry(norm_frame)
yup.pack()
norm_button = Button(norm_frame, text="Normalize", command = normalize_from_entry)
norm_button.pack()
norm_button_click = Button(norm_frame, text="Manual Selection", command = normalize_from_click)
norm_button_click.pack()

#Creating Tab for determining banddepth Function with listbox and activation button
banddepth_frame = Frame(notebook)
banddepth_frame.pack()
banddepth_label = Label(banddepth_frame, text="Please select the spectra orientation \nfor which you would like to determine the band depth.").pack()
orientation = Listbox(banddepth_frame, selectmode='SINGLE', exportselection=False)
orientation.pack()
banddepth_label2 = Label(banddepth_frame, text="To determine band depth of this orientation, \nplease click ''collect'' and then select your left shoulder, right shoulder and \nminimum points on the plot.").pack()
banddepth_button = Button(banddepth_frame, text = "Collect", command = calc_banddepth)
banddepth_button.pack()

#Creating Tab for Slope Function with listbox and activation button
slope_frame = Frame(notebook)
slope_frame.pack()
slope_label = Label(slope_frame, text="Please, click on desired locations for points A, B and C to determine the slope between points A and B, and B and C.").pack()
slope_listbox = Listbox(slope_frame, selectmode='SINGLE', exportselection=False)
slope_listbox.pack()
slope_button = Button(slope_frame, text="Select Points", command = calc_slope)
slope_button.pack()

#Creating Tab for Annotations with activation buttons 
annotation_frame = Frame(notebook)    
annotation_frame.pack()
annotation_label = Label(annotation_frame, text="Select a feature that you would like to have a vetical line be placed through.").pack()
annotation_button = Button(annotation_frame, text = "Place Vertical Line", command = annotate)
annotation_button.pack()

#Adding Tab to the Notebook
notebook.add(rockface_frame, text="Rock Selection")
notebook.add(norm_frame, text="Normalization")
notebook.add(banddepth_frame, text="Band Depth")
notebook.add(slope_frame, text="Slope")
notebook.add(annotation_frame, text="Annotations")
notebook.pack()

mainloop( )