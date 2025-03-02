import brian2 as b2
import numpy as np
from network_setup import setup_multi_scale_network

def run_network_simulation(params, model_type='conductance_based'):
    b2.start_scope()
    b2.defaultclock.dt = 0.1 * b2.ms

    if model_type == "conductance_based":

        neurons, exc_synapses, inh_synapses, external_input = setup_multi_scale_network(params, model_type)

        N_E = params['N_E']
        N_I = params['N_I']

        spike_monitor = b2.SpikeMonitor(neurons[:500])
        rate_monitor_E = b2.PopulationRateMonitor(neurons[:N_E])
        rate_monitor_I = b2.PopulationRateMonitor(neurons[N_E:])
        
        state_monitor = b2.StateMonitor(neurons, ['v', 'g_e',], record=np.random.choice(N_E + N_I, 100, replace=False))
        net = b2.Network(neurons, state_monitor,spike_monitor, rate_monitor_E, rate_monitor_I, exc_synapses, inh_synapses, external_input)

        net.run(params['sim_time'], report='text')
        
        bin_size = 20 * b2.ms

        return {
            'spike_monitor': spike_monitor,
            'rate_monitor_E': rate_monitor_E,
            'rate_monitor_I': rate_monitor_I,
            'state_monitor': state_monitor,
            
        }
    elif model_type == "cotransmission":

        neurons, exc_synapses, inh_synapses, external_input, inh_synapses_cotrans = setup_multi_scale_network(params, model_type) #, 

        N_E = params['N_E']
        N_I = params['N_I']

        spike_monitor = b2.SpikeMonitor(neurons[:500])
        rate_monitor_E = b2.PopulationRateMonitor(neurons[:N_E])
        rate_monitor_I = b2.PopulationRateMonitor(neurons[N_E:])
        
        state_monitor = b2.StateMonitor(neurons, ['v', 'g_e', 'g_i_c'], record=np.random.choice(N_E + N_I, 100, replace=False))
        net = b2.Network(neurons, state_monitor,spike_monitor, rate_monitor_E, rate_monitor_I, exc_synapses, inh_synapses, external_input, inh_synapses_cotrans) #

        net.run(params['sim_time'], report='text')
        
        return {
            'spike_monitor': spike_monitor,
            'rate_monitor_E': rate_monitor_E,
            'rate_monitor_I': rate_monitor_I,
            'state_monitor': state_monitor,

        }


__all__ = ['run_network_simulation']
