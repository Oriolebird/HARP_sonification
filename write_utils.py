import pandas as pd
import soundfile as sf

def write_pos_file(start_time, end_time, pos_time, pos_x, pos_y, pos_z, probe,
                   filename_str='Events'):   
    time_index = (pos_time >= start_time) & (pos_time <= end_time)
    st_str = start_time.strftime("%Y%m%d")
    et_str = end_time.strftime("%Y%m%d")
    
    d = {'datetime':pos_time[time_index],
         'GSM_X_RE':pos_x[time_index],
         'GSM_Y_RE':pos_y[time_index],
         'GSM_Z_RE':pos_z[time_index]}
    pos_df = pd.DataFrame(data=d)
    df_round2 = pos_df.round({'GSM_X_RE': 2, 'GSM_Y_RE': 2, 'GSM_Z_RE': 2})
    #print(df_round2)
    filename = 'text_output/'+filename_str+'_'+probe.upper()+'_GSMpositions_'+st_str+'_'+et_str+'.txt'
    df_round2.to_csv(filename,index=False)
    
    
def write_sound_file(probe, start_time, end_time, stretch, data, 
                     samplerate,filetype='wav',filename_str='Events'):
    sf.write('sound_output/'+filename_str+'_'+probe.upper()+'_dBphidt_'+
             start_time.strftime("%Y%m%d")+'_'+end_time.strftime("%Y%m%d")+'_paulstretch'+
             str(stretch)+'.'+filetype, data, samplerate)