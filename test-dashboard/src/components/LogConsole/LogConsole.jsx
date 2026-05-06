import React, { useEffect, useRef } from 'react';
import { useDashboard } from '../../context/DashboardContext';
import './LogConsole.css';
 
function LogConsole() {
  const { logEntries, clearLogs } = useDashboard();
  const logBodyRef = useRef(null);
 
  useEffect(() => {
    if (logBodyRef.current) {
      logBodyRef.current.scrollTop = logBodyRef.current.scrollHeight;
    }
  }, [logEntries]);
 
  return (
<div className="log-section">
<div className="log-header">
<span>Command Log</span>
<button
          className="btn btn-secondary clear-btn"
          onClick={clearLogs}
>
          Clear
</button>
</div>
<div className="log-body" ref={logBodyRef}>
        {logEntries.map((entry, index) => (
<div key={index} className="entry">
<span className="ts">[{entry.ts}]</span>
<span className={`msg ${entry.level}`}>{entry.msg}</span>
</div>
        ))}
</div>
</div>
  );
}
 
export default LogConsole;
