import brian2 as b2

def create_neuron_group(N, model_type='cotransmission', **params):
    if model_type == 'cotransmission':
  
        neuron_eqs = '''
        dv/dt = (
        -(v - V_rest) / tau_m + 
            (
                g_e * (E_e - v) +
                g_e_c * (E_e - v) +
                g_i_c * (E_i - v)
            ) / C_m
        ) : volt (unless refractory)

        dg_e/dt = -g_e / tau_d_e : siemens
        
        dg_e_c/dt = -g_e_c / tau_d_e_c : siemens
        dg_i_c/dt = -g_i_c / tau_d_i_c : siemens
        '''

        return b2.NeuronGroup(N, neuron_eqs,
                        threshold='v > V_th',
                        reset='v = V_reset',
                        refractory='t_ref',
                        method='euler',
                        namespace=params)
    elif model_type == 'conductance_based':
  
        neuron_eqs = '''
        dv/dt = (-(v - V_rest) / tau_m + (g_e * (E_e - v) + g_i * (E_i - v)) / C_m) : volt (unless refractory)
        dg_e/dt = -g_e / tau_d_e : siemens
        dg_i/dt = -g_i / tau_d_i : siemens
        '''

        return b2.NeuronGroup(N, neuron_eqs,
                        threshold='v > V_th',
                        reset='v = V_reset',
                        refractory='t_ref',
                        method='euler',
                        namespace=params)
    else:
        raise ValueError(f"Unknown model type: {model_type}")
__all__ = ['create_neuron_group']


