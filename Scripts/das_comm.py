"""
Copyright (c) 2017, Sandia National Labs and SunSpec Alliance
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.

Redistributions in binary form must reproduce the above copyright notice, this
list of conditions and the following disclaimer in the documentation and/or
other materials provided with the distribution.

Neither the names of the Sandia National Labs and SunSpec Alliance nor the names of its
contributors may be used to endorse or promote products derived from
this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Questions can be directed to support@sunspec.org
"""

import sys
import os
import math
import time
import traceback
import script

#from svpelab import pvsim
from svpelab import das

def test_run():

    result = script.RESULT_FAIL
    #pv = None
    
    try:
        sc_points = ['PF_TARGET', 'PF_MAX', 'PF_MIN']
        daq=das.das_init(ts, sc_points=sc_points)
        ts.log('DAS device: %s' % daq.info())
        
        ts.log('Running capture 1')
        #daq.data_capture(True)          #???   # wanbin # really need it?
        times=[]
        start=time.time()
        times.append(start)
        for i in range(1):
                times.append(time.time())
                #ts.log(time.time()-start)
                a=daq.data_capture_read()
                #ts.log('current data: %s' % daq.data_capture_read())
                
        for item in times:
                ts.log(item-start)
        
        
        daq.waveform_capture(True)
        ts.log(time.time())
        ds=daq.waveform_capture_dataset()
        ts.log(time.time())
        #ds.to_csv(ts.result_file_path("ts.csv"))
        #ts.result_file("ts.csv")
        
        ts.log(daq.waveform_status())
        daq.waveform_capture(False)
        
        
        '''
        ds = daq.data_capture_dataset()
        # save captured data set to capture file in SVP result directory
        filename = 'capture_1.csv'
        ds.to_csv(ts.result_file_path(filename))
        ts.result_file(filename)            
        '''
        # bug 1 : first capture is not saved in the csv file
        # bug 2 : WT3000 works but shows header error? on the display 
        
        #ts.sleep(0.2)
        
        #ts.log('current data: %s' % daq.data_capture_read())
        
        #ts.log_debug(daq.data_capture_read())
        #ts.log_debug(sc_points)
        #inst.query(":INPut?")
        #for i in range(5):
        #    ts.sleep(1)
        
        #daq.data_capture(False)                # wanbin # really need it?
        
        '''
        # initialize pv simulation
        batt = battsim.battsim_init(ts)
        ts.log(batt.info())
        batt.open()
        batt.power_on()
               
        for i in range(10):
            vol=batt.get_volt()
            if batt.is_error():
                ts.log_error("error")
                batt.close()
                return result
            #ts.log(success)
            ts.log("%s" % vol)
            ts.sleep(1)
            
            
        batt.power_off()
        '''
        result = script.RESULT_PASS

    except script.ScriptFail, e:
        reason = str(e)
        if reason:
            ts.log_error(reason)
    finally:
        None
        #if daq is not None:
        #    daq.close()
    
    return result


def run(test_script):
    try:
        global ts
        ts= test_script
        rc = 0
        result = script.RESULT_COMPLETE

        ts.log_debug('')
        ts.log_debug('**************  Starting %s  **************' % (ts.config_name()))
        ts.log_debug('Script: %s %s' % (ts.name, ts.info.version))
        ts.log_active_params()

        result = test_run()

        ts.result(result)
        if result == script.RESULT_FAIL:
            rc = 1

    except Exception, e:
        ts.log_error('Test script exception: %s' % traceback.format_exc())
        rc = 1

    sys.exit(rc)

info = script.ScriptInfo(name=os.path.basename(__file__), run=run, version='1.0.0')

#PV simulator
das.params(info)

def script_info():
    return info


if __name__ == "__main__":


    # stand alone invocation
    config_file = None
    if len(sys.argv) > 1:
        config_file = sys.argv[1]

    test_script = script.Script(info=script_info(), config_file=config_file)

    run(test_script)



