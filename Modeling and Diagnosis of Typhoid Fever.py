import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import tkinter

fever=ctrl.Antecedent(np.arange(0,11,1),'fever')
headache=ctrl.Antecedent(np.arange(0,11,1),'headache')
nausea=ctrl.Antecedent(np.arange(0,11,1),'nausea')
vomiting=ctrl.Antecedent(np.arange(0,11,1),'vomiting')
jaundice=ctrl.Antecedent(np.arange(0,11,1),'jaundice')
joint_pain=ctrl.Antecedent(np.arange(0,11,1),'joint_pain')
body_weakness=ctrl.Antecedent(np.arange(0,11,1),'body_weakness')
dizziness=ctrl.Antecedent(np.arange(0,11,1),'dizziness')
loss_of_appetite=ctrl.Antecedent(np.arange(0,11,1),'loss_of_appetite')

typhoid_fever=ctrl.Consequent(np.arange(0,11,1),'typhoid_fever')

fever['very_mild']=fuzz.trimf(fever.universe,[0,0,1])
fever['mild']=fuzz.trimf(fever.universe,[1,2,4])
fever['moderate']=fuzz.trimf(fever.universe,[3,5,6])
fever['severe']=fuzz.trimf(fever.universe,[5,7,9])
fever['very_severe']=fuzz.trimf(fever.universe,[7,10,10])

headache['very_mild']=fuzz.trimf(headache.universe,[0,0,1])
headache['mild']=fuzz.trimf(headache.universe,[1,2,4])
headache['moderate']=fuzz.trimf(headache.universe,[3,5,6])
headache['severe']=fuzz.trimf(headache.universe,[5,7,9])
headache['very_severe']=fuzz.trimf(headache.universe,[7,10,10])

nausea['very_mild']=fuzz.trimf(nausea.universe,[0,0,1])
nausea['mild']=fuzz.trimf(nausea.universe,[1,2,4])
nausea['moderate']=fuzz.trimf(nausea.universe,[3,5,6])
nausea['severe']=fuzz.trimf(nausea.universe,[5,7,9])
nausea['very_severe']=fuzz.trimf(nausea.universe,[7,10,10])

vomiting['very_mild']=fuzz.trimf(vomiting.universe,[0,0,1])
vomiting['mild']=fuzz.trimf(vomiting.universe,[1,2,4])
vomiting['moderate']=fuzz.trimf(vomiting.universe,[3,5,6])
vomiting['severe']=fuzz.trimf(vomiting.universe,[5,7,9])
vomiting['very_severe']=fuzz.trimf(vomiting.universe,[7,10,10])

jaundice['very_mild']=fuzz.trimf(jaundice.universe,[0,0,1])
jaundice['mild']=fuzz.trimf(jaundice.universe,[1,2,4])
jaundice['moderate']=fuzz.trimf(jaundice.universe,[3,5,6])
jaundice['severe']=fuzz.trimf(jaundice.universe,[5,7,9])
jaundice['very_severe']=fuzz.trimf(jaundice.universe,[7,10,10])

joint_pain['very_mild']=fuzz.trimf(joint_pain.universe,[0,0,1])
joint_pain['mild']=fuzz.trimf(joint_pain.universe,[1,2,4])
joint_pain['moderate']=fuzz.trimf(joint_pain.universe,[3,5,6])
joint_pain['severe']=fuzz.trimf(joint_pain.universe,[5,7,9])
joint_pain['very_severe']=fuzz.trimf(joint_pain.universe,[7,10,10])

body_weakness['very_mild']=fuzz.trimf(body_weakness.universe,[0,0,1])
body_weakness['mild']=fuzz.trimf(body_weakness.universe,[1,2,4])
body_weakness['moderate']=fuzz.trimf(body_weakness.universe,[3,5,6])
body_weakness['severe']=fuzz.trimf(body_weakness.universe,[5,7,9])
body_weakness['very_severe']=fuzz.trimf(body_weakness.universe,[7,10,10])

dizziness['very_mild']=fuzz.trimf(dizziness.universe,[0,0,1])
dizziness['mild']=fuzz.trimf(dizziness.universe,[1,2,4])
dizziness['moderate']=fuzz.trimf(dizziness.universe,[3,5,6])
dizziness['severe']=fuzz.trimf(dizziness.universe,[5,7,9])
dizziness['very_severe']=fuzz.trimf(dizziness.universe,[7,10,10])

loss_of_appetite['very_mild']=fuzz.trimf(loss_of_appetite.universe,[0,0,1])
loss_of_appetite['mild']=fuzz.trimf(loss_of_appetite.universe,[1,2,4])
loss_of_appetite['moderate']=fuzz.trimf(loss_of_appetite.universe,[3,5,6])
loss_of_appetite['severe']=fuzz.trimf(loss_of_appetite.universe,[5,7,9])
loss_of_appetite['very_severe']=fuzz.trimf(loss_of_appetite.universe,[7,10,10])

typhoid_fever['very_mild']=fuzz.trimf(typhoid_fever.universe,[0,0,1])
typhoid_fever['mild']=fuzz.trimf(typhoid_fever.universe,[1,2,4])
typhoid_fever['moderate']=fuzz.trimf(typhoid_fever.universe,[3,5,6])
typhoid_fever['severe']=fuzz.trimf(typhoid_fever.universe,[5,7,9])
typhoid_fever['very_severe']=fuzz.trimf(typhoid_fever.universe,[7,10,10])

rule1=ctrl.Rule((fever['very_mild'] & headache['very_mild'] & nausea['very_mild'])
                | (vomiting['very_mild'] & jaundice['very_mild'] & joint_pain['very_mild'])
                | (body_weakness['very_mild'] & dizziness['very_mild'] & loss_of_appetite['very_mild'])
                ,typhoid_fever['very_mild'])

rule2=ctrl.Rule((fever['mild'] & headache['mild'] & nausea['mild'])
                | (vomiting['mild'] & jaundice['moderate'] & joint_pain['mild'])
                | (body_weakness['moderate'] & dizziness['moderate'] & loss_of_appetite['mild'])
                ,typhoid_fever['mild'])
rule3=ctrl.Rule((fever['moderate'] & headache['mild'] & nausea['moderate'])
                | (vomiting['moderate'] & jaundice['mild'] & joint_pain['moderate'])
                | (body_weakness['moderate'] & dizziness['moderate'] & loss_of_appetite['moderate'])
                ,typhoid_fever['mild'])

rule4=ctrl.Rule((fever['moderate'] & headache['moderate'] & nausea['moderate'])
                | (vomiting['moderate'] & jaundice['moderate'] & joint_pain['moderate'])
                | (body_weakness['moderate'] & dizziness['moderate'] & loss_of_appetite['severe'])
                ,typhoid_fever['moderate'])
rule5=ctrl.Rule((fever['severe'] & headache['moderate'] & nausea['moderate'])
                | (vomiting['moderate'] & jaundice['severe'] & joint_pain['moderate'])
                | (body_weakness['severe'] & dizziness['moderate'] & loss_of_appetite['severe'])
                ,typhoid_fever['moderate'])
rule6=ctrl.Rule((fever['moderate'] & headache['severe'] & nausea['severe'])
                | (vomiting['moderate'] & jaundice['severe'] & joint_pain['severe'])
                | (body_weakness['severe'] & dizziness['moderate'] & loss_of_appetite['moderate'])
                ,typhoid_fever['moderate'])

rule7=ctrl.Rule((fever['severe'] & headache['severe'] & nausea['severe'])
                | (vomiting['severe'] & jaundice['severe'] & joint_pain['severe'])
                | (body_weakness['severe'] & dizziness['severe'] & loss_of_appetite['severe'])
                ,typhoid_fever['severe'])
rule8=ctrl.Rule((fever['very_severe'] & headache['severe'] & nausea['severe'])
                | (vomiting['severe'] & jaundice['very_severe'] & joint_pain['severe'])
                | (body_weakness['severe'] & dizziness['severe'] & loss_of_appetite['very_severe'])
                ,typhoid_fever['severe'])

rule9=ctrl.Rule((fever['very_severe'] & headache['severe'] & nausea['very_severe'])
                | (vomiting['very_severe'] & jaundice['very_severe'] & joint_pain['severe'])
                | (body_weakness['very_severe'] & dizziness['severe'] & loss_of_appetite['very_severe'])
                ,typhoid_fever['very_severe'])
rule10=ctrl.Rule((fever['very_severe'] & headache['very_severe'] & nausea['very_severe'])
                | (vomiting['very_severe'] & jaundice['very_severe'] & joint_pain['very_severe'])
                | (body_weakness['very_severe'] & dizziness['very_severe'] & loss_of_appetite['very_severe'])
                ,typhoid_fever['very_severe'])


rulecollection=ctrl.ControlSystem([rule10,rule9,rule8,rule7,rule5,rule5,rule4,rule3,rule2,rule1])
simulator=ctrl.ControlSystemSimulation(rulecollection)

root=None
SUBMIT=None

def view_antecedent(obj):
    obj.view()

def typhoid_display_window():
    global f,h,n,v,j,jp,bw,d,la

    f=float(e1.get())
    h=float(e2.get())
    n=float(e3.get())
    v=float(e4.get())
    j=float(e5.get())
    jp=float(e6.get())
    bw=float(e7.get())
    d=float(e8.get())
    la=float(e9.get())
    
    simulator.input['fever']=f
    simulator.input['headache']=h
    simulator.input['nausea']=n
    simulator.input['vomiting']=v
    simulator.input['jaundice']=j
    simulator.input['joint_pain']=jp
    simulator.input['body_weakness']=bw
    simulator.input['dizziness']=d
    simulator.input['loss_of_appetite']=la

    simulator.compute()

    e11=tkinter.Entry(root,bg='white',fg='black',width=60,font='Arial 12')

    e11.delete(0,tkinter.END)
    e11.insert(0,simulator.output['typhoid_fever'])
    typhoid_fever.view(sim=simulator)

    e11.place(x=50,y=645)
    

    
def simulator_window():
    global main_tag,l1,e1,l2,e2,l3,e3,l4,e4,l5,e5,l6,e6,l7,e7,l8,e8,l9,e9,l10,e10,e11,v1,v2,v3,v4,v5,v6,v7,v8,v9
    
    root=tkinter.Tk()
    root.title(" SIMULATION WINDOW")
    root.geometry("1000x800")
    root.configure(background='cyan4')
    
    main_tag=tkinter.Label(root,text="Modeling and Diagnosis of Typhoid Fever",bg='white',fg='cyan4',font="Times 16 bold italic",height=1)
    
    l1=tkinter.Label(root,text="Fever",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    e1=tkinter.Entry(root,bg='white',fg='cyan4',width=20,font='Arial 12')
    l2=tkinter.Label(root,text="Headache",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    e2=tkinter.Entry(root,bg='white',fg='cyan4',width=20,font='Arial 12')
    l3=tkinter.Label(root,text="Nausea",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    e3=tkinter.Entry(root,bg='white',fg='cyan4',width=20,font='Arial 12')
    l4=tkinter.Label(root,text="Vomiting",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    e4=tkinter.Entry(root,bg='white',fg='cyan4',width=20,font='Arial 12')
    l5=tkinter.Label(root,text="Jaundice",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    e5=tkinter.Entry(root,bg='white',fg='cyan4',width=20,font='Arial 12')
    l6=tkinter.Label(root,text="Joint Pain",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    e6=tkinter.Entry(root,bg='white',fg='cyan4',width=20,font='Arial 12')
    l7=tkinter.Label(root,text="Body Weakness",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    e7=tkinter.Entry(root,bg='white',fg='cyan4',width=20,font='Arial 12')
    l8=tkinter.Label(root,text="Dizziness",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    e8=tkinter.Entry(root,bg='white',fg='cyan4',width=20,font='Arial 12')
    l9=tkinter.Label(root,text="Loss of Appetite",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    e9=tkinter.Entry(root,bg='white',fg='cyan4',width=20,font='Arial 12')
    l10=tkinter.Label(root,text="Typhoid Fever Anaysis",bg='gray25',fg='white',height=1,width=20,font='Times 16 bold italic')
    e10=tkinter.Entry(root,bg='white',fg='black',width=60,font='Arial 12')
    e12=tkinter.Entry(root,bg='white',fg='black',width=60,font='Arial 12')
    e13=tkinter.Entry(root,bg='white',fg='black',width=60,font='Arial 12')
    e14=tkinter.Entry(root,bg='white',fg='black',width=60,font='Arial 12')
    e15=tkinter.Entry(root,bg='white',fg='black',width=60,font='Arial 12')
    e16=tkinter.Entry(root,bg='white',fg='black',width=60,font='Arial 12')
    e17=tkinter.Entry(root,bg='white',fg='black',width=60,font='Arial 12')
    e10.insert(0,'Simulation Scale is defined as :')
    e12.insert(0,'---      0-1 : Very Mild     ---')
    e13.insert(0,'---      1-4 : Mild          ---') 
    e14.insert(0,'---      3-6 : Moderate      ---')          
    e15.insert(0,'---      5-9 : Severe        ---')
    e16.insert(0,'---      7-10: Very Severe   ---') 
    e17.insert(0,'Hence Crisp Typhoid Fever Value is :')
               
    v1=tkinter.Button(root,text="*",command=lambda:view_antecedent(fever),font="arial 12",bg='gray25',fg='white',height=1,width=1)
    v2=tkinter.Button(root,text="*",command=lambda:view_antecedent(headache),font="arial 12",bg='gray25',fg='white',height=1,width=1)
    v3=tkinter.Button(root,text="*",command=lambda:view_antecedent(nausea),font="arial 12",bg='gray25',fg='white',height=1,width=1)
    v4=tkinter.Button(root,text="*",command=lambda:view_antecedent(vomiting),font="arial 12",bg='gray25',fg='white',height=1,width=1)
    v5=tkinter.Button(root,text="*",command=lambda:view_antecedent(jaundice),font="arial 12",bg='gray25',fg='white',height=1,width=1)
    v6=tkinter.Button(root,text="*",command=lambda:view_antecedent(joint_pain),font="arial 12",bg='gray25',fg='white',height=1,width=1)
    v7=tkinter.Button(root,text="*",command=lambda:view_antecedent(body_weakness),font="arial 12",bg='gray25',fg='white',height=1,width=1)
    v8=tkinter.Button(root,text="*",command=lambda:view_antecedent(dizziness),font="arial 12",bg='gray25',fg='white',height=1,width=1)
    v9=tkinter.Button(root,text="*",command=lambda:view_antecedent(loss_of_appetite),font="arial 12",bg='gray25',fg='white',height=1,width=1)
    
    SUBMIT=tkinter.Button(root,text="  SUBMIT  ",command=typhoid_display_window,font="arial 12",bg='gray25',fg='white',height=1,width=10)
    
    main_tag.place(x=0,y=0)
    l1.place(x=50,y=50)
    e1.place(x=250,y=50)
    l2.place(x=500,y=50)
    e2.place(x=700,y=50)
    l3.place(x=50,y=100)
    e3.place(x=250,y=100)
    l4.place(x=500,y=100)
    e4.place(x=700,y=100)
    l5.place(x=50,y=150)
    e5.place(x=250,y=150)
    l6.place(x=500,y=150)
    e6.place(x=700,y=150)
    l7.place(x=50,y=200)
    e7.place(x=250,y=200)
    l8.place(x=500,y=200)
    e8.place(x=700,y=200)
    l9.place(x=50,y=250)
    e9.place(x=250,y=250)
    l10.place(x=50,y=350)
    e10.place(x=50,y=400)
    e12.place(x=50,y=435)
    e13.place(x=50,y=470)
    e14.place(x=50,y=505)
    e15.place(x=50,y=540)
    e16.place(x=50,y=575)
    e17.place(x=50,y=610)

    v1.place(x=25,y=50)
    v2.place(x=900,y=50)
    v3.place(x=25,y=100)
    v4.place(x=900,y=100)
    v5.place(x=25,y=150)
    v6.place(x=900,y=150)
    v7.place(x=25,y=200)
    v8.place(x=900,y=200)
    v9.place(x=25,y=250)
    
    SUBMIT.place(x=50,y=300)
    
    root.mainloop()

simulator_window()
print('End of simulation !!! Have a nice day :)')
