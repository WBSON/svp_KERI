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

import os
import pvsim

chroma_info = {
    'name': os.path.splitext(os.path.basename(__file__))[0],
    'mode': 'Chroma'
}

def pvsim_info():
    return chroma_info

def params(info, group_name):
    gname = lambda name: group_name + '.' + name
    pname = lambda name: group_name + '.' + GROUP_NAME + '.' + name
    mode = chroma_info['mode']
    info.param_add_value(gname('mode'), mode)
    info.param_group(gname(GROUP_NAME), label='%s Parameters' % mode,
                     active=gname('mode'),  active_value=mode, glob=True)
    info.param(pname('comm'), label='Communications Interface', default='VISA',
               values=['Serial', 'GPIB', 'VISA'])
    info.param(pname('serial_port'), label='Serial Port',
              active=pname('comm'), active_value=['Serial'], default='com1')
    info.param(pname('gpib_bus_address'), label='GPIB Bus Address',
               active=pname('comm'), active_value=['GPIB'], default=6)
    info.param(pname('gpib_board'), label='GPIB Board Number',
               active=pname('comm'), active_value=['GPIB'], default=0)
    #info.param(pname('visa_device'), label='VISA Device String', active=pname('comm'),
    #           active_value=['VISA'], default='GPIB0::6::INSTR')
    #info.param(pname('visa_device'), label='VISA Device String', active=pname('comm'),
    #           active_value=['VISA'], default='USB0::0x0A69::0x084B::S02000000541::INSTR')   #wanbin
    info.param(pname('visa_device'), label='VISA Device String', active=pname('comm'),
               active_value=['VISA'], default='TCPIP::192.168.0.11::2101::SOCKET')   #wanbin


    info.param(pname('baud_rate'), label='Baud Rate', active=pname('comm'),
               active_value=['VISA'], default=115200) # wanbin 
    info.param(pname('visa_path'), label='VISA Driver Path', active=pname('comm'),
               active_value=['VISA'], default="C:/Program Files (x86)/IVI Foundation/VISA/WinNT/agvisa/agbin/visa32.dll")
    info.param(pname('pmp'), label='MPP Power (W)', default=4995.97)
    info.param(pname('vmp'), label='MPP Voltage (V)', default=448.27)
    info.param(pname('voc'), label='Open Circuit Voltage (V)', default=562.02)
    info.param(pname('isc'), label='Short Circuit Current (I)', default=12.346)

GROUP_NAME = 'chroma'




class PVSim(pvsim.PVSim):
    def _param_value(self, name):	#wanbin # from pvsim_terrasas.py
        return self.ts.param_value(self.group_name + '.' + GROUP_NAME + '.' + name)

    def __init__(self, ts, group_name):
        pvsim.PVSim.__init__(self, ts, group_name)

        self.ts = ts
        self.sas = None
        self.comm = self._param_value('comm')
        self.serial_port = self._param_value('serial_port')	

        self.gpib_bus_address = self._param_value('gpib_bus_address')
        self.gpib_board = self._param_value('gpib_board')

        self.visa_device = self._param_value('visa_device')
      # self.visa_path = ts._param_value('test.visa_path')
        self.visa_path = self._param_value('visa_path') #wanbin
        self.baud_rate= self._param_value('baud_rate')	#wanbin

        self.pmp = self._param_value('pmp')
        self.vmp = self._param_value('vmp')
        self.voc = self._param_value('voc')
        self.isc = self._param_value('isc')
        self.irraciance = 1000
		
		#wanbin
        ts.log_debug("comm : %s" % self.comm)
        ts.log_debug("visa path : %s" % self.visa_path)
        ts.log_debug("baud rate : %s" % self.baud_rate)


        try:
            import chromapv

            #self.ipaddr = ts._param_value('ipaddr')
            self.pmp = self._param_value('pmp')
            self.vmp = self._param_value('vmp')
            self.irr_start = self._param_value('irr_start')
            self.profile_name = None
            #self.ts.log('Initializing PV Simulator with Pmp = %d and Vmp = %d.' % (self.pmp, self.vmp))
            #wanbin
            
            self.sas = chromapv.ChromaPV(self.comm, self.visa_path, self.visa_device,self.baud_rate)	#wanbin

            # re-add EN50530 curve with active parameters
            #self.sas.curve_en50530(pmp=self.pmp, vmp=self.vmp)  #wanbin

        except Exception:
            if self.sas is not None:
                self.sas.close()
            raise

    def close(self):
        if self.sas is not None:
            self.sas.close()
            self.sas = None

    def info(self):
        return self.sas.info()


    def power_set(self, power):
        if self.sas is not None:
            # spread across active channels
            count = 1
            if count > 1:
                power = power/count
            if power > self.pmp:
                self.ts.log_warning('Requested power > Pmp so irradiance will be > 1000 W/m^2)')
            # convert to irradiance for now
            irradiance = (power * 1000)/self.pmp
            self.irradiance_set(irradiance=irradiance)
                    # self.ts.log('TerraSAS power output changed to %0.2f on channel %d.' % (power, c))
        else:
            raise pvsim.PVSimError('Power was not changed.')

    def irradiance_set(self, irradiance=1000):
        if self.sas is not None:
            self.irradiance = irradiance
            self.sas.irradiance_set(self.irradiance, self.voc, self.isc, self.pmp, self.vmp)
            self.ts.log('chroma irradiance changed to %0.2f' % (irradiance))
        else:
            raise pvsim.PVSimError('Irradiance was not changed.')

    def profile_load(self, profile_name):	#wanbin
        if profile_name != 'None' and profile_name is not None:
            self.ts.log('Loading irradiance profile %s' % profile_name)
            self.profile_name = profile_name
            
            profiles = self.sas.profiles_get()
            if profile_name in profiles:
                self.proc=self.sas.profile_load(profile_name, self.voc, self.isc, self.pmp, self.vmp, self.ts)
                # pass params
                
            else:
                self.ts.log('No irradiance profile loaded')	
            '''
            if profile_name not in profiles:
                self.sas.profile(profile_name)

            if self.sas is not None:
                c = self.channel
                if c is not None:
                    channel = self.sas.channels[c]
                    channel.profile_set(profile_name)
                    self.ts.log('chroma Profile is configured.')
                else:
                    raise pvsim.PVSimError('chroma Profile could not be configured.')
            else:
                raise pvsim.PVSimError('chroma Profile was not changed.')
			'''
        else:
            self.ts.log('No irradiance profile loaded')
			
    def power_on(self):
        if self.sas is not None:
            self.sas.power_on()
            #self.ts.log('chroma channel %d turned on' % c)
            self.ts.log('chroma channel turned on')
        else:
            raise pvsim.PVSimError('Not initialized')

    def power_off(self):     #wanbin
        if self.sas is not None:
            self.sas.power_off()
            #self.ts.log('chroma channel %d turned on' % c)
            self.ts.log('chroma channel turned off')
        else:
            raise pvsim.PVSimError('Not initialized')



    def profile_start(self):
        if self.sas is not None:
            profile_name = self.profile_name
            if profile_name != 'None' and profile_name is not None:
                self.sas.profile_start()
                self.ts.log('Starting PV profile')
            else:
                raise pvsim.PVSimError('Simulation channel not specified')
        else:
            raise pvsim.PVSimError('PV Sim not initialized')

# Execute only when run as a script
# Test Code Only
if __name__ == "__main__":
    pass
