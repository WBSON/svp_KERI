<scriptConfig name="bbb" script="battsim_comm">
  <params>
    <param name="battsim.Chroma.ESR" type="float">0.015</param>
    <param name="battsim.Chroma.BVL" type="int">1</param>
    <param name="battsim.Chroma.VOLP" type="int">1</param>
    <param name="battsim.Chroma.INIT_SOC" type="int">50</param>
    <param name="battsim.Chroma.BVH" type="int">51</param>
    <param name="battsim.Chroma.VOH" type="float">55.0</param>
    <param name="battsim.Chroma.CAP" type="int">100</param>
    <param name="battsim.Chroma.DCR_C" type="string">0.001,0.001,0.001,0.01</param>
    <param name="battsim.Chroma.DCR_D" type="string">0.01,0.01,0.01,0.1</param>
    <param name="battsim.Chroma.SOC" type="string">100,80,30,10</param>
    <param name="battsim.Chroma.OCV" type="string">50,40,15,5</param>
    <param name="battsim.mode" type="string">Chroma</param>
    <param name="battsim.Chroma.visa_device" type="string">TCPIP::192.168.1.100::60000::SOCKET</param>
    <param name="battsim.Chroma.comm" type="string">VISA</param>
  </params>
</scriptConfig>
