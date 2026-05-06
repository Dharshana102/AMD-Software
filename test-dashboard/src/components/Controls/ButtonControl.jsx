import React from 'react';
import './Controls.css';
 
function ButtonControl({ items, onButtonClick, disabled }) {
  return (
<div className="btn-row">
      {items.map((button, index) => (
<button
          key={`${button.action}-${index}`}
          className={`btn ${button.cls}`}
          onClick={() => onButtonClick(button.action)}
          disabled={disabled}
>
          {button.label}
</button>
      ))}
</div>
  );
}
 
export default ButtonControl;
