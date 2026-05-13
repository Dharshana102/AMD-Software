import React from 'react';
import './Controls.css';

function ButtonControl({
  items,
  onButtonClick,
  onToggleButtonClick,
  toggleState = {},
  disabled
}) {
  return (
    <div className="btn-row">
      {items.map((button, index) => {
        const isToggleButton = button.toggle && button.stateKey;
        const isActive = isToggleButton ? !!toggleState[button.stateKey] : false;

        const IconComponent =
          isActive && button.activeIcon ? button.activeIcon : button.icon;

        const handleClick = () => {
          if (isToggleButton && onToggleButtonClick) {
            onToggleButtonClick(button);
          } else {
            onButtonClick(button.action);
          }
        };

        return (
          <button
            key={`${button.action || button.title}-${index}`}
            className={`btn ${button.cls} ${isActive ? 'active' : ''}`}
            onClick={handleClick}
            disabled={disabled}
            title={button.title || button.label}
          >
            {IconComponent ? <IconComponent size={16} /> : button.label}
          </button>
        );
      })}
    </div>
  );
}

export default ButtonControl;