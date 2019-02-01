<scriptConfig name="sa13_0" script="SA13_volt_var">
  <params>
    <param name="srd.vv_k_var_min" type="float">0.0</param>
    <param name="vv.n_r_min" type="int">0</param>
    <param name="eut_vv.var_ramp_max" type="float">0.0</param>
    <param name="vv.n_r_66" type="int">0</param>
    <param name="eut_vv.v_msa" type="float">1.0</param>
    <param name="vv.n_r_100" type="int">1</param>
    <param name="eut_vv.var_msa" type="float">1.0</param>
    <param name="eut_vv.vv_deadband_min" type="float">1.0</param>
    <param name="eut_vv.vv_t_settling" type="float">1.0</param>
    <param name="eut_vv.vv_deadband_max" type="float">1.0</param>
    <param name="srd.vv_segment_point_count" type="int">3</param>
    <param name="der.sma.slave_id" type="int">3</param>
    <param name="gridsim.chroma.phases" type="int">3</param>
    <param name="pvsim.chroma.isc" type="float">12.346</param>
    <param name="srd.vv_p_min_pct" type="float">20.0</param>
    <param name="srd.vv_p_max_pct" type="float">50.0</param>
    <param name="gridsim.chroma.freq" type="float">60.0</param>
    <param name="gridsim.chroma.i_max" type="float">75.0</param>
    <param name="eut_vv.v_min" type="float">244.0</param>
    <param name="eut_vv.v_nom" type="float">277.0</param>
    <param name="eut_vv.v_max" type="float">295.0</param>
    <param name="gridsim.chroma.v_max" type="float">299.0</param>
    <param name="gridsim.chroma.v_range" type="int">300</param>
    <param name="pvsim.chroma.vmp" type="float">448.27</param>
    <param name="das.wt3000.sample_interval" type="int">500</param>
    <param name="der.sma.ipport" type="int">502</param>
    <param name="pvsim.chroma.voc" type="float">562.02</param>
    <param name="eut_vv.k_var_max" type="float">1200.0</param>
    <param name="eut_vv.var_rated" type="float">4000.0</param>
    <param name="eut_vv.p_rated" type="float">4000.0</param>
    <param name="eut_vv.s_rated" type="float">4000.0</param>
    <param name="pvsim.chroma.pmp" type="float">4995.97</param>
    <param name="eut_vv.q_max_under" type="float">12000.0</param>
    <param name="eut_vv.q_max_over" type="float">12000.0</param>
    <param name="das.wt3000.baud_rate" type="int">38400</param>
    <param name="pvsim.chroma.baud_rate" type="int">115200</param>
    <param name="der.sma.gridguard" type="string">3980494444</param>
    <param name="das.wt3000.chan_1_label" type="string">1</param>
    <param name="der.sma.ipaddr" type="string">192.168.0.170</param>
    <param name="gridsim.chroma.baud_rate" type="string">19200</param>
    <param name="das.wt3000.chan_2_label" type="string">2</param>
    <param name="das.wt3000.chan_3_label" type="string">3</param>
    <param name="eut_vv.phases" type="string">3-Phase 3-Wire</param>
    <param name="das.wt3000.chan_1" type="string">AC</param>
    <param name="das.wt3000.chan_3" type="string">AC</param>
    <param name="das.wt3000.chan_2" type="string">AC</param>
    <param name="das.wt3000.visa_id" type="string">ASRL1::INSTR</param>
    <param name="pvsim.chroma.visa_path" type="string">C:/Program Files (x86)/IVI Foundation/VISA/WinNT/agvisa/agbin/visa32.dll</param>
    <param name="gridsim.chroma.visa_path" type="string">C:/Program Files (x86)/IVI Foundation/VISA/WinNT/agvisa/agbin/visa32.dll</param>
    <param name="pvsim.mode" type="string">Chroma</param>
    <param name="gridsim.mode" type="string">Chroma</param>
    <param name="das.wt3000.chan_4" type="string">DC</param>
    <param name="hil.mode" type="string">Disabled</param>
    <param name="vv.pp_active" type="string">Disabled</param>
    <param name="vv.spec_curve" type="string">Disabled</param>
    <param name="vv.test_3" type="string">Disabled</param>
    <param name="vv.test_1" type="string">Disabled</param>
    <param name="gridsim.auto_config" type="string">Disabled</param>
    <param name="vv.pp_reactive" type="string">Enabled</param>
    <param name="vv.test_2" type="string">Enabled</param>
    <param name="das.wt3000.chan_4_label" type="string">None</param>
    <param name="der.mode" type="string">SMA</param>
    <param name="gridsim.chroma.visa_device" type="string">TCPIP::192.168.0.10::2101::SOCKET</param>
    <param name="der.sma.confgridguard" type="string">True</param>
    <param name="pvsim.chroma.visa_device" type="string">USB0::0x0A69::0x084B::S02000000541::INSTR</param>
    <param name="gridsim.chroma.comm" type="string">VISA</param>
    <param name="das.wt3000.comm" type="string">VISA</param>
    <param name="pvsim.chroma.comm" type="string">VISA</param>
    <param name="das.mode" type="string">Yokogawa WT3000</param>
  </params>
</scriptConfig>
