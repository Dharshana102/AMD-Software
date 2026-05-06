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
                { id: 'time', label: 'Time (0-60 sec)', type: 'number', min: 0, max: 60, placeholder: 'Time' }
              ],
              'CRB': [
                { id: 'time', label: 'Time (0-60 sec)', type: 'number', min: 0, max: 60, placeholder: 'Time' }
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
            type: 'buttons',
            items: [
              { label: 'Hotplug', cls: 'btn-success', action: 'disp_hotplug' },
              { label: 'Unplug', cls: 'btn-danger', action: 'disp_unplug' }
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
                { id: 'time', label: 'Time (0-60 sec)', type: 'number', min: 0, max: 60, placeholder: 'Time' }
              ],
              'CRB': [
                { id: 'angle', label: 'Angle (0-180°)', type: 'number', min: 0, max: 180, placeholder: 'Angle' },
                { id: 'time', label: 'Time (0-60 sec)', type: 'number', min: 0, max: 60, placeholder: 'Time' }
              ]
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
        id: 'hdmi_audio',
        title: 'HDMI Audio Hotplug / Unplug',
        desc: 'Simulate HDMI audio connection and disconnection.',
        controls: [
          {
            type: 'buttons',
            items: [
              { label: 'Hotplug', cls: 'btn-success', action: 'hdmi_audio_plug' },
              { label: 'Unplug', cls: 'btn-danger', action: 'hdmi_audio_unplug' }
            ]
          }
        ]
      },
      {
        id: 'usb_audio',
        title: 'USB Audio Hotplug / Unplug',
        desc: 'Simulate USB audio device connection and disconnection.',
        controls: [
          {
            type: 'buttons',
            items: [
              { label: 'Hotplug', cls: 'btn-success', action: 'usb_audio_plug' },
              { label: 'Unplug', cls: 'btn-danger', action: 'usb_audio_unplug' }
            ]
          }
        ]
      },
      {
        id: 'jack_audio',
        title: '3.5 mm Audio Jack Hotplug / Unplug',
        desc: 'Simulate 3.5 mm audio jack insertion and removal.',
        controls: [
          {
            type: 'buttons',
            items: [
              { label: 'Hotplug', cls: 'btn-success', action: 'jack_audio_plug' },
              { label: 'Unplug', cls: 'btn-danger', action: 'jack_audio_unplug' }
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
            type: 'toggle',
            id: 'bt_recv_toggle',
            label: 'Receiver',
            action_on: 'bt_recv_on',
            action_off: 'bt_recv_off'
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
              { label: 'Pair', cls: 'btn-primary', action: 'bt_pair' },
              { label: 'Connect', cls: 'btn-success', action: 'bt_connect' },
              { label: 'Disconnect', cls: 'btn-danger', action: 'bt_disconnect' }
            ]
          }
        ]
      },
      {
        id: 'onboard_speaker',
        title: 'Onboard Speaker',
        desc: 'Test onboard speaker output.',
        controls: [
          {
            type: 'toggle',
            id: 'spk_toggle',
            label: 'Speaker',
            action_on: 'spk_on',
            action_off: 'spk_off'
          },
          {
            type: 'buttons',
            items: [
              { label: 'Play Test Tone', cls: 'btn-primary', action: 'spk_test' }
            ]
          }
        ]
      },
      {
        id: 'dmic',
        title: 'Onboard Microphone Array (DMIC)',
        desc: 'Test the digital microphone array input.',
        controls: [
          {
            type: 'toggle',
            id: 'dmic_toggle',
            label: 'DMIC',
            action_on: 'dmic_on',
            action_off: 'dmic_off'
          },
          {
            type: 'buttons',
            items: [
              { label: 'Record Sample', cls: 'btn-primary', action: 'dmic_record' }
            ]
          }
        ]
      }
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
            id: 'camera_params',
            label: 'Parameters',
            fields: {
              'default': [
                { id: 'angle', label: 'Angle (0-180°)', type: 'number', min: 0, max: 180, placeholder: 'Angle' },
                { id: 'time', label: 'Time (0-60 sec)', type: 'number', min: 0, max: 60, placeholder: 'Time' }
              ]
            }
          },
          {
            type: 'buttons',
            items: [
              { label: 'Open', cls: 'btn-success', action: 'cam_open' },
              { label: 'Close', cls: 'btn-danger', action: 'cam_close' },
              { label: 'Step +', cls: 'btn-primary', action: 'cam_step_fwd' },
              { label: 'Step −', cls: 'btn-secondary', action: 'cam_step_rev' }
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
            type: 'buttons',
            items: [
              { label: 'Red', cls: 'btn-danger', action: 'rgb_red' },
              { label: 'Green', cls: 'btn-success', action: 'rgb_green' },
              { label: 'Blue', cls: 'btn-primary', action: 'rgb_blue' },
              { label: 'White', cls: 'btn-secondary', action: 'rgb_white' },
              { label: 'OFF', cls: 'btn-danger', action: 'rgb_off' }
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
                { id: 'time', label: 'Time (0-60 sec)', type: 'number', min: 0, max: 60, placeholder: 'Time' }
              ],
              'CRB': [
                { id: 'angle', label: 'Angle (0-180°)', type: 'number', min: 0, max: 180, placeholder: 'Angle' },
                { id: 'time', label: 'Time (0-60 sec)', type: 'number', min: 0, max: 60, placeholder: 'Time' }
              ]
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
        id: 'module1_info',
        title: 'Module 1',
        desc: 'Network information for Module 1',
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
        title: 'Module 2',
        desc: 'Network information for Module 2',
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
      }
    ]
  }
];