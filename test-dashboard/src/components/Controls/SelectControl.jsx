import React from 'react';
import './Controls.css';
 
function SelectControl({ control, value, onChange }) {
  return (
<div className="select-wrap" style={{ marginBottom: '10px' }}>
<label style={{ fontSize: '.75rem', color: 'var(--text-muted)' }}>
        {control.label}:
</label>
<select
        id={control.id}
        value={value}
        onChange={(e) => onChange(control.id, e.target.value)}
>
        {control.options.map(option => (
<option key={option} value={option}>
            {option}
</option>
        ))}
</select>
</div>
  );
}
 
export default SelectControl; 
