import React from 'react';
import './StatusIndicator.css';

function StatusIndicator({ status }) {
  return (
    <div className="f-status">
      <span className={`f-status-dot ${status}`}></span>
      <span>{status.toUpperCase()}</span>
    </div>
  );
}

export default StatusIndicator;
