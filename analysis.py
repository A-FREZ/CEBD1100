import os
import numpy

def average_inflammations(patient_id, file_name='inflammation-01.csv'):
    ''' 
    Return the average number of inflammations for a patient in a data file.
    patient_id -- id of the patient
    file_name  -- data file name, must be under directory 'data'
    '''

    # Concatenate directory name with file name
    data_dir = 'data'
    complete_file_name = os.path.join(data_dir, file_name)

    # Load data
    inflammations = numpy.loadtxt(fname=complete_file_name, delimiter=',')

    # Compute and return the average
    avg = numpy.average(inflammations[patient_id])
    return avg

def max_inflammations(patient_id, file_name='inflammation-01.csv'):
    '''
    Return the max number of inflammations for a patient in a data file;
    patient_id -- id of the patient
    file_name  -- data file name, must be under directory 'data'
    '''

    # Concatenate directory name with file name
    data_dir = 'data'
    complete_file_name = os.path.join(data_dir, file_name)

    # Load data
    inflammations = numpy.loadtxt(fname=complete_file_name, delimiter=',')

    # Compute and return the max
    max = numpy.max(inflammations[patient_id])
    return max

def acute_patient(file_name='inflammation-01.csv'):
    '''
    Return the id of the patient with the highest average number of 
    inflammations in the dataset.
    patient_id -- id of the patient
    file_name  -- data file name, must be under directory 'data'
    '''

    # Concatenate directory name with file name
    data_dir = 'data'
    complete_file_name = os.path.join(data_dir, file_name)

    # Load data
    # inflammations = numpy.loadtxt(fname=complete_file_name, delimiter=',')
    # Compute and return the Acute
    # avg = numpy.argmax(numpy.average(inflammations, axis=1))

#print("My Solution of Maximum Average number of inflammations in dataset with Loop + numpy")
    inflammations = numpy.loadtxt(fname=complete_file_name, delimiter=',')
    a = inflammations
    from numpy import average
    maxavg = 0
    for i in range(60):
        if  average(a[i]) > maxavg:
            patientid = i + 1
            maxavg = average(a[i])
        #print("For Patientid: ", patientid, "   Average No of inflammations= ", average(a[i]))

    acute = int(patientid)
    return acute