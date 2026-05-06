import React, { useState } from 'react';
import './Controls.css';
 
function InfoDisplayControl({ control }) {
  const [copiedField, setCopiedField] = useState(null);
 
  const handleCopy = (fieldId, value) => {
    navigator.clipboard.writeText(value).then(() => {
      setCopiedField(fieldId);
      setTimeout(() => setCopiedField(null), 2000);
    }).catch(err => {
      console.error('Failed to copy:', err);
    });
  };
 
  return (
<div className="info-display-wrap">
<div className="info-fields">
        {control.fields.map(field => (
<div key={field.id} className="info-field-row">
<div className="info-field-label">{field.label}</div>
<div className="info-field-value-wrap">
<div className="info-field-value">{field.value}</div>
<button
                className={`btn-copy ${copiedField === field.id ? 'copied' : ''}`}
                onClick={() => handleCopy(field.id, field.value)}
                title={`Copy ${field.label}`}
>
                {copiedField === field.id ? (
                  // Checkmark icon when copied
<svg 
                    width="16" 
                    height="16" 
                    viewBox="0 0 24 24" 
                    fill="none" 
                    stroke="currentColor" 
                    strokeWidth="2.5" 
                    strokeLinecap="round" 
                    strokeLinejoin="round"
>
<polyline points="20 6 9 17 4 12"></polyline>
</svg>
                ) : (
                  // Double square copy icon
<svg 
                    width="16" 
                    height="16" 
                    viewBox="0 0 24 24" 
                    fill="none" 
                    stroke="currentColor" 
                    strokeWidth="2" 
                    strokeLinecap="round" 
                    strokeLinejoin="round"
>
<rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
<path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
</svg>
                )}
</button>
</div>
</div>
        ))}
</div>
</div>
  );
}
 
export default InfoDisplayControl;