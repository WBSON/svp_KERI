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
import time
import os
import pvsim
import pv_profiles
import script
from multiprocessing.reduction import reduce_handle
from multiprocessing.reduction import rebuild_handle
#from multiprocessing.reduction import reduce_ctype

EN_50530_CURVE = 'EN 50530 CURVE'

STATUS_PROFILE_RUNNING = 64
STATUS_PROFILE_PAUSED = 128
STATUS_PROFILE_IN_PROGRESS = STATUS_PROFILE_RUNNING + STATUS_PROFILE_PAUSED

global tempconn
tempconn=None

class ChromaPVError(Exception):
    pass

class ChromaPV(object):

    def __init__(self,
                 comm='VISA',
                 visa_path="C:/Program Files (x86)/IVI Foundation/VISA/WinNT/agvisa/agbin/visa32.dll",
                 visa_device="GPIB0::12::INSTR", baud_rate=115200):	#wanbin
        self.rm = None
        self.conn = None
        self.comm = comm
        self.visa_device = visa_device
        self.visa_path = visa_path
        self.baud_rate=baud_rate	#wanbin
        self.open()

    def _query(self, cmd_str):
        """
        Performs an SCPI Querry
        :param cmd_str:
        :return:
        """
        try:
            if self.conn is None:
                raise ChromaPVError('GPIB connection not open')
            print cmd_str
            return self.conn.query(cmd_str)

        except Exception, e:
            raise ChromaPVError(str(e))

    def query(self, cmd_str):
        return self._query(cmd_str)

    def open(self):

        #Open the communications resources associated with the PV simulator.

        if self.comm == 'Serial':
            ''' Config according to th SyCore manual
                Baudrate:   9600 B/s
                Databit:    8
                Stopbit:    1
                Parity:     no
                Handshake:  none
                use CR at the end of a command
            '''
            raise NotImplementedError('The driver for serial connection (RS232/RS485) is not implemented yet. ' +
                                      'Please use VISA which supports also serial connection')
        elif self.comm == 'GPIB':
            raise NotImplementedError('The driver for plain GPIB is not implemented yet. ' +
                                      'Please use VISA which supports also GPIB devices')
        elif self.comm == 'VISA':
            try:
                # sys.path.append(os.path.normpath(self.visa_path))
                import visa
                #self.rm = visa.ResourceManager("C:/Program Files (x86)/IVI Foundation/VISA/WinNT/agvisa/agbin/visa32.dll")
                self.rm = visa.ResourceManager() #wanbin
                self.conn = self.rm.open_resource(self.visa_device)
                self.conn.baud_rate=self.baud_rate	#wanbin
                # the default pyvisa write termination is '\r\n' which does not work with the SPS
                self.conn.write_termination = "\n"
                self.conn.read_termination="\n" #wanbin
                #global tempconn
                tempconn=self.conn
                time.sleep(1)

            except Exception, e:
                raise ChromaPVError('Cannot open VISA connection to %s\n\t%s' % (self.visa_device,str(e)))
        else:
            raise ValueError('Unknown communication type %s. Use Serial, GPIB or VISA' % self.comm)

    def cmd(self, cmd_str):
        try:
            self._cmd(cmd_str)
        except Exception, e:
            raise ChromaPVError(str(e))

    def _cmd(self, cmd_str):
        '''
        try:
            temp=self.conn.session()       # if conn is closed, then error raise
        except Exception, e:
            self.open()                     # reopen
        '''
        try:
            print cmd_str
            self.conn.write(cmd_str)
        except Exception, e:
            raise

    def info(self):
        return self._query('*IDN?')

    def reset(self):
        self._query('*RST')
        time.sleep(5)

    def power_on(self):
        print self.output_status()
        if self.output_status().strip() == 'OFF':
            if self.output_mode().strip != 'SAS':
                self.cmd('OUTPut:MODE SAS')
             
            self.cmd ('OUTPut ON')
            #self.cmd ('CONFigure:OUTPut ON')

    def power_off(self):
        self.cmd ('OUTPut OFF')
        self.cmd ('CONFigure:OUTPut OFF')

    def close(self):
        """
        Close any open communications resources associated with the grid
        simulator.
        """

        if self.comm == 'Serial':
            raise NotImplementedError('The driver for serial connection (RS232/RS485) is not implemented yet')
        elif self.comm == 'GPIB':
            raise NotImplementedError('The driver for plain GPIB is not implemented yet.')
        elif self.comm == 'VISA':
            try:
                if self.rm is not None:
                    if self.conn is not None:
                        self.conn.close()
                    self.rm.close()

                time.sleep(1)
            except Exception, e:
                raise pvsim.PVSimError(str(e))
        else:
            raise ValueError('Unknown communication type %s. Use Serial, GPIB or VISA' % self.comm)

    def curve(self, filename=None, voc=None, isc=None, pmp=None, vmp=None, form_factor=None,
              beta_v=None, beta_p=None, kfactor_voltage=None, kfactor_irradiance=None):
        # Chroma, load curve from file and send to Chroma
        # All must be set ISC, VOC, VMP, IMP
        if filename is not None:
            self.cmd('CURVe:READFile "%s"\r' % (filename))
        elif voc is not None and isc is not None and pmp is not None and vmp is not None:
            imp = str(float(pmp)/float(vmp))
            self.cmd('SAS:VOC %s\r' % (voc))
            self.cmd('SAS:ISC %s\r' % (isc))
            self.cmd('SAS:VMP %s\r' % (vmp))
            self.cmd('SAS:IMP %s\r' % (imp))
        else: raise NotImplementedError('All four parameters VOC, ISC, VMP, and PMP must be provided')

    def irradiance_set(self, irradiance, voc, isc, pmp, vmp):
        self.irradiance = irradiance
        #Since Chroma doesn't support it, we need to calcalate new parameters based on irradiance
        print 'in irradiance'
        isc = isc * irradiance/1000
        pmp = pmp * irradiance/1000

        if self.output_status().strip() == 'ON':
            #self.power_off()   #wanbin
            self.curve(None, voc, isc, pmp, vmp)
            #self.power_on()    #wanbin
            self.cmd('TRIG')    #wanbin
        else:
            self.curve(None, voc, isc, pmp, vmp)
    def status(self):
        return str(self._query('*STB?'))

    def output_status(self):
        return str(self._query('OUTPut:STATus?'))

    def output_mode(self):
        return str(self._query('OUTPut:MODE?'))

    def profile_load(self, profile_name,voc, isc, pmp, vmp, ts): #wanbin
        self.ts=ts
        self.profile=pv_profiles.profiles[profile_name]
        h=0
        self.proc=script.Process(target=profile_thread,args=(self.profile,voc,isc,pmp,vmp,self.ts,))
        return
        #raise NotImplementedError ("Profiles are not currently implemented on Chroma PV Simulator")
    
    
    def profile_start(self):    #wanbin
        self.conn.close()
        self.proc.start()
        #self.proc.join()

    def profiles_get(self): #wanbin
        return pv_profiles.profiles


def profile_thread(profile,voc=0, isc=0, pmp=0, vmp=0,ts=None,):    #wanbin
    import visa
    #self.rm = visa.ResourceManager("C:/Program Files (x86)/IVI Foundation/VISA/WinNT/agvisa/agbin/visa32.dll")
    rm = visa.ResourceManager() #wanbin
    conn = rm.open_resource('ASRL5::INSTR')
    conn.baud_rate=115200	#wanbin    
    conn.write_termination = '\n'
    conn.read_termination='\n' #wanbin
    
    ts.log_debug("%s" % conn)
    conn.write('SAS:VOC %0.2f\r' % float(voc))
    conn.write('SAS:VMP %0.2f\r' % float(vmp))
    
    T=1
    ts.sleep(float(profile[0][0])/T)
    ts.log_debug(profile[0][1])
    conn.write('SAS:ISC %0.2f\r' % (float(isc)*profile[0][1]/1000))
    conn.write('SAS:IMP %0.2f\r' % (float(pmp)/float(vmp)*profile[0][1]/1000))
    conn.write('TRIG')
        
    for i in range(1,len(profile)):
        ts.sleep(float(profile[i][0]-profile[i-1][0])/T)
        ts.log_debug(profile[i][1])
        conn.write('SAS:ISC %0.2f\r' % (float(isc)*profile[i][1]/1000))
        conn.write('SAS:IMP %0.2f\r' % (float(pmp)/float(vmp)*profile[i][1]/1000))
        conn.write('TRIG')

    ts.log_debug("done")
    conn.close()
    return

def profile_get(): #wanbin
    return pv_profiles.profiles



if __name__ == "__main__":
    #sas = ChromaPV()
    a=profile_get()
    profile_thread(a['STPsIrradiance'],10,2,10,12)
    
