<scriptConfig name="sa9_UV1" script="SA9_volt_ride_through">
  <params>
    <param name="eut.v_msa" type="float">0.0</param>
    <param name="eut.t_msa" type="float">0.0</param>
    <param name="vrt.n_r" type="int">1</param>
    <param name="der.sma.slave_id" type="int">3</param>
    <param name="eut.vrt_t_dwell" type="int">3</param>
    <param name="gridsim.chroma.phases" type="int">3</param>
    <param name="pvsim.chroma.isc" type="float">12.346</param>
    <param name="vrt.t_hold" type="float">20.0</param>
    <param name="gridsim.chroma.freq" type="float">60.0</param>
    <param name="gridsim.chroma.i_max" type="float">75.0</param>
    <param name="vrt.v_test" type="float">87.0</param>
    <param name="vrt.v_grid_max" type="float">100.0</param>
    <param name="vrt.v_grid_min" type="float">100.0</param>
    <param name="eut.v_nom" type="float">277.0</param>
    <param name="gridsim.chroma.v_max" type="float">299.0</param>
    <param name="gridsim.chroma.v_range" type="int">300</param>
    <param name="pvsim.chroma.vmp" type="float">448.27</param>
    <param name="das_das_rms.wt3000.sample_interval" type="int">500</param>
    <param name="das_das_wf.wt3000.sample_interval" type="int">500</param>
    <param name="der.sma.ipport" type="int">502</param>
    <param name="pvsim.chroma.voc" type="float">562.02</param>
    <param name="pvsim.chroma.pmp" type="float">4995.97</param>
    <param name="eut.p_rated" type="int">5000</param>
    <param name="das_das_rms.wt3000.baud_rate" type="int">38400</param>
    <param name="das_das_wf.wt3000.baud_rate" type="int">38400</param>
    <param name="pvsim.chroma.baud_rate" type="int">115200</param>
    <param name="der.sma.gridguard" type="string">3980494444</param>
    <param name="das_das_wf.wt3000.chan_1_label" type="string">1</param>
    <param name="das_das_rms.wt3000.chan_1_label" type="string">1</param>
    <param name="der.sma.ipaddr" type="string">192.168.0.170</param>
    <param name="gridsim.chroma.baud_rate" type="string">19200</param>
    <param name="das_das_rms.wt3000.chan_2_label" type="string">2</param>
    <param name="das_das_wf.wt3000.chan_2_label" type="string">2</param>
    <param name="das_das_rms.wt3000.chan_3_label" type="string">3</param>
    <param name="das_das_wf.wt3000.chan_3_label" type="string">3</param>
    <param name="eut.phases" type="string">3-Phase 3-Wire</param>
    <param name="das_das_wf.wt3000.chan_2" type="string">AC</param>
    <param name="das_das_rms.wt3000.chan_3" type="string">AC</param>
    <param name="das_das_wf.wt3000.chan_3" type="string">AC</param>
    <param name="das_das_wf.wt3000.chan_1" type="string">AC</param>
    <param name="das_das_rms.wt3000.chan_2" type="string">AC</param>
    <param name="das_das_rms.wt3000.chan_1" type="string">AC</param>
    <param name="das_das_rms.wt3000.visa_id" type="string">ASRL1::INSTR</param>
    <param name="das_das_wf.wt3000.visa_id" type="string">ASRL1::INSTR</param>
    <param name="pvsim.chroma.visa_path" type="string">C:/Program Files (x86)/IVI Foundation/VISA/WinNT/agvisa/agbin/visa32.dll</param>
    <param name="gridsim.chroma.visa_path" type="string">C:/Program Files (x86)/IVI Foundation/VISA/WinNT/agvisa/agbin/visa32.dll</param>
    <param name="pvsim.mode" type="string">Chroma</param>
    <param name="gridsim.mode" type="string">Chroma</param>
    <param name="das_das_wf.wt3000.chan_4" type="string">DC</param>
    <param name="das_das_rms.wt3000.chan_4" type="string">DC</param>
    <param name="loadsim.mode" type="string">Disabled</param>
    <param name="vrt.phase_3" type="string">Disabled</param>
    <param name="vrt.phase_2" type="string">Disabled</param>
    <param name="vrt.p_20" type="string">Disabled</param>
    <param name="vrt.p_100" type="string">Enabled</param>
    <param name="vrt.phase_1" type="string">Enabled</param>
    <param name="vrt.phase_1_2_3" type="string">Enabled</param>
    <param name="gridsim.auto_config" type="string">Enabled</param>
    <param name="vrt.mode" type="string">Mandatory Operation</param>
    <param name="das_das_wf.wt3000.chan_4_label" type="string">None</param>
    <param name="das_das_rms.wt3000.chan_4_label" type="string">None</param>
    <param name="der.mode" type="string">SMA</param>
    <param name="gridsim.chroma.visa_device" type="string">TCPIP::192.168.0.10::2101::SOCKET</param>
    <param name="pvsim.chroma.visa_device" type="string">TCPIP::192.168.0.11::2101::SOCKET</param>
    <param name="der.sma.confgridguard" type="string">True</param>
    <param name="gridsim.chroma.comm" type="string">VISA</param>
    <param name="das_das_wf.wt3000.comm" type="string">VISA</param>
    <param name="das_das_rms.wt3000.comm" type="string">VISA</param>
    <param name="pvsim.chroma.comm" type="string">VISA</param>
    <param name="das_das_rms.mode" type="string">Yokogawa WT3000</param>
    <param name="das_das_wf.mode" type="string">Yokogawa WT3000</param>
    <param name="vrt.test_label" type="string">vrt</param>
  </params>
</scriptConfig>
