<scriptConfig name="sa12_0" script="SA12_power_factor">
  <params>
    <param name="eut.pf_min_cap" type="float">-0.8</param>
    <param name="eut.pf_msa" type="float">0.02</param>
    <param name="eut.pf_min_ind" type="float">0.8</param>
    <param name="spf.n_r" type="int">1</param>
    <param name="eut.pf_settling_time" type="int">2</param>
    <param name="der.sma.slave_id" type="int">3</param>
    <param name="pvsim.chroma.isc" type="float">12.346</param>
    <param name="pvsim.chroma.vmp" type="float">448.27</param>
    <param name="der.sma.ipport" type="int">502</param>
    <param name="pvsim.chroma.voc" type="float">562.02</param>
    <param name="das.wt3000.sample_interval" type="int">1000</param>
    <param name="pvsim.chroma.pmp" type="float">4995.97</param>
    <param name="eut.p_rated" type="int">5000</param>
    <param name="das.wt3000.baud_rate" type="int">38400</param>
    <param name="pvsim.chroma.baud_rate" type="int">115200</param>
    <param name="der.sma.gridguard" type="string">3980494444</param>
    <param name="das.wt3000.chan_1_label" type="string">1</param>
    <param name="der.sma.ipaddr" type="string">192.168.0.170</param>
    <param name="das.wt3000.chan_2_label" type="string">2</param>
    <param name="das.wt3000.chan_3_label" type="string">3</param>
    <param name="eut.phases" type="string">3-Phase 3-Wire</param>
    <param name="das.wt3000.chan_1" type="string">AC</param>
    <param name="das.wt3000.chan_3" type="string">AC</param>
    <param name="das.wt3000.chan_2" type="string">AC</param>
    <param name="das.wt3000.visa_id" type="string">ASRL1::INSTR</param>
    <param name="pvsim.chroma.visa_path" type="string">C:/Program Files (x86)/IVI Foundation/VISA/WinNT/agvisa/agbin/visa32.dll</param>
    <param name="pvsim.mode" type="string">Chroma</param>
    <param name="das.wt3000.chan_4" type="string">DC</param>
    <param name="loadsim.mode" type="string">Disabled</param>
    <param name="gridsim.mode" type="string">Disabled</param>
    <param name="spf.p_20" type="string">Disabled</param>
    <param name="spf.pf_mid_ind" type="string">Disabled</param>
    <param name="spf.p_50" type="string">Disabled</param>
    <param name="spf.pf_mid_cap" type="string">Disabled</param>
    <param name="gridsim.auto_config" type="string">Disabled</param>
    <param name="spf.pf_min_cap" type="string">Enabled</param>
    <param name="spf.pf_min_ind" type="string">Enabled</param>
    <param name="spf.p_100" type="string">Enabled</param>
    <param name="das.wt3000.chan_4_label" type="string">None</param>
    <param name="der.mode" type="string">SMA</param>
    <param name="der.sma.confgridguard" type="string">True</param>
    <param name="pvsim.chroma.visa_device" type="string">USB0::0x0A69::0x084B::S02000000541::INSTR</param>
    <param name="das.wt3000.comm" type="string">VISA</param>
    <param name="pvsim.chroma.comm" type="string">VISA</param>
    <param name="das.mode" type="string">Yokogawa WT3000</param>
  </params>
</scriptConfig>
