import React from 'react';
import './Controls.css';
 
function ToggleControl({ control, isOn, onToggle }) {
  return (
<div className="toggle-row" style={{ marginBottom: '10px' }}>
<div
        className={`toggle ${isOn ? 'on' : ''}`}
        id={control.id}
        onClick={() => onToggle(control.id, control.action_on, control.action_off)}
></div>
<span className="toggle-label">
        {control.label}: {isOn ? 'ON' : 'OFF'}
</span>
</div>
  );
}
 
export default ToggleControl;
