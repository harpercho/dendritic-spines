
# Model Equations
print('executed model_eqs')
eqs_main = '''
Im = gl * (El - v) : amp/meter**2
I_long = gDN * (v_neck - v) : amp (point current)
gDN : siemens
v_neck : volt
'''

eqs_neck = '''
Im = gl * (El - v) + gK * (VK - v): amp/meter**2
I_long = gND * (v_dend - v) + gNH * (v_head - v) : amp (point current)
dgK/dt = - gK/tauK
gND : siemens
gNH : siemens
v_dend : volt
v_head : volt
'''

eqs_head = '''
Im = gl * (El - v) + g_AMPA * (E_AMPA - v) + g_NMDA * B_N * (E_NMDA - v): amp/meter**2
I_long = gHN * (v_neck - v) : amp (point current)
g_AMPA : siemens/meter**2
g_NMDA : siemens/meter**2
B_N = 1/(1 + MG_conc/3.57*np.exp(-v/16.13))
gHN : siemens
v_neck : volt
'''
