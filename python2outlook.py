
import pandas as pd
import win32com.client


archivo =  'hoja_eventos.xlsx'
hoja = 'Sheet1'

#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------

def addevent(start, subject):
    
    oOutlook = win32com.client.Dispatch("Outlook.Application")
    appointment = oOutlook.CreateItem(1) # 1=outlook appointment item
    appointment.Start = start
    appointment.Subject = subject
    appointment.Duration = 20
    appointment.Location = 'EAFIT'
    appointment.ReminderSet = True
    appointment.ReminderMinutesBeforeStart = 1
    appointment.MeetingStatus = 1
    appointment.Recipients.Add('cvalen20@eafit.edu.co')
    appointment.Save()
    appointment.Send()

    return appointment.EntryID 

#-------------------------------------------------------------------------------------------

params = pd.read_excel( archivo , sheet_name = hoja, header = 1 )

fechas = params['Fecha']
horas = params['Hora']
eventos = params['Evento']


for i in range(len(fechas)):
    f_temp = fechas[i]
    h_temp = horas[i]
    e_temp = eventos[i]
    inicio = str(f_temp.year) +'-'+ str(f_temp.month) +'-'+ str(f_temp.day)+' '+ str(h_temp)

    asunto = e_temp
    
    addevent(inicio, e_temp)
    
    










