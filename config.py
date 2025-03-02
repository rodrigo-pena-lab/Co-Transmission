import brian2 as b2

# Multi-scale dynamics parameters
multi_scale_common_params = {
    "N_E": 2000,
    "N_I": 500,
    "epsilon": 0.2,

    "J_e_value": 0.1,
    "J_e_unit": b2.nS,
    "J_i_value": 0.8,
    "J_i_unit": b2.nS,

    "tau_m": 20 * b2.ms,
    "tau_m_e": 20 * b2.ms,
    "tau_m_i": 10 * b2.ms,

    "V_th": -50 * b2.mV,
    "V_reset": -60 * b2.mV,

    "t_ref": 2 * b2.ms,  
    "t_ref_e": 2 * b2.ms, 
    "t_ref_i": 1 * b2.ms,  

    "E_e": 0 * b2.mV,  
    "E_i": -70 * b2.mV, 
    "C_m": 200 * b2.pF,  
    "nu_ext": 2.5 * b2.Hz,
    "sim_time": 2000 * b2.ms,
}