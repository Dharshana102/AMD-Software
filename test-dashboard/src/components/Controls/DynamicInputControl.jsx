/*import React from 'react';
import './Controls.css';
 
function DynamicInputControl({ control, value, target, onChange }) {
  const fields = control.fields[target] || [];
 
  if (!fields || fields.length === 0) {
    return null;
  }
 
  const handleInputChange = (fieldId, inputValue) => {
    onChange(control.id, {
      ...value,
      [fieldId]: inputValue
    });
  };
 
  const currentValues = value || {};
 
  return (
<div className="dynamic-input-inline">
      {fields.map(field => (
<div key={field.id} className="input-group-inline">
<label className="input-label-inline">{field.label}</label>
<input
            type={field.type}
            className="param-input-inline"
            min={field.min}
            max={field.max}
            placeholder={field.placeholder}
            value={currentValues[field.id] || ''}
            onChange={(e) => handleInputChange(field.id, e.target.value)}
          />
</div>
      ))}
</div>
  );
}
 
export default DynamicInputControl;*/