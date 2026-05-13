import {
  Plus,
  Minus,
  VolumeX,
  Volume2,
  Play,
  Pause,
  SkipBack,
  SkipForward
} from "lucide-react";
export const MODULES = [
  {
    id: 'power',
    name: 'Power',
    icon: 'Power',
    color: '#f39c12',
    sub: 'Power control & status',
    features: [
      {
        id: 'power_onoff',
        title: 'Power ON / OFF / Restart',
        desc: 'Control power state for Laptop OEM, Desktop, and CRB platforms.',
        controls: [
          {
            type: 'select',
            id: 'power_target',
            label: 'Target',
            options: ['Laptop OEM', 'Desktop', 'CRB']
          },
          {
            type: 'dynamic',
            id: 'power_params',
            label: 'Parameters',
            fields: {
              'Laptop OEM': [
                { id: 'angle', label: 'Angle (0-180°)', type: 'number', min: 0, max: 180, placeholder: 'Angle' },
                { id: 'time', label: 'Time (0-60 sec)', type: 'number', min: 0, max: 60, placeholder: 'Time' }
              ],
              'Desktop': [
                { id: 'time', label: 'Time (0-5 sec)', type: 'number', min: 0, max: 5, placeholder: 'Time' }
              ],
              'CRB': [
                { id: 'time', label: 'Time (0-5 sec)', type: 'number', min: 0, max: 5, placeholder: 'Time' }
              ]
            }
          },
          {
            type: 'buttons',
            items: [
              { label: 'Power ON', cls: 'btn-success', action: 'power_on' },
              { label: 'Power OFF', cls: 'btn-danger', action: 'power_off' },
              { label: 'Restart', cls: 'btn-warning', action: 'power_restart' }
            ]
          }
        ]
      },
      {
        id: 'power_status',
        title: 'Power Status Detection',
        desc: 'Detect current power state of Laptop, Desktop, and CRB.',
        controls: [
          {
            type: 'select',
            id: 'pstat_target',
            label: 'Target',
            options: ['Laptop', 'Desktop', 'CRB']
          },
          {
            type: 'buttons',
            items: [
              { label: 'Read Status', cls: 'btn-primary', action: 'power_read_status' }
            ]
          }
        ]
      },
      {
        id: 'ac_power',
        title: 'AC Power ON / OFF Control',
        desc: 'Control AC power supply to the system.',
        controls: [
          {
            type: 'buttons',
            items: [
              { label: 'AC ON', cls: 'btn-success', action: 'ac_on' },
              { label: 'AC OFF', cls: 'btn-danger', action: 'ac_off' }
            ]
          }
        ]
      },
      {
        id: 'ac_status',
        title: 'AC Power Status Detection',
        desc: 'Read current AC power supply status.',
        controls: [
          {
            type: 'buttons',
            items: [
              { label: 'Read AC Status', cls: 'btn-primary', action: 'ac_read_status' }
            ]
          }
        ]
      }
    ]
  },
  {
    id: 'display',
    name: 'Display',
    icon: 'Monitor',
    color: '#4f8cff',
    sub: 'Display & lid control',
    features: [
      {
        id: 'disp_hotplug',
        title: 'Display Hotplug / Unplug',
        desc: 'Simulate display hotplug and unplug events for DP, HDMI, USB4.',
        controls: [
          {
            type: 'select',
            id: 'hp_port',
            label: 'Interface',
            options: ['DP', 'HDMI', 'USB4']
          },
          {
            type: 'select',
            id: 'hp_number',
            label: 'Port Number',
            options: ['1', '2']
          },
          {
            type: 'buttons',
            items: [
              { label: 'Hotplug', cls: 'btn-success', action: 'disp_hotplug' },
              { label: 'Unplug', cls: 'btn-danger', action: 'disp_unplug' }
            ]
          }
        ]
      },
      {
        id: 'plug_status',
        title: 'Display Plug Status',
        desc: 'Check plug status for all display ports.',
        controls: [
          {
            type: 'select',
            id: 'plug_status_port',
            label: 'Interface',
            options: ['DP_1', 'DP_2', 'HDMI_1', 'HDMI_2', 'USB_1', 'USB_2']
          },
          {
            type: 'buttons',
            items: [
              { label: 'Check Status', cls: 'btn-primary', action: 'check_plug_status' }
            ]
          }
        ]
      },
      {
        id: 'disp_sense',
        title: 'Display Color & Brightness Sensing',
        desc: 'Read RGB, Color Temperature, and Luminance from the display sensor.',
        controls: [
          {
            type: 'buttons',
            items: [
              { label: 'Read RGB', cls: 'btn-primary', action: 'sense_rgb' },
              { label: 'Read Color Temp', cls: 'btn-primary', action: 'sense_ctemp' },
              { label: 'Read Luminance', cls: 'btn-primary', action: 'sense_lum' },
              { label: 'Read All', cls: 'btn-warning', action: 'sense_all' }
            ]
          }
        ]
      },
      {
        id: 'lid_ctrl',
        title: 'Lid Open / Close',
        desc: 'Control lid servo for Laptop OEM and CRB.',
        controls: [
          {
            type: 'select',
            id: 'lid_target',
            label: 'Target',
            options: ['Laptop OEM', 'CRB']
          },
          {
            type: 'dynamic',
            id: 'lid_params',
            label: 'Parameters',
            fields: {
              'Laptop OEM': [
                { id: 'angle', label: 'Angle (0-180°)', type: 'number', min: 0, max: 180, placeholder: 'Angle' },
                { id: 'time', label: 'Time (0-300 sec)', type: 'number', min: 0, max: 300, placeholder: 'Time' }
              ],
              'CRB': []
            }
          },
          {
            type: 'buttons',
            items: [
              { label: 'Open Lid', cls: 'btn-success', action: 'lid_open' },
              { label: 'Close Lid', cls: 'btn-danger', action: 'lid_close' }
            ]
          }
        ]
      },
      {
        id: 'lid_status',
        title: 'Lid Status Detection',
        desc: 'Detect current lid state for Laptop OEM and CRB.',
        controls: [
          {
            type: 'select',
            id: 'lstat_target',
            label: 'Target',
            options: ['Laptop OEM', 'CRB']
          },
          {
            type: 'buttons',
            items: [
              { label: 'Read Lid Status', cls: 'btn-primary', action: 'lid_read_status' }
            ]
          }
        ]
      }
    ]
  },
  {
    id: 'audio',
    name: 'Audio',
    icon: 'Volume2',
    color: '#9b59b6',
    sub: 'Audio hotplug & Bluetooth',
    features: [
      {
        id: 'audio_hotplug',
        title: 'Audio Hotplug / Unplug',
        desc: 'Simulate audio device connection and disconnection for 3.5mm, USB-A, USB-C, HDMI.',
        controls: [
          {
            type: 'select',
            id: 'audio_port',
            label: 'Audio Port',
            options: ['3.5_MM', 'USB_A', 'USB_C', 'HDMI']
          },
          {
            type: 'buttons',
            items: [
              { label: 'Hotplug', cls: 'btn-success', action: 'audio_hotplug' },
              { label: 'Unplug', cls: 'btn-danger', action: 'audio_unplug' }
            ]
          }
        ]
      },
      {
        id: 'bt_receiver',
        title: 'Bluetooth Receiver',
        desc: 'Control the Bluetooth receiver module.',
        controls: [
          {
            type: 'buttons',
            items: [
              { label: 'Turn ON BT', cls: 'btn-success', action: 'bt_on' },
              { label: 'Turn OFF BT', cls: 'btn-danger', action: 'bt_off' }
            ]
          }
        ]
      },
      {
        id: 'bt_control',
        title: 'Bluetooth Pairing, Connection & Disconnection',
        desc: 'Manage Bluetooth pairing, connection, and disconnection.',
        controls: [
          {
            type: 'buttons',
            items: [
              { label: 'Enable Pairing', cls: 'btn-primary', action: 'bt_pairing_mode' },
              { label: 'Connect', cls: 'btn-success', action: 'bt_connect' },
              { label: 'Disconnect', cls: 'btn-danger', action: 'bt_disconnect' },
              { label: 'Status', cls: 'btn-secondary', action: 'bt_status' }
            ]
          }
        ]
      },
      {
        id: 'bt_name',
        title: 'Bluetooth Name Change',
        desc: 'Change the Bluetooth device name.',
        controls: [
          {
            type: 'dynamic',
            id: 'bt_name_params',
            label: 'Bluetooth Name',
            fields: {
              'default': [
                { id: 'bt_name', label: 'New Name', type: 'text', min: 0, max: 100, placeholder: 'Enter BT name' }
              ]
            }
          },
          {
            type: 'buttons',
            items: [
              { label: 'Change Name', cls: 'btn-primary', action: 'bt_change_name' }
            ]
          }
        ]
      },
      {
  id: 'bt_audio_control',
  title: 'Bluetooth Audio Control',
  desc: 'Control audio playback and volume via Bluetooth.',
  controls: [
    {
      type: 'buttons',
      items: [
        {
          icon: Plus,
          cls: 'btn-primary btn-icon',
          action: 'bt_vol_up',
          title: 'Volume Up'
        },
        {
          icon: Minus,
          cls: 'btn-primary btn-icon',
          action: 'bt_vol_down',
          title: 'Volume Down'
        },
        {
          icon: VolumeX,
          activeIcon: Volume2,
          cls: 'btn-warning btn-icon',
          action: 'bt_mute',
          activeAction: 'bt_unmute',
          toggle: true,
          stateKey: 'isMuted',
          title: 'Mute / Unmute'
        },
        {
          icon: Play,
          activeIcon: Pause,
          cls: 'btn-success btn-icon',
          action: 'bt_play',
          activeAction: 'bt_pause',
          toggle: true,
          stateKey: 'isPlaying',
          title: 'Play / Pause'
        },
        {
          icon: SkipBack,
          cls: 'btn-primary btn-icon',
          action: 'bt_previous',
          title: 'Previous'
        },
        {
          icon: SkipForward,
          cls: 'btn-primary btn-icon',
          action: 'bt_next',
          title: 'Next'
        }
      ]
    }
  ]
      },
      // {
      //   id: 'dmic',
      //   title: 'Onboard Microphone Array (DMIC)',
      //   desc: 'Test the digital microphone array input.',
      //   controls: [
      //     {
      //       type: 'toggle',
      //       id: 'dmic_toggle',
      //       label: 'DMIC',
      //       action_on: 'dmic_on',
      //       action_off: 'dmic_off'
      //     },
      //     {
      //       type: 'buttons',
      //       items: [
      //         { label: 'Record Sample', cls: 'btn-primary', action: 'dmic_record' }
      //       ]
      //     }
      //   ]
      // }
    ]
  },
  {
    id: 'isp',
    name: 'ISP',
    icon: 'Camera',
    color: '#1abc9c',
    sub: 'Camera, Display & Lid Control',
    features: [
      {
        id: 'camera_stepper',
  title: 'Camera Actuation (Stepper Motor)',
  desc: 'Control stepper motor for camera positioning.',
  controls: [
    {
      type: 'dynamic',
      id: 'stepper_params',
      label: 'Parameters',
      fields: {
        'default': [
          { id: 'steps', label: 'Steps (0-2048)', type: 'number', min: 0, max: 2048, placeholder: 'Steps' },
          { id: 'speed', label: 'Speed (ms)', type: 'number', min: 10, max: 1000, placeholder: 'Speed ms' }
        ]
      }
    },
    {
      type: 'buttons',
      items: [
        { label: 'CW Move', cls: 'btn-success', action: 'stepper_cw' },
        { label: 'CCW Move', cls: 'btn-danger', action: 'stepper_ccw' },
        { label: 'Stop', cls: 'btn-warning', action: 'stepper_stop' }
      ]
    }
  ]
      },
      {
        id: 'rgb_illum',
        title: 'RGB Illumination Control',
        desc: 'Control RGB LED illumination for ISP testing.',
        controls: [
          {
            type: 'select',
            id: 'led_id',
            label: 'LED ID',
            options: ['1', '2']
          },
          {
            type: 'dynamic',
            id: 'rgb_params',
            label: 'RGB Values',
            fields: {
              '1': [
                { id: 'r', label: 'R (0-255)', type: 'number', min: 0, max: 255, placeholder: 'R' },
                { id: 'g', label: 'G (0-255)', type: 'number', min: 0, max: 255, placeholder: 'G' },
                { id: 'b', label: 'B (0-255)', type: 'number', min: 0, max: 255, placeholder: 'B' }
              ],
              '2': [
                { id: 'r', label: 'R (0-255)', type: 'number', min: 0, max: 255, placeholder: 'R' },
                { id: 'g', label: 'G (0-255)', type: 'number', min: 0, max: 255, placeholder: 'G' },
                { id: 'b', label: 'B (0-255)', type: 'number', min: 0, max: 255, placeholder: 'B' }
              ]
            }
          },
          {
            type: 'buttons',
            items: [
              { label: 'Set RGB', cls: 'btn-primary', action: 'rgb_set' },
              { label: 'Turn OFF', cls: 'btn-danger', action: 'rgb_off' }
            ]
          }
        ]
      },
      {
        id: 'ambient_light',
        title: 'Ambient Light Level Detection',
        desc: 'Read ambient light sensor levels.',
        controls: [
          {
            type: 'buttons',
            items: [
              { label: 'Read Light Level', cls: 'btn-primary', action: 'ambient_read' }
            ]
          }
        ]
      },
      {
        id: 'isp_disp_sense',
        title: 'Display Color & Brightness Sensing',
        desc: 'Read RGB, Color Temperature, and Luminance from the display sensor.',
        controls: [
          {
            type: 'buttons',
            items: [
              { label: 'Read RGB', cls: 'btn-primary', action: 'isp_sense_rgb' },
              { label: 'Read Color Temp', cls: 'btn-primary', action: 'isp_sense_ctemp' },
              { label: 'Read Luminance', cls: 'btn-primary', action: 'isp_sense_lum' },
              { label: 'Read All', cls: 'btn-warning', action: 'isp_sense_all' }
            ]
          }
        ]
      },
      {
        id: 'isp_lid_ctrl',
        title: 'Lid Open / Close',
        desc: 'Control lid servo for Laptop OEM and CRB.',
        controls: [
          {
            type: 'select',
            id: 'isp_lid_target',
            label: 'Target',
            options: ['Laptop OEM', 'CRB']
          },
          {
            type: 'dynamic',
            id: 'isp_lid_params',
            label: 'Parameters',
            fields: {
              'Laptop OEM': [
                { id: 'angle', label: 'Angle (0-180°)', type: 'number', min: 0, max: 180, placeholder: 'Angle' },
                { id: 'time', label: 'Time (0-300 sec)', type: 'number', min: 0, max: 300, placeholder: 'Time' }
              ],
              'CRB': [
                { id: 'angle', label: 'Angle (0-180°)', type: 'number', min: 0, max: 180, placeholder: 'Angle' },
                { id: 'time', label: 'Time (0-300 sec)', type: 'number', min: 0, max: 300, placeholder: 'Time'}
              ],
            }
          },
          {
            type: 'buttons',
            items: [
              { label: 'Open Lid', cls: 'btn-success', action: 'isp_lid_open' },
              { label: 'Close Lid', cls: 'btn-danger', action: 'isp_lid_close' }
            ]
          }
        ]
      },
      {
        id: 'isp_lid_status',
        title: 'Lid Status Detection',
        desc: 'Detect current lid state for Laptop OEM and CRB.',
        controls: [
          {
            type: 'select',
            id: 'isp_lstat_target',
            label: 'Target',
            options: ['Laptop OEM', 'CRB']
          },
          {
            type: 'buttons',
            items: [
              { label: 'Read Lid Status', cls: 'btn-primary', action: 'isp_lid_read_status' }
            ]
          }
        ]
      }
    ]
  },
  {
    id: 'host',
    name: 'HOST',
    icon: 'Server',
    color: '#e67e22',
    sub: 'KVM capture & BIOS',
    features: [
      {
        id: 'module_status',
        title: 'Module Status Check',
        desc: 'Check status of all modules (1-4).',
        controls: [
          {
            type: 'select',
            id: 'module_number',
            label: 'Module Number',
            options: ['1', '2', '3', '4']
          },
          {
            type: 'buttons',
            items: [
              { label: 'Check Status', cls: 'btn-primary', action: 'check_module_status' }
            ]
          }
        ]
      },
      {
        id: 'module1_info',
        title: 'RPI',
        desc: 'Network information for Rpi',
        controls: [
          {
            type: 'info',
            id: 'module1_ip',
            fields: [
              { label: 'IP Address', value: '192.168.1.100', id: 'ip' },
              { label: 'MAC Address', value: '00:1A:2B:3C:4D:5E', id: 'mac' }
            ]
          },
          {
            type: 'buttons',
            items: [
              { label: 'Refresh', cls: 'btn-primary', action: 'module1_refresh' },
              { label: 'Copy IP', cls: 'btn-secondary', action: 'module1_copy_ip' },
              { label: 'Copy MAC', cls: 'btn-secondary', action: 'module1_copy_mac' }
            ]
          }
        ]
      },
      {
        id: 'module2_info',
        title: 'STM32MP257F',
        desc: 'Network information for STM32MP257F',
        controls: [
          {
            type: 'info',
            id: 'module2_ip',
            fields: [
              { label: 'IP Address', value: '192.168.1.101', id: 'ip' },
              { label: 'MAC Address', value: '00:1A:2B:3C:4D:5F', id: 'mac' }
            ]
          },
          {
            type: 'buttons',
            items: [
              { label: 'Refresh', cls: 'btn-primary', action: 'module2_refresh' },
              { label: 'Copy IP', cls: 'btn-secondary', action: 'module2_copy_ip' },
              { label: 'Copy MAC', cls: 'btn-secondary', action: 'module2_copy_mac' }
            ]
          }
        ]
      },
      // {
      //   id: 'combinational_commands',
      //   title: 'Combinational Commands',
      //   desc: 'Execute combined power and display commands.',
      //   controls: [
      //     {
      //       type: 'dynamic',
      //       id: 'combo_params',
      //       label: 'Parameters',
      //       fields: {
      //         'default': [
      //           { id: 'delay_time', label: 'Delay (0-1000 sec)', type: 'number', min: 0, max: 1000, placeholder: 'Time' }
      //         ]
      //       }
      //     },
      //     {
      //       type: 'buttons',
      //       items: [
      //         { label: 'Power ON with Delay', cls: 'btn-primary', action: 'pwron_with_delay' },
      //         { label: 'Close Lid & Power ON', cls: 'btn-warning', action: 'close_lid_pwron' },
      //         { label: 'Hotplug All Ports', cls: 'btn-success', action: 'hotplug_all' },
      //         { label: 'Unplug All Ports', cls: 'btn-danger', action: 'unplug_all' }
      //       ]
      //     }
      //   ]
      // }
    ]
  }
];