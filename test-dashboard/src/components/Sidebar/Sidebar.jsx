import React from 'react';
import { useDashboard } from '../../context/DashboardContext';
import ModuleButton from './ModuleButton';
import './Sidebar.css';

function Sidebar() {
  const { modules, moduleStatus, activeModule } = useDashboard();

  return (
    <nav className="sidebar">
      <h2 className="sidebar-heading">Modules</h2>
      <div className="module-list">
        {modules.map(module => (
          <ModuleButton
            key={module.id}
            module={module}
            status={moduleStatus[module.id]}
            isActive={activeModule === module.id}
          />
        ))}
      </div>
    </nav>
  );
}

export default Sidebar;
