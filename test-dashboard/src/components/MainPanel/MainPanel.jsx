import React from 'react';
import { useDashboard } from '../../context/DashboardContext';
import { Power, Monitor, Volume2, Camera, Server } from 'lucide-react';
import FeatureCard from '../FeatureCard/FeatureCard';
import LogConsole from '../LogConsole/LogConsole';
import Placeholder from '../Placeholder/Placeholder';
import './MainPanel.css';
 
// Map icon names to components
const iconMap = {
  'Power': Power,
  'Monitor': Monitor,
  'Volume2': Volume2,
  'Camera': Camera,
  'Server': Server
};
 
function MainPanel() {
  const { modules, activeModule, moduleStatus } = useDashboard();
 
  if (!activeModule) {
    return (
<main className="main">
<Placeholder />
</main>
    );
  }
 
  const module = modules.find(m => m.id === activeModule);
  if (!module) return null;
 
  const status = moduleStatus[module.id];
  const IconComponent = iconMap[module.icon] || Power;
 
  return (
<main className="main">
<div className="panel-header">
<div
          className="panel-icon"
          style={{ background: `${module.color}22`, color: module.color }}
>
<IconComponent size={24} />
</div>
<div>
<div className="panel-title">{module.name} Module</div>
<div className="panel-desc">
            {module.sub} · Status:{' '}
<strong style={{ color: status === 'online' ? 'var(--green)' : 'var(--red)' }}>
              {status.toUpperCase()}
</strong>
</div>
</div>
</div>
 
      <div className="features-grid">
        {module.features.map(feature => (
<FeatureCard
            key={feature.id}
            feature={feature}
            moduleStatus={status}
          />
        ))}
</div>
 
      <LogConsole />
</main>
  );
}
 
export default MainPanel;