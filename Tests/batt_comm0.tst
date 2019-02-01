<scriptConfig name="batt_comm0" script="battsim_comm">
  <params>
    <param name="battsim.Chroma.ESR" type="float">0.01</param>
    <param name="battsim.Chroma.VOLP" type="int">5</param>
    <param name="battsim.Chroma.BVL" type="int">10</param>
    <param name="battsim.Chroma.BVH" type="int">38</param>
    <param name="battsim.Chroma.VOH" type="float">40.1</param>
    <param name="battsim.Chroma.INIT_SOC" type="int">50</param>
    <param name="battsim.Chroma.CAP" type="int">70</param>
    <param name="battsim.Chroma.DCR_C" type="string">0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.1</param>
    <param name="battsim.Chroma.DCR_D" type="string">0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.1</param>
    <param name="battsim.Chroma.SOC" type="string">100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0</param>
    <param name="battsim.Chroma.OCV" type="string">41.1,40,39.1,38.3,37.6,36.9,36.6,36.3,35.9,35,33.8</param>
    <param name="battsim.mode" type="string">Chroma</param>
    <param name="battsim.Chroma.visa_device" type="string">TCPIP::192.168.1.100::60000::SOCKET</param>
    <param name="battsim.Chroma.comm" type="string">VISA</param>
  </params>
</scriptConfig>
