import React from 'react';
import { useDashboard } from '../../context/DashboardContext';
import {Monitor, Volume2, Camera, Server, Power } from 'lucide-react';
import './ModuleButton.css';
 
// Map icon names to components
const iconMap = {
  'Power':Power,
  'Monitor': Monitor,
  'Volume2': Volume2,
  'Camera': Camera,
  'Server': Server
};
 
function ModuleButton({ module, status, isActive }) {
  const { setActiveModule } = useDashboard();
  const IconComponent = iconMap[module.icon] || Power;
 
  const handleClick = () => {
    setActiveModule(module.id);
  };
 
  return (
<button
      className={`module-btn ${isActive ? 'active' : ''}`}
      onClick={handleClick}
>
<div
        className="module-icon"
        style={{ background: `${module.color}22`, color: module.color }}
>
<IconComponent size={20} />
</div>
<div className="module-meta">
<div className="module-name">{module.name}</div>
<div className="module-sub">{module.sub}</div>
</div>
<span className={`status-pill ${status}`}>{status}</span>
</button>
  );
}
 
export default ModuleButton;