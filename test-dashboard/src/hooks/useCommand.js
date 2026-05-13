import { useCallback } from 'react';
import { useDashboard } from '../context/DashboardContext';

// Command mapping based on Excel sheet
const COMMAND_MAP = {
  // MODULE - 1 (POWER)
  'power_on': (params) => {
    const target = params.power_target || 'Laptop OEM';
    const powerParams = params.power_params || {};
    
    if (target === 'Laptop OEM') {
      const angle = powerParams.angle || 45;
      const time = powerParams.time || 5;
      return `PWR_ON_LT:${angle},${time};`;
    } else if (target === 'Desktop') {
      const time = powerParams.time || 5;
      return `PWR_ON_DT:${time};`;
    } else if (target === 'CRB') {
      const time = powerParams.time || 5;
      return `PWR_ON_CRB:${time};`;
    }
  },
  
  'power_off': (params) => {
    const target = params.power_target || 'Laptop OEM';
    const powerParams = params.power_params || {};
    
    if (target === 'Laptop OEM') {
      const angle = powerParams.angle || 45;
      const time = powerParams.time || 5;
      return `PWR_OFF_LT:${angle},${time};`;
    } else if (target === 'Desktop') {
      const time = powerParams.time || 5;
      return `PWR_OFF_DT:${time};`;
    } else if (target === 'CRB') {
      const time = powerParams.time || 5;
      return `PWR_OFF_CRB:${time};`;
    }
  },
  
  'power_restart': (params) => {
    const target = params.power_target || 'Laptop OEM';
    const powerParams = params.power_params || {};
    
    if (target === 'Laptop OEM') {
      const angle = powerParams.angle || 45;
      return `PWR_RST_LT:${angle};`;
    } else if (target === 'Desktop') {
      const time = powerParams.time || 16;
      return `PWR_RST_DT:${time};`;
    } else if (target === 'CRB') {
      const time = powerParams.time || 14;
      return `PWR_RST_CRB:${time};`;
    }
  },
  
  'power_read_status': (params) => {
    const target = params.pstat_target || 'Laptop';
    if (target === 'Laptop') return 'PWR_STATUS_LT;';
    if (target === 'Desktop') return 'PWR_STATUS_DT;';
    if (target === 'CRB') return 'PWR_STATUS_CRB;';
  },
  
  'ac_on': () => 'PWR_ON_AC;',
  'ac_off': () => 'PWR_OFF_AC;',
  'ac_read_status': () => 'PWR_STATUS_AC;',
  
  // MODULE - 2 (DISPLAY)
  'disp_hotplug': (params) => {
    const port = params.hp_port || 'DP';
    const number = params.hp_number || '1';
    
    if (port === 'DP') return `HOTPLUG_DP_${number};`;
    if (port === 'HDMI') return `HOTPLUG_HDMI_${number};`;
    if (port === 'USB4') return `HOTPLUG_USB4_${number};`;
  },
  
  'disp_unplug': (params) => {
    const port = params.hp_port || 'DP';
    const number = params.hp_number || '1';
    
    if (port === 'DP') return `UNPLUG_DP_${number};`;
    if (port === 'HDMI') return `UNPLUG_HDMI_${number};`;
    if (port === 'USB4') return `UNPLUG_USB4_${number};`;
  },
  
  'check_plug_status': (params) => {
    const port = params.plug_status_port || 'DP_1';
    return `PLUG_STATUS_${port};`;
  },
  
  'sense_rgb': () => 'READ_DISP_PROP;',
  'sense_ctemp': () => 'READ_DISP_PROP;',
  'sense_lum': () => 'READ_DISP_PROP;',
  'sense_all': () => 'READ_DISP_PROP;',
  
  'lid_open': (params) => {
    const target = params.lid_target || 'Laptop OEM';
    const lidParams = params.lid_params || {};
    
    if (target === 'Laptop OEM') {
      const angle = lidParams.angle || 45;
      return `LID_OPEN_LT:${angle};`;
    } else if (target === 'CRB') {
      return 'LID_OPEN_CRB;';
    }
  },
  
  'lid_close': (params) => {
    const target = params.lid_target || 'Laptop OEM';
    const lidParams = params.lid_params || {};
    
    if (target === 'Laptop OEM') {
      const angle = lidParams.angle || 50;
      const time = lidParams.time || 170;
      return `LID_CLOSE_LT:${angle},${time};`;
    } else if (target === 'CRB') {
      return 'LID_CLOSE_CRB;';
    }
  },
  
  'lid_read_status': () => 'READ_DISP_PROP;',
  
  // MODULE - 3 (Camera/ISP)
  // MODULE - 3 (Camera/ISP)
// MODULE - 3 (Camera/ISP) - Updated stepper commands
'stepper_cw': (params) => {
  const stepperParams = params.stepper_params || {};
  const steps = stepperParams.steps || 1024;
  const speed = stepperParams.speed || 100;
  return `STEPPER_MOVE:CW,${steps},${speed};`;
},
 
'stepper_ccw': (params) => {
  const stepperParams = params.stepper_params || {};
  const steps = stepperParams.steps || 1024;
  const speed = stepperParams.speed || 100;
  return `STEPPER_MOVE:CCW,${steps},${speed};`;
},
 
'stepper_stop': () => 'STEPPER_STOP;',
  
  'rgb_set': (params) => {
    const ledId = params.led_id || '1';
    const rgbParams = params.rgb_params || {};
    const r = rgbParams.r || 255;
    const g = rgbParams.g || 255;
    const b = rgbParams.b || 255;
    return `RGB_SET:${ledId},${r},${g},${b};`;
  },
  
  'rgb_off': (params) => {
    const ledId = params.led_id || '1';
    return `RGB_OFF:${ledId};`;
  },
  
  'ambient_read': () => 'LIGHT_READ;',
  
  'isp_sense_rgb': () => 'READ_DISP_PROP;',
  'isp_sense_ctemp': () => 'READ_DISP_PROP;',
  'isp_sense_lum': () => 'READ_DISP_PROP;',
  'isp_sense_all': () => 'READ_DISP_PROP;',
  
  'isp_lid_open': (params) => {
    const target = params.isp_lid_target || 'Laptop OEM';
    const lidParams = params.isp_lid_params || {};
    
    if (target === 'Laptop OEM') {
      const angle = lidParams.angle || 45;
      return `LID_OPEN_LT:${angle};`;
    } else if (target === 'CRB') {
      return 'LID_OPEN_CRB;';
    }
  },
  
  'isp_lid_close': (params) => {
    const target = params.isp_lid_target || 'Laptop OEM';
    const lidParams = params.isp_lid_params || {};
    
    if (target === 'Laptop OEM') {
      const angle = lidParams.angle || 50;
      const time = lidParams.time || 170;
      return `LID_CLOSE_LT:${angle},${time};`;
    } else if (target === 'CRB') {
      return 'LID_CLOSE_CRB;';
    }
  },
  
  'isp_lid_read_status': () => 'READ_DISP_PROP;',
  
  // MODULE - 4 (Audio)
  'audio_hotplug': (params) => {
    const port = params.audio_port || '3.5_MM';
    return `HOTPLUG_${port};`;
  },
  
  'audio_unplug': (params) => {
    const port = params.audio_port || '3.5_MM';
    return `UNPLUG_${port};`;
  },
  
  'bt_on': () => 'TURN_ON_BT;',
  'bt_off': () => 'TURN_OFF_BT;',
  
  'bt_pairing_mode': () => 'EN_BT_PARING_MODE;',
  'bt_connect': () => 'BT_CONNECT;',
  'bt_disconnect': () => 'BT_DISCONNECT;',
  'bt_status': () => 'BT_CONNECTION_STATUS;',
  
  'bt_change_name': (params) => {
    const btNameParams = params.bt_name_params || {};
    const name = btNameParams.bt_name || 'PARADISE';
    return `CHANGE_BT_NAME:${name};`;
  },
  
  'bt_vol_up': () => 'BT_AUDIO_UP;',
  'bt_vol_down': () => 'BT_AUDIO_DOWN;',
  'bt_mute': () => 'BT_AUDIO_MUTE;',
  'bt_unmute': () => 'BT_AUDIO_UNMUTE;',
  'bt_play': () => 'BT_PLAY;',
  'bt_pause': () => 'BT_PAUSE;',
  'bt_next': () => 'BT_NEXT;',
  'bt_previous': () => 'BT_PREVIOUS;',
  
  'spk_on': () => 'BT_AUDIO_UNMUTE;',
  'spk_off': () => 'BT_AUDIO_MUTE;',
  'spk_test': () => 'BT_PLAY;',
  
  'dmic_on': () => 'BT_AUDIO_UNMUTE;',
  'dmic_off': () => 'BT_AUDIO_MUTE;',
  'dmic_record': () => 'BT_CONNECTION_STATUS;',
  
  // MODULE - 0 & 1 (Combinational / HOST)
  'check_module_status': (params) => {
    const moduleNum = params.module_number || '1';
    return `MODULE_STATUS:${moduleNum};`;
  },
  
  'module1_refresh': () => 'MODULE_STATUS:1;',
  'module2_refresh': () => 'MODULE_STATUS:2;',
  
  'pwron_with_delay': (params) => {
    const comboParams = params.combo_params || {};
    const delayTime = comboParams.delay_time || 600;
    return `PWRON_WITH_DELAY:${delayTime};`;
  },
  
  'close_lid_pwron': () => 'CLOSE_LID_PWRON_SUT;',
  
  'hotplug_all': () => 'HOTPLUG_ALL_PORTS;',
  
  'unplug_all': () => 'UNPLUG_ALL_PORTS;',
};

// Expected responses based on Excel sheet
const RESPONSE_MAP = {
  'PWR_ON_LT': 'LAPTOP POWERED ON',
  'PWR_ON_DT': 'DESKTOP POWERED ON',
  'PWR_ON_CRB': 'CRB POWERED ON',
  'PWR_STATUS_LT': 'LAPTOP POWERED: ON, 12.5V',
  'PWR_STATUS_DT': 'DESKTOP POWERED: OFF, 0V',
  'PWR_STATUS_CRB': 'CRB POWERED: ON, 5V',
  'PWR_OFF_LT': 'LAPTOP POWERED OFF',
  'PWR_OFF_DT': 'DESKTOP POWERED OFF',
  'PWR_OFF_CRB': 'CRB POWERED OFF',
  'PWR_RST_LT': 'LAPTOP RESTARTED',
  'PWR_RST_DT': 'DT RESTARTED',
  'PWR_RST_CRB': 'CRB RESTARTED',
  'PWR_ON_AC': 'AC ON',
  'PWR_OFF_AC': 'AC OFF',
  'PWR_STATUS_AC': 'AC: ON, 230V',
  'MODULE_STATUS': 'ONLINE',
  'HOTPLUG_DP_1': 'DP_1 HOTPLUGED',
  'HOTPLUG_DP_2': 'DP_2 HOTPLUGED',
  'HOTPLUG_HDMI_1': 'HDMI_1 HOTPLUGED',
  'HOTPLUG_HDMI_2': 'HDMI_2 HOTPLUGED',
  'HOTPLUG_USB4_1': 'USB4_1 HOTPLUGED',
  'HOTPLUG_USB4_2': 'USB4_2 HOTPLUGED',
  'UNPLUG_DP_1': 'DP_1 UNPLUGED',
  'UNPLUG_DP_2': 'DP_2 UNPLUGED',
  'UNPLUG_HDMI_1': 'HDMI_1 UNPLUGED',
  'UNPLUG_HDMI_2': 'HDMI_2 UNPLUGED',
  'UNPLUG_USB4_1': 'USB4_1 UNPLUGED',
  'UNPLUG_USB4_2': 'USB4_2 UNPLUGED',
  'PLUG_STATUS_DP_1': 'DP_1: PLUGED',
  'PLUG_STATUS_DP_2': 'DP_2: PLUGED',
  'PLUG_STATUS_HDMI_1': 'HDMI_1: PLUGED',
  'PLUG_STATUS_HDMI_2': 'HDMI_2: PLUGED',
  'PLUG_STATUS_USB_1': 'USB_1: PLUGED',
  'PLUG_STATUS_USB_2': 'USB_2: PLUGED',
  'LID_OPEN_LT': 'LID_OPENED',
  'LID_CLOSE_LT': 'LID_CLOSED',
  'LID_OPEN_CRB': 'LID_OPENED',
  'LID_CLOSE_CRB': 'LID_CLOSED',
  'READ_DISP_PROP': 'R:128, G: 200, B: 150, C: 75, LUX: 500, CT: 6500, K INT: 1500',
  'RGB_SET': 'RGB LED SET',
  'RGB_OFF': 'RGB LED OFF',
  'STEPPER_MOVE': 'STEPPER MOVED',
  'STEPPER_STOP': 'STEPPER STOPPED',
  'LIGHT_READ': 'ADC: 512, LUX: 400',
  'HOTPLUG_3.5_MM': '3.5_MM_HOTPLUGGED',
  'UNPLUG_3.5_MM': '3.5_MM_UNPLUGGED',
  'HOTPLUG_USB_A': 'USB_A_HOTPLUGGED',
  'UNPLUG_USB_A': 'USB_A_UNPLUGGED',
  'HOTPLUG_USB_C': 'USB_C_HOTPLUGGED',
  'UNPLUG_USB_C': 'USB_C_UNPLUGGED',
  'HOTPLUG_HDMI': 'HDMI_HOTPLUGGED',
  'UNPLUG_HDMI': 'HDMI_UNPLUGGED',
  'TURN_ON_BT': 'BT_TURNED_ON',
  'TURN_OFF_BT': 'BT_TURNED_OFF',
  'CHANGE_BT_NAME': 'BT_NAME_CHANGED',
  'EN_BT_PARING_MODE': 'BT_PARING_EN',
  'BT_CONNECT': 'BT_CONNECTED',
  'BT_DISCONNECT': 'BT_DISCONNECTED',
  'BT_CONNECTION_STATUS': 'CONNECTED',
  'BT_AUDIO_UP': 'BT_AUDIO_VOL-INCREACED',
  'BT_AUDIO_DOWN': 'BT_AUDIO_VOL-REDUCED',
  'BT_AUDIO_MUTE': 'BT_AUDIO_MUTE',
  'BT_AUDIO_UNMUTE': 'BT_AUDIO_UNMUTE',
  'BT_PLAY': 'BT_PLAYED',
  'BT_PAUSE': 'BT_PAUSEED',
  'BT_NEXT': 'BT_NEXTED',
  'BT_PREVIOUS': 'BT_PREVIOUSED',
  'PWRON_WITH_DELAY': 'POWERED_ON_WITH_DELAY',
  'CLOSE_LID_PWRON_SUT': 'CLOSED_LID_PWRDON_SUT',
  'HOTPLUG_ALL_PORTS': 'HOTPLUGED_ALL_PORTS',
  'UNPLUG_ALL_PORTS': 'UNPLUGED_ALL_PORTS',
};

export function useCommand() {
  const { addLog } = useDashboard();

  const sendCommand = useCallback(async (action, params = {}) => {
    // Get the command string from the mapping
    const commandBuilder = COMMAND_MAP[action];
    
    if (!commandBuilder) {
      addLog(`TX → Unknown action: ${action}`, 'warn');
      return { ok: false, error: 'Unknown command' };
    }
    
    const command = typeof commandBuilder === 'function' ? commandBuilder(params) : commandBuilder;
    
    // Extract command name for response lookup (remove arguments)
    const commandName = command.split(':')[0].replace(';', '');
    
    addLog(`TX → ${command}`, 'info');
    
    // Simulate sending command and receiving response
    return new Promise(resolve => {
      const delay = 300 + Math.random() * 700; // 300-1000ms delay
      setTimeout(() => {
        const ok = Math.random() > 0.1; // 90% success rate
        if (ok) {
          // Get response from mapping or generate generic response
          let response = RESPONSE_MAP[commandName];
          
          if (!response) {
            response = 'OK:1';
          }
          
          addLog(`RX ← ${response}`, 'ok');
          resolve({ ok: true, data: response, command });
        } else {
          const errorResponse = 'ERR:TIMEOUT';
          addLog(`RX ← ${errorResponse}`, 'err');
          resolve({ ok: false, error: 'timeout', command });
        }
      }, delay);
    });
  }, [addLog]);

  // Function to get command string for display
  const getCommandString = useCallback((action, params = {}) => {
    const commandBuilder = COMMAND_MAP[action];
    if (!commandBuilder) return '';
    return typeof commandBuilder === 'function' ? commandBuilder(params) : commandBuilder;
  }, []);

  return { sendCommand, getCommandString };
}