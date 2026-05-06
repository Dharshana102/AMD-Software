import React from 'react';
import './Placeholder.css';
 
function Placeholder() {
  return (
<div className="placeholder">
<svg
        width="64"
        height="64"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth="1.5"
>
<rect x="3" y="3" width="18" height="18" rx="3" />
<path d="M9 3v18M3 9h18" />
</svg>
<p>Select a module from the sidebar to view its features</p>
</div>
  );
}
 
export default Placeholder;
