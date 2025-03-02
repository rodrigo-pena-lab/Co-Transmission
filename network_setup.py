import brian2 as b2
from neuron_models import create_neuron_group
import logging
from termcolor import colored
from brian2.units import mV
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def setup_multi_scale_network(params, model_type='conductance_based'):
    N_E = params['N_E']
    N_I = params['N_I']
    N = N_E + N_I
    epsilon = params['epsilon']
    C_E = int(epsilon * N_E)

    neuron_params = {
        'V_th': params['V_th'],
        'V_reset': params['V_reset'],
        'tau_m': params['tau_m'],
        't_ref': params['t_ref'],
        'V_rest': params['V_reset'],
        'E_e': params['E_e'],
        'E_i': params['E_i'],
        'C_m': params['C_m'],
    }

    if model_type == 'conductance_based':
        neuron_params['tau_d_i'] = params['tau_d_i']
        neuron_params['tau_d_e'] = params['tau_d_e']
        
        neurons = create_neuron_group(N, 'conductance_based', **neuron_params)
        neurons.v = 'V_reset + rand() * (V_th - V_reset)'

        J_e = params['J_e_value'] * params['J_e_unit']
        J_i = params['J_i_value'] * params['J_i_unit']

        exc_synapses = b2.Synapses(neurons[:N_E], neurons, 
                                   on_pre=f'g_e += {params["J_e_value"]}*{params["J_e_unit"]}')
        exc_synapses.connect(p=epsilon)

        inh_synapses = b2.Synapses(neurons[N_E:], neurons, 
                                   on_pre=f'g_i += {params["J_i_value"]}*{params["J_i_unit"]}')
        inh_synapses.connect(p=epsilon)

        external_input = b2.PoissonInput(neurons[:N_E], 'g_e', C_E, params['nu_ext'], weight=5*J_e)

        return neurons, exc_synapses, inh_synapses, external_input
    elif model_type == 'cotransmission':

        neuron_params['tau_d_e'] = params['tau_d_e']
        neuron_params['tau_d_e_c'] = params['tau_d_e_c']
        neuron_params['tau_d_i_c'] = params['tau_d_i_c']

        neurons = create_neuron_group(N, 'cotransmission', **neuron_params)
        neurons.v = 'V_reset + rand() * (V_th - V_reset)'

        J_e = params['J_e_value'] * params['J_e_unit']
        J_i = params['J_i_value'] * params['J_i_unit']

        exc_synapses = b2.Synapses(neurons[:N_E], neurons, 
                                   on_pre=f'g_e += {params["J_e_value"]}*{params["J_e_unit"]}')
        exc_synapses.connect(p=epsilon)

        inh_synapses = b2.Synapses(neurons[N_E:], neurons, 
                                   on_pre=f'g_i_c += {params["J_i_value"]}*{params["J_i_unit"]}')
        inh_synapses.connect(p=epsilon)

        inh_synapses_cotrans = b2.Synapses(neurons[N_E:], neurons, 
                                   on_pre=f'g_e_c += {params["J_e_value"]}*{params["J_e_unit"]}')
        inh_synapses_cotrans.connect(p=epsilon)

        external_input = b2.PoissonInput(neurons[:N_E], 'g_e', C_E, params['nu_ext'], weight=5*J_e)

        return neurons, exc_synapses, inh_synapses, external_input, inh_synapses_cotrans

