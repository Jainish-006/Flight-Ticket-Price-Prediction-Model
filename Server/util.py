import pickle
import json
import numpy as np

__airlines = None
__departure_time = None
__sources = None
__destinations = None
__cls_types = None
__data_columns = None
__model1 = None

def get_estimated_price(airline,time,source,destination,class_type):
    try:
        al_index = __data_columns.index('airline_'+airline.lower())
        det_index = __data_columns.index('dep_time_'+time.lower())
        sc_index = __data_columns.index('source_'+source.lower())
        dest_index = __data_columns.index('destination_'+destination.lower())
        cl_index = __data_columns.index(class_type.lower())
    except:
        al_index = -1
        det_index = -1
        sc_index = -1
        dest_index = -1
        cl_index = -1

    x = np.zeros(len(__data_columns))
    if al_index >= 0:
        x[al_index] = 1

    if det_index >= 0:
        x[det_index] = 1

    if sc_index >= 0:
        x[sc_index] = 1

    if dest_index >= 0:
        x[dest_index] = 1

    if cl_index >= 0:
        x[cl_index] = 1

    return round(__model1.predict([x])[0],2)

def get_airlines():
    return __airlines

def get_deptime():
    return __departure_time

def get_source():
    return __sources

def get_destination():
    return __destinations

def get_clstype():
    return __cls_types

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __airlines
    global __departure_time
    global __sources
    global __destinations
    global __cls_types

    with open("./Artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __airlines = __data_columns[3:10]  # first 3 columns different
        __departure_time = __data_columns[10:14]
        __sources = __data_columns[14:19]
        __destinations = __data_columns[23:]
        __cls_types = __data_columns[2:3]

    global __model1
    with open('./Artifacts/Flight_price_pred.pickle', 'rb') as f:
        __model1 = pickle.load(f)
    print("loading saved artifacts...done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_airlines())
    print(get_deptime())
    print(get_source())
    print(get_destination())
    print(get_clstype())
    #print(get_estimated_price('AirAsia','Evening','Mumbai','Kolkata','Economy'))
    #print(get_estimated_price('AirAsia','Morning','Mumbai','Kolkata','Business'))
    #print(get_estimated_price('Vistara', 'Morning', 'Mumbai', 'Delhi', 'Business'))
